# AI Usage Documentation

## 1. AI Tool Used
ChatGPT was used as an AI assistance tool during the development of the AI-Assisted Box Selection System.

## 2. Areas Where AI Assistance Was Used
- Understanding Django project structure and application setup.
- Understanding Django models, serializers, views, and URL routing.
- Developing the box recommendation and order-weight calculation logic.
- Understanding API implementation and request validation.
- Writing and debugging automated test cases.
- Understanding errors encountered during development.

## 3. Prompts Used
Examples of prompts used during development:
1. How do I create and configure a Django project?
2. How can I create models for products, shipping boxes, and orders?
3. How can I calculate the total weight of an order?
4. How can I recommend the cheapest suitable shipping box?
5. How can I create and test a REST API using Django REST Framework?
6. How can I run automated tests in Django?

## 4. AI Suggestions Accepted
- Guidance on Django project structure and configuration.
- Suggestions for creating models and API serializers.
- Guidance on implementing box recommendation logic.
- Suggestions for writing automated tests.
- Explanations of Django commands and error messages.

## 5. Corrections and Improvements
- Updated the `ALLOWED_HOSTS` setting after encountering a test client host validation error.
- Corrected project setup and terminal command issues during development.
- Reviewed API responses and test results to verify the implementation.

## 6. Verification
AI-generated suggestions were reviewed and tested manually.

The following checks were performed:
- Django migrations completed successfully.
- Django admin was used to add sample products and shipping boxes.
- API endpoint was tested using Django REST Framework's APIClient.
- Automated tests were executed using `python manage.py test box_selection`.
- All four automated test cases passed successfully.

## 7. Known Limitations
The box-packing implementation uses a heuristic approach. It checks product orientations and available spaces but does not guarantee an optimal packing arrangement for every possible combination of products.

## 8. Conclusion
ChatGPT was used as a supporting tool