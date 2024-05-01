from django.shortcuts import render
from django.http import JsonResponse
import os
# Create your views here.
# chatbot_app/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# from .forms import ImageUploadForm


def chatbot_page(request):
    return render(request, 'chat page.html')



def upload_image(request):
    if request.method == 'POST':
        image_file = request.FILES.get('image')
        if image_file:
            # Save the image file
            file_path = os.path.join('images', image_file.name)
            with open(file_path, 'wb+') as destination:
                for chunk in image_file.chunks():
                    destination.write(chunk)


            return JsonResponse({'message': 'Image uploaded and processed successfully'})
        else:
            return JsonResponse({'error': 'No image file found'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)