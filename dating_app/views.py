from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render, redirect

# Create your views here.
from dating_app.forms import EmailUserCreationForm


def home(request):
    return render(request, 'index.html')


def video(request):
    return render(request, 'video.html')


def theone(request):
    return render(request, 'theone.html')


def questions(request):
    return render(request, 'questions.html')


def payment(request):
    return render(request, 'payment.html')

# def charge(request):
#     return render(request, 'charge.html')


def register(request):
    if request.method == 'POST':
        form = EmailUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = EmailUserCreationForm()

    return render(request, "registration/register.html", {
        'form': form,
    })
