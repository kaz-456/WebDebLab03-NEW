import google.generativeai as genai
import os
import streamlit as st
import requests

genai.configure(api_key="AIzaSyC6luHAwRGrtkq6OKAc6Wjq2hzBhKe8XXE")

import pathlib
import textwrap

#Here I enter the api url and api key that I generated in my google cabinet
api_key = "AIzaSyDKdLULoLEOvdTs5JSG6Mqbbh6Mnyy_BBI" 
GOOGLE_BOOKS_API_URL = f"https://www.googleapis.com/books/v1/volumes?key={api_key}"

def fetch_books(name, author=None, publication_date=None):

    params = name #params is going to be appended to the link to search books
    if author: #if optional author was input
        params += f"+inauthor:{author}" #append author to params
    if publication_date: #if optional date was input
        params += f"+inpublisher:{publication_date}" #append publication date to params

    try:
        response = requests.get(f"https://www.googleapis.com/books/v1/volumes?q={params}&key={api_key}") #ask the api to search for the book and has the api key
        response.raise_for_status() #check the status of the api response
        return response.json().get("items", [])
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching books: {e}") 
        return []

# Used to securely store your API key
def main():
    name = st.text_input("Book Title or Keyword", "")
    author = st.text_input("Author Name (Optional)", "")
    publication_date = st.text_input("Publication Date (e.g., 2020) (Optional)", "")
    books = None

    if st.button("Search"):
        with st.spinner("Searching for books..."):
            books = fetch_books(name, author, publication_date)
            bookquery = books[0].get('volumeInfo', {}).get('title')
            if bookquery:

                model = genai.GenerativeModel('gemini-1.5-flash')
                response = model.generate_content(f"Give a brief description of the following book:{bookquery} . Use the following format: [brief description], line break, bold[read if you like], line break, bold[avoid if you dislike].")
                st.write(response.text)

        
        if not books:
            st.warning("No books found. Try refining your search criteria.")

    



if __name__ == "__main__":
    main()