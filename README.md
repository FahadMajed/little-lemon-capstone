# Little Lemon Restaurant API

This repository contains the source code for the Little Lemon Restaurant API, a backend development project created as part of Meta's backend development program. The API is designed to support the development for a fictional restaurant. It enables users with different roles, such as customers, managers, and delivery crew members, to browse, add, and edit menu items, place orders, browse orders, assign delivery crew to orders, book tables and deliver orders.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [API Documentation](#api-documentation)
  - [Endpoints](#endpoints)
- [Testing](#testing)
- [Course Information](#course-information)
- [Built With](#built-with)
- [Contributing](#contributing)

## Getting Started

These instructions will help you set up the project on your local machine for development and testing purposes.

### Prerequisites

- Python 3.8+
- pipenv

### Installation

1. Clone the repository:

   ````
   git clone https://github.com/FahadMajed/little-lemon.git
   ```

   ````

2. Change into the project directory:

   ```
   cd little-lemon-api
   ```

3. Install the dependencies using pipenv:

   ```
   pipenv install
   ```

4. Activate the virtual environment:

   ```
   pipenv shell
   ```

5. Apply the migrations:

   ```
   python manage.py migrate
   ```

6. Create a superuser for the Django admin panel:

   ```
   python manage.py createsuperuser
   ```

7. Run the development server:

   ```
   python manage.py runserver
   ```

The API will now be accessible at `http://127.0.0.1:8000/`.

## Usage

1. Access the Django admin panel at `http://127.0.0.1:8000/admin/` and log in using the superuser credentials you created earlier.

2. Create user groups and assign users to these groups as needed.

3. Use a tool like Postman or curl to interact with the API endpoints.

## API Documentation

The API documentation provides detailed information about the available API endpoints, their methods, and roles. The following sections describe the endpoints and provide examples of requests and responses.

### Endpoints

The following are the main API endpoints:

1. **Authentication**

   - `/api/auth/login/` - Log in a user
   - `/api/auth/logout/` - Log out a user
   - `/api/auth/register/` - Register a new user

2. **Menu Items**

   - `/api/menu-items/` - List all menu items (GET), create a new menu item (POST)
   - `/api/menu-items/:id/` - Retrieve (GET), update (PUT), or delete (DELETE) a menu item

3. **Table Bookings**

   - `/api/bookings/tables` - List all bookings (GET), reserve new table (POST)

4. **Orders**

   - `/api/orders/` - List all orders (GET), create a new order (POST)
   - `/api/orders/:id/` - Retrieve (GET), update (PUT), or delete (DELETE) an order
   - `/api/orders/:id/delivery-crew/` - Assign a delivery crew member to an order (PUT)

5. **Delivery Crew**

   - `/api/delivery-crew/` - List all delivery crew members (GET), create a new delivery crew member (POST)
   - `/api/delivery-crew/:id/` - Retrieve (GET), update (PUT), or delete (DELETE) a delivery crew member

#

## Testing

Testing is an essential part of the development process. To ensure that the API functions correctly, tests have been written for each of the main components. Follow these steps to run tests:

1. Activate the virtual environment:

   ```
   pipenv shell
   ```

2. Run the tests:

   ```
   python3.9  manage.py test restaurant/test
   ```

You should see the test results in the terminal. If any tests fail, please review the error messages and make the necessary changes to the code.

## Course Information

This project is a part of Meta's backend development course, which aims to teach students the essentials of building scalable, maintainable, and secure backend systems. The course covers topics such as database design, API development, authentication, authorization, and deployment. By working on projects like the Little Lemon Restaurant API, students gain hands-on experience and develop a deeper understanding of backend development concepts.

For more information about Meta's backend development course and other courses offered by Meta, visittheir [official website](https://www.coursera.org).

## Built With

- [Django](https://www.djangoproject.com/) - The web framework used
- [Django REST framework](https://www.django-rest-framework.org/) - Toolkit for building Web APIs
- [Pipenv](https://pipenv.pypa.io/) - Dependency management and virtual environment

## Contributing

If you would like to contribute to the project, please follow these steps:

1. Fork the repository.
2. Create a new branch with a descriptive name.
3. Make your changes in the branch.
4. Commit and push the changes to your fork.
5. Create a pull request, providing a clear description of your changes.
