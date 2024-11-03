from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from . forms import SignUpForm, UserProfileChange, ProfilePic

# Create your views here.
def signup(request):
    form = SignUpForm()
    registered = False

    if request.method == 'POST':
        
        form = SignUpForm(data=request.POST)
        
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
@login_required
def profile(request):
    return render(request, 'LoginApp/user_profile.html', context={})

@login_required
def user_change(request):
    current_user = request.user
    form = UserProfileChange(instance=current_user)
    
    if request.method == "POST":
        form = UserProfileChange(request.POST, instance=current_user)
        
        if form.is_valid():
            form.save()
            
            
    return render(request, "LoginApp/change_profile.html", context={'form':form})


@login_required
def pass_change(request):
    changed = False
    current_user = request.user
    form = PasswordChangeForm(current_user)
    
    if request.method == 'POST':
        form = PasswordChangeForm(current_user, data=request.POST)
        
        if form.is_valid():
            form.save()
            changed = True
            
    context = {'form':form, 'changed': changed}
    
    return render(request, 'LoginApp/password_change.html', context=context)
        

@login_required
def add_profile_pic(request):
    form = ProfilePic()
    
    if request.method == "POST":
        form = ProfilePic(request.POST, request.FILES)
        
        if form.is_valid():
            user_obj = form.save(commit=False)
            user_obj.user = request.user
            user_obj.save()
            return redirect('Login:profile')
    
    return render(request, 'LoginApp/add_profile_pic.html', context={'form':form})
 
 
@login_required
def update_profile_pic(request):
    form = ProfilePic(instance=request.user.user_profile)
    
    if request.method == "POST":
        form = ProfilePic(request.POST, request.FILES, instance=request.user.user_profile)
        
        if form.is_valid():
            form.save()
            return redirect('Login:profile')
            

    return render(request, 'LoginApp/add_profile_pic.html', context={'form':form})