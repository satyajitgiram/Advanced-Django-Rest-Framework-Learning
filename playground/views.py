from django.core.mail import BadHeaderError
from django.shortcuts import render
from templated_mail.mail import BaseEmailMessage


def say_hello(request):
    try:
        mail = BaseEmailMessage(template_name='emails/welcome.html',context={'name':'Satyajit Giram'})
        mail.send(['satyajitgiram9545@gmail.com'])
        print("MAIL SENT")
    except BadHeaderError:
        print("AN ERROR OCCURED")
        pass
    return render(request, 'hello.html', {'name': 'Satyajit Giram'})
