# My Django Blog Project :newspaper:

This is my Django blog project which uses the Django Rest Framework to build a RESTful API.

## Project Structure :file_folder:

### The project consists of two Django apps:

**posts**: This app contains the models, views, serializers, and urls related to the blog posts.
**users**: This app contains the models, views, serializers, and urls related to the users of the blog.

## Installation :rocket:
To run this project on your local machine, follow these steps:

- Clone this repository: 
```
git clone https://github.com/yourusername/django-blog-project.git.
```
- Navigate into the project directory: 
```
cd django-blog-project.
```

- Create a virtual environment:
```
python -m venv env.
```
- Activate the virtual environment:

(on Linux/Mac):
```
source env/bin/activate 
```
(on Windows):
```
.\env\Scripts\activate .
```


- Install the project dependencies: 
pip install -r requirements.txt.

- Run the migrations:
```
python manage.py migrate.
```
- Create a superuser:
```
python manage.py createsuperuser.
```
- Run the server:
```
python manage.py runserver.
```

## API Endpoints :computer:

The following API endpoints are available:

- GET /api/posts/: Get a list of all blog posts.
- POST /api/posts/: Create a new blog post.
- GET /api/posts/:id/: Get a specific blog post by ID.
- PUT /api/posts/:id/: Update a specific blog post by ID.
- DELETE /api/posts/:id/: Delete a specific blog post by ID.
- GET /api/users/: Get a list of all users.
- POST /api/users/: Create a new user.
- GET /api/users/:id/: Get a specific user by ID.
- PUT /api/users/:id/: Update a specific user by ID.
- DELETE /api/users/:id/: Delete a specific user by ID.