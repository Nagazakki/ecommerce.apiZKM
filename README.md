E-Commerce Product API (ZKM)

Overview
This project is a Django REST Framework-based E-Commerce Product API, built as part of a backend engineering capstone. It provides secure and extensible endpoints for managing users, products, categories, and reviews — with JWT authentication, product filtering, and stock management support.

The goal was to build a professional-grade backend capable of supporting a full-featured e-commerce application.

1. Project Initialization
Commits: dcd9ff5, 3001f9c, 1594c47, c5c5a82, f60a5c1

- Initialized a new Django project named ecommerce_api and created the foundational app structure.
- Verified that the local development server was running correctly.
- Added a starter README and basic configurations.

2. Core App Setup and Product Model
Commits: afd70d6, 4e41872, e02f33d, bc395c4

- Created the products app.
- Defined the initial Product model with essential fields like name, description, price, stock_quantity, and image_url.
- Connected the model data to the Django admin panel and REST framework.
- Exposed the /api/products/ endpoint through DRF for easy access and testing.

3. Product Seeding and CRUD Access
Commits: 15cedc0, 8b5f78a, b566d98

- Implemented a seed.py script to populate the database with initial product data.
- Secured CRUD operations so only authenticated users could create, update, or delete products.
- Limited unauthorized users to read-only access.
- Ensured that malformed or incomplete data could not enter the database.

4. Filtering, Searching, and Pagination
Commits: 63337f8, e8105f6

- Added query-based product filtering (by name, price, and category).
- Enabled full-text search across product fields.
- Integrated pagination for improved performance and cleaner API responses.
- Enhanced the /api/products/ endpoint to support flexible queries and cleaner data retrieval.

5. Authentication and User Management
Commits: 89bc7fe, fa2c4af, e208e69, 2c2f1bd

- Integrated JWT Authentication to secure endpoints.
- Implemented user registration, login, and profile management endpoints.
- Verified authentication workflows using Postman and ensured only verified users could perform sensitive operations.
- Confirmed token-based access and refresh mechanisms were working correctly.

6. Category Model and Data Relationships
Commit: b767cf3

- Reintroduced and restructured the Category model to allow proper product classification.
- Updated serializers, viewsets, and routes to reflect the many-to-one relationship between Category and Product.
- Enhanced seed data to include categories dynamically during database seeding.

7. Reviews and Testing
Commit: 5e8a51d

- Added a Review model linking users and products.
- Enabled authenticated users to submit ratings and comments for products.
- Adjusted the API to display average product ratings and associated reviews.
- Reseeded the database and verified functionality through the Django shell and API testing.

8. Additional Enhancements
- Verified user permissions for CRUD operations.
- Implemented proper error handling and data validation.
- Confirmed stability of all endpoints and relationships after reseeding and model changes.
- Prepared for deployment and UI polishing (including optional styling and stock management features).

9. Future Improvements
- Stock Management: Automatically adjust stock quantity after purchases.
- Discounts and Promotions: Add logic for temporary price adjustments.
- Frontend Integration: Connect to a React or Next.js client for live visualization.
- Enhanced Styling: Override DRF templates for a more polished, branded API interface.

Technologies Used
- Backend: Django 5.x, Django REST Framework
- Authentication: JWT (via djangorestframework-simplejwt)
- Database: SQLite (development)
- Environment: Python 3.12, Django ORM
- Testing: Postman, Django shell

Author
Zachary Kariuki Mohamed
Backend Developer & Psychology Graduate