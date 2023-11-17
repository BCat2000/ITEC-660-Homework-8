# Edit **mycontactsapp/views.py 
# import Contact from Models
from django.http import HttpResponse
from .models import Contact

def index(request):
    #return HttpResponse('Hello World')
    # Display contacts
    mylist = ''
    contactList = Contact.objects.all().order_by('first_name', 'last_name') # The order_by function sorts the query response by first name in ascending order. This is useful since the response is an object of the QuerySet type,  
    
    for i in contactList: # The example code here concatenates all of the contact info into a single string, which means that the sort() function of lists is not available. 
        
        mylist += i.first_name + " " + i.last_name +", " #update this code to list first name and last name as below
        # The above code concatenates a single string with all of the contact names, which are pre-sorted by the order_by() function
        # Henry Fox
        # James Brown
        # Kate Charnes
        # Make sure the list is alphabetically sorted.
    
        
    return HttpResponse("<html style='background-color:tan;'>" +"Brennan Catalan <BR> Professor Bradley Watson <br> Franklin University <br> ITEC 660 <br> 11/9/23" + "<div style='background-color:gray; color:white; border-radius:50px; text-align:center;'>" "All Contacts:<br>" + mylist + "</div>" + "</html>") # Center the list and add other CSS changes
    # update return: Center the list, 
    # and make two other css modifications as you wish.