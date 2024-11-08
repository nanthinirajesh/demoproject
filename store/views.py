from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
# Create your views here.

@login_required()
def home(request):
    return render(request, 'home.html')

def register_views(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    form= CustomerUserCreationForm()
    if request.method == 'POST':
        form= CustomerUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('login'))
    return render(request, 'register.html', {'form': form})

def index(resquest):
    return HttpResponse('bangtan')

def about(request):
    return HttpResponse('hii nile, welcome')

# def contact(request):
#     return HttpResponse('contact')

# def display_info(request):
#     name = "nile"
#     age = 21
#     return HttpResponse(f"Name: {name}, Age: {age}")

# def self1(request):
#     return render(request, 'self.html')

# def about2(request):
#     return render(request, 'about.html', context={'name':'nile', 'age': 21})

# def basic(request):
#     var1={}
#     var1['Name'] = 'Nile'
#     var1['Age'] = '21'
#     var1['Address'] = 'Kottayam'
#     var1['Product'] = ['Book', 'Pen', 'Pencil']
#     var1['Gender'] = 0
#     var1['Phone'] = '9876543210'
#     return render(request=request, template_name='context.html', context=var1)

def base(request):
    return render(request, 'base.html')

def home(request):
    return render(request, 'home.html')

# def booking(request):
#     return render(request, 'booking.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

# def department(request):
#     return render(request, 'department.html')

def doctors(request):
    dict_docs = {
        'doctors': Doctors.objects.all()
    }
    return render(request, 'doctors.html',dict_docs)

def departments(request):
    dict1 = {
        'dept': department.objects.all()
    }
    return render(request, 'department.html',dict1)

# def create_todo(request):
#     if request.method=='GET':
#         return render(request, 'booking.html')
#     elif request.method=='POST':
#         title1= request.POST['title']
#         description1=request.POST.get('des', None)
#         rating=request.POST.get('rating',None)
#         status=request.POST.get('status','off')
#         if status=='on':
#             status=True
#         else:
#             status=False
#         todo= Todo(title=title1, description=description1, rating=rating, status=status)
#         todo.save()
#         return HttpResponse('<h1> Completed </h1>')
    
def contact_todo(request):
    if request.method=='GET':
        return render(request, 'contact.html')
    elif request.method=='POST':
        conname= request.POST['name']
        conno= request.POST.get('contactno', None)
        
        contact= Contact(Name=conname, Phone_Number=conno)
        contact.save()
        return HttpResponse('<h1> Completed </h1>')
    
from .forms import BookingForm

def bookingss(request):
    if request.method=="POST":
        form=BookingForm(request.POST)
        if form.is_valid():
            form.save()
    form=BookingForm()
    dict_form={
       'form':form
    }
    return render(request, 'booking1.html', dict_form)

from django.views.generic import ListView
class Tasklistviews(ListView):
    model = department
    template_name = 'department.html'
    context_object_name = 'dept'
    
from django.views.generic.detail import DetailView

class TaskDetailview(DetailView):
    model = department
    template_name = 'dep_details.html'
    context_object_name = 'dept'

from django.views.generic.edit import UpdateView,DeleteView
from django.urls import reverse_lazy
class TaskUpadateView(UpdateView):
    model = department
    template_name = 'update.html'
    fields = ('deptname', 'description')
    
    def get_success_url(self):
        return reverse_lazy('dept', kwargs={'pk': self.object.id})
    
class TaskDeleteView(DeleteView):
    model = department
    template_name = 'delete.html'
    success_url = reverse_lazy('home')
    
from django.views.generic.edit import CreateView
class EmployeeCreate(CreateView):
    model = department
    template_name = 'create.html'
    fields = '__all__'
    success_url = reverse_lazy('home')