

# FastAPI Blog Project with PostgreSQL

This project implements a full blog system including user authentication, blog management, and **PostgreSQL** as the database backend. It is fully containerized with **Docker** for easy setup.

---

## 🚀 Features

* **CRUD Operations:** Create, Read, Update, and Delete blog posts.
* **User Management:** User registration and profile management.
* **Authentication:** Secure login using **JWT (JSON Web Tokens)** and OAuth2.
* **Security:** Password hashing using `bcrypt`.
* **Database:** PostgreSQL via **SQLAlchemy ORM**.
* **Relationships:** Each blog post is linked to a specific user (Creator).

---

## 📁 Project Structure

```text
FastAPI_course/
├── blog/                  # Main Application Package
│   ├── repository/        # Database logic (CRUD operations)
│   ├── routers/           # API Route handlers (blog, user, auth)
│   ├── main.py            # Application entry point
│   ├── database.py        # SQLAlchemy connection setup (PostgreSQL)
│   ├── models.py          # Database tables
│   ├── schemas.py         # Pydantic models (data validation)
│   ├── hashing.py         # Password encryption logic
│   ├── oauth2.py          # Security/Authentication middleware
│   └── JWTtoken.py        # Token generation and verification
├── Dockerfile             # FastAPI container
├── docker-compose.yml     # Docker Compose for FastAPI + PostgreSQL
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
└── .gitignore             # Files ignored by Git
```

---

## 🛠️ Installation & Setup

1. **Clone the repository:**

```bash
git clone https://github.com/lamaDayoub/fastapi_course_project.git
cd fastapi_course_project
```

2. **Build and run containers using Docker Compose:**

```bash
docker-compose up --build
```

This will start:

* **PostgreSQL** on port `5432`
* **FastAPI app** on port `8000`

3. **Environment variable (DATABASE_URL):**
   The FastAPI app uses:

```
postgresql://admin:password123@db:5432/blog_db
```

defined in `docker-compose.yml`.

---

## 🏃 Running Locally without Docker

1. Create a virtual environment:

```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Set your PostgreSQL environment variable:

```bash
export DATABASE_URL=postgresql://admin:password123@localhost:5432/blog_db  # Linux/Mac
set DATABASE_URL=postgresql://admin:password123@localhost:5432/blog_db     # Windows
```

4. Run the app:

```bash
uvicorn blog.main:app --reload
```

---

## 📖 API Documentation

* **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* **Redoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 🔒 Security Note

This project uses **OAuth2 with Password Bearer flow**. To access protected routes, register a user and log in via the `/login` endpoint to get a JWT token.


