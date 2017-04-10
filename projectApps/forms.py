from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User, Group

class CommentForm(forms.Form):
    comment = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': 'enter your comment'
            }))

class ResultForm(forms.Form):
    # result = User.objects.all()
    user = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={
            'name':'username',
        })
    )


class LoginForm(AuthenticationForm):
    username=forms.CharField(
        label="Username",
        max_length=30,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'name':'username',
        })
    )
    password=forms.CharField(
        label="Password",
        max_length=32,
        widget=forms.PasswordInput()
    )


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(
        label="Email",
        required=True
        )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user=super(RegistrationForm,self).save(commit=False)
        user.email=self.cleaned_data["email"]
        if commit:
            user.save()
        return user
