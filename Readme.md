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
