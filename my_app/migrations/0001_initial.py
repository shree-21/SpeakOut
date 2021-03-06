# Generated by Django 2.1.3 on 2018-12-11 06:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=600)),
            ],
        ),
        migrations.CreateModel(
            name='ListenerProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('MALE', 'Male'), ('FEMALE', 'Female'), ('OTHER', 'Other')], max_length=10)),
                ('age_group', models.CharField(choices=[('13-19', '13-19'), ('20-25', '20-25'), ('26-35', '26-35'), ('36-45', '36-45'), ('46-55', '46-55'), ('56-65', '56-65')], max_length=10)),
                ('preferred_time', multiselectfield.db.fields.MultiSelectField(choices=[('EARLY MORNING (6-8)', 'Early Morning (6-8)'), ('MORNING (8-11)', 'Morning (8-11)'), ('NOON (12-2)', 'Noon (12-2)'), ('LATE AFTERNOON (2-5)', 'Late Afternoon (2-5)'), ('EVENING (5-9)', 'Evening (5-9)'), ('NIGHT (9-11)', 'Night (9-11)')], max_length=94)),
                ('preferred_days', multiselectfield.db.fields.MultiSelectField(choices=[('MONDAY', 'Monday'), ('TUESDAY', 'Tuesday'), ('WEDNESDAY', 'Wednesday'), ('THURSDAY', 'Thursday'), ('FRIDAY', 'Friday'), ('SATURDAY', 'Saturday'), ('SUNDAY', 'Sunday')], max_length=56)),
                ('is_listener', models.BooleanField(default=True)),
                ('category', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='my_app.Categories')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='listener_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PatientProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('MALE', 'Male'), ('FEMALE', 'Female'), ('PREFER NOT TO SAY', 'Prefer Not To Say')], max_length=20)),
                ('age_group', models.CharField(choices=[('13-19', '13-19'), ('20-25', '20-25'), ('26-35', '26-35'), ('36-45', '36-45'), ('46-55', '46-55'), ('56-65', '56-65')], max_length=10)),
                ('preferred_gender', models.CharField(choices=[('MALE', 'Male'), ('FEMALE', 'Female'), ('OTHER', 'Other')], max_length=20)),
                ('preferred_time', multiselectfield.db.fields.MultiSelectField(choices=[('EARLY MORNING (6-8)', 'Early Morning (6-8)'), ('MORNING (8-11)', 'Morning (8-11)'), ('NOON (12-2)', 'Noon (12-2)'), ('LATE AFTERNOON (2-5)', 'Late Afternoon (2-5)'), ('EVENING (5-9)', 'Evening (5-9)'), ('NIGHT (9-11)', 'Night (9-11)')], max_length=94)),
                ('is_patient', models.BooleanField(default=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='patient_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TherapistProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('gender', models.CharField(choices=[('MALE', 'Male'), ('FEMALE', 'Female'), ('OTHER', 'Other')], max_length=10)),
                ('age_group', models.CharField(choices=[('13-19', '13-19'), ('20-25', '20-25'), ('26-35', '26-35'), ('36-45', '36-45'), ('46-55', '46-55'), ('56-65', '56-65')], max_length=10)),
                ('preferred_time', multiselectfield.db.fields.MultiSelectField(choices=[('EARLY MORNING (6-8)', 'Early Morning (6-8)'), ('MORNING (8-11)', 'Morning (8-11)'), ('NOON (12-2)', 'Noon (12-2)'), ('LATE AFTERNOON (2-5)', 'Late Afternoon (2-5)'), ('EVENING (5-9)', 'Evening (5-9)'), ('NIGHT (9-11)', 'Night (9-11)')], max_length=94)),
                ('preferred_days', multiselectfield.db.fields.MultiSelectField(choices=[('MONDAY', 'Monday'), ('TUESDAY', 'Tuesday'), ('WEDNESDAY', 'Wednesday'), ('THURSDAY', 'Thursday'), ('FRIDAY', 'Friday'), ('SATURDAY', 'Saturday'), ('SUNDAY', 'Sunday')], max_length=56)),
                ('education', models.TextField()),
                ('experience', models.TextField()),
                ('is_therapist', models.BooleanField(default=True)),
                ('category', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='my_app.Categories')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='therapist_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
