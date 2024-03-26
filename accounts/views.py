from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect



def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exist! Please try some other username.")
            return redirect('signup')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('signup')
        
        if len(username)>20:
            messages.error(request, "Username must be under 20 charcters!!")
            return redirect('signup')
        
        if pass1 != pass2:
            messages.error(request, "Passwords didn't matched!!")
            return redirect('signup')
        
        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!!")
            return redirect('signup')
        
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        # myuser.is_active = False
        #myuser.is_active = True
        myuser.save()
        messages.success(request, "Your Account has been created succesfully!!")
        return redirect('signin')

    return render(request, 'signup.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']
        
        print(f"Attempting to authenticate user: {username}")

        user = authenticate(username=username, password=pass1)
        
        if user is not None:

            print(f"User {username} authenticated successfully")

            login(request, user)
            fname = user.first_name
            return redirect('dashboard')
            messages.success(request, "Logged In Sucessfully!!")
            
        else:

            print(f"Authentication failed for user: {username}")

            messages.error(request, "Bad Credentials!!")
            return redirect('signin')
    
    return render(request, 'signin.html')



@login_required
def dashboard(request):
    user = request.user
    context = {
        'user': user,
    }
    return render(request, 'dashboard.html', context)


def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!!")
    return redirect('index.html')