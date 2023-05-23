# Ecommerce

## Project dependencies

- Django
- Django restframework
- Pillow

## Custom management command to create sample data

```
python manage.py load_fake_data <number>
```

Replace `<number>` with an actual number to load that number of projects


## Custom management command to delete all products

```
python manage.py delete_products
```