from ckeditor.widgets import CKEditorWidget
from django import forms
from .models import Project

class ProjectAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Project
        fields = '__all__'
