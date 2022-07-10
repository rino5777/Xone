from django.urls import path 
from . import views
from user.views import SigninView

app_name = 'user'


urlpatterns = [
    
    path('account', views.account, name = 'account' ),
    path('logout', views.logoutuser, name = 'logout' ),
    path('registr', views.registr, name = 'registr' ),
    path('authorization',  SigninView.as_view(), name = 'authorization'),
]