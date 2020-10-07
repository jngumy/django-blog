# Blog system - Django

This is a blog project using Django Framework, Sqlite for the database and Bootsrap and Javascript for the frontend. You can upload your favorite 
posts and classify them in categories such as Movies, Reading, Music, among others and also search posts by name. Production settings and static files included.

## Usage

It's best to install Python projects in a Virtual Environment. Once you have set up a VE, clone this project

```
git clone https://github.com/jngumy/blog_prod.git
```
Then

```
cd blog_prod
```
Once inside the project's folder, 

```
pip install -r requirements.txt #install required packages
python manage.py migrate # run first migration
```

You can set up a superuser account to manage your posts through the admin page, using the following command:

```python
python manage.py createsuperuser
```

To start the server, use the following (by default on localhost:8000):

```python
python manage.py runserver
```

