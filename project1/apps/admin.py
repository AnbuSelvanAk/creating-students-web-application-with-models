from django.contrib import admin
from apps.models import Student
class StudentAdmin(admin.ModelAdmin):
	list_display=['sno','sname','ssalary','saddress']
admin.site.register(Student,StudentAdmin)