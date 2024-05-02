from chatbot.models import question_master
from chatbot.models import question_details
from chatbot.models import option_details


# Create an instance of your model with the data you want to insert
instance1 = question_master(qust_title='Pneumonia symptoms', is_enabled=1)
instance2 = question_master(qust_title='Covid symptoms', is_enabled=1)
instance11 = question_master(qust_title='General questions', is_enabled=1)

instance3 = question_details(qust_id=1, questions="Which symptoms are you experiencing right now?", qust_type=1, order=1, parent_id=0, is_enabled=1)
instance4 = question_details(qust_id=2, questions="Which symptoms are you experiencing right now?", qust_type=1, order=1, parent_id=0, is_enabled=1)
instance5 = question_details(qust_id=3, questions="Do you want to book an appointment with the doctor?", qust_type=1, order=1, parent_id=0, is_enabled=1)

ins3option1 = option_details(qust_d_id=1, option="High fever", order=1, is_enabled=1)
ins3option2 = option_details(qust_d_id=1, option="Coughing up greenish, yellow, or bloody mucus", order=2, is_enabled=1)
ins3option3 = option_details(qust_d_id=1, option="Chills that make you shake", order=3, is_enabled=1)
ins3option4 = option_details(qust_d_id=1, option="Feeling like you can’t catch your breath", order=4, is_enabled=1)
ins3option5 = option_details(qust_d_id=1, option="Feeling very tired", order=5, is_enabled=1)
ins3option6 = option_details(qust_d_id=1, option="Loss of appetite", order=6, is_enabled=1)
ins3option7 = option_details(qust_d_id=1, option="Sharp or stabbing chest pain", order=7, is_enabled=1)
ins3option8 = option_details(qust_d_id=1, option="Sweating a lot", order=8, is_enabled=1)
ins3option9 = option_details(qust_d_id=1, option="Fast breathing and heartbeat", order=9, is_enabled=1)
ins3option10 = option_details(qust_d_id=1, option="Lips and fingernails turning blue", order=10, is_enabled=1)
ins3option11 = option_details(qust_d_id=1, option="None", order=11, is_enabled=1)

ins4option1 = option_details(qust_d_id=2, option="Fever or chills", order=1, is_enabled=1)
ins4option2 = option_details(qust_d_id=2, option="Cough", order=2, is_enabled=1)
ins4option3 = option_details(qust_d_id=2, option="Shortness of breath or difficulty breathing", order=3, is_enabled=1)
ins4option4 = option_details(qust_d_id=2, option="Fatigue", order=4, is_enabled=1)
ins4option5 = option_details(qust_d_id=2, option="Muscle or body aches", order=5, is_enabled=1)
ins4option6 = option_details(qust_d_id=2, option="Headache", order=6, is_enabled=1)
ins4option7 = option_details(qust_d_id=2, option="New loss of taste or smell", order=7, is_enabled=1)
ins4option8 = option_details(qust_d_id=2, option="Sore throat", order=8, is_enabled=1)
ins4option9 = option_details(qust_d_id=2, option="Congestion or runny nose", order=9, is_enabled=1)
ins4option10 = option_details(qust_d_id=2, option="Nausea or vomiting", order=10, is_enabled=1)
ins4option11 = option_details(qust_d_id=2, option="Diarrhea", order=11, is_enabled=1)
ins4option12 = option_details(qust_d_id=2, option="None", order=12, is_enabled=1)

ins5option1 = option_details(qust_d_id=3, option="Yes", order=1, is_enabled=1)
ins5option2 = option_details(qust_d_id=3, option="No", order=2, is_enabled=1)
# Save the instance to insert it into the database
instance1.save()
instance2.save()

instance3.save()
instance4.save()

ins3option1.save()
ins3option2.save()
ins3option3.save()
ins3option4.save()
ins3option5.save()
ins3option6.save()
ins3option7.save()
ins3option8.save()
ins3option9.save()
ins3option10.save()
ins3option11.save()

ins4option1.save()
ins4option2.save()
ins4option3.save()
ins4option4.save()
ins4option5.save()
ins4option6.save()
ins4option7.save()
ins4option8.save()
ins4option9.save()
ins4option10.save()
ins4option11.save()
ins4option12.save()





data = question_master.objects.all()
for item in data:
    print(item)
data1 = question_details.objects.all()
for item in data1:
    print(item)