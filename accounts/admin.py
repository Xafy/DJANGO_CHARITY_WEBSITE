from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserAdminCreationForm, UserAdminChangeForm

from django.contrib.auth import get_user_model
User = get_user_model()


class UserAdmin(BaseUserAdmin):
    model = User
    # The forms to add and change user instances
    form =  UserAdminChangeForm
    add_form = UserAdminCreationForm
    

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ['email', 'full_name', 'is_admin' , 'is_staff']
    list_filter = ['is_admin', 'is_active', 'is_staff']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('full_name', 'user_name',
                                    'slug','bio', 'avatar_thumbnail', 'contact_information', 'location'
                                    )}),
        ('Permissions', {'fields': ('is_admin','is_staff', 'is_active')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'full_name', 'user_name', 'password', 'password_2',
                        'slug', 'bio', 'avatar_thumbnail', 'contact_information', 'location'
                         )}
        ),
    )
    search_fields = ['email', 'full_name', 'user_name']
    ordering = ['email']
    filter_horizontal = ()


admin.site.register(User, UserAdmin)