from django import forms

from file.models import File


# create forms here
class add_filefolder_form(forms.ModelForm):
    folders = forms.ModelChoiceField(queryset=File.objects.filter(is_file=False))
    
    class Meta:
        model = File
        fields = [
            'name'
        ]