import re
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from dating_app.models import Dater


def validate_name(value):
    if not re.match(r'[a-zA-Z]{1,20}', value):
        raise ValidationError("Please enter a valid name")


class EmailUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = Dater
        fields = ("username", "email", "password1", "password2")

    def clean_username(self):
        # Since User.username is unique, this check is redundant,
        # but it sets a nicer error message than the ORM. See #13147.
        username = self.cleaned_data["username"]
        try:
            Dater.objects.get(username=username)
        except Dater.DoesNotExist:
            return username
        raise forms.ValidationError(
            self.error_messages['duplicate_username'],
            code='duplicate_username',
        )
