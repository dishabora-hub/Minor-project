from django.contrib import admin
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import Member, Attendance, Payment, Notification

# Register your models here.
class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'membership_plan', 'fees_paid', 'fees_due')
    search_fields = ('name', 'email')
    list_filter = ('membership_plan',)

class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('member', 'date', 'status')
    list_filter = ('status', 'date')

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('member', 'payment_date', 'amount', 'status')
    list_filter = ('status',)

class NotificationAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
    search_fields = ('title',)

# Registering the models with admin
admin.site.register(Member, MemberAdmin)
admin.site.register(Attendance, AttendanceAdmin)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(Notification, NotificationAdmin)

# Create a 'Gym Owner' group and assign permissions manually
@receiver(post_migrate)
def create_gym_owner_group(sender, **kwargs):
    group, created = Group.objects.get_or_create(name='Gym Owner')
    
    if created:
        # Get the content types for the models
        member_content_type = ContentType.objects.get_for_model(Member)
        attendance_content_type = ContentType.objects.get_for_model(Attendance)
        payment_content_type = ContentType.objects.get_for_model(Payment)
        notification_content_type = ContentType.objects.get_for_model(Notification)

        # Get the permissions for the models
        add_member_permission = Permission.objects.get(content_type=member_content_type, codename='add_member')
        change_member_permission = Permission.objects.get(content_type=member_content_type, codename='change_member')
        view_member_permission = Permission.objects.get(content_type=member_content_type, codename='view_member')
        delete_member_permission = Permission.objects.get(content_type=member_content_type, codename='delete_member')

        add_attendance_permission = Permission.objects.get(content_type=attendance_content_type, codename='add_attendance')
        change_attendance_permission = Permission.objects.get(content_type=attendance_content_type, codename='change_attendance')
        view_attendance_permission = Permission.objects.get(content_type=attendance_content_type, codename='view_attendance')
        delete_attendance_permission = Permission.objects.get(content_type=attendance_content_type, codename='delete_attendance')

        add_payment_permission = Permission.objects.get(content_type=payment_content_type, codename='add_payment')
        change_payment_permission = Permission.objects.get(content_type=payment_content_type, codename='change_payment')
        view_payment_permission = Permission.objects.get(content_type=payment_content_type, codename='view_payment')
        delete_payment_permission = Permission.objects.get(content_type=payment_content_type, codename='delete_payment')

        add_notification_permission = Permission.objects.get(content_type=notification_content_type, codename='add_notification')
        change_notification_permission = Permission.objects.get(content_type=notification_content_type, codename='change_notification')
        view_notification_permission = Permission.objects.get(content_type=notification_content_type, codename='view_notification')
        delete_notification_permission = Permission.objects.get(content_type=notification_content_type, codename='delete_notification')

        # Assign permissions to the group
        group.permissions.set([
            add_member_permission, change_member_permission, view_member_permission, delete_member_permission,
            add_attendance_permission, change_attendance_permission, view_attendance_permission, delete_attendance_permission,
            add_payment_permission, change_payment_permission, view_payment_permission, delete_payment_permission,
            add_notification_permission, change_notification_permission, view_notification_permission, delete_notification_permission
        ])
        group.save()
