from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import UserRegistrationForm
from django.contrib.auth import  logout
from django.views.generic import TemplateView
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
# Create your views here.
from .forms import OwnerUrlsForm
from .models import OwnerUrls
import time
def account(request ):
    ownerlist = {}
    actual = ''
    user = request.user
    history = OwnerUrls.objects.all()
    #--------------------------------------------->перевести в клас и передать во вьюс главный
    for i in history:
        if i.owner == user:
                ownerlist[i.short_url] = i.long_url
                actual = list(ownerlist.keys())[-1::][0]

    return render (request, 'user_pages/account-profile.html', {'user':user, 'ownerlist':ownerlist, 'history':history})



def registr(request):

    form = UserRegistrationForm(request.POST)
    data = {}
    if request.method == 'POST':
        if form.is_valid():
            form.save(commit='FALSE')
            form.changed_data
            
            messages.success(request, 'Отлично, теперь авторизируйтесь !')
            return redirect('user:authorization')
    else: 
        return render(request, 'user_pages/account-signin.html',{ 'form':form } ,)
    return render(request, 'user_pages/account-signin.html',{ 'form':form })


class SigninView(TemplateView):
    
    template_name = 'user_pages/account-login.html'

    def dispatch(self, request, *args, **kwargs):
        error_dict = {}
        
        if request.method == 'POST':
            
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                
                login(request, user)
                return redirect('user:account')
            else:
                 messages.success(request, 'Username/Password Invalid')

	    
        return render(request, self.template_name, error_dict)


def logoutuser(request):
    logout(request)
    return redirect('/')



