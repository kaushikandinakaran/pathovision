from django.shortcuts import render
from django.http import JsonResponse
import os
# Create your views here.
# chatbot_app/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# from .forms import ImageUploadForm
import random
from .models import question_master




def chatbot_page(request):
    return render(request, 'Attach image.html')



def model_image(request):
    if request.method == 'POST':
        image_file = request.FILES.get('image')

        if image_file:
            # Create the image folder if it doesn't exist
            if not os.path.exists('image'):
                os.makedirs('image')

            # Save the image file
            file_path = os.path.join('image', image_file.name)
            with open(file_path, 'wb+') as destination:
                for chunk in image_file.chunks():
                    destination.write(chunk)

            result = ml_code(file_path)

            data1 = question_master.objects.all()
            print(data1)
            for item in data1:
                 
                print("ID:", item.qust_id)
                print("Question:", item.qust_title)
                print("is_enabled:", item.is_enabled)


            questions = ['asd', 'ert', 'dfg', 'dry']
            

    return render(request, 'quiz.html', {'result': result, 'questions': questions})




def ml_code(filename):
    ra = ["NORMAL", "COVID19", "PNEUMONIA"]
    return random.choice(ra)




# def upload_image(request):
#     if request.method == 'POST':
#         image_file = request.FILES.get('image')
#         if image_file:
#             # Save the image file
#             file_path = os.path.join('image', image_file.name)
#             with open(file_path, 'wb+') as destination:
#                 for chunk in image_file.chunks():
#                     destination.write(chunk)
#
#
#             return JsonResponse({'message': 'Image uploaded and processed successfully'})
#         else:
#             return JsonResponse({'error': 'No image file found'}, status=400)
#     else:
#         return JsonResponse({'error': 'Invalid request method'}, status=400)