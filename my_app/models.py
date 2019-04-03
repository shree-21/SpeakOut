# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField


# Create your models here.
class Volunteer(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=600)

    def __str__(self):
        return self.name

class PatientProfile(models.Model):
    
    GENDER_CHOICES = [
        ('MALE', 'Male'), 
        ('FEMALE', 'Female'),
        ('PREFER NOT TO SAY', 'Prefer Not To Say')
    ]

    AGE_GROUP_CHOICES = [
        ('13-19', '13-19'),
        ('20-25', '20-25'),
        ('26-35', '26-35'),
        ('36-45', '36-45'),
        ('46-55', '46-55'),
        ('56-65', '56-65')
    ]

    PREFERRED_GENDER_CHOICES = [
        ('MALE', 'Male'),
        ('FEMALE', 'Female'),
        ('OTHER', 'Other')
    ]

    PREFERRED_TIME_CHOICES = [
        ('EARLY MORNING (6-8)', 'Early Morning (6-8)'),
        ('MORNING (8-11)', 'Morning (8-11)'),
        ('NOON (12-2)', 'Noon (12-2)'),
        ('LATE AFTERNOON (2-5)', 'Late Afternoon (2-5)'),
        ('EVENING (5-9)', 'Evening (5-9)'),
        ('NIGHT (9-11)', 'Night (9-11)')
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='patient_profile')
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES)
    age_group = models.CharField(max_length=10, choices=AGE_GROUP_CHOICES)
    preferred_gender = models.CharField(max_length=20, choices=PREFERRED_GENDER_CHOICES)
    preferred_time = MultiSelectField(choices=PREFERRED_TIME_CHOICES)
    is_patient = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username

class Categories(models.Model):
    category_name = models.CharField(max_length=30)

    def __str__(self):
        return self.category_name

class ListenerProfile(models.Model):

    GENDER_CHOICES = [
        ('MALE', 'Male'), 
        ('FEMALE', 'Female'),
        ('OTHER', 'Other')
    ]

    AGE_GROUP_CHOICES = [
        ('13-19', '13-19'),
        ('20-25', '20-25'),
        ('26-35', '26-35'),
        ('36-45', '36-45'),
        ('46-55', '46-55'),
        ('56-65', '56-65')
    ]

    PREFERRED_TIME_CHOICES = [
        ('EARLY MORNING (6-8)', 'Early Morning (6-8)'),
        ('MORNING (8-11)', 'Morning (8-11)'),
        ('NOON (12-2)', 'Noon (12-2)'),
        ('LATE AFTERNOON (2-5)', 'Late Afternoon (2-5)'),
        ('EVENING (5-9)', 'Evening (5-9)'),
        ('NIGHT (9-11)', 'Night (9-11)')
    ]

    PREFERRED_DAY_CHOICES = [
        ('MONDAY', 'Monday'),
        ('TUESDAY', 'Tuesday'),
        ('WEDNESDAY', 'Wednesday'),
        ('THURSDAY', 'Thursday'),
        ('FRIDAY', 'Friday'),
        ('SATURDAY', 'Saturday'),
        ('SUNDAY', 'Sunday'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='listener_profile')
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    age_group = models.CharField(max_length=10, choices=AGE_GROUP_CHOICES)
    preferred_time = MultiSelectField(choices=PREFERRED_TIME_CHOICES)
    preferred_days = MultiSelectField(choices=PREFERRED_DAY_CHOICES)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, default=None)
    is_listener = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username
        
class TherapistProfile(models.Model):

    GENDER_CHOICES = [
        ('MALE', 'Male'), 
        ('FEMALE', 'Female'),
        ('OTHER', 'Other')
    ]

    AGE_GROUP_CHOICES = [
        ('13-19', '13-19'),
        ('20-25', '20-25'),
        ('26-35', '26-35'),
        ('36-45', '36-45'),
        ('46-55', '46-55'),
        ('56-65', '56-65')
    ]

    PREFERRED_TIME_CHOICES = [
        ('EARLY MORNING (6-8)', 'Early Morning (6-8)'),
        ('MORNING (8-11)', 'Morning (8-11)'),
        ('NOON (12-2)', 'Noon (12-2)'),
        ('LATE AFTERNOON (2-5)', 'Late Afternoon (2-5)'),
        ('EVENING (5-9)', 'Evening (5-9)'),
        ('NIGHT (9-11)', 'Night (9-11)')
    ]

    PREFERRED_DAY_CHOICES = [
        ('MONDAY', 'Monday'),
        ('TUESDAY', 'Tuesday'),
        ('WEDNESDAY', 'Wednesday'),
        ('THURSDAY', 'Thursday'),
        ('FRIDAY', 'Friday'),
        ('SATURDAY', 'Saturday'),
        ('SUNDAY', 'Sunday'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='therapist_profile')
    name = models.CharField(max_length=100, default="")
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    age_group = models.CharField(max_length=10, choices=AGE_GROUP_CHOICES)
    preferred_time = MultiSelectField(max_length=100, choices=PREFERRED_TIME_CHOICES)
    preferred_days = MultiSelectField(max_length=100, choices=PREFERRED_DAY_CHOICES)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, default=None)
    education = models.TextField()
    experience = models.TextField()
    is_therapist = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username


