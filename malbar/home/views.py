from django.http import HttpResponse, HttpRequest
# from .forms import EmployeeForm
from django.shortcuts import render, redirect
# from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
# from .forms import UserRegistrationForm
from django.views.generic import CreateView
from django.contrib.auth.models import User
# from . forms import ManagerRegistrationForm,EmployeeRegistrationForm,Employee_LoginForm,Stock_reportForm,Sales_reportForm,Alert_Form,To_do_Form
from . forms import *
from . models import User, Manager, Employee, Salesreport, Stockreport, todolist
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
from django.views import View
from . filters import *
# Create your views here.


def index(request):
    return render(request, 'index.html')


# def managersignup(request):
#     form = CreateUserForm()
#     if request.method == 'POST':
#         form = CreateUserForm(request.POST)
#         if form.is_valid():
#             form.save()
#     context = {'form': form}
#     return render(request, 'managersignup.html', context)


# def employee_login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password1 = request.POST.get('password1')

#         User = authenticate(request, username=username, password=password1)
#         if User is not None:
#             login(request, User)
#             return redirect('Home')
#         else:
#             messages.info(request, 'Username or password is incorrect')

#         context = {}


# class manager_register(CreateView):
#     model=User
#     form_class=ManagerRegistrationForm
#     template_name='managersignup.html'

#     def validation(self,form,request):
#         user=form.save()
#         login(self.request,user)
#         messages.success(request, f'Your account has been created. You can log in now!')
#         success_url = reverse_lazy('login')
    # return redirect('index')

    # def get_absolute_url(self): # new
    #     from django.core.urlresolvers import reverse
    #     return reverse('login', args=[str(self.id)])


def manager_register(request):
    if request.method == 'POST':
        form = ManagerRegistrationForm(request.POST)
        if form.is_valid():

            form.save()

            messages.success(
                request, f'Your account has been created. You can log in now!')
            return redirect('login')
    else:
        messages.warning(request, 'Invalid data')

        form = ManagerRegistrationForm()

    context = {'form': form}
    return render(request, 'managersignup.html', locals())

# def employee_register(request):
#      if request.method == 'POST':
#         form = EmployeeRegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()

#             messages.success(request, f'Employee account has been created.')
#             return redirect('employeedetails')
#      else:
#         form = EmployeeRegistrationForm()

#      context = {'form': form}
#      return render (request,'employeesignup.html',context)
#


def employee_register(request):
    if request.method == 'POST':
        form = EmployeeRegistrationForm(request.POST or None)
    #    my_Address = Address.objects.all()

        if form.is_valid():
            #    form = EmployeeRegistrationForm()
            instance = form.save(commit=False)
            instance.Name = form.cleaned_data.get("Name")
            instance.MobileNumber = form.cleaned_data.get("MobileNumber")
            instance.Address = form.cleaned_data.get("Address")
            instance.Dob = form.cleaned_data.get("Dob")
            instance.Gender = form.cleaned_data.get("Gender")
            instance.Startdate = form.cleaned_data.get("Startdate")
            instance.Shift = form.cleaned_data.get("Shift")
            instance.Branch_name = form.cleaned_data.get("Branch_name")
            instance.Department = form.cleaned_data.get("Department")
            instance.user = request.user

            instance.save()
            messages.success(request, f'Employee Added successfully')
            form = EmployeeRegistrationForm()

        #    messages.success(request, messages.INFO,'Address Added')

            return redirect('mgremployeedetails')

    else:
        messages.warning(request, 'Invalid data')
        form = EmployeeRegistrationForm()

    return render(request, 'employeesignup.html', {'form': form})


def deleteemployee(request, pk):
    employees = Employee.objects.get(pk=pk)
    employees.delete()
    return redirect('/mgremployeedetails')

# def editemployee(request,id):
#     employees=Employee.objects.get(id=id)
#     return render(request,'editemployee.html',locals())


class updateemployee(View):
    def get(self, request, pk):
        add = Employee.objects.get(pk=pk)
        form = EmployeeRegistrationForm(instance=add)
        return render(request, 'updateemployee.html', locals())

    def post(self, request, pk):
        form = EmployeeRegistrationForm(request.POST)
        if form.is_valid():
            add = Employee.objects.get(pk=pk)
            add.Name = form.cleaned_data['Name']
            add.MobileNumber = form.cleaned_data['MobileNumber']
            add.Address = form.cleaned_data['Address']
            add.Dob = form.cleaned_data['Dob']
            add.Gender = form.cleaned_data['Gender']
            add.Startdate = form.cleaned_data['Startdate']
            add.Shift = form.cleaned_data['Shift']
            add.Branch_name = form.cleaned_data['Branch_name']
            add.Department = form.cleaned_data['Department']

            add.save()
            messages.success(
                request, "congratulations!! Employee profile updated successfully")
        # else:
            # messages.warning(request, "Invalid input data")
        return redirect('mgremployeedetails')


