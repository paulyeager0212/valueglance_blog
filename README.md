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
- PostgreSQL

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/paulyeager0212/valueglance_blog.git
    cd valueglance_blog
    ```

2. **Build and Start Docker Containers:**:
    ```bash
    docker-compose up --build
    ```

3. **Create a superuser**:

    ```bash
    docker-compose run --rm app sh -c "python manage.py createsuperuser"
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
docker-compose run --rm app sh -c "python manage.py test"
```

## Design Decisions and Trade-offs

### Use of Docker

**Decision**: Docker was chosen to ensure a consistent development environment across different machines and setups. It also simplifies the deployment process.

**Trade-offs**:

- **Pros**: Consistent environments, easy dependency management, and simplified deployment.
- **Cons**: Initial setup complexity and potential performance overhead.

### PostgreSQL

**Decision**: PostgreSQL was chosen as the database for its robustness, scalability, and widespread use in production environments.

**Trade-offs**:

- **Pros**: Reliable, ACID-compliant, and supports advanced SQL features.
- **Cons**: Slightly more complex setup compared to lightweight databases like SQLite.

### Django Rest Framework (DRF)

**Decision**: DRF was used to build the RESTful API for its powerful and flexible toolkit.

**Trade-offs**:

- **Pros**: Simplifies API development, robust authentication and permission systems.
- **Cons**: Additional learning curve for developers not familiar with DRF.

### JWT for Authentication

**Decision**: JWT was chosen for stateless, secure, and scalable authentication.

**Trade-offs**:

- **Pros**: Stateless authentication, easy to scale.
- **Cons**: Requires secure handling of tokens and potential vulnerability to token theft.

## Additional Features and Improvements

Given more time, the following features and improvements could be implemented:

- **Pagination**: Implementing pagination to handle large lists of blog posts efficiently.

- **Search and Filtering**: Adding search and filtering capabilities to allow users to search for and filter blog posts based on various criteria.

- **Comments System**: Integrating a comment system for each blog post to enhance user interaction.

- **Like/Dislike Feature**: Implementing a like/dislike feature for blog posts to provide user feedback mechanisms.

- **Enhanced Security**: Implementing additional security measures such as rate limiting, IP whitelisting/blacklisting, and two-factor authentication (2FA).


