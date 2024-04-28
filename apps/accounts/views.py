from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView

from webProject.utils import recaptcha_is_valid

from .forms import SignUpForm, UserInformationUpdateForm, UpdateProfileForm

from django.contrib.auth.decorators import login_required

from django.contrib import messages


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid() and recaptcha_is_valid(request):
            user = form.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'accounts\signup.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UserInformationUpdateForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='my_profile')
    else:
        user_form = UserInformationUpdateForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'accounts\my_profile.html', {'user_form': user_form, 'profile_form': profile_form})


@method_decorator(login_required, name='dispatch')
class UserUpdateView(UpdateView):
    form_class = UserInformationUpdateForm
    template_name = 'accounts\my_account.html'
    success_url = reverse_lazy('my_account')

    def get_object(self):
        return self.request.user




