from django.contrib import admin

from application.models import Student, Login, MonthlyPackage, HalfPackage, YearlyPackage, NewAdmin

# Register your models here.
admin.site.register(Student)
admin.site.register(Login)
admin.site.register(MonthlyPackage)
admin.site.register(HalfPackage)
admin.site.register(YearlyPackage)
admin.site.register(NewAdmin)