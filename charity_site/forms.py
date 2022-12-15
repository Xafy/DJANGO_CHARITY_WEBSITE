from django import forms
from django.contrib.auth.password_validation import validate_password
from django.core import validators
from django.contrib.auth import get_user_model
User = get_user_model()


class SigninForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'input', 'name' : 'user-name' , 'id' : "username"}), label='')    
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input', 'name' : 'password' , 'id' : "password"}), label='')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email = email)
        if not qs.exists():
            raise forms.ValidationError('the email or the password you are using are not correct')
        else :
            return email
    
    def clean_password(self):
        password = self.cleaned_data.get('password')
        if not password:
            raise forms.ValidationError("Please enter your password")
        # elif not qs.exists():
        #     raise forms.ValidationError("wrong password")
        else:
            return password


class SignupForm(forms.Form):
    # firstname       = forms.CharField(widget=forms.TextInput(attrs={'class': 'col-3 border rounded-pill p-2 my-2 mx-2', 'placeholder' : 'الاسم الأول'}), label='')
    # seconedname     = forms.CharField(widget=forms.TextInput(attrs={'class': 'col-3 border rounded-pill p-2 my-2 mx-auto', 'placeholder' : 'الاسم الثاني'}), label='')
    # lastname        = forms.CharField(widget=forms.TextInput(attrs={'class': 'col-3 border rounded-pill p-2 my-2 mx-2', 'placeholder' : 'الاسم الثالث'}), label='')
    # phone           = forms.CharField(widget=forms.TextInput(attrs={'class': 'col-12 border rounded-pill p-2 my-2 mx-1', 'type':'tel', 'placeholder' : 'رقم الهاتف'}), label='رقم الهاتف')
    # birth_date      = forms.DateField(widget=forms.DateInput(attrs={'class': 'col-12 border rounded-pill p-2 my-2 mx-1', 'type':'date', 'placeholder' : 'تاريخ الميلاد'}), label='تاريخ الميلاد')
    email           = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'input', 'name' : 'email' , 'id' : "email"}), label='البريد الالكتروني')
    password        = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input', 'name' : 'password' , 'id' : "pass"}), label='كلمة السر')
    password_2      = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input', 'name' : 'confirmpassword' , 'id' : "pass-conf"}), label='تأكيد كلمة السر')
    full_name       = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'name' : 'fullname' , 'id' : "fullname"}), label='الاسم كامل')
    user_name       = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'name' : 'username' , 'id' : "user"}), label='اسم العضو المميز')

    def clean_user_name(self):
        user_name = self.cleaned_data.get('user_name') 
        qs = User.objects.filter(user_name = user_name)
        if qs.exists():
            raise forms.ValidationError('username is taken')
        return user_name

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email = email)
        if qs.exists():
            raise forms.ValidationError('email is taken')
        return email

    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password_2')
        if password2 != password:
            raise forms.ValidationError('passwords must match')
        
        return data
