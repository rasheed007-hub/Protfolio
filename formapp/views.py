from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


# Create your views here.
from django.core.mail import send_mail
from django.conf import settings

def index(request):
    if request.method == 'POST':
        message = request.POST['message']
        email = request.POST['email']
        name = request.POST['name']
        send_mail(
            'Contact Form',
            message,
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False)
        return JsonResponse({'message': 'Success'})
