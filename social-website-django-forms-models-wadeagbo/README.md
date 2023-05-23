## Social media application

Some code has been provided for the student, it has django-alluth enabled so you already have a way to create an account on the system.

e.g. `http://localhost:8000/acc/signup`

To login, user visits the following link: 

Tasks for the students include the following:

- Study the `UserProfile` model and add a `__repr__` method so that we can easily tell what is inside.
  - You can play with the shell plus extension by creating some users on the system as well as UserProfiles 
  
```python
user = User.objects.first()

# make a user profile
user_profile = UserProfile.objects.create(user = user, bio="Awesome person")

# if you want to see the list of followers of that user, you can type this:

user_profile.followers.all() # It is a queryset, most of the methods you know about ORM will work
```
- Create an application called "tweets", in that application design a model called `Tweet` that contains the following attributes:
    - message
    - created_at (date at which the message was created)
    - user (the person that created the message)

In the tweets application, create a form and corresponding views / templates and use a ModelForm. You are only allowed to use Class based views.


- Build out the functionality that updates our database record when a user "follows" another user. Some tips have been left in the TODO.
- As soon as someone follows a person (by clicking a button), an email should be sent to that person telling them they have a new follower.
- As a constraint, someone should not be able to follow a user more than once (logic should be provided to check for existing followers before adding new ones)

Other improvements that you can make include:
- Change the button from "follow" to "unfollow" after following

For now, functionality to unfollow is not expected to be implemented. This is left as a challenge for the student.

>Note: To avoid any issues, I encourage you to pair up with a buddy and use their email as a test to confirm that an email was received.
