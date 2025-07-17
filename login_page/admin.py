from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['email', 'name', 'is_active', 'is_staff', 'is_superuser']  # Include other fields you want in the list view
    list_filter = ['is_active', 'is_staff', 'is_superuser']  # Removed 'groups' field as it is part of PermissionsMixin
    search_fields = ['email', 'name']  # Allow searching by email and name
    ordering = ['email']  # Order by email by default

    # To display fields in the form for user creation and change
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('name',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Important dates', {'fields': ('last_login',)}),
    )

    # When adding a new user, the following fields will be displayed
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'name', 'is_active', 'is_staff', 'is_superuser'),
        }),
    )

    # Optionally, if you want to add user permissions and groups, 
    # you can uncomment this line (though it's not used in your model):
    # filter_horizontal = ('groups', 'user_permissions')

# Register the CustomUser model with the CustomUserAdmin
admin.site.register(CustomUser, CustomUserAdmin)
