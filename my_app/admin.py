# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Volunteer, Contact, Categories, PatientProfile, ListenerProfile, TherapistProfile

# Register your models here.

admin.site.register(Volunteer)
admin.site.register(Contact)
admin.site.register(Categories)
admin.site.register(PatientProfile)
admin.site.register(ListenerProfile)
admin.site.register(TherapistProfile)