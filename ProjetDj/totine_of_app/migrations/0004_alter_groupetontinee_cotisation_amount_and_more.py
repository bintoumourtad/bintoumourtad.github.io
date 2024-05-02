# Generated by Django 4.0 on 2019-01-01 12:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('totine_of_app', '0003_groupetontinee_delete_groupetontine'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupetontinee',
            name='cotisation_amount',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='groupetontinee',
            name='date_decréation',
            field=models.DateTimeField(),
        ),
        migrations.CreateModel(
            name='paiement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('montant_paiement', models.CharField(max_length=150)),
                ('date_paeiement', models.DateTimeField()),
                ('groupe_tontine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='totine_of_app.groupetontinee')),
                ('utilisateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='totine_of_app.user')),
            ],
        ),
    ]
