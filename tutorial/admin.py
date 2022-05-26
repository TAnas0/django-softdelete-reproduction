from django.contrib import admin
from tutorial.models import Company, Employee


class CompanyAdmin(admin.ModelAdmin):
    pass
admin.site.register(Company, CompanyAdmin)


class EmployeeAdmin(admin.ModelAdmin):
    pass
admin.site.register(Employee, EmployeeAdmin)
