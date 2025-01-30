from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from .models import CreateMOU

class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    ROLE_CHOICES = [
        ('admin', 'Admin'),
        
        ('customer', 'Student')
    ]

    role = forms.ChoiceField(
        choices=ROLE_CHOICES,
        widget=forms.Select(
            attrs={
                "class": "form-control"
            }
        )
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'role')



class CreateMOUForm(forms.ModelForm):
    class Meta:
        model = CreateMOU
        fields = ['sector', 'first_party', 'second_party', 'department', 'preamble', 'purpose', 'duration', 'pdf_doc']

