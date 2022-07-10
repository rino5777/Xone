
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import OwnerUrls
from django import forms



class UserRegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):   # игнорирование стандартных стилей 
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({ 'class': 'form-control', 'placeholder': 'пароль' , 'rows': 1, })
        self.fields['password2'].widget.attrs.update({ 'class': 'form-control', 'placeholder': 'подтвердите пароль' , 'rows': 1, })
       
        self.fields['username'].widget.attrs.update({ 'class': 'form-control', 'placeholder': 'логин' , 'rows': 1, })
        

    class Meta:
        model = User
        fields = [ 'username', 'password1', 'password2']

    
class OwnerUrlsForm(ModelForm):
    def __init__(self, *args, **kwargs):   # игнорирование стандартных стилей 
        super().__init__(*args, **kwargs)
        self.fields['long_url'].widget.attrs.update({ 'class': 'form-control', 'placeholder': 'введите url' })
        
    
    class Meta:
        model = OwnerUrls
        fields = '__all__'
        exclude = ['owner', 'short_url',]
    
        

