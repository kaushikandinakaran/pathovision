from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import UserCredentials
from django.contrib.auth.hashers import check_password

import json
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse




def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            # Retrieve user credentials from the database
            user_credentials = UserCredentials.objects.get(username=username)
            print("got")
            
            # Check if the provided password matches the stored password
            if password==user_credentials.password:
                # Authentication successful, redirect to dashboard or perform other actions
                print("hi")
                return redirect(reverse('chatbot:chatbot_page'))
            else:
                # Authentication failed, display error message
                print("something worng")
                return render(request, 'login.html', {'error': 'Invalid username or password'})
        except UserCredentials.DoesNotExist:
            print("wrong")
            # User not found, display error message
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'login.html')


# def signup(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
    
#         if form.is_valid():
#             form.save()
#             print("hi")
#             # Redirect to the login page after successful signup
#             return redirect('login')
#         else :
#             print('bye')

#     else:
#         form = UserCreationForm()
        
#     return render(request, 'signup.html', {'form': form})




from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import UserCredentials
import json

@csrf_exempt
def signup(request):
    if request.method == 'POST':
        try:
            username = request.POST.get('username')
            email = request.POST.get('email')
            password =request.POST.get('password1')
            conform_password = request.POST.get('password2')

            if not (username and email and password and conform_password):
                return JsonResponse({'message': 'Invalid request data'}, status=400)

            if password != conform_password:
                return JsonResponse({'message': 'Passwords do not match'}, status=400)

            # Check if username or email already exists
            if UserCredentials.objects.filter(username=username).exists() or UserCredentials.objects.filter(email=email).exists():
                return JsonResponse({'message': 'Username or email already exists'}, status=400)

            # Create a new UserCredentials instance
            user_credentials = UserCredentials.objects.create(username=username, email=email, password=password)
            # Redirect to login page after successful signup
            return redirect(reverse('login'))
        except json.JSONDecodeError:
            return JsonResponse({'message': 'Invalid JSON data'}, status=400)
        except KeyError:
            return JsonResponse({'message': 'Invalid request data'}, status=400)
    else:
        return render(request, 'signup.html')
    if request.method == 'POST':
        try:
            # Parse JSON data from request body
            data = json.loads(request.body)
            username = data['username']
            email = data['email']
            password = data['password1']
            conform_password = data['password2']

            if password != conform_password:
                return JsonResponse({'message': 'password not mached'}, status=400)


            # Check if username or email already exists
            if UserCredentials.objects.filter(username=username).exists() or UserCredentials.objects.filter(email=email).exists():
                return JsonResponse({'message': 'Username or email already exists'}, status=400)

            # Create a new UserCredentials instance
            user_credentials = UserCredentials.objects.create(username=username, email=email, password=password)
            print("hi")
            
            return redirect('login')
        except KeyError:
            return JsonResponse({'message': 'Invalid request data'}, status=400)
    else:
        return render(request, 'signup.html')
