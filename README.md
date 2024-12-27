# Little Lemon API Capstone Final Assignment

This document provides an overview of the API endpoints available in the project, along with their usage instructions.

## Endpoints

### 1. **Login**

- **Endpoint**: `POST http://127.0.0.1:8000/auth/token/login`
- **Description**: Authenticates a user and generates a login token.

### 2. **Create User**

- **Endpoint**: `POST http://127.0.0.1:8000/auth/users/`
- **Description**: Registers a new user.

### 3. **Get Menu Details**

- **Endpoint**: `GET http://127.0.0.1:8000/restaurant/menus/1`
- **Description**: Retrieves the detailed view of a specific menu item.

## Instructions for Running the API

1. **Setup the Environment**:

   - Ensure Python and required dependencies are installed.
   - Install project dependencies using:
     ```bash
     pip install -r requirements.txt
     ```

   Alternatively, create a `pipenv` environment for testing on Windows:

   ```bash
   pip install pipenv
   pipenv install
   pipenv shell
   ```

2. **Start the Server**:

   - Run the development server using:
     ```bash
     python manage.py runserver
     ```

3. **Testing the API**:

   - Use tools like Postman or `curl` to test the endpoints.
   - Replace `127.0.0.1:8000` with the server's IP or domain if hosted remotely.
   - Alternatively, import the `Insomnia_2024-12-27.json` file into Insomnia or Postman for easy testing of API endpoints.

##
