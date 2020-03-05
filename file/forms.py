from django import forms

from file.models import File


# create forms here
class add_filefolder_form(forms.ModelForm):
    folders = forms.ModelChoiceField(queryset=File.objects.filter(is_file=False))
    
    def __init__(self, user, *args, **kwargs):
        super(add_filefolder_form, self).__init__(*args, **kwargs)

        if user:
            available_folders = user.folder \
                .get_descendants(include_self=True) \
                .filter(is_file=False)
            self.fields['folders'].queryset = available_folders

    class Meta:
        model = File
        fields = [
            'name'
        ]