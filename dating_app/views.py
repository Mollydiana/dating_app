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
            user = form.save()
#            user.email_user("Welcome!", "Thank you for signing up for our website.")
#            text_content = 'Thank you for signing up for our website, {}{}'.format(user.first_name, user.last_name)
#            html_content = '<h2>Thanks {}{} for signing up!</h2> <div>I hope you enjoy using our site</div>'.format(user.first_name, user.last_name)
#            msg = EmailMultiAlternatives("Welcome!", text_content, settings.DEFAULT_FROM_EMAIL, [user.email])
#            msg.attach_alternative(html_content, "text/html")
#            msg.send()
            return redirect("login")
    else:
        form = EmailUserCreationForm()

    return render(request, "registration/register.html", {
        'form': form,
    })
