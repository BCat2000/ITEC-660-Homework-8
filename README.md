Homework-8

We will use Django templates and static files in this homework.

#Clone using your repository
git clone https://github.com/ITEC660/homework-8-profkemalaydin

Please copy your previous homework environment into "Homework 8" folder.

#Please change directory names accordingly
cp -r myproject/* ../hw8

MVC stands for Model View Controller. MVC is a general framework for the separation of concerns. Templates are the View portion of that framework.

Templates are essential for maintaining complex and dynamic applications. They require significantly less time to build. Lists can be populated programmatically. Templates can be reused. Templates prevent SQL injection by escaping user data.

Let's setup a template. Create a folder named "templates" inside "mycontactsapp". Add the following content for "index.html" file.

<!DOCTYPE html>
<html lang = "en">

<head>
  <title>Page Title</title>
  <link rel="stylesheet" href={% static 'styles.css' %} />
</head>
<body>

<h1>My Contacts</h1>
<p>This is only the first one:</p>
<p>{{contacts.0.first_name}}</p>
</body>
</html>

Update views.py file so you can use contacts in the index.html.

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Contact

def index(request):
    #return HttpResponse('Hello World')

    # Display contacts
    all_contacts = Contact.objects.all()
    
    return render(request, 'index.html', {'contacts':all_contacts})

Run the website and check if the first contact name is displayed.
Please complete the following:

    Add a for loop to display all contacts. This will be similar to v-for in Vue but using python and Django syntax. Please do your research and find a solution.
    Add more users using the admin interface and make sure they are displayed on the website. (You can access admin interface via: http://localhost:8000/admin/)
    Use {% load static %} inside index.html appropriately so it can reach the static files and use styles.css.
    Update styles.css with your design. Change at least three properties.
    Make sure you push your repository back with the working version of your code.
