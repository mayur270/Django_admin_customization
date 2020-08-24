from django.contrib import admin
from django.contrib.auth.models import Group
from .models import coffee, coffee_file
from .functions import download_csv_function
from django.urls import path
from django.http import HttpResponseRedirect

class coffeeAdmin(admin.ModelAdmin, download_csv_function):
    list_display=['name','price','description']
    list_filter=['name',]
    search_fields=['name']
    actions=['download_csv']
    change_list_template = 'admin/local_change_list.html'

    download_csv_function.download_csv.short_description = 'Download CSV File'

    def get_urls(self):
        urls=super().get_urls()
        custom_urls = [path('fontsize/<int:size>/', self.change_font_size)]
        return custom_urls + urls

    def change_font_size(self,request,size):
        self.model.objects.all().update(font_size=size)
        self.message_user(request, 'font size successful')
        return HttpResonseRedirect("../")



# from django.contrib.admin import AdminSite
# class MyAdminSite(AdminSite):
#     login_template = 'admin/login.html'
#
# # Register templates for customization
# site = MyAdminSite()

# Register your models here.
admin.site.register(coffee, coffeeAdmin)
admin.site.register(coffee_file)

# UnRegister
admin.site.unregister(Group)
