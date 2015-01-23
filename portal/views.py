from django.shortcuts import render, render_to_response
from django.contrib.auth.decorators import login_required
from portal.forms import UserProfileForm
from portal.models import UserProfile


@login_required
def portal_main_page(request):
    '''
    If a user is authenticated, direct them to the main page. Otherwise, 
    take them to the login page. 
    '''
    updated = False

    latest_profile = UserProfile.objects.order_by('-timestamp')[:1] 

    if request == ("POST"):
        profile_form = UserProfileForm(request.POST)

        if profile_form.is_valid():
            profile = profile_form.save()
            updated = True
            latest_profile = UserProfile.objects.order_by('-timestamp')[:1] 

            return render(request, 'portal/index.html', { 'profile': profile,
                                                           'updated': updated })
        else:
            print profile_form.errors
    else:
        profile_form = UserProfileForm()
        
    return render(request, 'portal/index.html', {'profile_form': profile_form })
                                               #     'profile': profile })

@login_required
def user_profile(request):
    '''
    Add, update, or view user profile
    '''
    pass


