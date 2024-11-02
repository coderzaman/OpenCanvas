from django.urls import path
from LoginApp import views
app_name = 'Login'

urlpatterns = [
    path('signup/',views.signup, name='signup'),
    path('user_sign_in/',views.user_sign_in, name='user_sign_in'),
    path('sign_out/',views.sign_out, name='sign_out'),
]
