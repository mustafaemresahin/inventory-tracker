# Project README

This Django-based project provides a basic inventory management system with user authentication and product tracking. Users can register, log in, and manage an inventory of products. The project involves the use of Django's built-in authentication system, models, forms, and views.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

1. User Registration and Authentication:
   - Users can register for an account.
   - Registered users can log in to their accounts.
   - Authentication is enforced for specific views.

2. Inventory Management:
   - Users can view a list of available inventory items on the home page.
   - Users can delete inventory items that they own or if a special condition is met.

3. Product Tracking:
   - Users can view detailed information about a specific inventory item, including its associated products.
   - Products are listed based on the number of units available.

4. History Tracking:
   - Deleted inventory items are recorded in a history log.

5. User Profile:
   - Users can view and update their profile information.

6. User Registration:
   - Custom user registration form is provided.
   - User profiles are automatically created upon registration.

7. Adding Products:
   - Users can add products to a specific inventory item.
   - Total value of the products is calculated based on the count and price.

8. Detailed Product View:
   - Users can view detailed information about a specific product.

9. UI Pages:
   - About: Displays information about the project.
   - Home: Lists available inventory items and allows deletion.
   - Main: Landing page after logging in.
   - View: Displays details of a specific inventory item and its associated products.
   - Profile: Allows users to view and update their profile information.
   - Add Product: Allows users to add products to an inventory item.
   - Product: Displays detailed information about a specific product.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python [Install Python](https://www.python.org/downloads/)
- Django [Install Django](https://docs.djangoproject.com/en/stable/intro/install/)

## Installation

1. Clone the project repository:

```bash
git clone <repository_url>
```
2. Navigate to the project directory:

```bash
cd <project_directory>
```

3. Install project dependencies:
```bash
pip install -r requirements.txt
```

4. Apply database migrations:
```bash
python manage.py migrate
```
5. Create a superuser (admin) account:
```bash
python manage.py createsuperuser
```

## Usage

1. Start the development server:
```bash
python manage.py runserver
```

2. Access the admin panel by navigating to http://localhost:8000/admin/ and log in with the superuser account.

3. Use the provided UI pages to register, log in, manage inventory items, view and update your profile, and add and view products.

### Inventory Model

The project uses the `Inventory` model to represent inventory items. This model has the following fields:

- `author`: A foreign key to the `User` model, representing the author of the inventory item.
- `title`: A character field representing the title of the inventory item.
- `description`: A character field representing the description of the inventory item.
- `created_at`: A datetime field representing the creation timestamp of the inventory item.
- `updated_at`: A datetime field representing the last update timestamp of the inventory item.

### Product Model

The `Product` model represents individual products associated with an inventory item. It includes the following fields:

- `description`: A text field describing the product.
- `count`: An integer field indicating the product count.
- `upc`: An integer field representing the product's UPC (Universal Product Code).
- `manufacturer`: A character field indicating the product manufacturer.
- `inventory`: A character field indicating the associated inventory item.
- `price`: A decimal field representing the product price.
- `total`: A decimal field representing the total value of the products.
- `picture`: An image field for uploading a picture of the product.

### History Model

The `History` model records historical events within the system. It includes the following fields:

- `title`: A text field describing the history event.
- `created_at`: A datetime field representing the timestamp of the history event.

### Profile Model

The `Profile` model stores user profile information. It includes the following fields:

- `user`: A text field representing the username.
- `name`: A text field representing the user's name.
- `last`: A text field representing the user's last name.
- `email`: A text field representing the user's email.
- `password`: A text field representing the user's password.

### Forms

The project includes several forms for user interactions:

- `RegisterForm`: A form for user registration, including fields for email, first name, and last name.
- `Create`: A form for creating inventory items, including fields for title and description.
- `Add`: A form for adding products to an inventory item, including fields for UPC, description, count, manufacturer, price, and picture (optional).

## Contributing

Contributions to this project are welcome. To contribute, follow these steps:

1. Fork the repository.
2. Create a new branch for your feature/fix.
3. Make your changes and test thoroughly.
4. Commit your changes with appropriate messages.
5. Push your changes to your fork.
6. Submit a pull request to the main repository.

## License

This project is licensed under the MIT License.