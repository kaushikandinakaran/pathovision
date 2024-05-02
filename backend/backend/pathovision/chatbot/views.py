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
    # import pdb
    # pdb.set_trace()
    if result == 'PNEUMONIA':
        excluded_ids = [2]  # Exclude COVID19 questions
    elif result == 'COVID19':
        excluded_ids = [1]  # Exclude PNEUMONIA questions
    else:
        excluded_ids = [1, 2]  # Exclude both PNEUMONIA and COVID19 questions

    questions = list(question_details.objects.exclude(qust_id__in=excluded_ids).values())
    options = list(option_details.objects.exclude(qust_d_id__in=excluded_ids).values())

    return question_processing({'questions': questions, 'options': options})

def question_processing(questions):
    question_data = []
    option_data = {}

    for q in questions['questions']:
        question_data.append({'qust_d_id': q['qust_d_id'], 'questions': q['questions']})

    for option in questions['options']:
        qust_d_id = option['qust_d_id']
        if qust_d_id not in option_data:
            option_data[qust_d_id] = {'qust_d_id': qust_d_id, 'options': []}
        option_data[qust_d_id]['options'].append({'option_id': option['option_id'], 'option': option['option']})

    return question_data, list(option_data.values())



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

            questions, options= Question1(result)
            print(result)
            print(questions)
            print(options)

            # data1 = question_master.objects.all()
            # print(data1)
            # for item in data1:
                 
            #     print("ID:", item.qust_id)
            #     print("Question:", item.qust_title)
            #     print("is_enabled:", item.is_enabled)


            # questions = ['asd', 'ert', 'dfg', 'dry']
            request.session['questions'] = questions
            return render(request, 'quiz.html', {'result': result, 'questions': questions, 'options': options  })

            

# def question_processing(questions):



from django.shortcuts import HttpResponse

def submit_answers(request):
    if request.method == 'POST':
        questions = request.session.get('questions')
        all_answers = []

        for question in questions:
            question_id = question['qust_d_id']
            if question_id == 1 or question_id == 2:
                # For questions with multiple correct answers
                selected_options = request.POST.getlist(f"answers_{question_id}[]")
                all_answers.append({'question': question['questions'], 'selected_options': selected_options})
            elif question_id == 3:
                # For questions with single correct answer
                selected_option = request.POST.get(f"answers_{question_id}")
                all_answers.append({'question': question['questions'], 'selected_option': selected_option})
            elif question_id == 4:
                # For questions requiring date and time selection
                selected_datetime = request.POST.get(f"answers_{question_id}")
                all_answers.append({'question': question['questions'], 'selected_datetime': selected_datetime})
        
        del request.session['questions']
        
        # Print or process the answers as needed
        for answer in all_answers:
            print("Question:", answer['question'])
            if 'selected_options' in answer:
                print("Selected Options IDs:", answer['selected_options'])
            elif 'selected_option' in answer:
                print("Selected Option ID:", answer['selected_option'])
            elif 'selected_datetime' in answer:
                print("Selected Datetime:", answer['selected_datetime'])
        
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