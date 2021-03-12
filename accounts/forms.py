from django.forms import ModelForm
# from django.contrib.auth.models import User
# from django.contrib.auth import get_user_model
from django.contrib.auth.forms import (
    AuthenticationForm, PasswordChangeForm,
    PasswordResetForm, SetPasswordForm,
    UserChangeForm, UserCreationForm
)

from django.conf import settings
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from django.contrib.auth import get_user_model

User = get_user_model()



class UserInfoChangeForm(ModelForm):
    class Meta:
        model = User
        fields = [
            'email',
        ]
    def __init__(self, email=None, first_name=None, last_name=None, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super().__init__(*args, **kwargs)
        if email:
            self.fields['email'].widget.attrs['value'] = email
        if first_name:
            self.fields['first_name'].widget.attrs['value'] = first_name
        if last_name:
            self.fields['last_name'].widget.attrs['value'] = last_name

    def update(self, user):
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()

class EmailChangeForm(ModelForm):
    class Meta:
        model = User
        fields = ['email']

    def __init__(self, email=None, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super().__init__(*args, **kwargs)
        if email:
            self.fields['email'].widget.attrs['value'] = email

    def update(self, user):
        user.email = self.cleaned_data['email']
        user.save()


class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super().__init__(*args, **kwargs)

class CustomPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super().__init__(*args, **kwargs)

class CustomPasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super().__init__(*args, **kwargs)

class CustomSetPasswordForm(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super().__init__(*args, **kwargs)

class AdminUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email','category')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = '__all__'
        
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email','category')

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix','')
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = '選択して下さい'

    def clean_email(self):
        email = self.cleaned_data['email']
        User.objects.filter(email=email, is_active=False).delete()
        return email



    