from django.contrib import admin
from .models import Tech, Project, ProjectAdmin

# Register your models here.

admin.site.register(Tech)
admin.site.register(Project, ProjectAdmin)
