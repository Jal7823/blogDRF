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

### Post

- GET /posts/: Get a list of all blog posts.
- POST /posts/: Create a new blog post.
- GET /posts/:id/: Get a specific blog post by ID.
- PUT /posts/:id/: Update a specific blog post by ID.
- DELETE /posts/:id/: Delete a specific blog post by ID.
- GET /posts/: Get a list of all users.
- POST /posts/: Create a new user.
- GET /posts/:id/: Get a specific user by ID.
- PUT /posts/:id/: Update a specific user by ID.
- DELETE /posts/:id/: Delete a specific user by ID.

### Token
- POST /token: create new token 
- POST /token/refresh: refresh token

### Users
- POST /users/register: register a new users