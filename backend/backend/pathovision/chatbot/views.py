from django.shortcuts import render

# Create your views here.
# chatbot_app/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# from .forms import ImageUploadForm


def chatbot_page(request):
    return render(request, 'chat page.html')

# @login_required
# def upload_image(request):
#     if request.method == 'POST':
#         form = ImageUploadForm(request.POST, request.FILES)
#         if form.is_valid():
#             # Process the uploaded image and make predictions
#             # Add your machine learning code here
#             image = form.cleaned_data['image']
#             # Example: predict(image)
#             return render(request, 'chatbot_app/results.html', {'result': 'Your prediction'})
#     else:
#         form = ImageUploadForm()
#     return render(request, 'chatbot_app/upload.html', {'form': form})
