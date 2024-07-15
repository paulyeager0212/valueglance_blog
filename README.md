# Simple Blogging Platform API

This is a RESTful API for a simple blogging platform built using Django and Django REST Framework. It provides endpoints for creating, retrieving, updating, and deleting blog posts, with JWT-based authentication.

## Features

- **Blog Posts CRUD**: Create, retrieve, update, and delete blog posts.
- **User Authentication**: Sign up, sign in, and authenticate requests using JWT.
- **Unit Tests**: Comprehensive unit tests for API endpoints.

## Requirements

- Python 3.x
- Django
- Django REST framework
- Django REST framework SimpleJWT
- PostgreSQL (or another database of your choice)

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/yourusername/blogging-platform-api.git
    cd blogging-platform-api
    ```

2. **Create and activate a virtual environment**:

    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
    ```

3. **Install the dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the database**:

    Update `DATABASES` in `blog_api/settings.py` with your database configuration. The default configuration uses SQLite:

    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
    ```

    Run migrations to set up the database schema:

    ```bash
    python manage.py migrate
    ```

5. **Create a superuser**:

    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server**:

    ```bash
    python manage.py runserver
    ```

## API Endpoints

### Authentication

- **Register**: `POST /api/register/`
    - Request body: `{"username": "yourusername", "password": "yourpassword"}`
    - Response: `{ "refresh": "token", "access": "token" }`

- **Login**: `POST /api/token/`
    - Request body: `{"username": "yourusername", "password": "yourpassword"}`
    - Response: `{ "refresh": "token", "access": "token" }`

- **Token Refresh**: `POST /api/token/refresh/`
    - Request body: `{"refresh": "yourrefreshtoken"}`
    - Response: `{ "access": "newaccesstoken" }`

### Blog Posts

- **Create Post**: `POST /api/posts/`
    - Headers: `Authorization: Bearer <access_token>`
    - Request body: `{"title": "Post Title", "content": "Post content"}`
    - Response: `{ "id": 1, "title": "Post Title", "content": "Post content", "author": 1, "created_at": "2024-07-11T10:00:00Z", "updated_at": "2024-07-11T10:00:00Z" }`

- **List Posts**: `GET /api/posts/`
    - Response: `[{"id": 1, "title": "Post Title", "content": "Post content", "author": 1, "created_at": "2024-07-11T10:00:00Z", "updated_at": "2024-07-11T10:00:00Z"}]`

- **Retrieve Post**: `GET /api/posts/<id>/`
    - Response: `{ "id": 1, "title": "Post Title", "content": "Post content", "author": 1, "created_at": "2024-07-11T10:00:00Z", "updated_at": "2024-07-11T10:00:00Z" }`

- **Update Post**: `PUT /api/posts/<id>/`
    - Headers: `Authorization: Bearer <access_token>`
    - Request body: `{"title": "Updated Title", "content": "Updated content"}`
    - Response: `{ "id": 1, "title": "Updated Title", "content": "Updated content", "author": 1, "created_at": "2024-07-11T10:00:00Z", "updated_at": "2024-07-11T10:00:00Z" }`

- **Delete Post**: `DELETE /api/posts/<id>/`
    - Headers: `Authorization: Bearer <access_token>`
    - Response: `204 No Content`

## Running Tests

Run the unit tests to ensure the API is working correctly:

```bash
python manage.py test
