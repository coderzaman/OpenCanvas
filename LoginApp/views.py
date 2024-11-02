from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.
def signup(request):
    form = UserCreationForm()
    registered = False

    if request.method == 'POST':
        
        form = UserCreationForm(data=request.POST)
        
        if form.is_valid():
            form.save()
            registered = True
            
    
    context = {'form':form, 'registered': registered}    
    return render(request, 'LoginApp/signup.html', context=context)
        
        
def user_sign_in(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(data= request.POST)
        
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            user = authenticate(username = username, password = password)
            
            if user is not None:
                login(request, user)
                return redirect('index')
    context = {'form':form}
    return render(request, 'LoginApp/sign_in.html', context=context)

@login_required
def sign_out(request):
    logout(request)
    return redirect('index')