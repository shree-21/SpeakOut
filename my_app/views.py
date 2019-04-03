# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from .models import Volunteer, Contact, ListenerProfile, TherapistProfile, PatientProfile
from my_app.forms import VolunteerForm, ContactForm, UserForm, PatientProfileForm, ListenerProfileForm, TherapistProfileForm, EditUserForm, EditPatientProfileForm, EditListenerProfileForm, EditTherapistProfileForm, SelectValue, SelectTherapistValue
from django.contrib.auth import authenticate, login, logout
from notifications.signals import notify
from django.db.models.signals import post_save

# Create your views here.
def index(request):
    return render(request, 'my_app/index.html')

class about_view(TemplateView):
    template_name = 'my_app/about.html'

def volunteer_view(request):
    volunteer_form = VolunteerForm()

    if request.method == 'POST':
        volunteer_form = VolunteerForm(data=request.POST)

        if volunteer_form.is_valid():
            name = volunteer_form.cleaned_data['name']
            email = volunteer_form.cleaned_data['email']
            v = Volunteer(name=name, email=email)
            v.save()
            return redirect('my_app:quiz')

    else:
        volunteer_form = VolunteerForm()

    context = {'volunteer_form': volunteer_form}
    return render(request, 'my_app/volunteer.html', context)

def contact_view(request):
    contact_form = ContactForm()

    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST)

        if contact_form.is_valid():
            name = contact_form.cleaned_data['name']
            email = contact_form.cleaned_data['email']
            subject = contact_form.cleaned_data['subject']
            message = contact_form.cleaned_data['message']
            c = Contact(name=name, email=email, subject=subject, message=message)
            c.save()
            return redirect('index')

    else: 
        contact_form = ContactForm()

    context = {'contact_form': contact_form}
    return render(request, 'my_app/contact.html', context)


def patient_profile_view(request):

    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        patient_profile_form = PatientProfileForm(data=request.POST)

        if user_form.is_valid() and patient_profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            patient_profile = patient_profile_form.save(commit=False)
            patient_profile.user = user
            patient_profile.save()

            registered = True
            return redirect('my_app:all_login')
        else:
            print(user_form.errors, patient_profile_form.errors)

    else:
        user_form = UserForm()
        patient_profile_form = PatientProfileForm()

    return render(request, 'my_app/patient_profile.html', {'user_form': user_form, 'patient_profile_form': patient_profile_form, 'registered':registered})

def listener_profile_view(request):

    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        listener_profile_form = ListenerProfileForm(data=request.POST)

        if user_form.is_valid() and listener_profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            listener_profile = listener_profile_form.save(commit=False)
            listener_profile.user = user
            listener_profile.save()

            registered = True
            return redirect('my_app:all_login')
        else:
            print(user_form.errors, listener_profile_form.errors)

    else:
        user_form = UserForm()
        listener_profile_form = ListenerProfileForm()

    return render(request, 'my_app/listener_profile.html', {'user_form': user_form, 'listener_profile_form': listener_profile_form, 'registered':registered})


