# streamlit_app.py

import streamlit as st
from registration import validate_username, validate_password
from login_credentials import (
    save_user,
    authenticate,
    user_exists,
    get_password,
    update_password
)

st.set_page_config(page_title="User Auth System", layout="centered")

st.title("🔐 Python User Registration and Login System")

menu = ["Login", "Register", "Forgot Password"]
choice = st.sidebar.selectbox("Menu", menu)

# -------------------------------
# LOGIN PAGE
# -------------------------------
if choice == "Login":
    st.subheader("Login")

    username = st.text_input("Username / Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if authenticate(username, password):
            st.success(f"Welcome {username}! Login Successful.")
        else:
            st.error("Invalid username or password.")


# -------------------------------
# REGISTRATION PAGE
# -------------------------------
elif choice == "Register":
    st.subheader("Register New User")

    username = st.text_input("Enter Email / Username")
    password = st.text_input("Enter Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")

    if st.button("Register"):

        if not validate_username(username):
            st.error("❌ Invalid username format.")

        elif not validate_password(password):
            st.error("❌ Password must be 6–16 chars, include uppercase, lowercase, digit, and special char.")

        elif password != confirm_password:
            st.error("❌ Passwords do not match.")

        elif user_exists(username):
            st.error("❌ Username already exists. Try logging in.")

        else:
            save_user(username, password)
            st.success("🎉 Registration successful! You can now login.")


# -------------------------------
# FORGOT PASSWORD PAGE
# -------------------------------
elif choice == "Forgot Password":
    st.subheader("Recover Password")

    username = st.text_input("Enter your registered username")

    if st.button("Get Password"):
        if user_exists(username):
            pwd = get_password(username)
            st.info(f"Your password is: **{pwd}**")
        else:
            st.error("❌ Username not found.")

    st.write("---")

    st.subheader("Update Password")
    new_pwd = st.text_input("New Password", type="password")
    confirm_new_pwd = st.text_input("Confirm New Password", type="password")

    if st.button("Update Password"):
        if not user_exists(username):
            st.error("❌ Username not found.")

        elif not validate_password(new_pwd):
            st.error("❌ Password does not meet requirements.")

        elif new_pwd != confirm_new_pwd:
            st.error("❌ Passwords do not match.")

        else:
            update_password(username, new_pwd)
            st.success("🔄 Password updated successfully.")