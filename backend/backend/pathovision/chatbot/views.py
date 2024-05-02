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
from django.http import HttpResponse


from django.shortcuts import render
from .models import question_details, option_details

def Question1(result):
    if result == 'PNEUMONIA':
        qust_id = 1
    elif result == 'COVID19':
        qust_id = 2
    # else:
        # Handle other cases or direct to the second question
        # For now, let's assume it's 3

    questions = list(question_details.objects.filter(qust_id=qust_id).values())
    options = list(option_details.objects.filter(qust_d_id=qust_id).values())

    return {'questions': questions, 'options': options}



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

            questionse = Question1(result)
            print(result)
            print(questionse)

            # data1 = question_master.objects.all()
            # print(data1)
            # for item in data1:
                 
            #     print("ID:", item.qust_id)
            #     print("Question:", item.qust_title)
            #     print("is_enabled:", item.is_enabled)


            questions = ['asd', 'ert', 'dfg', 'dry']
            request.session['questions'] = questions

            

    return render(request, 'quiz.html', {'result': result, 'questions': questions})



def submit_answers(request):
    if request.method == 'POST':
        answers = request.POST.getlist('answers')
        questions = request.session.get('questions')
        del request.session['questions']
        print(answers)
        print(questions)

        # Print the questions and answers
        for question, answer in zip(questions, answers):
            print(f"Question: {question}")
            print(f"Answer: {answer}")

        # You can process the answers further here, such as saving them to a database
        
        return HttpResponse("Answers submitted successfully.")
    else:
        return HttpResponse("Invalid request method.")


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