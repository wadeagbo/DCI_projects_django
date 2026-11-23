# DCI – Django projects

Django and backend projects from the Python Backend Development course at the Digital Career Institute (DCI), Berlin (2022–2023).
Each folder is a separate Django project or exercise.

## Web applications

| Folder | What it does |
|---|---|
| `django-authentication-system-from-scratch-wadeagbo` | user registration, login and logout built without third-party packages |
| `social-website-django-forms-models-wadeagbo` | small social website with models and forms |
| `url_shortener-wadeagbo` | URL shortener |
| `email-api-contact-form-wadeagbo` | contact form that sends email through an API |
| `ecommerce-live-coding-teamrando` | e-commerce site built in a team live-coding session |
| `CRUD_Django_practice` | create, read, update and delete with Django models |

## APIs

| Folder | What it does |
|---|---|
| `reminders-api-wadeagbo` | REST API for reminders |
| `inclass-weather-api-wadeagbo` | app that calls a public weather API |

## Django concepts and exercises

`python-django-start_new_project-wadeagbo`, `python-django-views_and_templating-wadeagbo`, `django-middleware-video-wadeagbo`,
`django-workshop-wadeagbo`, `feb_7_testing_forms_wadeagbo` (testing forms), `live-coding-jan-20-wadeagbo`, `Exercises_and_practices`

## Algorithms

`python-algorithmic_thinking-quicksort-wadeagbo`, `python-algorithmic_thinking-mergesort-wadeagbo`

## Running a project

```bash
cd <folder>
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt   # if the folder has one, otherwise: pip install django
python manage.py migrate
python manage.py runserver
```
