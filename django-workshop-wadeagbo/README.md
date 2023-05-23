Welcome to the one-day workshop on Django frontend development! In this workshop, we will cover several essential
topics related to Django templating language, including tags, logic within templates, passing variables from views to
templates, and template inheritance.

This workshop is designed to be hands-on, so please make sure you have your laptop with you, and you have Django
installed in your system. If you haven't installed Django yet, please visit the official Django website and follow the
installation instructions.

First let's try to understand the concepts and syntax of DTL.

# Django Templating Language

Django Templating Language (DTL) is a built-in templating system in Django that allows you to build dynamic web pages by
defining reusable templates that can be filled with data from your Python code. In this way, you can separate the
presentation layer from the business logic of your application.

DTL includes various tags and filters that allow you to perform different operations within templates, such as loops,
conditionals, and accessing object attributes. Here's an overview of some of the most commonly used tags and filters:

## Tags

| Tag                           | Description                                                                                               |
|-------------------------------|-----------------------------------------------------------------------------------------------------------|
| {% block %}:                  | Defines a named block that can be overridden in child templates using {% extends %} and {% block %} tags. |
| {% extends %}:                | Specifies that the current template extends a parent template, and overrides one or more of its blocks.   |
| {% include %}:                | Includes the content of another template in the current template.                                         |
| {% if %} and {% elif %}:      | Conditionally include content based on a boolean expression.                                              |
| {% for %} and {% endfor %}:   | Loops over a sequence and includes content for each item in the sequence.                                 |
| {% with %} and {% endwith %}: | Assigns a value to a variable for use within the current block.                                           |

**{% block %}**

The **{% block %}** tag defines a named block that can be overridden in child templates using the **{% extends %} and {%
block %}** tags.

```html
<!-- base.html -->
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}{% endblock %}</title>
</head>
<body>
<div class="header">
    {% block header %}
    <h1>Welcome to my site!</h1>
    {% endblock %}
</div>
<div class="content">
    {% block content %}
    {% endblock %}
</div>
<div class="footer">
    {% block footer %}
    <p>Copyright &copy; 2023</p>
    {% endblock %}
</div>
</body>
</html>
```

The {% block %} tags define named blocks for the page title, header, content, and footer. In a child template that
extends this base template, any of these blocks can be overridden by defining a block with the same name.

**{% extends %}**

The **{% extends %}** tag specifies that the current template extends a parent template, and overrides one or more of
its blocks.

```html
<!-- child.html -->
{% extends "base.html" %}

{% block title %}
My Page Title
{% endblock %}

{% block header %}
<h1>Welcome to my awesome site!</h1>
{% endblock %}

{% block content %}
<p>This is my page content.</p>
{% endblock %}
```

The child.html template extends the base.html template and overrides the title, header, and content blocks with its own
content.

**{% include %}**

The **{% include %}** tag includes the content of another template in the current template.

```html
<!-- my_template.html -->
{% include "header.html" %}

<p>This is my page content.</p>

{% include "footer.html" %}
```

In this example, the my_template.html template includes the contents of header.html and footer.html templates.

**{% if %} and {% elif %}**

The {% if %} and {% elif %} tags conditionally include content based on a boolean expression. For example:

```html
{% if user.is_authenticated %}
<p>Welcome, {{ user.username }}!</p>
{% else %}
<p>Please log in to view this content.</p>
{% endif %}
```

In this example, the if tag checks if the user is authenticated and includes a welcome message with the username if they
are, or a message to log in if they are not.

**{% for %} and {% endfor %}**

The {% for %} and {% endfor %} tags loop over a sequence and include content for each item in the sequence. For example:

````html
{% for item in items %}
<li>{{ item }}</li>
{% endfor %}
````

In this example, the for tag loops over the items sequence and includes an **\<li>** element for each item in the
sequence.

**{% with %} and {% endwith %}**

The {% with %} and {% endwith %} tags assign a value to a variable for use within the current block. For example:

```html
{% with author=book.author %}
<p>{{ author.first_name }} {{ author.last_name }}</p>
{% endwith %}
```

