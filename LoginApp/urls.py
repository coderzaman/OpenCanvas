from django.urls import path
from LoginApp import views
app_name = 'Login'

urlpatterns = [
    path('signup/',views.signup, name='signup'),
    path('user_sign_in/',views.user_sign_in, name='user_sign_in'),
    path('sign_out/',views.sign_out, name='sign_out'),
    path('profile/',views.profile, name='profile'),
    path('update_profile/',views.user_change, name='update_profile'),
    path('password/',views.pass_change, name='changed_password'),
    path('add_profile_pic/',views.add_profile_pic, name='add_profile_pic'),
    path('update_profile_pic/',views.update_profile_pic, name='update_profile_pic'),
]
