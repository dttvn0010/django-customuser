
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import CustomUserCreationForm

def signUp(request):
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            
            user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'])

            login(request, user) 

            return redirect('home')
        else:
            for field in form.errors:
                for error in form.errors[field].data:
                    fieldErrorMessages = CustomUserCreationForm.errorMessages.get(field, {})
                    if error.code in fieldErrorMessages:
                        error.message = fieldErrorMessages[error.code]

                    print(f'Error : Field = {field}, Code = {error.code}, Message = {error.message} ')
    
    return render(request, 'registration/signup.html', {'form' : form})