from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Doctor, Appointment, ContactUs, Email, Testimonial

def index(request):
    list_testimonials = Testimonial.objects.all()

    if len(list_testimonials) >= 1:
        first_testimonial = list_testimonials[0]
        list_testimonials = list_testimonials[1:]
    else:
        first_testimonial = None
        list_testimonials = None

    doctors = Doctor.objects.filter(is_active=True)
    context = {
        'list_doctors': doctors,
        'first_testimonial': first_testimonial,
        'list_testimonials': list_testimonials
    }
    return render(request, 'index.html', context=context)

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        message = request.POST.get('message')

        # Сохраняем данные в базу данных
        contact = ContactUs(
            name=name,
            email=email,
            phone_number=phone_number,
            message=message
        )
        contact.phone_number = phone_number.replace(' ', '')
        contact.save()   
        # 2 вариант записи в базу данных 
        # contact = ContactUs.objects.create(
        #     name=name,
        #     email=email,
        #     phone_number=phone_number,
        #     message=message
        # )
     
        messages.success(request, 'Ваше сообщение успешно отправлено!')
    return render(request, 'contact.html')

def doctor(request):
    doctors = Doctor.objects.filter(is_active=True)
    context = {
        'list_doctors': doctors
    }
    return render(request, 'doctor.html', context=context)

def testimonials(request):
    list_testimonials = Testimonial.objects.all()

    if len(list_testimonials) >= 1:
        first_testimonial = list_testimonials[0]
        list_testimonials = list_testimonials[1:]
    else:
        first_testimonial = None
        list_testimonials = None

    context = {
        'first_testimonial': first_testimonial,
        'list_testimonials': list_testimonials
    }
    return render(request, 'testimonials.html', context=context)

def treatment(request):
    return render(request, 'treatment.html')

def book_appointment(request):
    if request.method == 'POST':
        patient_name = request.POST.get('patient_name')
        doctor_id = request.POST.get('doctor_id')
        time = request.POST.get('time')
        phone_number = request.POST.get('phone_number')
        symptoms = request.POST.get('symptoms')
        date = request.POST.get('date')

        # Сохраняем данные в базу данных
        appointment = Appointment(
            patient_name=patient_name,
            doctor_id=doctor_id,
            time=time,
            phone_number=phone_number,
            symptoms=symptoms,
            date=date
        )
        appointment.save()        
     
        messages.success(request, 'Вы успешно записались на прием!')

    return redirect('index')    


# создать новую функцию для обработки формы подписки на рассылку
def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        
        # Сохраняем данные в базу данных
        email = Email(
            email=email
        )
        email.save()        
        print(email,'Подписался')
        messages.success(request, 'Вы успешно подписались на рассылку!')

    return redirect('index')