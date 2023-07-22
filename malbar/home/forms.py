from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.db import transaction
from django.core.exceptions import ValidationError
from . models import *
from django.core import validators
import datetime


# class UserRegistrationForm(UserCreationForm):
#     first_name = forms.CharField(max_length=101)
#     last_name = forms.CharField(max_length=101)
#     email = forms.EmailField()

#     class Meta:
#         model = User
#         fields = ['username', 'first_name', 'last_name',
#                   'email', 'password1', 'password2']


class ManagerRegistrationForm(UserCreationForm):

    # def name_value(value):
    #     alphabets = str(value)
    #     if len(alphabets) != ('^[a-zA-z.]*$'):
    #         raise forms.ValidationError("Doesnot match name format")

    Name = forms.CharField(required=True, max_length=201
                           )

    # email = forms.EmailField(required=True)
    def mobile_no(value):
        mobile = str(value)
        if len(mobile) != 10:
            raise forms.ValidationError("Mobile Number Should be 10 digit")
    MobileNumber = forms.IntegerField(validators=[mobile_no])
    Branch_name = forms.CharField(required=True, max_length=201)

    def clean_Name(self):
        Name = self.cleaned_data.get('Name')
        # if not category:
        # 	raise forms.ValidationError('This field is required')
        for instance in Manager.objects.all():
            if instance.Name == Name:
                raise forms.ValidationError(str(Name) + ' is already created')
        return Name

    def clean_Email_address(self):
        Email_address = self.cleaned_data.get('Email_address')
        # if not category:
        # 	raise forms.ValidationError('This field is required')
        for instance in User.objects.all():
            if instance.Email_address == Email_address:
                raise forms.ValidationError(
                    str(Email_address) + ' is already created')
        return Email_address

    def clean_MobileNumber(self):
        MobileNumber = self.cleaned_data.get('MobileNumber')
        # if not category:
        # 	raise forms.ValidationError('This field is required')
        for instance in Manager.objects.all():
            if instance.MobileNumber == MobileNumber:
                raise forms.ValidationError(
                    str(MobileNumber) + ' is already created')
        return MobileNumber

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'Name',
                  'email', 'MobileNumber', 'Branch_name', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'style': 'width: 200px; margin:auto;'}),
            'Name': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 300px; margin:auto;', 'pattern': '  [A-Za-z ]+', 'title': 'Enter Character Only'}),
            'MobileNumber': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 300px; margin:auto;', 'minlength': 10, 'maxlength': 10, 'required': True}),
            #   'email':forms.EmailInput(attrs={'class' : 'form-control','style': 'width: 300px;'}),
            'Branch_name': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 300px; margin:auto;'}),
            'password1': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 300px; margin:auto;'}),
            'password2': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 300px; margin:auto;'}),



        }
    # def clean_category(self):
    #   Name = self.cleaned_data.get('Name')
    #   # if not category:
    #   # 	raise forms.ValidationError('This field is required')
    #   for instance in Manager.objects.all():
    #     if instance.Name== Name:
    #       raise forms.ValidationError(str(Name) + ' is already created')
    #   return Name

    @ transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_manager = True
        # user.first_name=self.cleaned_data.get('first_name')
        # user.last_name=self.cleaned_data.get('last_name')
        user.save()
        manager = Manager.objects.create(user=user)
        manager.Name = self.cleaned_data.get('Name')
        # manager.email=self.cleaned_data.get('email')
        manager.MobileNumber = self.cleaned_data.get('MobileNumber')
        manager.Branch_name = self.cleaned_data.get('Branch_name')
        manager.save()
        return user


class EmployeeRegistrationForm(forms.ModelForm):

    def birthday_check(self, form):
        cleaned_data = super(EmployeeRegistrationForm, self).clean()
        bday = self.cleaned_data["Dob"]
        fraud_detect = abs(date.today() - bday)
        if ((fraud_detect.days / 365.0) < 18):
            # WHAT ABOUT THE BABIES!!!!
            raise forms.ValidationError("Sorry, you cannot create an account.",
                                        code="too_young",
                                        )
        return cleaned_data

    class Meta:
        model = Employee
        fields = ['Name', 'MobileNumber', 'Address', 'Dob', 'Gender',
                  'Startdate', 'Shift', 'Branch_name', 'Department']
        widgets = {
            'Name': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 300px; margin:auto;', 'pattern': '[A-Za-z ]+', 'title': 'Enter Character Only'}),
            'MobileNumber': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 300px; margin:auto;', 'minlength': 10, 'maxlength': 10, 'required': True}),
            #   'email':forms.EmailInput(attrs={'class' : 'form-control','style': 'width: 300px;'}),
            'Address': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 300px; margin:auto;'}),
            'Dob': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'style': 'width: 300px; margin:auto;'}),
            'Gender': forms.Select(attrs={'class': 'form-control', 'style': 'width: 300px; margin:auto;'}),
            'Startdate': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'style': 'width: 300px; margin:auto;'}),
            'Shift': forms.Select(attrs={'class': 'form-control', 'style': 'width: 300px; margin:auto;'}),
            'Branch_name': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 300px; margin:auto;'}),
            'Department': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 300px; margin:auto;'}),



        }

    # def clean_Name(self):
    #   for instance in Employee.objects.all():
    #     Name = self.cleaned_data.get('Name')
    #     if instance.Name==Name:
    #       raise forms.ValidationError(Name + ' is already added')
    #   return Name


