from django.contrib import admin
from .models import *


class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_number', 'website', 'company_name', 'subject', 'message')

class PasswordResetAdmin(admin.ModelAdmin):
    list_display = ('user', 'reset_id', 'created_when')

class UserTestimonialAdmin(admin.ModelAdmin):
    list_display = ('image', 'name', 'designation', 'message')    

class InforAdmin(admin.ModelAdmin):
    list_display = ('name', 'email_id', 'message')



admin.site.register(Contact, ContactAdmin)

admin.site.register(PasswordReset, PasswordResetAdmin)

admin.site.register(UserTestimonial, UserTestimonialAdmin)

admin.site.register(Infor, InforAdmin)