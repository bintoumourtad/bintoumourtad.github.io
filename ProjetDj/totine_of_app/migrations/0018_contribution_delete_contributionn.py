# Generated by Django 4.0 on 2024-05-02 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('totine_of_app', '0017_paiements_delete_paiement'),
    ]

    operations = [
        migrations.CreateModel(
            name='contribution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=150)),
                ('prenom', models.CharField(max_length=150)),
                ('montant', models.CharField(max_length=150)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='contributionn',
        ),
    ]