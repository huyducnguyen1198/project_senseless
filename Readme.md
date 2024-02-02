# Project Senseless Backend Setup

This guide will help you set up the `project_senseless` backend on your local machine. The backend is built with Django and uses MySQL as the database.

## Requirements

- MySQL
- Django
- Python 3.x

## Setup Instructions

### 1. Install MySQL

Ensure MySQL is installed on your system. For installation, use your system's package manager or download it from the [official MySQL downloads page](https://dev.mysql.com/downloads/mysql/).

### 2. Install Python Dependencies

After cloning the repository and navigating to the project directory, install the required Python packages using pip:

```bash
pip install -r requirements.txt
```

### 3. Configure MySQL Database

**_This is for local only due to the need of installing MySQL on your separate machine.**_

Before running the migrations, you need to create the database and a user with the necessary permissions from your terminal:

```bash
mysql -u root -p -e "CREATE DATABASE project_senseless;"
mysql -u root -p -e "CREATE USER 'huynguyen'@'localhost' IDENTIFIED BY 'G0dMercy!!';"
mysql -u root -p -e "GRANT ALL PRIVILEGES ON project_senseless.* TO 'huynguyen'@'localhost';"
mysql -u root -p -e "FLUSH PRIVILEGES;"
```

You will be prompted to enter the root password for MySQL after each command.

### 4. Run Migrations

With the database configured, apply the migrations to create the necessary database tables:

```bash
python manage.py migrate
```

### 5. Run the Development Server

To start the Django development server, use the following command:

```bash
python manage.py runserver
```

You can now access the API at `http://127.0.0.1:8000/`.

## Local Testing and future cloud deployment

Ensure your `.env` file (or environment variables) is set up with the correct database credentials for local testing:

- `DATABASE_NAME=project_senseless`
- `DATABASE_USER=huynguyen`
- `DATABASE_PASSWORD=G0dMercy!!`
- `DATABASE_HOST=localhost`

These values should match your local MySQL setup.

Follow these instructions to set up and run the `project_senseless` backend for development and testing.




# Testing Project Senseless API Endpoints

This guide provides instructions for testing the `project_senseless` backend API endpoints using Django's admin interface and Postman. The API supports operations on `UserType` and `User` entities.

## API Endpoints

The following endpoints are available for `UserType` and `User`:

- **UserType Endpoints**
  - List all user types: `GET /api/userType/`
  - Retrieve user type details: `GET /api/userType/<str:pk>/`
  - Create a new user type: `POST /api/userType/create/`
  - Update an existing user type: `PUT or PATCH /api/userType/<str:pk>/update/`
  - Delete a user type: `DELETE /api/userType/<str:pk>/delete/`

- **User Endpoints**
  - List all users: `GET /api/user/`
  - Retrieve user details: `GET /api/user/<int:pk>/`
  - Create a new user: `POST /api/user/create/`
  - Update an existing user: `PUT or PATCH /api/user/<int:pk>/update/`
  - Delete a user: `DELETE /api/user/<int:pk>/delete/`

## Testing Using Django Admin Interface

To test the API through Django's admin interface, ensure you have created superuser access:

```bash
python manage.py createsuperuser
```

Follow the prompts to set up a username, email, and password. Then, start the server:

```bash
python manage.py runserver
```

Navigate to `http://127.0.0.1:8000/admin/` in your web browser, log in with your superuser credentials, and use the admin interface to create, update, or delete `UserType` and `User` entities.

## Testing Using Postman

[Postman](https://www.postman.com/) is a powerful tool for testing APIs. To use Postman for testing the endpoints:

1. **Install Postman**: Download and install Postman from its official website.
2. **Configure Request**: For each endpoint you wish to test:
   - Select the appropriate HTTP method (GET, POST, PUT/PATCH, DELETE).
   - Enter the request URL, e.g., `http://127.0.0.1:8000/api/userType/` for listing user types.
   - For POST, PUT, and PATCH requests, set the header `Content-Type` to `application/json` and include the request body in JSON format.
   - Send the request and review the response.

### Example: Creating a UserType

- Method: POST
- URL: `http://127.0.0.1:8000/api/userType/create/`
- Headers: Key: `Content-Type`, Value: `application/json`
- Body (raw JSON):
  ```json
  {
    "userTypeName": "New UserType",
    "userTypeDesc": "Description for New UserType"
  }
  ```

Repeat similar steps for other endpoints, adjusting the HTTP method, URL, and request body as necessary.

By following these instructions, you can test the functionality of your API endpoints using both Django's admin interface and Postman.