class updatesalesreport(View):
    def get(self, request, pk):
        add = Salesreport.objects.get(pk=pk)
        form = Sales_reportForm(instance=add)
        return render(request, 'updatesalesreport.html', locals())

    def post(self, request, pk):
        form = Sales_reportForm(request.POST)
        if form.is_valid():
            add = Salesreport.objects.get(pk=pk)

            add.Branch = form.cleaned_data['Branch']
            add.date = form.cleaned_data['date']
            add.cash_values = form.cleaned_data['cash_values']
            add.card_sales = form.cleaned_data['card_sales']
            add.return_amount = form.cleaned_data['return_amount']
            add.discount = form.cleaned_data['discount']
            add.total_sales = form.cleaned_data['total_sales']
            add.net_sales = form.cleaned_data['net_sales']
            add.total_VAT = form.cleaned_data['total_VAT']
        #    add.Department=form.cleaned_data['Department']

            add.save()
            messages.success(
                request, "congratulations!! Sales report updated successfully")
        # else:
        #     messages.warning(request, "Invalid input data")

        return redirect('mgrallsalesreports')


class updatestockreport(View):
    def get(self, request, pk):
        add = Stockreport.objects.get(pk=pk)
        form = Stock_reportForm(instance=add)
        return render(request, 'updatestockreport.html', locals())

    def post(self, request, pk):
        form = Stock_reportForm(request.POST)
        if form.is_valid():
            add = Stockreport.objects.get(pk=pk)
            add.date = form.cleaned_data['date']
            add.Branch_name = form.cleaned_data['Branch_name']
            add.cost_per_unit = form.cleaned_data['cost_per_unit']
            add.stock_value = form.cleaned_data['stock_value']
            add.item_name = form.cleaned_data['item_name']
            add.stock = form.cleaned_data['stock']
            add.UOM = form.cleaned_data['UOM']

            add.save()
            messages.success(
                request, "congratulations!! Stock report updated successfully")
        # else:
        #     messages.warning(request, "Invalid input data")

        return redirect('mgrallstockreports')


class updatetaskassign(View):
    def get(self, request, pk):
        add = taskassign.objects.get(pk=pk)
        form = Task_Assign_Form(instance=add)
        return render(request, 'updatetaskassign.html', locals())

    def post(self, request, pk):
        form = Task_Assign_Form(request.POST)
        if form.is_valid():
            add = taskassign.objects.get(pk=pk)
            add.task = form.cleaned_data['task']
            add.deadline = form.cleaned_data['deadline']
            add.assigned_to = form.cleaned_data['assigned_to']
            add.save()
            messages.success(
                request, "congratulations!! Task updated successfully")

        # else:
        #     messages.warning(request, "Invalid input data")

        return redirect('taskassignment')


class updatealert(View):
    def get(self, request, pk):
        add = Alert.objects.get(pk=pk)
        form = Alert_Form(instance=add)
        return render(request, 'updatealert.html', locals())

    def post(self, request, pk):
        form = Alert_Form(request.POST)
        if form.is_valid():
            add = Alert.objects.get(pk=pk)
            add.subject = form.cleaned_data['subject']
            add.alert = form.cleaned_data['alert']
            add.save()
            messages.success(
                request, "Alert updated successfully")

        else:
            print(form.errors)

        return redirect('alerts')


class updatetodolist(View):
    def get(self, request, pk):
        add = todolist.objects.get(pk=pk)
        form = To_do_Form(instance=add)
        return render(request, 'updatetodolist.html', locals())

    def post(self, request, pk):
        form = To_do_Form(request.POST)
        if form.is_valid():
            add = todolist.objects.get(pk=pk)
            add.priority = form.cleaned_data['priority']
            add.task = form.cleaned_data['task']
            add.status = form.cleaned_data['status']

            add.save()
            messages.success(
                request, "Todolist updated successfully")

            # print(form.errors)

        return redirect('todolist')


def deletesalesreport(request, pk):
    sale_report = Salesreport.objects.get(pk=pk)
    sale_report.delete()
    return redirect('/mgrallsalesreports')


def deletetaskassign(request, pk):
    task_assign = taskassign.objects.get(pk=pk)
    task_assign.delete()
    return redirect('/taskassignment')


def deletestockreport(request, pk):
    stock_report = Stockreport.objects.get(pk=pk)
    stock_report.delete()
    return redirect('/mgrallstockreports')


def deletealert(request, pk):
    alert_page = Alert.objects.get(pk=pk)
    alert_page.delete()
    return redirect('/todolist')


