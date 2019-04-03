from django import forms
from django.contrib.auth.models import User
from my_app.models import Volunteer, Contact, PatientProfile, Categories, ListenerProfile, TherapistProfile
from django.contrib.auth.forms import UserChangeForm

class VolunteerForm(forms.ModelForm):

    class Meta():
        model = Volunteer
        fields = ('name', 'email')

class ContactForm(forms.ModelForm):

    class Meta():
        model = Contact
        fields = ('name', 'email', 'subject', 'message')

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')

class PatientProfileForm(forms.ModelForm):
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
        ('ANY', 'Any')
    ]

    PREFERRED_TIME_CHOICES = [
        ('EARLY MORNING (6-8)', 'Early Morning (6-8)'),
        ('MORNING (8-11)', 'Morning (8-11)'),
        ('NOON (12-2)', 'Noon (12-2)'),
        ('LATE AFTERNOON (2-5)', 'Late Afternoon (2-5)'),
        ('EVENING (5-9)', 'Evening (5-9)'),
        ('NIGHT (9-11)', 'Night (9-11)')
    ]

    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect())
    age_group = forms.CharField(max_length=10, widget=forms.Select(choices=AGE_GROUP_CHOICES))
    preferred_gender = forms.ChoiceField(choices=PREFERRED_GENDER_CHOICES, widget=forms.RadioSelect())
    preferred_time = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=PREFERRED_TIME_CHOICES)

    class Meta():
        model = PatientProfile
        fields = ('gender', 'age_group', 'preferred_gender', 'preferred_time')

class CategoriesForm(forms.ModelForm):

    class Meta():
        model = Categories
        fields = ('category_name',)

class ListenerProfileForm(forms.ModelForm):

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

    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect())
    age_group = forms.CharField(max_length=10, widget=forms.Select(choices=AGE_GROUP_CHOICES))
    preferred_time = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=PREFERRED_TIME_CHOICES)
    preferred_days = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=PREFERRED_DAY_CHOICES)
    category = forms.ModelChoiceField(queryset=Categories.objects.all(), required=True)

    class Meta():
        model = ListenerProfile
        fields = ('gender', 'age_group', 'preferred_time', 'preferred_days', 'category')

class TherapistProfileForm(forms.ModelForm):

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

    name = forms.CharField(max_length=100)
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect())
    age_group = forms.CharField(max_length=10, widget=forms.Select(choices=AGE_GROUP_CHOICES))
    preferred_time = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=PREFERRED_TIME_CHOICES)
    preferred_days = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=PREFERRED_DAY_CHOICES)
    category = forms.ModelChoiceField(queryset=Categories.objects.all(), required=True)
    education = forms.CharField(widget=forms.Textarea)
    experience = forms.CharField(widget=forms.Textarea)

    class Meta():
        model = TherapistProfile
        fields = ('name', 'gender', 'age_group', 'preferred_time', 'preferred_days', 'category', 'education', 'experience')


class EditUserForm(UserChangeForm):

    class Meta():
        model = User
        fields = ('username', 'email')

class EditPatientProfileForm(UserChangeForm):

    class Meta():
        model = PatientProfile
        fields = ('gender', 'age_group', 'preferred_gender', 'preferred_time')

class EditListenerProfileForm(UserChangeForm):

    class Meta():
        model = ListenerProfile
        fields = ('gender', 'age_group', 'preferred_time', 'preferred_days', 'category')

class EditTherapistProfileForm(UserChangeForm):

    class Meta():
        model = TherapistProfile
        fields = ('name', 'gender', 'age_group', 'preferred_time', 'preferred_days', 'category', 'education', 'experience')

class SelectValue(forms.Form):
    listener_name = forms.CharField(max_length=20)

class SelectTherapistValue(forms.Form):
    therapist_name = forms.CharField(max_length=20)
