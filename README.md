 💬 Real-Time Chat Application using Flet

This is a real-time chat application built with [Flet](https://flet.dev), a Python framework for creating frontend web apps without HTML/JS/CSS. Users can sign up, log in, and chat in real-time using a simple, clean interface.


🚀 Features

* ✅ User Sign-Up with validation
* 🔐 Secure Sign-In
* 💬 Real-time chat messaging
* 👥 Multi-user session support
* 🔄 Page routing and navigation
* 🎨 Emoji picker for messages
* 💾 User data stored locally (`users_db.txt`)



📁 Project Structure

```
.
├── main.py              # Main application entry point
├── signin_form.py       # Sign-in UI and logic
├── signup_form.py       # Sign-up UI and logic
├── users_db.py          # User database (read/write logic)
├── chat_message.py      # Message format and rendering
└── users_db.txt         # Local storage of user credentials




🛠️ Setup Instructions

1. Install Dependencies

   ```bash
   pip install flet
   

 Run the App

   ```bash
   python main.py
   

3. Access in Browser
   The app will automatically open in your default browser.

🧠 How It Works

 SignUpForm: Handles new user registration. On success, prompts to sign in.
 SignInForm: Authenticates users and redirects to the chat window.
 Chat Page : Displays messages from all users in real-time using Flet’s `pubsub`.
 UsersDB : Manages local file-based user data for simplicity.



⚠️ Notes

Not for production: This app uses local file-based user authentication (no hashing, no DB).
Sessions: Uses `page.session` to manage active users.
Emojis: Insert emojis with the dropdown emoji picker next to the message box.