def deletetodolist(request, pk):
    alert_page = todolist.objects.get(pk=pk)
    alert_page.delete()
    return redirect('/todolist')


def employeelogin(request):
    if request.method == 'GET':
        form = Employee_LoginForm()
        return render(request, 'employeelogin.html', {'form': form})

    elif request.method == 'POST':
        Name = request.POST.get('Name', None)
        MobileNumber = request.POST.get('MobileNumber', None)
        Branch_name = request.POST.get('Branch_name', None)
        Department = request.POST.get('Department', None)
        user = authenticate(request, Name=Name, MobileNumber=MobileNumber,
                            Branch_name=Branch_name, Department=Department)
        # if user is not None:
        # login(request, user)
        return redirect('Home')
        # Redirect to a success page?
        # return HttpResponseRedirect('/')
        # else:
        #     # context = {'error': 'Wrong credintials'}  # to display error?
        #     form=Employee_LoginForm()
        #     messages.error(request,"Invalid details.")
    return render(request, 'employeelogin.html', locals())
    # if request.method == 'POST':
    #     Name = request.POST.get('Name')
    #     MobileNumber = request.POST.get('MobileNumber')
    #     Branch_name = request.POST.get('Branch_name')
    #     Department= request.POST.get('Department')
    #     Employee = authenticate(request, Name=Name, MobileNumber=MobileNumber, Branch_name=Branch_name, Department=Department )
    #     if Employee  is not None:
    #         login(request, Employee)
    #         return redirect('Home')
    #     else:
    #         messages.info(request, 'details are incorrect')

    #     context = {}
    #     return render(request, 'employeelogin.html', locals())


def mgrlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')

        User = authenticate(request, username=username, password=password1)
        if User is not None:
            login(request, User)
            return redirect('index')
        else:
            messages.info(request, 'Username or password is incorrect')

        context = {}
        return render(request, 'mgrlogin.html', context)


def customerreviewform(request):
    return render(request, 'customerreviewform.html')


def addemployee(request):
    # context = {}
    # context['Form'] = EmployeeForm
    return render(request, 'addemployee.html')


# def index(request):
#     return render(request, 'index.html')


def employeeprofile(request):
    return render(request, 'employeeprofile.html')


def mgrlogin(request):
    return render(request, 'mgrlogin.html')


def Addemployee(request):
    return render(request, 'Addemployee.html')


def alerts(request):
    alarm = Alert.objects.filter(user=request.user)
    if request.method == 'POST':
        form = Alert_Form(request.POST or None)
    #    my_Address = Address.objects.all()

        if form.is_valid():
            instance = form.save(commit=False)
            instance.subject = form.cleaned_data.get("subject")
            instance.alert = form.cleaned_data.get("alert")
            instance.user = request.user

            instance.save()
            messages.success(request, f'Alert gone!!!')
        #    messages.success(request, messages.INFO,'Address Added')
            form = Alert_Form()

    else:
        #    messages.warning(request,'Invalid data')
        form = Alert_Form()
    return render(request, 'alert.html', locals())


# def mgremployeedetails(request):
#     return render(request, 'mgremployeedetails.html')


def mgrallstockreports(request):
    reports = Stockreport.objects.filter(user=request.user)

    # Stock=Stockreport.objects.all()
    # if request.method=="GET":
    #     st=request.GET.get('Search_something')
    #     if st!=None:
    #        Stock=Stockreport.objects.filter(item_name__icontains=st)

    # data={
    #     'Stock':Stock
    # }
    myFilter = Stockreport_Filter(request.GET, queryset=reports)
    return render(request, 'mgrallstockreports.html', locals())


def mgremployeedetails(request):
    staff = Employee.objects.filter(user=request.user)
    return render(request, 'mgremployeedetails.html', locals())


def mgrallsalesreports(request):
    reports = Salesreport.objects.filter(user=request.user)
    # sales=sales.filter(Salesreport=Salesreport)
    # Sales=Salesreport.objects.all()
    # if request.method=="GET":
    #     st=request.GET.get('Search_something')
    #     if st!=None:
    #        Sales=Salesreport.objects.filter(date__icontains=st)

    # data={
    #     'Sales':Sales
    # }
    # myFilter = Salesreport_Filter(request.GET)
    myFilter = Salesreport_Filter(request.GET, queryset=reports)
    # Sales=myFilter.qs
    return render(request, 'mgrallsalesreports.html', locals())


def mgr(request):
    return render(request, 'index.html')


