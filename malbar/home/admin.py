from django.contrib import admin
from . models import *
# from django.contrib.admin.views.decorators import staff_member_required
# from django.shortcuts import render
# from django.urls import path
# from .models import Employee
# Register your models here.


# @admin.register(Employee)
# class EmployeeFormModelAdmin(admin.ModelAdmin):
#     list_display = ['emp_id', 'Name', 'Email',
#                     'Address', 'DOB', 'Gender', 'MobileNumber', 'Startdate', 'Location', 'Shift', 'Departement', 'Username', 'Password']
admin.site.register(User)
admin.site.register(Employee)
admin.site.register(Manager)

# admin.site.register(taskassign)
admin.site.register(Rating)
admin.site.register(Post)


@admin.register(Stockreport)
class StockreportModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'Branch_name', 'date', 'cost_per_unit',
                    'stock_value', 'item_name', 'stock', 'UOM']
    search_fields = ['Branch_name', 'date', 'item_name']
    list_filter = Stockreport.FilterFields

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False


@admin.register(taskassign)
class taskassignModelAdmin(admin.ModelAdmin):
    list_display = ['user', 'task', 'deadline', 'assigned_to']

    # search_fields = ['Branch_name', 'date', 'item_name']
    # list_filter = Stockreport.FilterFields

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False


@ admin.register(Salesreport)
class SalesreportModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'Branch', 'date', 'cash_values', 'card_sales',
                    'return_amount', 'discount', 'total_sales', 'net_sales', 'total_VAT']
    search_fields = ['Branch', 'date']
    # filter_horizontal=('total_sales','net_sales')
    list_filter = Salesreport.FilterFields

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False


@ admin.register(Alert)
class AlertModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'subject', 'alert']

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return True

    def has_change_permission(self, request, obj=None):
        return False
# @admin.register(todolist)
# class  todolistModelAdmin(admin.ModelAdmin):
#     # list_display=['id','subject','alert']
#     def get_form(self, request, obj=None, **kwargs):
#         form = super().get_form(request, obj=None, **kwargs)
#         if obj is None:

#             form.base_fields["priority"].disabled = True
#             form.base_fields["task"].disabled = True
#             form.base_fields["status"].disabled = True

#         return form

    # def has_add_permission(self, request):
    #   return False

    # def has_delete_permission(self, request, obj=None):
    #   return False


@ admin.register(todolist)
class todolistModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'priority', 'task', 'status']

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False
