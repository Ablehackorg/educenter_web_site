from django.contrib import admin

from course.models import Course,Subject,Student,Tutor,CourseLang,SubjectLang,TutorLang



# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display =['name','description']
class TutorAdmin(admin.ModelAdmin):
    list_display =['name','description']
    list_filter= ['subject']


admin.site.register(Course)
admin.site.register(Subject)
admin.site.register(Student,StudentAdmin)
admin.site.register(Tutor,TutorAdmin)
admin.site.register(CourseLang)
admin.site.register(SubjectLang)
admin.site.register(TutorLang)
