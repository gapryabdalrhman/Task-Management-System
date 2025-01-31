
# Task Management Application

A simple Task Management Application built using **Django**, **Django REST Framework (DRF)**, and **JWT Authentication**. This application allows users to create, read, update, and delete tasks. It also includes a basic frontend using Django templates.

## Features

- **Task Management**:
  - Create, read, update, and delete tasks.
  - Tasks are associated with authenticated users.
- **Authentication**:
  - JWT-based authentication using `djangorestframework-simplejwt`.
- **Frontend**:
  - Basic HTML templates for task listing and task creation.
- **REST API**:
  - Fully functional REST API for task management.
- **Git Version Control**:
  - Proper Git usage with meaningful commit messages.

---

## Requirements

The project requires the following Python packages, which are listed in `requirements.txt`:

asgiref==3.8.1
colorama==0.4.6
Django==5.1.5
djangorestframework==3.15.2
djangorestframework_simplejwt==5.4.0
drf-yasg==1.21.8
gunicorn==23.0.0
inflection==0.5.1
iniconfig==2.0.0
packaging==24.2
pluggy==1.5.0
PyJWT==2.10.1
pytz==2024.2
PyYAML==6.0.2
sqlparse==0.5.3
tzdata==2025.1
uritemplate==4.1.1
```

---



---

## Installation

1. **Clone the repository**:
   ```
   git clone https://github.com/yourusername/task_manager.git
   cd task_manager
   ```

2. **Create a virtual environment**:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (for admin access)**:
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

7. **Access the application**:
   - The API will be available at `http://127.0.0.1:8000/api/`.
   - The frontend will be available at `http://127.0.0.1:8000/tasks/`.
   - Admin panel: `http://127.0.0.1:8000/admin/`.

---

## API Endpoints

The following REST API endpoints are available:

| Method | Endpoint             | Description                          |
|--------|----------------------|--------------------------------------|
| POST   | `/api/tasks/`        | Create a new task (Authenticated)    |
| GET    | `/api/tasks/`        | Retrieve a list of tasks (Authenticated) |
| GET    | `/api/tasks/{id}/`   | Retrieve a single task               |
| PUT    | `/api/tasks/{id}/`   | Update a task                        |
| DELETE | `/api/tasks/{id}/`   | Delete a task                        |

### Authentication

To access the API, users must authenticate using JWT. Use the following endpoint to obtain a token:

- **Token Obtain Pair**: `POST /api/token/`
  - Request Body:
    ```json
    {
      "username": "yourusername",
      "password": "yourpassword"
    }
    ```
  - Response:
    ```json
    {
      "refresh": "xxxxx",
      "access": "xxxxx"
    }
    ```

- Use the `access` token in the `Authorization` header for authenticated requests:
  ```bash
  Authorization: Bearer <access_token>
  ```

---

## Frontend

The frontend is built using Django templates and includes:

1. **Task List Page** (`task_list.html`):
   - Displays all tasks for the authenticated user.
   - Links to edit or delete tasks.

2. **Task Form Page** (`task_form.html`):
   - Form to create or edit tasks.

---

## Git Version Control

- The project is version-controlled using Git.
- Meaningful commit messages are used to track changes.

## Bonus Features

1. **Unit Tests**:
   - Unit tests are written for at least one API endpoint (e.g., task creation).
  

2. **Git Branching Strategy**:
   - The project follows a feature-based branching strategy:
     - `main`: Stable production-ready code.
     - `feature/*`: Feature branches for new functionality.
     - `bugfix/*`: Bugfix branches for fixing issues.

3. **Swagger API Documentation**:
   - API documentation is available using `drf-yasg`.
   - Access it at `http://127.0.0.1:8000/swagger/`

4. **Docker Support**:
   - The project is Dockerized for easy deployment.
   - Run the following commands to build and start the Docker container:
     ```
     docker-compose up --build
     ```

---

separation of concerns between API and template views

