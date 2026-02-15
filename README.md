
# FastAPI Blog Project

 This project implements a full blog system including user authentication, blog management, and relational database mapping.

## 🚀 Features

* **CRUD Operations:** Create, Read, Update, and Delete blog posts.
* **User Management:** User registration 
* **Authentication:** Secure Login using **JWT (JSON Web Tokens)** and OAuth2.
* **Security:** Password hashing using `bcrypt`.
* **Database:** Integrated with **SQLAlchemy ORM** (SQLite by default).
* **Relationships:** Each blog post is linked to a specific user (Creator).

## 📁 Project Structure

```text
FastAPI_course/
├── blog/                # Main Application Package
│   ├── repository/      # Database logic (CRUD operations)
│   ├── routers/         # API Route handlers (blog, user, auth)
│   ├── main.py          # Application entry point
│   ├── database.py      # SQLAlchemy connection setup
│   ├── models.py        # Database tables
│   ├── schemas.py       # Pydantic models (data validation)
│   ├── hashing.py       # Password encryption logic
│   ├── oauth2.py        # Security/Authentication middleware
│   └── JWTtoken.py      # Token generation and verification
├── README.md            # Project documentation
└── .gitignore           # Files to be ignored by Git

```

## 🛠️ Installation & Setup

1. **Clone the repository:**
```bash
git clone [https://github.com/lamaDayoub/fastapi_course_project.git](https://github.com/lamaDayoub/fastapi_course_project.git)
cd fastapi_course_project

```


2. **Create and activate a virtual environment:**
```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

```


3. **Install dependencies:**
```bash
pip install fastapi uvicorn sqlalchemy passlib[bcrypt] python-jose[cryptography] python-multipart

```



## 🏃 Running the Application

Start the server using Uvicorn from the root directory:

```bash
uvicorn blog.main:app --reload

```

The API will be available at: `http://127.0.0.1:8000`

## 📖 API Documentation

Once the server is running, you can explore the interactive API docs:

* **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* **Redoc:** [http://127.0.0.1:8000/redoc](https://www.google.com/search?q=http://127.0.0.1:8000/redoc)

## 🔒 Security Note

This project uses **OAuth2 with Password Bearer flow**. To access protected blog routes, you must first register a user and log in via the `/login` endpoint to receive a JWT access token.

```

