# Views and templating in Django  

## Tasks
1. So far we have created virtual environment inside 'django-exercise' folder and we have project named 'mysite' with app named 'myapp'.  
*  App handles two urls (both in  app's ```urls.py``` file ), and each url allows user for calling specific view (from ```views.py``` file).  
*  Both views return simple response object (HttpRespons or JsonResponse) with hardcoded values.  

*  **Don't forget to activate you virtualenv!**  

2. Create app-level template ```base.html``` in ```myapp/templates/myapp/``` directory.  
  
*  For now use only HTML. Add some paragraphs  and headers to ```body``` section and empty [block](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#block) for overriding by child templates (name this block 'content'). CSS and JavaScript files will be added later. 

3. Create next app-level template ```about.html``` in the same ```myapp/templates/myapp/``` directory. Use template  extending of ```base.html``` template. Add few HTML tags inside 'content' block.  
Hint: use [extends](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#extends) template tag.  

4. In ```views.py``` file of your ```myapp``` app:  
* add another  function based view (named for example ```base_view```), that uses [render](https://docs.djangoproject.com/en/3.2/topics/http/shortcuts/#render) function with previously created template ```base.html```,
* add class based view (named for example ```AboutView```), that uses previously created template ```about.html```,
*  Hint: you can use [TemplateView](https://docs.djangoproject.com/en/3.2/topics/class-based-views/).

5. Update your app-level ```urls.py```. Import created views and create two different paths (for both views, for example '' and 'about/').

6. Run development server to check if recently added added urls work:  

*  Check links ```http://127.0.0.1:8000/``` and ```http://127.0.0.1:8000/about/``` in the browser. 

7. In the ```base.html``` template add links to other created pages using [url](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#url) template tag

## Input/Output:
```
Working urls, views and templates files.
```
