from django.shortcuts import render , redirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required

#scope.core/views.py

from core.models import Airdrop, Blockchain, Task, Notification, FollowerProfile ,ScopeUser, Event

from django.http import HttpResponse

#from .form import SignupForm, FileUploadForm

from django.views.generic import ListView, DetailView
from calendar import HTMLCalendar
from datetime import date

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.db import IntegrityError, transaction
from google.oauth2 import id_token
from google.auth.transport import requests
from django.conf import settings
import logging
from .models import ScopeUser


def index(req):
    
    airdrops = Airdrop.objects.all()
    
    return render(req , 'core/index.html',
    {
     'airdrops' : airdrops,
     
    })
    
    
def edit(req):
    return render(req , 'core/edit.html')
  
def calendar(req):
    return render(req , 'core/calendar.html')





"""
class AirdropListView(ListView):
    model = Airdrop
    template_name = 'airdrops.html'
"""

class EventCalendarView(ListView):
    model = Event
    template_name = 'core/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        calendar = HTMLCalendar()
        context['calendar'] = calendar.formatmonth(self.request.GET.get('year', date.today().year), self.request.GET.get('month', date.today().month))
        context['events'] = Event.objects.filter(start_date__month=self.request.GET.get('month', date.today().month), start_date__year=self.request.GET.get('year', date.today().year))
        
        return context





    
def tokenScreen(req):
    return render(req , 'core/tokenScreen.html')
    
'''    
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/login')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {'form': form})
    
'''    

        
        
def userprofile(req,username):
    user = ScopeUser.objects.get(username=username)
    return render(req, 'core/profile.html', {'user': user})
    
 
#Google one-tap signin 

logger = logging.getLogger(__name__)

@csrf_exempt
def google_login(request):
    if request.method != 'POST':
        return JsonResponse({'success': False, 'error': 'Invalid request method'}, status=405)

    token = request.POST.get('id_token')
    if not token:
        return JsonResponse({'success': False, 'error': 'No token provided'}, status=400)

    try:
        # Verify the token
        idinfo = id_token.verify_oauth2_token(token, requests.Request(), settings.GOOGLE_CLIENT_ID)

        # Check if the token is issued by Google
        if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
            raise ValueError('Wrong issuer.')

        # Get user info from the token
        google_id = idinfo['sub']
        email = idinfo['email']
        name = idinfo.get('name', '')
        
        # Try to get the user by email
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            # Create a new user if not exists
            with transaction.atomic():
                try:
                    user = User.objects.create_user(
                        username=email,  # Using email as username
                        email=email,
                        password=None  # Set a unusable password
                    )
                    user.first_name = name.split(' ')[0] if name else ''
                    user.last_name = ' '.join(name.split(' ')[1:]) if name else ''
                    user.save()

                    # Update the ScopeUser model
                    scope_user = user.scopeuser
                    scope_user.email = email
                    scope_user.save()

                except IntegrityError:
                    return JsonResponse({'success': False, 'error': 'User creation failed'}, status=400)

        # Log the user in
        login(request, user)
        
        return JsonResponse({
            'success': True,
            'redirect_url': '/dashboard/'  # or wherever you want to redirect after login
        })

    except ValueError as e:
        logger.error(f"Token verification failed: {str(e)}")
        return JsonResponse({'success': False, 'error': 'Invalid token'}, status=400)
    except Exception as e:
        logger.error(f"Unexpected error during Google login: {str(e)}")
        return JsonResponse({'success': False, 'error': 'Login failed'}, status=500) 
    
"""
 
@login_required       
def login(req):
    if req.method == 'POST':
        username = req.POST.get('username')
        password = req.POST.get('password')
        
        user = auth.authenticate(username=username , password=password)
        
        if user is not None:
            auth.login(req,user)
            if req.user.is_authenticated and req.user.username:
                return redirect('profile', username=req.user.username)
            else:
                return render(req , 'core/login.html')
    return render(req, 'core/login.html')
    
"""