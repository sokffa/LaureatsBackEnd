# Generated by Django 3.0.2 on 2020-01-10 20:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('laureats', '0008_etudiant'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employe',
            fields=[
                ('laureat_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='laureats.Laureat')),
                ('profession', models.CharField(default='', max_length=255)),
                ('date_debut', models.DateField()),
            ],
            options={
                'ordering': ['date_debut'],
            },
            bases=('laureats.laureat',),
        ),
    ]