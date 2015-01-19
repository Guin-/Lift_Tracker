from django.contrib.auth import logout, authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, render
from portal.forms import UserForm

def main_page(request):
    return render_to_response('index.html')

def logout_page(request):
    '''
    Logs a user out and re-directs them to the home page
    '''
    logout(request)
    return HttpResponseRedirect('/')

def register(request):
    '''
    Displays new user registration page, and redirects 
    user to the portal home page
    '''

    registered = False

    if request.method == "POST":
        user_form = UserForm(data = request.POST)

        if user_form.is_valid():
            user = user_form.save()
            
            user.set_password(user.password)
            user.save()
            registered = True
            
            new_user = authenticate(username = user_form.cleaned_data['username'],
                                    password = user_form.cleaned_data['password'])
            login(request, new_user)
            return render(request, 'portal/index.html') 
        else:
            print user_form.errors
    else:
        user_form = UserForm()


    return render(request, 'registration/register.html', {'user_form': user_form,
                                                         'registered': registered})

