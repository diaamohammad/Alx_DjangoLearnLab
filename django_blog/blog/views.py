
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.views import LoginView,LogoutView
from . forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required


class CustomLoginView(LoginView):

    template_name='login.html'

class CustomLogoutView(LogoutView):

    template_name='logout.html'

def register_view(request):

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid:
            user = form.save()
            login = (request,user)
            return redirect('profile')
        
    else:
        form = CustomUserCreationForm
    return render(request,'register.html',{'form':form})

@login_required
def profile_view(request):

    if request.method == 'POST':
        user = request.user
        user.email = request.POST.get('email')
        user.save()
        return redirect('profile')
    return render(request,'profile.html',{'user':request.user})