class Employee_LoginForm(forms.ModelForm):
    # email = forms.EmailField(required=True)

    class Meta:
        model = Employee
        fields = ["Name", "MobileNumber", "Branch_name", "Department"]
        widgets = {
            'Name': forms.TextInput(attrs={'style': 'width: 200px; margin:auto;', 'pattern': '[A-Za-z ]+'}),
            'MobileNumber': forms.TextInput(attrs={'style': 'width: 200px; margin:auto;', 'minlength': 10, 'maxlength': 10, 'required': True}),
        }


class Sales_reportForm(forms.ModelForm):

    class Meta:
        model = Salesreport
        fields = ['Branch', 'date', 'cash_values', 'card_sales',
                  'return_amount', 'discount', 'total_sales', 'net_sales', 'total_VAT']
        widgets = {
            'Branch': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 300px; margin:auto; background-color:grey; color:white;'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'style': 'width: 300px; margin:auto; background-color:grey; color:white;'}),
            'cash_values': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 300px; margin:auto; background-color:grey; color:white; '}),
            #   'email':forms.EmailInput(attrs={'class' : 'form-control','style': 'width: 300px;'}),
            'card_sales': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 300px; margin:auto; background-color:grey; color:white;'}),
            'return_amount': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 300px; margin:auto; background-color:grey; color:white;'}),
            'discount': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 300px; margin:auto; background-color:grey; color:white;'}),
            'total_sales': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 300px; margin:auto; background-color:grey; color:white;'}),
            'net_sales': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 300px; margin:auto; background-color:grey; color:white;'}),
            'total_VAT': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 300px; margin:auto; background-color:grey; color:white;'}),
        }


class Stock_reportForm(forms.ModelForm):
    class Meta:
        model = Stockreport
        fields = ['Branch_name', 'date', 'cost_per_unit',
                  'stock_value', 'item_name', 'stock', 'UOM']
        widgets = {
            'Branch_name': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 300px; margin:auto; background-color:grey; color:white;'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'style': 'width: 300px; margin:auto; background-color:grey; color:white;'}),
            'cost_per_unit': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 300px; margin:auto; background-color:grey; color:white; '}),
            #   'email':forms.EmailInput(attrs={'class' : 'form-control','style': 'width: 300px;'}),
            'stock_value': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 300px; margin:auto; background-color:grey; color:white;'}),
            'item_name': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 300px; margin:auto; background-color:grey; color:white;'}),
            'stock': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 300px; margin:auto; background-color:grey; color:white;'}),
            'UOM': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 300px; margin:auto; background-color:grey; color:white;'}),

        }


class Alert_Form(forms.ModelForm):
    class Meta:
        model = Alert
        fields = ['subject', 'alert']
        widgets = {
            'subject': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 300px; margin:auto; background-color:white;'}),
            'alert': forms.Textarea(attrs={'class': 'form-control', 'style': 'width: 300px; margin:auto; background-color:white;'}),
        }


class To_do_Form(forms.ModelForm):
    class Meta:
        model = todolist
        fields = ['priority', 'task', 'status']
        widgets = {
            'priority': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 300px; margin:auto; background-color:white;'}),
            'task': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 300px; margin:auto; background-color:white;'}),
            'status': forms.Select(attrs={'class': 'form-control', 'style': 'width: 300px; margin:auto; background-color:white;'}),
        }


class Task_Assign_Form(forms.ModelForm):
    class Meta:
        model = taskassign
        fields = ['task', 'deadline', 'assigned_to']
        widgets = {
            'task': forms.TextInput(attrs={'style': 'width: 300px; margin:auto; background-color:white;'}),
            'deadline': forms.DateInput(attrs={'type': 'date', 'style': 'width: 300px; margin:auto; background-color:white; '}),
            'assigned_to': forms.Select(attrs={'style': 'width: 300px; margin:auto; background-color:white;'}),
            # 'Branch_name':forms.TextInput(attrs={'class' : 'form-control','style': 'width: 300px; margin:auto; background-color:white;'}),
        }
