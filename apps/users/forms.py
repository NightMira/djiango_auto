from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'avatar', 'privacy_level']

        widgets = {
            'bio': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Расскажите о себе...'
            }),

            'privacy_level': forms.Select(attrs={
                'class': 'form-control'
            }),
        }

    def clean_avatar(self):
        avatar = self.cleaned_data.get('avatar')

        if avatar:
            if avatar.size > 5 * 1024 * 1024:
                raise forms.ValidationError("Файл слишком большой (макс 5MB)")

        return avatar