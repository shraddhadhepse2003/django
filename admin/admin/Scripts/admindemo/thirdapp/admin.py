from django.contrib import admin
from .models import Project

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    list_display=['project_name','project_status','emp','client']
    list_filter=['project_name','project_status']
admin.site.register(Project,ProjectAdmin)

