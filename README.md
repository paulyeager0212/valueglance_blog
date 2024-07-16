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
    git clone https://github.com/paulyeager0212/valueglance_blog.git
    cd valueglance_blog
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

4. **Create a superuser**:

    ```bash
    python manage.py createsuperuser
    ```

5. **Run the development server**:

    ```bash
    python manage.py runserver
    ```

## API Endpoints

### Authentication

- **Register**: `POST /api/register/`

- **Login**: `POST /api/token/`

- **Token Refresh**: `POST /api/token/refresh/`

### Blog Posts

- **Create Post**: `POST /api/posts/`

- **List Posts**: `GET /api/posts/`

- **Retrieve Post**: `GET /api/posts/<id>/`

- **Update Post**: `PUT /api/posts/<id>/`

- **Delete Post**: `DELETE /api/posts/<id>/`

## Running Tests

Run the unit tests to ensure the API is working correctly:

```bash
python manage.py test
