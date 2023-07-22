from django.db.models import Avg
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.validators import RegexValidator
# Create your models here.
Gender_choices = (
    ("Male", "Male"),
    ("Female", "Female"),
)

Shift_choices = (
    ("Day", "Day"),
    ("Night", "Night"),
)
STATUS_CHOICES = (
    ('Not started yet', 'Not started yet'),
    ('Processing', 'Processing'),
    ('Finished', 'Finished')
)


class User(AbstractUser):
    is_manager = models.BooleanField(default=False)
    # is_employee=models.BooleanField(default=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def get_absolute_url(self):  # new
        #     from django.core.urlresolvers import reverse
        return reverse('login', args=[str(self.id)])


class Post(models.Model):
    header = models.CharField(max_length=100, default="Header")
    text = models.TextField()

    def average_rating(self) -> float:
        return Rating.objects.filter(post=self).aggregate(Avg("rating"))["rating__avg"] or 0

    def __str__(self):
        return f"{self.header}: {self.average_rating()}"


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.post.header}: {self.rating}"


class Manager(models.Model):
    alphabetic = RegexValidator(r'^[a-zA-Z]*$', 'Only alphabets  are allowed.')

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    Name = models.CharField(max_length=200, validators=[alphabetic])
    MobileNumber = models.IntegerField(default=0)
    Branch_name = models.CharField(max_length=200)
    # email=models.EmailField()

    class Meta:
        unique_together = [("Name", "MobileNumber", "Branch_name")]

    def __str__(self):
        return self.Name


class Employee(models.Model):
    # user=models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    MobileNumber = models.IntegerField(default='')
    Branch_name = models.CharField(max_length=200)
    Name = models.CharField(max_length=200, unique=True)
    # Email = models.EmailField(max_length=100)
    Address = models.TextField(max_length=500)
    Dob = models.DateField(null=True)
    Gender = models.CharField(choices=Gender_choices, max_length=100)
    Startdate = models.DateField(null=True)
    Shift = models.CharField(choices=Shift_choices, max_length=50)
    Department = models.CharField(max_length=100)

    def __str__(self):
        return self.Name


# class Employee(models.Model):

#     # fields of the model
#     emp_id = models.CharField
#     Name = models.CharField(max_length=200)
#     Email = models.EmailField(max_length=100)
#     Address = models.TextField(max_length=500)
#     DOB = models.DateField
#     Gender = models.BooleanField
#     MobileNumber = models.IntegerField
#     Startdate = models.DateField
#     Location = models.CharField
#     Shift = models.BooleanField
#     Departement = models.CharField(max_length=50)
#     Username = models.CharField(max_length=200)
#     Password = models.CharField(max_length=100)


class Stockreport(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # product_id = models.CharField
    Branch_name = models.CharField(max_length=200)
    date = models.DateField()
    cost_per_unit = models.IntegerField()
    stock_value = models.IntegerField()
    item_name = models.CharField(max_length=200)
    # stock_value = models.IntegerField()
    # item_name = models.CharField
    stock = models.IntegerField()
    UOM = models.IntegerField()
    FilterFields = ['Branch_name', 'date', 'item_name']


class Salesreport(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Branch = models.CharField(max_length=200)
    date = models.DateField()
    cash_values = models.IntegerField()
    card_sales = models.IntegerField()
    return_amount = models.IntegerField()
    discount = models.IntegerField()
    total_sales = models.IntegerField()
    net_sales = models.IntegerField()
    total_VAT = models.IntegerField()
    FilterFields = ['Branch', 'date']


# class employeeattendance(models.Model):
#     # emp_id = models.CharField
#     check_in = models.DateTimeField
#     check_out = models.DateTimeField
#     workinghour = models.DateTimeField
#     date = models.DateField


# class Stafflogin(models.Model):
#     # emp_id = models.CharField
#     username = models.CharField
#     password = models.CharField


class todolist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    priority = models.IntegerField()
    task = models.CharField(null=True, max_length=300)
    status = models.CharField(max_length=200, choices=STATUS_CHOICES)


# class customerfeedback(models.Model):
#     star = models.IntegerField
#     comment = models.CharField


class Alert(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    alert = models.CharField(max_length=500)


class taskassign(models.Model):
    # emp_id = models.CharField
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.CharField(max_length=200)
    deadline = models.DateField()
    # assigned_to=models.CharField(max_length=200)
    # Branch_name=models.CharField(max_length=200)
    assigned_to = models.ForeignKey(
        Employee, on_delete=models.DO_NOTHING, null=False, blank=False)
