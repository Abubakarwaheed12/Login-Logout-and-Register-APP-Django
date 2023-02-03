from django.urls import path
from . import views
urlpatterns = [
    path('signup/' , views.signup , name='signup'),
    path('' , views.signin , name='login'),
    path('profileuser/' , views.user_profile , name='profile'),
    path('logout/' , views.logout_user , name='logout_user'),
    path('changepass/' , views.changepass , name='changepass'),
    path('userdetails/<int:id>' , views.userdetails , name='userdetails')
]