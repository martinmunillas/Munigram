from django import forms

from django.contrib.auth.models import User

class SignUpForm(forms.Form):
    username = forms.CharField(max_length=50, min_length=4)

    password = forms.CharField(max_length=70, min_length=8, widget=forms.PasswordInput())
    password_confirmation = forms.CharField(max_length=70, min_length=8, widget=forms.PasswordInput())

    first_name = forms.CharField(min_length=2, max_length=20)
    last_name = forms.CharField(min_length=2, max_length=20)

    email = forms.CharField(min_length=6, max_length=70, widget=forms.EmailInput())

    def clean_username(self):
        user = self.cleaned_data['username']
        q = User.objects.filter(username=user).exists()
        if q:
            raise forms.ValidationError('Username is already in use')
        return user
    def clean(self):
        data = super().clean()
        password = data['password']
        password_confirmation = data['password_confirmation']
        if password != password_confirmation:
            raise forms.ValidationError('Password confirmation does not match')
        else:
            return data

class ProfileForm(forms.Form):
    website = forms.URLField(max_length=200, required=True)
    biography = forms.CharField(max_length=500, required=False)
    phone_number = forms.CharField(max_length=20, required=True)
    picture = forms.ImageField()