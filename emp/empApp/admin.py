from django.contrib import admin
from empApp.models import Employee


class EmplyoeeAdmin(admin.ModelAdmin):
    list_display=['eno','ename','esal','eaddr']

admin.site.register(Employee, EmplyoeeAdmin)