## Filters

**{{ var|filter }}:**

Applies a filter to a variable before outputting it. Filters can modify the output of the variable in various ways, such
as truncating text, formatting dates, or escaping special characters.
To pass variables from views to templates, you can use the render function provided by Django's shortcuts module. This
function takes a request object, a template name, and a context dictionary as arguments. The context dictionary contains
the variables that you want to make available in the template. Here's an example:

````python
from django.shortcuts import render


def my_view(request):
    my_var = "Hello, world!"
    context = {'my_var': my_var}
    return render(request, 'my_template.html', context)
````

In the example above, the my_var variable is passed to the template my_template.html using a context dictionary. In the
template, you can access this variable using the {{ my_var }} syntax.

## Template inheritance

Template inheritance is a powerful feature of DTL that allows you to define a base template with common elements, such
as the header, footer, and navigation menu, and extend it in child templates to fill in the unique content. Here's an
example:

**base.html:**

```html
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}{% endblock %}</title>
</head>
<body>
{% block content %}
{% endblock %}
</body>
</html>
```

**child.html:**

```html
{% extends "base.html" %}

{% block title %}
My Page Title
{% endblock %}

{% block content %}
<p>This is my page content.</p>
{% endblock %}
```

In this example, the child.html template extends the base.html template and overrides the title and content blocks to
define its own content. When the child.html template is rendered, it will include the contents of the base.html template
and replace the blocks with its own content.

## Live Coding - Follow Along Project

Throughout the workshop, we will be working on a hands-on project, which will give you practical experience with Django
templating language. The project is to build a simple blog application that allows users to create and view blog posts.

Let's get started with the project!

**Step 1:** Create a Django project

The first step is to create a new Django project. Open your terminal or command prompt and run the following command:

`django-admin startproject blog_project`

This will create a new directory called **blog_project** in your current directory, which contains the basic structure
of a Django project.

**Step 2:** Create a new Django app

Next, we need to create a new Django app within the project. Run the following command in your terminal or command
prompt:

`python manage.py startapp blog`

This will create a new directory called **blog** within the **blog_project** directory, which contains the basic
structure of a Django app.

**Step 3:** Define the Post model

In the blog app directory, open the **models.py** file and define the **Post** model as follows:

````python
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
````

This defines a simple **Post model** with three fields: _title, content, and created_at_. The _title_ and _content_
fields
are a CharField and TextField, respectively, and the _created_at_ field is a DateTimeField that is automatically set to
the current date and time when a new post is created.

**Step 4:** Set up the database

Now that we've defined the **Post** model, we need to create the corresponding database table. Run the following command
in
your terminal or command prompt:

`python manage.py makemigrations`

This will generate a new migration file in the **blog/migrations** directory, which contains the instructions for
creating
the **Post table** in the database.

Next, run the following command to apply the migration and create the table in the database:

`python manage.py migrate`

**Step 5:** Create a Django admin user

Before we can create any posts, we need to create a **superuser** who can log in to the Django admin panel and create
new
posts. Run the following command in your terminal or command prompt:

`python manage.py createsuperuser`

This will prompt you to enter a _username, email (optional), and password_ for the superuser. Once you've entered the
details, the superuser will be created.

**Step 6:** Define the views

Next, we need to define the views that will render the blog posts. Open the **views.py** file in the blog app directory
and
define two views as follows:

````python
from django.shortcuts import render
from .models import Post


def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
````

The **post_list** view retrieves all the **Post** objects from the database and passes them to the **
blog/post_list.html** template
as a context variable called **posts**. The **post_detail** view retrieves a **single Post** object based on the
specified primary
key (**pk**) and passes it to the **blog/post_detail.html** template as a context variable called **post**.

**Step 7:** Define the URL patterns

Now that we've defined the views, we need to define the **URL patterns that map the URLs to those views**. Open the **
urls.py**
file in the blog app directory and define the URL patterns as follows:

````python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]
````

