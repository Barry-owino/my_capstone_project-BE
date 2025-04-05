# 📚 LibraryAPI - Library Management System

This is a simple Library Management System built with Django and Django REST Framework. It provides a web API that allows users to view, borrow, and return books.

---

## 🧩 Features

- **Book Management**: Add, edit, delete, and list books.
- **User Management**: Register, update, and manage library users.
- **Borrow/Return Books**: Users can check out and return books.
- **RESTful API**: Easily interact with the system programmatically.

---

## 🛠️ Tech Stack

- **Backend**: Django
- **API**: Django REST Framework
- **Database**: SQLite (default)

---

## 🌐 API Endpoints (Books)

| Action            | Method | URL                          | Description                           |
|------------------|--------|------------------------------|---------------------------------------|
| List Books        | GET    | `/api/books/`                | Get all books                         |
| Book Details      | GET    | `/api/books/<id>/`           | Get info on a specific book           |
| Add Book          | POST   | `/api/books/`                | Create a new book                     |
| Borrow Book       | PUT    | `/api/books/<id>/borrow/`    | Borrow a book                         |
| Return Book       | PUT    | `/api/books/<id>/return/`    | Return a borrowed book                |

---

## 👤 User Management (Sample Views)

- `UserListCreate`: Handles user registration and listing all users.
- `UserRetrieveUpdateDestroy`: View, update, or delete a specific user.

---

## 🔄 Book Checkout & Return

- Users can only borrow if a copy is available.
- Borrowed books are tracked using a `BookCheckout` model.
- Return functionality updates the book availability and checkout record.

---

## 🧪 API Testing

You can use the browsable DRF API or tools like Postman to test endpoints.

---

## 🚀 Getting Started

```bash
# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Run development server
python manage.py runserver