#    return render(request, 'Sales_Report_form.html')
def Sales_Report_form(request):
    branches = Manager.objects.filter(user=request.user)
    #  add=Manager.objects.get(Branch_name=Branch_name)
    if request.method == 'POST':
        form = Sales_reportForm(request.POST or None)
    #    my_Address = Address.objects.all()

        if form.is_valid():
            instance = form.save(commit=False)
            instance.Branch = form.cleaned_data.get("Branch")
            instance.date = form.cleaned_data.get("date")
            instance.cash_values = form.cleaned_data.get("cash_values")
            instance.card_sales = form.cleaned_data.get("card_sales")
            instance.return_amount = form.cleaned_data.get("return_amount")
            instance.discount = form.cleaned_data.get("discount")
            instance.total_sales = form.cleaned_data.get("total_sales")
            instance.net_sales = form.cleaned_data.get("net_sales")
            instance.total_VAT = form.cleaned_data.get("total_VAT")
            instance.user = request.user

            instance.save()
            messages.success(request, f'Sales Report Added successfully')
        #    messages.success(request, messages.INFO,'Address Added')
            form = Sales_reportForm()

    else:
        #  messages.warning(request,'Invalid data')
        form = Sales_reportForm()
    return render(request, 'Sales_Report_form.html', locals())


def stock_report_form(request):
    branches = Manager.objects.filter(user=request.user)
    if request.method == 'POST':
        form = Stock_reportForm(request.POST or None)
    #    my_Address = Address.objects.all()

        if form.is_valid():
            instance = form.save(commit=False)
            instance.Branch_name = form.cleaned_data.get("Branch_name")
            instance.date = form.cleaned_data.get("date")
            instance.cost_per_unit = form.cleaned_data.get("cost_per_unit")
            instance.stock_value = form.cleaned_data.get("stock_value")
            instance.item_name = form.cleaned_data.get("item_name")
            instance.stock = form.cleaned_data.get("stock")
            instance.UOM = form.cleaned_data.get("UOM")
            instance.user = request.user

            instance.save()
            messages.success(request, f'Stock Report Added successfully')
        #    messages.success(request, messages.INFO,'Address Added')
            form = Stock_reportForm()

    else:
        # #  messages.warning(request,'Invalid data')
        form = Stock_reportForm()
    return render(request, 'stock_report_form.html', locals())


def taskassignment(request):
    tasks = taskassign.objects.filter(user=request.user)
    if request.method == 'POST':
        form = Task_Assign_Form(request.POST or None)
    #    my_Address = Address.objects.all()

        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user

            instance.task = form.cleaned_data.get("task")
            instance.deadline = form.cleaned_data.get("deadline")
            instance.assigned_to = form.cleaned_data.get("assigned_to")
        #    instance.Branch_name = form.cleaned_data.get("Branch_name")
            instance.save()
            messages.success(request, f'Task Assigned succesfully!!!')
        #    messages.success(request, messages.INFO,'Address Added')
            form = Task_Assign_Form()

        else:
            print(form.errors)

    else:
        #    messages.warning(request,'Invalid data')
        form = Task_Assign_Form()
    myFilter = Taskassign_Filter(request.GET, queryset=tasks)
    return render(request, 'taskassignment.html', locals())

    # return render(request, 'taskassignment.html')


def Todolist(request):
    add = todolist.objects.filter(user=request.user)
    if request.method == 'POST':
        form = To_do_Form(request.POST or None)
    #    my_Address = Address.objects.all()

        if form.is_valid():
            instance = form.save(commit=False)
            instance.priority = form.cleaned_data.get("priority")
            instance.task = form.cleaned_data.get("task")
            instance.status = form.cleaned_data.get("status")
            instance.user = request.user
            instance.save()
            messages.success(request, f'Your task Added successfully')
        #    messages.success(request, messages.INFO,'Address Added')
            form = To_do_Form()

    else:
        #  messages.warning(request,'Invalid data')
        form = To_do_Form()
    return render(request, 'todolist.html', locals())


def alertstaff(request):
    alarm = Alert.objects.filter(user=request.user)
    return render(request, 'alertstaff.html', locals())


def Home(request):
    tasks = taskassign.objects.filter(user=request.user)
    myFilter = Taskassign_Filter(request.GET, queryset=tasks)
    return render(request, 'Home.html', locals())


def customerfeedback(request: HttpRequest) -> HttpResponse:
    posts = Post.objects.all()
    for post in posts:
        rating = Rating.objects.filter(post=post, user=request.user).first()
        post.user_rating = rating.rating if rating else 0
    return render(request, "customerfeedback.html", {"posts": posts})


def rate(request: HttpRequest, post_id: int, rating: int) -> HttpResponse:
    post = Post.objects.get(id=post_id)
    Rating.objects.filter(post=post, user=request.user).delete()
    post.rating_set.create(user=request.user, rating=rating)
    return customerfeedback(request)