The first URL pattern maps the **root URL (/)** to the **post_list** view, and the second URL pattern maps URLs of the
form
**/post/<pk>/ to the post_detail view**, where <pk> is the primary key of the post.

**Step 8:** Create the templates

Now that we've defined the views and URL patterns, we need to create the templates that will render the blog posts. In
the blog app directory, create a new directory called **templates**, and within that directory, create another directory
called **blog**.

Inside the blog directory, create two new files: **post_list.html and post_detail.html**. The post_list.html template
should
look something like this:

````html
{% extends 'base.html' %}

{% block content %}
{% for post in posts %}
<div class="post">
    <h2><a href="{% url 'post_detail' pk=post.pk %}">{{ post.title }}</a></h2>
    <p class="date">{{ post.created_at|date:"F d, Y" }}</p>
    <p>{{ post.content }}</p>
</div>
{% endfor %}
{% endblock %}
````

This template extends a base template called base.html and iterates over the posts context variable, displaying the
title, creation date, and content of each post. The url template tag is used to generate the URL for the post_detail
view, based on the post's primary key (pk).

The post_detail.html template should look something like this:

````html
{% extends 'base.html' %}

{% block content %}
<div class="post">
    <h2>{{ post.title }}</h2>
    <p class="date">{{ post.created_at|date:"F d, Y" }}</p>
    <p>{{ post.content }}</p>
</div>
{% endblock %}
````

This template also extends the base.html template and displays the title, creation date, and content of a single post.


> **NOTE:**
> 
> **{% extends 'base.html' %}** - This tag is used to inherit the contents of another template file, in this case,
> base.html. This means that the current template will include all the content from the base.html template and only
> replace the content defined in {% block %} tags.
>
>**{% block content %} and {% endblock %}** - These tags define a block of content that can be overridden by child
> templates that extend this template. In this case, the content within this block is being replaced with the contents of
> a loop that follows.
>
>**{% for post in posts %} and {% endfor %}** - This tag is used to loop through a set of objects and perform some
> action on each object. In this case, the loop is iterating over the posts queryset and rendering a `<div>` element for
> each post.
>
>**{% url 'post_detail' pk=post.pk %}** - This tag is used to generate a URL for a specific view, in this case, the
> post_detail view with the primary key pk parameter set to the current post's primary key.
>
>**{{ post.title }}, {{ post.created_at|date:"F d, Y" }}, and {{ post.content }}** - These are variable tags used to
> display the values of the title, created_at, and content fields of the post object, respectively. The date filter is
> also applied to post.created_at to format it in the "F d, Y" date format.



**Step 9:** Define the base template
The templates we just created extend a base template called base.html, so we need to define that template as well. In
the templates directory of the blog_project directory, create a new file called **base.html** and define it as follows:

