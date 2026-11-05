# AI-Assisted Box Selection System

## Project Overview

The AI-Assisted Box Selection System is a Django REST Framework application that recommends a suitable shipping box for an ecommerce order.

It considers:
- Product dimensions (length, width and height)
- Product weight and quantity
- Shipping box internal dimensions
- Maximum box weight capacity
- Shipping box cost

The system recommends the lowest-cost box that satisfies the packing and weight requirements.

## Technologies Used

- Python 3.12
- Django 6.1.3
- Django REST Framework 3.18.3
- SQLite
- Git and GitHub

## Features

- Product and shipping box management through Django Admin
- Order and order-item management
- Product rotation checking
- Total order weight calculation
- 3D space-based packing heuristic
- Cheapest suitable box recommendation
- REST API for box recommendations
- Automated unit tests

## Project Structure

box-selection-system/
├── config/
├── box_selection/
│   ├── models.py
│   ├── admin.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   ├── services.py
│   └── tests.py
├── manage.py
├── requirements.txt
├── README.md
├── AI_USAGE.md
├── TEST_CASES.md
└── TEST_OUTPUT.md

## Installation and Setup

1. Clone the repository:

git clone YOUR_GITHUB_REPOSITORY_URL
cd box-selection-system

2. Create a virtual environment:

python -m venv venv

3. Activate the virtual environment on Windows:

.\venv\Scripts\Activate.ps1

4. Install dependencies:

pip install -r requirements.txt

5. Apply database migrations:

python manage.py migrate

6. Create an admin account:

python manage.py createsuperuser

7. Start the development server:

python manage.py runserver

8. Open the admin panel:

http://127.0.0.1:8000/admin/

## API Endpoint

POST '/api/recommend-box/'

Example request:

{
  "items": [
    {
      "product_id": 1,
      "quantity": 1
    },
    {
      "product_id": 2,
      "quantity": 1
    }
  ]
}


Example response:

{
  "order_id": 2,
  "total_weight": "2.20",
  "recommended_box": {
    "id": 1,
    "name": "small",
    "cost": "20.00",
    "max_weight": "3.00"
  },
  "message": "Suitable box found."
}


## Packing Approach

The application uses a heuristic-based 3D packing approach.

Products are sorted by volume in descending order. The algorithm checks possible product orientations and places products into available free spaces within the shipping box.

The recommendation process also checks total order weight and selects the lowest-cost suitable box.

Limitation: This is a heuristic approach, not an optimal 3D bin-packing solver. It may fail to find a valid arrangement even when another arrangement exists.

## Running Tests

Execute:

python manage.py test box_selection

## Test Results

Four automated tests currently pass, covering product rotation, total order weight, cheapest suitable box selection and weight-capacity failure.

See `TEST_CASES.md` and `TEST_OUTPUT.md` for details.
