from django.conf.urls import url
from my_app import views
from .views import about_view, home_view, listener_quiz_view, video_chat_view, articles_view

app_name = 'my_app'

urlpatterns = [
    url(r'^about/', about_view.as_view(), name='about'),
    url(r'^volunteer_view/', views.volunteer_view, name='volunteer'),
    url(r'^contact_view/', views.contact_view, name='contact'),
    url(r'^patient_profile/', views.patient_profile_view, name='patient'),
    url(r'^listener_profile/', views.listener_profile_view, name='listener'),
    url(r'^login_view/', views.login_view, name='all_login'),
    url(r'^logout_view/', views.logout_view, name='all_logout'),
    url(r'home_view/', home_view.as_view(), name='home'),
    url(r'^therapist_profile/', views.therapist_profile_view, name='therapist'),
    url(r'^edit_patient_profile/', views.edit_patient_profile, name='edit_patient_profile'),
    url(r'^edit_listener_profile/', views.edit_listener_profile, name='edit_listener_profile'),
    url(r'^edit_therapist_profile/', views.edit_therapist_profile, name='edit_therapist_profile'),
    url(r'^listener_quiz/', listener_quiz_view.as_view(), name='quiz'),
    url(r'^listener_list/', views.listener_list_view, name='listener_list'),
    url(r'^therapist_list/', views.therapist_list_view, name='therapist_list'),
    url(r'^video_chat/', video_chat_view.as_view(), name='video_chat'),
    url(r'^stories/', articles_view.as_view(), name='blog'),
    url(r'^chat/', views.Webrtc, name='chat'),
    url(r'^web_chat/', views.web_chat, name='listener_chat'),
    url(r'^select/', views.get_selected, name='select'),
    url(r'^notify/', views.notify_user, name='notify'),
    url(r'^chat_therapist/', views.Webrtc_therapist, name='chat_therapist'),
    url(r'^web_chat_therapist/', views.web_chat_therapist, name='therapist_chat'),
    url(r'^select_therapist/', views.get_selected_therapist, name='select_therapist'),
    url(r'^notify_therapist/', views.notify_therapist, name='notify_therapist'),
]