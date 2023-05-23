# Reminders Application API Design challenge

**Deadline for the task is Friday 24th, February 2023 at 12**



Some common mistakes to avoid
-----------------------------

- DO NOT push your virtual environments
- Do not push the `__pycache__` directory
- Please look for an appropriate `.gitignore` file which you can use to avoid these mistakes.
- Do not forget to write tests.
- Do not forget to include a `requirements.txt` file or similar
- Do not forget to `black`en your code so it conforms to PEP8 standards of style

## Mission Notes

Your mission should you accept it is building out a RESTful API application. 

The model schema should look like the following:

```
Reminder
---------

- title (char)
- description (char)
- due_date (Date type)
```

It should have a relationship with the existing Django User model (`django.contrb.auth.models.User`).

One user has many reminders; a 1 to many relationship. Go through this 
https://medium.com/analytics-vidhya/difference-between-one-to-one-many-to-many-and-many-to-one-relationships-in-django-2304b567152f in order to better understand the differences.

The following are 
the URL designs we are going for today.


1) List of All Reminders

    `/api/v1/reminders/` 

2) Get a single Reminder, Updating it and deleting it

    `/api/v1/reminders/<some pk or id>/`


The JSON serializer for results should produce output that looks like this:


```json
{
  "count": 9,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 406275,
      "title": "Running",
      "description": "Running with a few friends",
      "due_date": "2024-01-01T15:00",
      "user": {
        "username": "some username",
        "email": "john@doe.com"
      }
    }
  ]
}

```

Note: The API results should be paginated when getting a list.


3) Add a serializer for the user and only expose list of users and a single user retrieval (do not support other CRUD operations)

- `/api/v1/users/` 
- `/api/v1/users/<some user id>` 

NOTE: DO NOT SUPPORT DELETE, UPDATE and CREATE for users.

```json
{
  "count": 9,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 406275,
      "username": "johndoe",
      "email": "john@doe.com",
      "reminders": [
        {
          "id": 406275,
          "title": "Go running",
          "description": "Running with my friends"
        }
      ]
    }
  ]
}
```

4) Add a test case and CI to your project

Technologies to be used
=======================

- Relational database (SQLITE3 or PostgreSQL)
- Django
- Django Restframework (a 3rd party application we install to build APIs)
