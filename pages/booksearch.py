import streamlit as st
import requests

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

def display_books(books):

    mainbook = books[0].get('volumeInfo', {}).get('title')
    for book in books:
        info = book.get("volumeInfo", {}) #This is parcing data from the api response for every book
        title = info.get("title", "No title available")
        authors = ", ".join(info.get("authors", ["Unknown author"]))
        published_date = info.get("publishedDate", "Unknown date")
        description = info.get("description", "No description available")
        preview_link = info.get("previewLink", "#")
        
        st.markdown(f"### {title}") #Now this is outputting every data that was parced before
        st.write(f"**Authors:** {authors}")
        st.write(f"**Published Date:** {published_date}")
        st.write(f"**Description:** {description[:200]}...")
        st.markdown(f"[More Info]({preview_link})")
        st.markdown("---")

#This is the default function that prompts the user to enter book info
def main():
    st.title("Google Books Search")
    st.write("Search for books by title, author name, and publication date using the Google Books API.")
    
    name = st.text_input("Book Title or Keyword", "")
    author = st.text_input("Author Name (Optional)", "")
    publication_date = st.text_input("Publication Date (e.g., 2020) (Optional)", "")

    if st.button("Search"):
        with st.spinner("Searching for books..."):
            books = fetch_books(name, author, publication_date)
        
        if books:
            st.success(f"Found {len(books)} books!")
            display_books(books)
        else:
            st.warning("No books found. Try refining your search criteria.")

if __name__ == "__main__":
    main()