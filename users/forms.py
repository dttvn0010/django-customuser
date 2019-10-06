from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    errorMessages = {
        'password2' : {
            'password_too_short' : 'Mật khẩu cần ít nhất 8 kí tự',
            'password_too_common' : 'Mật khẩu quá đơn giản'
        }
    }

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'phone', 'address')

    def clean_phone(self):
        phone = self.cleaned_data.get('phone', '')
        
        if not all('0' <= c <= '9' for c in phone):
            raise forms.ValidationError('SĐT chỉ được chứa chữ số')

        if len(phone) < 9:
            raise forms.ValidationError('SĐT phải có ít nhất 9 số')

        return phone

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'phone', 'address')