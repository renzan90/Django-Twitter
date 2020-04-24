from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.utils.html import strip_tags
from TClone.models import Tweet

class UserCreateForm(UserCreationForm):
    email=forms.EmailField(required=True, widget=forms.widgets.TextInput(attrs={'class': 'special'}))
    first_name=forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder':'First Name'}))
    last_name=forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder':'Last Name'}))
    username=forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder':'username'}))
    password1=forms.CharField(required=True, widget=forms.widgets.PasswordInput(attrs={'placeholder':'password', }), max_length=32)
    password2=forms.CharField(required=True, widget=forms.widgets.PasswordInput(attrs={'placeholder':'password'}), max_length=32)

    def is_valid(self):
        form = super(UserCreateForm, self).is_valid()
        for f, error in self.errors.items():
            if f != '__all_':
                self.fields[f].widget.attrs.update({'class': 'error', 'value': strip_tags(error)})
        return form
 
    class Meta:
        fields = ['email', 'username', 'first_name', 'last_name', 'password1',
                  'password2']
        model = User



class LoginForm(AuthenticationForm):

    username = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '', 'id': 'hello'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '', 'id': 'hi',}))

    def is_valid(self):
        form = super(LoginForm, self).is_valid()
        for f, error in self.errors.items():
            if f != '__all__':
                self.fields[f].widget.attrs.update({'class': 'error', 'value': strip_tags(error)})
        return form

class TweetForm(forms.ModelForm):
    class Meta:
        model=Tweet
        fields=['text',]