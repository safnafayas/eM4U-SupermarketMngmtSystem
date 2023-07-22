import django_filters

from django_filters import DateFilter, CharFilter
from . models import *


class Salesreport_Filter(django_filters.FilterSet):
    date = DateFilter(field_name="date", lookup_expr='icontains')

    class Meta:
        model = Salesreport
        fields = ['date']
#         # exclude=['Branch','return_amount','total_VAT','discount','user','cash_values']


class Stockreport_Filter(django_filters.FilterSet):

    date = DateFilter(field_name="date", lookup_expr='icontains')

    item_name = CharFilter(field_name="item_name", lookup_expr='icontains')

    class Meta:
        model = Stockreport
        fields = ['date', 'item_name']


class Taskassign_Filter(django_filters.FilterSet):
    task = CharFilter(field_name="task", lookup_expr='icontains')
    deadline = CharFilter(field_name="deadline", lookup_expr='icontains')
    # assigned_to = CharFilter(field_name="assigned_to")

    class Meta:
        model = taskassign
        fields = ['task', 'deadline', 'assigned_to']
# class Stockreport_Filter(django_filters.FilterSet):
#     start_date=DateFilter(field_name="date", lookup_expr='gte')
#     end_date=DateFilter(field_name="date", lookup_expr='lte')
#     class Meta:
#         model = Stockreport
#         fields =  ['date']
