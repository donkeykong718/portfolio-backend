from django.db import models
from django import forms
from django.contrib import admin

# Create your models here.


class Tech(models.Model):
    name = models.CharField(max_length=120)
    logo = models.ImageField(upload_to="images/logos/", default="")

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=120)
    projectType = models.CharField(max_length=120)
    thumbnail = models.ImageField(upload_to="images/thumbnails/", default="")
    description = models.TextField(default="")
    tech = models.ManyToManyField(Tech, blank=True)
    url = models.URLField(default="")
    git = models.URLField(default="")

    def __str__(self):
        return self.title


class ProjectForm(forms.ModelForm):
    tech = forms.ModelMultipleChoiceField(
        queryset=Tech.objects.all(),
        widget=admin.widgets.FilteredSelectMultiple("Tech", is_stacked=False),
        required=False,
    )

    class Meta:
        model = Project
        fields = "__all__"


class ProjectAdmin(admin.ModelAdmin):
    form = ProjectForm
