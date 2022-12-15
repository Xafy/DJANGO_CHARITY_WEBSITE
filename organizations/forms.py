from django import forms
from .models import Organization

class OrganizationChangeForm(forms.ModelForm):

    class Meta:
        model = Organization
        fields = ['name', 'bio', 'avatar_thumbnail', 'logo',
                    'contact_information', 'location']
        widgets = {
            'name' : forms.TextInput(attrs={'class': '', 'name' : 'name', id : 'fullname'
                                                , 'placeholder' : 'الاسم الكامل'}),
            'bio' : forms.Textarea(attrs={'class': '', 'name' : 'bio', id : 'bio'
                                                , 'placeholder' : 'نبذة شخصية'}),
            'avatar_thumbnail' : forms.FileInput(attrs={'class': '', 'type' : 'file', 'name' : 'pic', id : 'pic' , 'accept' : 'image/*'
                                                , 'placeholder' : 'االصورة الشخصية'}),
            'logo' : forms.FileInput(attrs={'class': '', 'type' : 'file', 'name' : 'pic', id : 'pic' , 'accept' : 'image/*'
                                                , 'placeholder' : 'االصورة الشخصية'}),
            'contact_information': forms.TextInput(attrs={'class': '', 'name' : 'contact', id : 'contact'
                                                    , 'placeholder' : 'معلومات الاتصال'}),
            'location': forms.TextInput(attrs={'class': '', 'name' : 'location', id : 'location'
                                                    , 'placeholder' : 'العنوان'})
        }


class OrganizationCreateForm(forms.ModelForm):

    class Meta:
        model = Organization
        fields = ['name', 'bio', 'avatar_thumbnail', 'logo',
                    'contact_information', 'location']
        widgets = {
            'name' : forms.TextInput(attrs={'class': '', 'name' : 'name', id : 'fullname'
                                                , 'placeholder' : 'الاسم الكامل'}),
            'bio' : forms.Textarea(attrs={'class': '', 'name' : 'bio', id : 'bio'
                                                , 'placeholder' : 'نبذة شخصية'}),
            'avatar_thumbnail' : forms.FileInput(attrs={'class': '', 'type' : 'file', 'name' : 'pic', id : 'pic' , 'accept' : 'image/*'
                                                , 'placeholder' : 'االصورة الشخصية'}),
            'logo' : forms.FileInput(attrs={'class': '', 'type' : 'file', 'name' : 'pic', id : 'pic' , 'accept' : 'image/*'
                                                , 'placeholder' : 'االصورة الشخصية'}),
            'contact_information': forms.TextInput(attrs={'class': '', 'name' : 'contact', id : 'contact'
                                                    , 'placeholder' : 'معلومات الاتصال'}),
            'location': forms.TextInput(attrs={'class': '', 'name' : 'location', id : 'location'
                                                    , 'placeholder' : 'العنوان'})
        }