````html
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}Blog{% endblock %}</title>
</head>
<body>
<h1><a href="/">Blog</a></h1>
{% block content %}
{% endblock %}
</body>
</html>
`````

This template defines the basic structure of an HTML document, including a title, a header with a link to the root URL,
and a **block** called content, which will be replaced by the content of the extending templates.

> **NOTE**: Django tags are special instructions or template directives used in Django's templating language. They allow
> you
> to perform certain operations and control the output of your web application's templates.
>
>The **{% block %}** tag is used to define a block of content that can be overridden in a child
> template. This allows you to define a template once and reuse it in multiple places, while allowing for customizations
> in specific instances.
>
>The **{% block title %}** and **{% block content%}** tags define areas in the template that can be overridden by child
> templates. The title block is used to set the title of the HTML document, while the content block is where the main
> content of the page will go.
>
>When a child template extends the base template, it can provide its own content for these blocks by using the same
> **{% block %}** tag and giving it a unique name. This allows the child template to reuse the base template while still
> customizing the content as needed.

**Step 10:** Run the development server

Finally, we're ready to test our blog application! Run the following command in your terminal or command prompt to start
the development server:

`python manage.py runserver`

This will start the server, and you should be able to view the blog by visiting http://localhost:8000 in your web
browser. You can log in to the admin panel by visiting http://localhost:8000/admin/ and entering the credentials you
created in Step 5.

Congratulations, you've built a simple blog application using Django! In this workshop, we covered several essential
topics related to Django templating language, including tags, logic within templates, passing variables from views to
templates, and template inheritance. We also created a hands-on project that gave you practical experience with these
concepts.

Of course, there's still much more to learn about Django and web development in general. I encourage you to continue
exploring the Django documentation and experimenting with building more complex applications.


## Project

### Objective

The objective of this project is to create a web page that displays a list of books and allows users to add new books to
the list.

### Duration

This project should take approximately 1-2 hours to complete, depending on your experience with Django.

### Complexity

This project is suitable for beginners with some experience with Django templates and forms.

### Task

1. Create a new Django project and app.
2. Define a Book model with fields for title, author, and publication date.
3. Create a form for adding new books to the database.
4. Create a view that displays a list of all books in the database.
5. Create a template that displays the list of books and the form for adding new books.
6. Use DTL tags and filters to display the data in the template.

### Solution

Here is a possible solution for this project:

**STEP 1:** Create a new Django project and app:
Run the following commands in your terminal:

````python
django - admin
startproject
booklist
cd
booklist
python
manage.py
startapp
book
````

**STEP 2:** Define a Book model with fields for title, author, and publication date:
Open the book/models.py file and add the following code:

```python
from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    publication_date = models.DateField()
```

**STEP 3:** Create a form for adding new books to the database:
Open the book/forms.py file and add the following code:

```python
from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_date']
```

**STEP 4:** Create a view that displays a list of all books in the database:
Open the book/views.py file and add the following code:

```python
from django.shortcuts import render
from .models import Book


def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})
```

**STEP 5:** Create a template that displays the list of books and the form for adding new books:
Create a new file called book_list.html in the book/templates directory and add the following code:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Book List</title>
</head>
<body>
<h1>Book List</h1>
<ul>
    {% for book in books %}
    <li>{{ book.title }} by {{ book.author }} ({{ book.publication_date }})</li>
    {% endfor %}
</ul>
<h2>Add a new book</h2>
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Add</button>
</form>
</body>
</html>
```

**STEP 6:** Use DTL tags and filters to display the data in the template:
In the book_list.html template, we used the for loop and the if statement DTL tags to iterate over the list of books and
check if it's empty:

```html
{% for book in books %}
<li>{{ book.title }} by {{ book.author }} ({{ book.publication_date }})</li>
{% empty %}
<li>No books yet.</li>
{% endfor %}
```

We also used the csrf_token template tag to add a Cross-Site Request Forgery (CSRF) token to the form:

`{% csrf_token %}`

And we used the as_p method of the form object to display the form fields as paragraphs:

`{{ form.as_p }}`

Finally, we added a button element to submit the form:

`<button type="submit">Add</button>`

**STEP 7:** Define URL patterns:
Open the book/urls.py file and add the following code:

```python
from django.urls import path
from .views import book_list

urlpatterns = [
    path('', book_list, name='book_list'),
]
```

**STEP 8:** Register the app and run the server:
Open the booklist/settings.py file and add the following code to the INSTALLED_APPS list:

`INSTALLED_APPS = [    'book', ...]`

Then, run the following command in your terminal:

`python manage.py runserver`

Now you can visit the Book List page in your web browser at http://localhost:8000/. You should see the list of books (
which is currently empty) and the form for adding new books.

When you fill out the form and click the "Add" button, the data will be sent to the server and a new book will be added
to the database. You can verify this by running the following command in your terminal:

`python manage.py shell`

And then executing the following Python code:

````python
from book.models import Book
Book.objects.all()
````

This should display a list of all books in the database, including the one you just added.

That's it! You have successfully created a Django web page that displays a list of books and allows users to add new
books to the list. Of course, this is just a starting point, and you can customize and improve the project in many ways.
For example, you could add validation to the form fields, implement editing and deleting of existing books, or use
pagination to display a limited number of books per page.


Thanks for attending this workshop, and happy coding!