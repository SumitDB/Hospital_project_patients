from django.contrib import admin
from .models import Customer


@admin.register(Customer)
class UserAdmin(admin.ModelAdmin):
    list_display=('id','name','age','gender','email', 'mobile','address','city','complaints','pulse','blood_pressure',"temprature",
        'blood_suger_level','genral_exams')