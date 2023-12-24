from django.core.mail import BadHeaderError
from django.shortcuts import render
from templated_mail.mail import BaseEmailMessage
from .tasks import notify_customers


def say_hello(request):
    # Send Mail 
    # try:
    #     mail = BaseEmailMessage(template_name='emails/welcome.html',context={'name':'Satyajit Giram'})
    #     mail.send(['satyajitgiram9545@gmail.com'])
    #     print("MAIL SENT")
    # except BadHeaderError:
    #     print("AN ERROR OCCURED")
    #     pass
    notify_customers.delay("Hello")

    

    return render(request, 'hello.html', {'name': 'Satyajit Giram'})
