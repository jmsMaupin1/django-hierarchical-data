from django.shortcuts import render
from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from file.models import File
from file.forms import add_filefolder_form


# Create your views here.
@login_required()
def show_files(request):
    return render(request, 'files.html', {
        'files': request.user.folder.get_descendants(include_self=True)
    })


# If user decides to add a file, make sure its marked as such
def add_file_view(request):
    form = None

    if request.method == 'POST':
        form = add_filefolder_form(None, request.POST)

        if form.is_valid():
            new_file = form.save(commit=False)
            new_file.parent = form.cleaned_data['folders']
            new_file.is_file = True
            new_file.save()

        return HttpResponseRedirect(reverse('home'))
    
    return render(request, 'generic_form.html', {
        'form': add_filefolder_form(request.user)
    })


# If user decides to add a folder, make sure to makr it as not a file
def add_folder_view(request):
    form = None

    if request.method == 'POST':
        form = add_filefolder_form(None, request.POST)

        if form.is_valid():
            new_folder = form.save(commit=False)
            new_folder.parent = form.cleaned_data['folders']
            new_folder.is_file = False
            new_folder.save()
        
        return HttpResponseRedirect(reverse('home'))
    
    return render(request, 'generic_form.html', {
        'form': add_filefolder_form(request.user)
    })