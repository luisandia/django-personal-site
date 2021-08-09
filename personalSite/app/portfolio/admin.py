from django.contrib import admin
from .models import Project
from .form import ProjectAdminForm


class ProjectAdmin(admin.ModelAdmin):
    form = ProjectAdminForm
    list_editable = ('order', )
    list_display = (
        'title',
        'order',
      )

    readonly_fields = ('created', 'updated')


admin.site.register(Project, ProjectAdmin)
