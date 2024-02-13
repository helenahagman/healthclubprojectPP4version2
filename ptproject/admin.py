from django.contrib import admin
from .models import Profile, Contact, Session, Booking
from django_summernote.admin import SummernoteModelAdmin


admin.site.register(Profile)
admin.site.register(Session)
admin.site.register(MemberComment)


@admin.register(Booking)
class BookingAdmin(SummernoteModelAdmin):
    list_display = ('name', 'phonenumber', 'email', 'age', 'gender', 'message', 'date', 'time', 'approved')
    search_fields = ('name', 'email')
    list_filter = ('approved', 'date')
    actions = ['approve_booking', 'deny_booking']

    def approve_booking(self, request, queryset):
        queryset.update(approved=True)
    approve_booking.short_description = "Approve selected bookings"

    def deny_booking(self, request, queryset):
        queryset.update(approved=False)
    deny_booking.short_description = "Deny selected bookings"

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name_contact', 'email', 'contact_message', 'created_on')
    list_filter = ('created_on',)
    list_display_links = ('name_contact',)
    search_fields = ('name_contact', 'email', 'contact_message')

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'phone_number', 'email')
    list_filter = ('user',)
    search_fields = ('user__username', 'first_name', 'last_name', 'phone_number', 'email')

@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ('trainer_name', 'session_type', 'date', 'start_time', 'end_time', 'booked')
    list_filter = ('date', 'trainer_name')
    search_fields = ('trainer_name', 'session_type')
