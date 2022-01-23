from django import forms
from django.core.exceptions import ValidationError

SEX_CHOICE = [
    (1, "Male"),
    (2, "Female"),
    (3, "Other")
]


class CreateUserForm(forms.Form):
    nickname = forms.CharField(max_length=30)
    email = forms.EmailField()
    password = forms.CharField(max_length=50, widget=forms.PasswordInput())
    re_password = forms.CharField(max_length=50, widget=forms.PasswordInput())
    sex = forms.ChoiceField(choices=SEX_CHOICE)
    is_staff = forms.BooleanField()
    is_active = forms.BooleanField()

    def clean(self):
        data = super().clean()
        if data.get('password') != data.get('password_repeat'):
            raise ValidationError("hasla nie sa takie same")
        return data
