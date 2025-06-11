from django.contrib import messages
from django.core.mail import EmailMessage, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import WorkExperience, Certificates, Education
import mailtrap as mt
from django.conf import settings

# Create your views here.
def home(request):
    return render(request, 'resume/home.html')

def work_experiences(request):
    workexperiences = WorkExperience.objects.all().order_by('-start_date')
    for exp in workexperiences:
        exp.work_description = exp.work_description.split(".")[:-1]
    return render(
        request, 'resume/work_exp.html', context={
            'workexperiences': workexperiences
        }
    )

def education(request):
    education = Education.objects.all().order_by('-start_year')
    certificates = Certificates.objects.all().order_by('-course_completion_date')
    return render(request, 'resume/education.html',
                  context={'education':education, 'certificates': certificates})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            mail = mt.Mail(
                sender=mt.Address(email="hello@demomailtrap.co", name=name),
                to=[mt.Address(email="prajwalrao@71lyz2.onmicrosoft.com")],
                subject=subject,
                text=f"From {email}\n{message}",
                category="Integration Test",
            )

            client = mt.MailtrapClient(token="d34da2106dc637e43b03c5501a23b3ac")
            response = client.send(mail)

            success_message = "Hi! Thanks for the message, I will get back to you shortly"
            messages.success(request, success_message)

            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'resume/contact.html', context={'form':form})


