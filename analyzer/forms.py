from django import forms
from .models import LegalDocument  # Make sure this matches your actual model name
from django.utils.translation import gettext_lazy as _

class UploadForm(forms.ModelForm):
    class Meta:
        model = LegalDocument
        fields = ['file']  # Add more fields if needed (e.g. 'title', 'description')

        widgets = {
            'file': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'accept': 'application/pdf',
            }),
        }

        labels = {
            'file': _('Upload your PDF document'),
        }
