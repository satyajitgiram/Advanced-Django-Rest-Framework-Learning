from django.core.mail import BadHeaderError, EmailMessage
from django.shortcuts import render


def say_hello(request):
    try:
        mail = EmailMessage("Subject","Body",'from@gmail.com',['to@gmail.com'])
        mail.attach_file('playground/static/images/bmw.jpeg')
        mail.send()
        print("MAIL SENT")
    except BadHeaderError:
        print("AN ERROR OCCURED")
        pass
    return render(request, 'hello.html', {'name': 'Mosh'})
