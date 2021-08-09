from django.contrib import admin
from .models import Project
from .form import ProjectAdminForm


class ProjectAdmin(admin.ModelAdmin):
    form = ProjectAdminForm
    readonly_fields = ('created', 'updated')


admin.site.register(Project, ProjectAdmin)
