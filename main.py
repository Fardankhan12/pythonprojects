import streamlit as st

# Book class
class Book:
    def __init__(self, title, author, slug):
        self.title = title
        self.author = author
        self.slug = slug

# Library class
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, slug):
        self.books.append(Book(title, author, slug))

    def get_books(self):
        return self.books

    def delete_book(self, slug):
        self.books = [book for book in self.books if book.slug != slug]

# Initialize library in session_state
if "library" not in st.session_state:
    st.session_state.library = Library()

library = st.session_state.library

st.title("📚 Simple Library Management System")

# Sidebar options
option = st.sidebar.selectbox("Select Action", ["Add Book", "View Books", "Delete Book"])

# Add Book
if option == "Add Book":
    st.header("Add a New Book")
    title = st.text_input("Book Title")
    author = st.text_input("Author Name")
    slug = st.text_input("Enter the slug (e.g., man_in_middle)")
    if st.button("Add Book"):
        if title and author and slug:
            library.add_book(title, author, slug)
            st.success(f"Book '{title}' added successfully!")
        else:
            st.warning("Please provide Title, Author, and Slug.")

# View Books
elif option == "View Books":
    st.header("List of Books")
    books = library.get_books()
    if books:
        for book in books:
            st.write(f"**{book.title}** by *{book.author}* — (slug: `{book.slug}`)")
    else:
        st.info("No books available.")

# Delete Book
elif option == "Delete Book":
    st.header("Delete a Book")
    slug = st.text_input("Enter slug to Delete")
    if st.button("Delete Book"):
        if slug:
            library.delete_book(slug)
            st.success(f"Book with slug '{slug}' deleted successfully!")
        else:
            st.warning("Please enter a slug.")
