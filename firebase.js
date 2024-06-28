// Import Firebase SDK modules
import firebase from 'firebase/app';
import 'firebase/auth'; // Import Firebase Authentication module if needed
import 'firebase/database'; // Import Firebase Realtime Database module if needed

// Your Firebase project configuration
const firebaseConfig = {
    apiKey: "AIzaSyA2-AuAUWtzk9lhMoZxi9ipR7cLtAnPd70",
    authDomain: "solara-ec953.firebaseapp.com",
    databaseURL: "https://solara-ec953-default-rtdb.asia-southeast1.firebasedatabase.app",
    projectId: "solara-ec953",
    storageBucket: "solara-ec953.appspot.com",
    messagingSenderId: "1080014983941",
    appId: "1:1080014983941:web:d56daa165fd97a0225dd6c",
    measurementId: "G-C64ZJLLSB6"
  };

// Initialize Firebase
firebase.initializeApp(firebaseConfig);

// Optional: Initialize Firebase Analytics
if (firebaseConfig.measurementId) {
  firebase.analytics();
}

// Example usage: Access Firebase Authentication
const auth = firebase.auth();

// Example usage: Access Firebase Realtime Database
const database = firebase.database();

export { firebase, auth, database };
