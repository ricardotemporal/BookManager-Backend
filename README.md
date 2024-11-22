# 📚 **BookManager - Backend**

Welcome to the back-end of **BookManager**, a powerful API built with Django and Ninja for managing books efficiently.

  

---

  

## 🌟 **Features**

-  **📖 CRUD operations**: Create, read, update, and delete books.

-  **✍️ Add ratings and comments**: Keep track of reviews for your books.

-  **🎲 Random book selector**: Retrieve a random book with flexible filtering options.

-  **🔗 RESTful API**: Seamlessly integrates with any front-end or client application.

  

---

  

## 🚀 **Getting Started**

  

### 🛠️ **Requirements**

- Python 3.10 or higher

- Django 4.2 or higher

- Django Ninja

  

---

  

### ⚙️ **Installation**

  

1.  **Clone this repository**:

`git clone https://github.com/your-username/BookManager-Backend.git`

`cd BookManager-Backend`

  

2.  **Set up a virtual environment**:

  

`python -m venv venv`

`source venv/bin/activate # For Windows: venv\Scripts\activate`



3.  **Run migrations**:

  

`python manage.py migrate`

  

4.  **Start the development server**:

`python manage.py runserver`



---



## 📋 **API Endpoints**


`GET` `/api/livros/` - Retrieve all books.

`POST` `/api/livros/` - Add a new book.

`PUT` `/api/livros/{id}` - Update a book's rating and comments.

`DELETE` `/api/livros/{id}` - Delete a book.

`GET` `/api/livros/sortear/` - Get a random book based on filters.

----------

## 🛠️ **Technologies Used**

-   **Django**: Framework for back-end development.
-   **Django Ninja**: Fast and modern API building library.
-   **SQLite**: Default database for development.