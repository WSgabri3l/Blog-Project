from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def register(request):

    """Register new users."""

    if request.method != 'POST':

        #Blank form for registration

        form = UserCreationForm()

    else:

        form = UserCreationForm(data=request.POST)

        #Process the data.

        if form.is_valid():

            #Make a new user.

            new_user = form.save()
        
            login(request, new_user)

            return redirect('blog:index')
        
    #Display a blank or invalid form.
        
    context = {'form' : form}

    return render(request, 'registration/register.html', context)