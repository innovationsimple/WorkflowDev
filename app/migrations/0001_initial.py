# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-15 00:43
from __future__ import unicode_literals

import app.files
import app.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='LegalAgreement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(editable=False)),
                ('modified', models.DateTimeField(editable=False)),
                ('label', models.CharField(default='', max_length=100)),
                ('slug', models.CharField(default='', max_length=100)),
                ('content', models.TextField(blank=True, default='')),
                ('pdf', models.FileField(blank=True, default='', upload_to='legal')),
                ('sign', models.BooleanField(default=False)),
                ('is_linked', models.BooleanField(default=False)),
                ('publicly_visible', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PdfGeneration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(editable=False)),
                ('modified', models.DateTimeField(editable=False)),
                ('name', models.CharField(default='', max_length=100)),
                ('pdf_file', models.FileField(default=None, null=True, storage=app.files.SecureFileSystemStorage(), upload_to='pdf_generation')),
                ('pagesize', models.CharField(blank=True, choices=[('LETTER', 'Letter'), ('LEGAL', 'Legal'), ('A4', 'A4')], default='LETTER', max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PdfGenerationField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(editable=False)),
                ('modified', models.DateTimeField(editable=False)),
                ('page_number', models.PositiveIntegerField()),
                ('x', models.PositiveIntegerField()),
                ('y', models.PositiveIntegerField()),
                ('field_type', models.CharField(choices=[('string', 'Text Field'), ('signature', 'Signature'), ('checkbox', 'Checkbox'), ('image', 'Image Field')], default='string', max_length=100)),
                ('field_name', models.CharField(default='', max_length=100)),
                ('field_model', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
                ('pdf', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.PdfGeneration')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SecureUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(editable=False)),
                ('modified', models.DateTimeField(editable=False)),
                ('name', models.CharField(default='', max_length=200)),
                ('upload', models.FileField(default=None, null=True, storage=app.files.SecureFileSystemStorage(), upload_to=app.models.secure_upload_path)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='WorkflowWizard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(editable=False)),
                ('modified', models.DateTimeField(editable=False)),
                ('is_template', models.BooleanField(default=False)),
                ('name', models.CharField(default='', max_length=200)),
                ('active', models.BooleanField(default=False)),
                ('deleted', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='WorkflowWizardForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(editable=False)),
                ('modified', models.DateTimeField(editable=False)),
                ('name', models.CharField(default='', max_length=200)),
                ('description', models.TextField(default='')),
                ('active', models.BooleanField(default=False)),
                ('deleted', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='WorkflowWizardFormField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(editable=False)),
                ('modified', models.DateTimeField(editable=False)),
                ('name', models.CharField(default='', max_length=200)),
                ('description', models.TextField(default='')),
                ('active', models.BooleanField(default=False)),
                ('deleted', models.BooleanField(default=False)),
                ('required', models.BooleanField(default=False)),
                ('ordering', models.PositiveIntegerField(default=2000)),
                ('form', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fields', to='app.WorkflowWizardForm')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='WorkflowWizardStep',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(editable=False)),
                ('modified', models.DateTimeField(editable=False)),
                ('name', models.CharField(default='', max_length=200)),
                ('description', models.TextField(default='')),
                ('completion_code', models.CharField(blank=True, default='', max_length=100)),
                ('active', models.BooleanField(default=False)),
                ('deleted', models.BooleanField(default=False)),
                ('required', models.BooleanField(default=False)),
                ('ordering', models.PositiveIntegerField(default=2000)),
                ('employer', models.BooleanField(default=False, verbose_name='Employer Step')),
                ('agreement', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.LegalAgreement')),
                ('form', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.WorkflowWizardForm')),
                ('pdfgen', models.ManyToManyField(blank=True, to='app.PdfGeneration', verbose_name='PDF Forms (Generated)')),
                ('workflow_wizard', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='steps', to='app.WorkflowWizard')),
            ],
            options={
                'ordering': ['workflow_wizard__id', 'ordering'],
            },
        ),
    ]