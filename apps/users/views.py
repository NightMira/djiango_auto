from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Profile
from .forms import ProfileForm


def get_profile(user):
    return Profile.objects.get_or_create(user=user)[0]


@login_required
def profile_view(request):
    profile = get_profile(request.user)

    return render(request, 'users/profile.html', {
        'profile': profile
    })


@login_required
def profile_edit(request):
    profile = get_profile(request.user)

    if request.method == 'POST':
        form = ProfileForm(
            request.POST,
            request.FILES,
            instance=profile
        )

        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'users/profile_edit.html', {
        'form': form,
        'profile': profile
    })