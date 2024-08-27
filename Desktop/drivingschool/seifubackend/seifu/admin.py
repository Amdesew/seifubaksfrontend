from django.contrib import admin
from .models import NewStudent, StudentResult

class NewStudentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone_number')

class ResultAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'result')

admin.site.register(NewStudent, NewStudentAdmin)
admin.site.register(StudentResult, ResultAdmin)