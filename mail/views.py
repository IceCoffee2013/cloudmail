from django.shortcuts import render_to_response

# Create your views here.
from mail import mail_manage

def home(request):
    return render_to_response('welcome.html')

def test(request):
    return render_to_response('test.html')

def result(request):
    if 'address' in request.GET:
        address = request.GET['address']
        print address
        mail_manage.sendMail(address)   # send mail
        message = 'You searched for: %r' % request.GET['address']
    else:
        message = 'You submitted an empty form.'
    return render_to_response('result.html', {'data' : message})