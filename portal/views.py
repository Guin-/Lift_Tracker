from django.shortcuts import render, render_to_response
from django.contrib.auth.decorators import login_required

@login_required
def portal_main_page(request):
    '''
    If a user is authenticated, direct them to the main page. Otherwise, 
    take them to the login page. 
    '''

    return render_to_response('portal/index.html')



