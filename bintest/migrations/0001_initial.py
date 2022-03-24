# Generated by Django 3.2.12 on 2022-03-24 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agentname',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_id', models.TextField(blank=True, null=True)),
                ('firstname', models.TextField(blank=True, null=True)),
                ('lastname', models.TextField(blank=True, null=True)),
                ('email', models.TextField(blank=True, null=True)),
                ('phone', models.TextField(blank=True, null=True)),
                ('pollingunit_uniqueid', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'agentname',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AnnouncedLgaResults',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result_id', models.TextField(blank=True, null=True)),
                ('lga_name', models.TextField(blank=True, null=True)),
                ('party_abbreviation', models.TextField(blank=True, null=True)),
                ('party_score', models.TextField(blank=True, null=True)),
                ('entered_by_user', models.TextField(blank=True, null=True)),
                ('date_entered', models.TextField(blank=True, null=True)),
                ('user_ip_address', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'announced_lga_results',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AnnouncedPuResults',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result_id', models.TextField(blank=True, null=True)),
                ('polling_unit_uniqueid', models.TextField(blank=True, null=True)),
                ('party_abbreviation', models.TextField(blank=True, null=True)),
                ('party_score', models.TextField(blank=True, null=True)),
                ('entered_by_user', models.TextField(blank=True, null=True)),
                ('date_entered', models.TextField(blank=True, null=True)),
                ('user_ip_address', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'announced_pu_results',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AnnouncedStateResults',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result_id', models.TextField(blank=True, null=True)),
                ('state_name', models.TextField(blank=True, null=True)),
                ('party_abbreviation', models.TextField(blank=True, null=True)),
                ('party_score', models.TextField(blank=True, null=True)),
                ('entered_by_user', models.TextField(blank=True, null=True)),
                ('date_entered', models.TextField(blank=True, null=True)),
                ('user_ip_address', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'announced_state_results',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AnnouncedWardResults',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result_id', models.TextField(blank=True, null=True)),
                ('ward_name', models.TextField(blank=True, null=True)),
                ('party_abbreviation', models.TextField(blank=True, null=True)),
                ('party_score', models.TextField(blank=True, null=True)),
                ('entered_by_user', models.TextField(blank=True, null=True)),
                ('date_entered', models.TextField(blank=True, null=True)),
                ('user_ip_address', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'announced_ward_results',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Lga',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uniqueid', models.TextField(blank=True, null=True)),
                ('lga_id', models.TextField(blank=True, null=True)),
                ('lga_name', models.TextField(blank=True, null=True)),
                ('state_id', models.TextField(blank=True, null=True)),
                ('lga_description', models.TextField(blank=True, null=True)),
                ('entered_by_user', models.TextField(blank=True, null=True)),
                ('date_entered', models.TextField(blank=True, null=True)),
                ('user_ip_address', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'lga',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Party',
            fields=[
                ('id', models.TextField(blank=True, primary_key=True, serialize=False)),
                ('partyid', models.TextField(blank=True, null=True)),
                ('partyname', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'party',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PollingUnit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uniqueid', models.TextField(blank=True, null=True)),
                ('polling_unit_id', models.TextField(blank=True, null=True)),
                ('ward_id', models.TextField(blank=True, null=True)),
                ('lga_id', models.TextField(blank=True, null=True)),
                ('uniquewardid', models.TextField(blank=True, null=True)),
                ('polling_unit_number', models.TextField(blank=True, null=True)),
                ('polling_unit_name', models.TextField(blank=True, null=True)),
                ('polling_unit_description', models.TextField(blank=True, null=True)),
                ('lat', models.TextField(blank=True, null=True)),
                ('long', models.TextField(blank=True, null=True)),
                ('entered_by_user', models.TextField(blank=True, null=True)),
                ('date_entered', models.TextField(blank=True, null=True)),
                ('user_ip_address', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'polling_unit',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='States',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_id', models.TextField(blank=True, null=True)),
                ('state_name', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'states',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Ward',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uniqueid', models.TextField(blank=True, null=True)),
                ('ward_id', models.TextField(blank=True, null=True)),
                ('ward_name', models.TextField(blank=True, null=True)),
                ('lga_id', models.TextField(blank=True, null=True)),
                ('ward_description', models.TextField(blank=True, null=True)),
                ('entered_by_user', models.TextField(blank=True, null=True)),
                ('date_entered', models.TextField(blank=True, null=True)),
                ('user_ip_address', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'ward',
                'managed': False,
            },
        ),
    ]