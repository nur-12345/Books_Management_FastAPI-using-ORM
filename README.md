# Books_Management_FastAPI-using-ORM
This is a **Book Management REST API** built using **FastAPI**, **SQLAlchemy ORM**, and **PostgreSQL**. It supports full **CRUD operations** for managing books with a clean and modular architecture.
---

## 🚀 Features

✅ Create, Read, Update, Delete (CRUD) books  
✅ SQLAlchemy ORM integration  
✅ PostgreSQL as the database  
✅ Dependency Injection using FastAPI  
✅ Pydantic for request validation  
✅ Interactive API documentation via Swagger  
✅ Ready for deployment and testing

---

## 📂 Project Structure

📁 my_fastapi_books_api/
│
├── books.py # FastAPI routes and logic
├── database.py # SQLAlchemy ORM and DB setup
├── requirements.txt # Python dependencies
└── README.md # Project documentation


---

## ⚙️ Tech Stack

| Technology     | Description                       |
|----------------|-----------------------------------|
| FastAPI        | High-performance API framework    |
| SQLAlchemy     | ORM for database interactions     |
| PostgreSQL     | Relational database               |
| Uvicorn        | ASGI server for running FastAPI   |
| Pydantic       | Data validation and serialization |
| Postman        | API testing tool (manual testing) |

---

## 🛠️ Setup Instructions

### 🔹 Step 1: Clone the Repository

```bash
git clone https://github.com/<your-username>/fastapi-books-api.git
cd fastapi-books-api
🔹 Step 2: Create & Activate Virtual Environment
python3 -m venv env
source env/bin/activate       # macOS/Linux
env\Scripts\activate          # Windows
🔹 Step 3: Install Dependencies
pip install -r requirements.txt
🔹 Step 4: Set up PostgreSQL Database
Ensure PostgreSQL is installed and running.

Create a database named demo:

CREATE DATABASE demo;

Update the connection URL in database.py if needed:

DATABASE_URL = "postgresql://postgres:root@localhost/demo"
▶️ Run the API Server
uvicorn books:app --reload

🧪 API Endpoints

Method	Endpoint	Description
GET	/books	Get all books
GET	/books/{title}	Get book by title
POST	/books/create_book	Add new book
PUT	/books/update_book	Update existing book
DELETE	/books/delete_book/{title}	Delete book by title
📝 Example Request (POST /books/create_book)
{
  "title": "Harry Potter",
  "author": "J.K. Rowling",
  "category": "Fantasy"
}
🧰 Tools for Testing

✅ Swagger UI - Built-in documentation interface
✅ Postman - Manual testing with JSON payloads


Built with ❤️ using FastAPI, SQLAlchemy, and PostgreSQL.
Open for contributions, improvements, and ideas.


📌 Author

👩‍💻 Nupur Shivani
🔗 https://www.linkedin.com/in/nupur-shivani-150b96262

📃 License

This project is licensed under the MIT License.
