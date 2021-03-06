from django.contrib import admin
from .models import TeacherUser
# Register your models here.
class TeacherUserAdmin(admin.ModelAdmin):
    list_display = ('teacherID', 'teacherName', 'teacherInstitute')
    list_filter = ('teacherInstitute',)
    raw_id_fields = ('teacherID', 'teacherInstitute')
admin.site.register(TeacherUser, TeacherUserAdmin)