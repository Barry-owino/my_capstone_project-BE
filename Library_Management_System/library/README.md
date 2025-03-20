🚀 Library Management System
📝 Description
This is a simple Library Management System built using Django. It allows users to view, borrow, and return books. The project also exposes an API built with Django REST Framework for managing books programmatically.

🛠️ Installation Instructions
The project is running within a virtual enviromment with python and django installations.

📚 Project Features
Manage Books: Add, edit, list, and delete books in the library.
Borrow/Return Books: Users can borrow books and return them when done.
API Endpoints: A RESTful API to interact with the system.
🛠️ Technology Stack
Backend: Django (Web Framework)
API: Django REST Framework (DRF)
Database: SQLite (default for Django)
📡 API Endpoints
1. Get All Books
Method: GET
URL: /api/books/
Response: Returns a list of all books in JSON format.

2. Get Book Details
Method: GET
URL: /api/books/<id>/
Response: Returns detailed information about a specific book by its ID.

3. Add a Book
Method: POST
URL: /api/books/
Body: JSON object with book information (e.g., title, author, etc.).
Response: Returns the newly added book's details.

4. Borrow a Book
Method: PUT
URL: /api/books/<id>/borrow/
Response: Marks the book as borrowed.

5. Return a Book
Method: PUT
URL: /api/books/<id>/return/
Response: Marks the book as returned.

🔧 Development Setup
Install dependencies: pip install -r requirements.txt
Run migrations: python manage.py migrate
Start server: python manage.py runserver
🤝 Contributing
Fork this repository.
Create your feature branch: git checkout -b feature-branch.
Commit your changes: git commit -m 'Add new feature'.
Push to your fork: git push origin feature-branch.
Open a pull request.
