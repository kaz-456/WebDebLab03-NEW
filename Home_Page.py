import streamlit as st

# Title of App
st.title("Web Development Lab03")

# Assignment Data 
st.header("CS 1301")
st.subheader("Team 33, Web Development - Section A")
st.subheader("Team Member 1: Lana Boudiab, Team Member 2: Iskander Dyussenov")

# Introduction
st.write("""
Welcome to our Streamlit Web Development Lab03 app! You can navigate between the pages using the sidebar to the left. The following pages are:

1. **Home Page**: A general overview of the project and the team, introducing the purpose of our app.
2. **Book Search**: Input a book's title, author, or description, and retrieve matching books using the Google Books API.
3. **Project Showcase**: A showcase of our favorite projects, highlighting what we've learned and accomplished during the course.
4. **About Us**: A page dedicated to team member bios, including interests, educational background, and skills.
5. **ChatGPT Book Search**: Search for a book by description and get the book's details (name, author, etc.).

We hope you enjoy exploring our app!
""")
