from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout

from fileuser.models import User
from fileuser.forms import LoginForm, RegisterForm

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                username=data['username'],
                password=data['password']
            )

            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))

    form = LoginForm()
    return render(request, 'generic_form.html', {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create_user(
                username=data['username'],
                password=data['password1']
            )
            login(request, user)
            return HttpResponseRedirect(reverse('home'))

    else:
        form = RegisterForm()

    return render(request, 'generic_form.html', {
        'form': form
    })