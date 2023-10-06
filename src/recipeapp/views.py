from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout  #library
from django.contrib.auth.forms import AuthenticationForm  #from for authentication

# create a Form object of class AuthForm
def login_view(request):
    #initialize error message to None
    error_message = None
    #form object with username and password field
    form = AuthenticationForm()

    # when the user hits "login" button, the POST request is generated
    if request.method == "POST":
        #read the data sent by the form via POST request
        form = AuthenticationForm(data = request.POST)

        #check if form is valid
        if form.is_valid():
            username =  form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            #use Django authenticate function to validate user
            user = authenticate(username=username, password=password)
            if user is not None:
                #use predefined django function to login
                login(request, user)
                return redirect('/list')
        else:
            error_message = "oops...something went wrong"
    #prepare data to send from view to template
    context ={
        'form': form,
        'error_message': error_message
    }

    #load the login page using "context" information
    return render(request, 'auth/login.html', context)

def logout_view(request):
    logout(request)
    return render(request, 'auth/success.html')