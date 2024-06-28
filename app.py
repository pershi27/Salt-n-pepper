import solara
import firebase_admin
from firebase_admin import credentials, db
from solara.server import app as solara_app

# Initialize the Firebase Admin SDK
cred = credentials.Certificate('/path/to/your/serviceAccountKey.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://solara-ec953-default-rtdb.asia-southeast1.firebasedatabase.app'
})

@solara.component
def OrderForm():
    table_number = solara.use_state(1)
    product = solara.use_state("")
    quantity = solara.use_state(1)
    menu_items_df = fetch_menu_items()

    def fetch_menu_items():
        ref = db.reference('menu_items')
        menu_items = ref.get()
        if menu_items:
            return pd.DataFrame.from_dict(menu_items, orient='index')
        else:
            return pd.DataFrame(columns=["Product", "Price"])

    def handle_submit():
        # Find the price of the selected product
        price = menu_items_df.loc[menu_items_df["Product"] == product.value, "Price"].values[0]
        total_price = quantity.value * price

        # Push new orders to Firebase Realtime Database
        ref = db.reference('orders')
        ref.push({
            "table_number": table_number.value,
            "product": product.value,
            "quantity": quantity.value,
            "total_price": total_price
        })
        solara.show("Order submitted successfully!")

    with solara.Column():
        solara.InputNumber("Table Number", value=table_number)
        solara.Select("Select Product", options=list(menu_items_df["Product"]), value=product)
        solara.InputNumber("Quantity", value=quantity)
        solara.Button("Submit Order", on_click=handle_submit)

@solara.component
def Page():
    with solara.Column():
        solara.Markdown("# Food Order App")
        OrderForm()

# Run the Solara app
solara_app.run(Page)