def login_view(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect('index')

            else:
                print('Account Inactive')
        else:
            print('Someone tried to login and failed.')
    else:
        return render(request, 'my_app/login.html', {})        

def logout_view(request):
    logout(request)
    return redirect('index')

class home_view(TemplateView):
    template_name = 'my_app/home.html'

def therapist_profile_view(request):

    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        therapist_profile_form = TherapistProfileForm(data=request.POST)

        if user_form.is_valid() and therapist_profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            therapist_profile = therapist_profile_form.save(commit=False)
            therapist_profile.user = user
            therapist_profile.save()

            registered = True
            return redirect('my_app:all_login')
        else:
            print(user_form.errors, therapist_profile_form.errors)

    else:
        user_form = UserForm()
        therapist_profile_form = TherapistProfileForm()

    return render(request, 'my_app/therapist_profile.html', {'user_form': user_form, 'therapist_profile_form': therapist_profile_form, 'registered':registered})

def edit_patient_profile(request):
    if request.method == 'POST':
        edit_user_form = EditUserForm(request.POST, instance=request.user)
        edit_patient_profile_form = EditPatientProfileForm(request.POST, instance=request.user.patient_profile)

        if edit_user_form.is_valid() and edit_patient_profile_form.is_valid():
            edit_user_form.save()
            edit_patient_profile_form.save()
            return redirect('index')

    else:
        edit_user_form = EditUserForm(instance=request.user)
        edit_patient_profile_form = EditPatientProfileForm(instance=request.user.patient_profile)
        args = {'edit_user_form': edit_user_form, 'edit_patient_profile_form': edit_patient_profile_form}
        return render(request, 'my_app/edit_patient_profile.html', args)



def edit_listener_profile(request):
    if request.method == 'POST':
        edit_user_form = EditUserForm(request.POST, instance=request.user)
        edit_listener_profile_form = EditListenerProfileForm(request.POST, instance=request.user.listener_profile)

        if edit_user_form.is_valid() and edit_listener_profile_form.is_valid():
            edit_user_form.save()
            edit_listener_profile_form.save()
            return redirect('index')

    else:
        edit_user_form = EditUserForm(instance=request.user)
        edit_listener_profile_form = EditListenerProfileForm(instance=request.user.listener_profile)
        args = {'edit_user_form': edit_user_form, 'edit_listener_profile_form': edit_listener_profile_form}
        return render(request, 'my_app/edit_listener_profile.html', args)

def edit_therapist_profile(request):
    if request.method == 'POST':
        edit_user_form = EditUserForm(request.POST, instance=request.user)
        edit_therapist_profile_form = EditTherapistProfileForm(request.POST, instance=request.user.therapist_profile)

        if edit_user_form.is_valid() and edit_therapist_profile_form.is_valid():
            edit_user_form.save()
            edit_therapist_profile_form.save()
            return redirect('index')

    else:
        edit_user_form = EditUserForm(instance=request.user)
        edit_therapist_profile_form = EditTherapistProfileForm(instance=request.user.therapist_profile)
        args = {'edit_user_form': edit_user_form, 'edit_therapist_profile_form': edit_therapist_profile_form}
        return render(request, 'my_app/edit_therapist_profile.html', args)
        
class listener_quiz_view(TemplateView):
    template_name = "my_app/listener_quiz.html"

def listener_list_view(request):
    listeners = ListenerProfile.objects.all()
    therapists = TherapistProfile.objects.all()
    print(listeners)
    context = {'listeners': listeners, 'therapists': therapists}
    return render(request, 'my_app/listener_list.html', context)
    
def therapist_list_view(request):
    therapists = TherapistProfile.objects.all()
    print(therapists)
    context = {'therapists': therapists}
    return render(request, 'my_app/therapist_list.html', context)
    
class video_chat_view(TemplateView):
    template_name = 'my_app/video_chat.html'

class articles_view(TemplateView):
    template_name = 'my_app/articles.html'

def my_handler(sender, instance, created, **kwargs): #notifications
    notify.send(instance, recipient, verb='was saved')

# post_save.connect(my_handler, sender=PatientProfile)

def Webrtc(request):
    user = request.user
    listeners = ListenerProfile.objects.filter(user_id=user.id)
    context = {'listeners': listeners}
    return render(request, 'my_app/web_chat.html', context)
    
def web_chat(request):
    listeners = ListenerProfile.objects.all()
    patients = PatientProfile.objects.all()
    # u = request.GET.get('id', '')
    # print(request.user)
    context = {'listeners': listeners, 'patients': patients}
    return render(request, 'my_app/web_chat1.html', context)

   

def get_selected(request): 
    listeners = ListenerProfile.objects.all()
    patients = PatientProfile.objects.all()
    form = SelectValue()
    
    
    print("working")
    
    if request.method == 'POST':
        form = SelectValue(data=request.POST)
        s = request.POST.get('drop')
        chat_hash = request.POST.get('chathash')
        print("chathash", chat_hash)
        link = "http://127.0.0.1:8000/my_app/chat/#" + chat_hash
        print(link)
        notify_user(request, s, link)
        print(s)
        print("post is working")
        # context = {'chat_hash': chat_hash}
        return redirect(link)
        
      
    context = {'listeners': listeners, 'patients': patients}       
    return render(request, 'my_app/select_listener.html', context)

INFO = 20

def notify_user(request, id, link):
    print("notify", id, link)
    user_id = int(request.POST['drop'])
    user = User.objects.get(id=user_id)
    listener = ListenerProfile.objects.filter(user_id=id)
    n = notify.send(request.user, recipient=user, verb='connect here: '+link)
    print("notifications", n)
    
def Webrtc_therapist(request):
    user = request.user
    therapists = TherapistProfile.objects.filter(user_id=user.id)
    context = {'therapists': therapists}
    return render(request, 'my_app/web_chat.html', context)
    
def web_chat_therapist(request):
    therapists = TherapistProfile.objects.all()
    patients = PatientProfile.objects.all()
    # u = request.GET.get('id', '')
    # print(request.user)
    context = {'therapists': therapists, 'patients': patients}
    return render(request, 'my_app/web_chat2.html', context)

   

def get_selected_therapist(request): 
    therapists = TherapistProfile.objects.all()
    patients = PatientProfile.objects.all()
    form = SelectTherapistValue()
    
    
    print("working")
    
    if request.method == 'POST':
        form = SelectValue(data=request.POST)
        s = request.POST.get('drop')
        chat_hash = request.POST.get('chathash')
        print("chathash", chat_hash)
        link = "http://127.0.0.1:8000/my_app/chat/#" + chat_hash
        print(link)
        notify_user(request, s, link)
        print(s)
        print("post is working")
        # context = {'chat_hash': chat_hash}
        return redirect(link)
        
      
    context = {'therapists': therapists, 'patients': patients}       
    return render(request, 'my_app/select_therapist.html', context)

INFO = 20

def notify_therapist(request, id, link):
    print("notify", id, link)
    user_id = int(request.POST['drop'])
    user = User.objects.get(id=user_id)
    therapist = TherapistProfile.objects.filter(user_id=id)
    n = notify.send(request.user, recipient=user, verb='connect here: '+link)
    print("notifications", n)
    