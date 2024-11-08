from django.urls import path, include
from .views import*

urlpatterns = [
    # path('', index, name='index'),
    # path('about/', about, name='about'),
    # # path('con/', contact, name='contant1'),
    # path('index/', index, name='templates'),
    # path('about1/', index, name='about'),
    # path('self/', self1, name='self'),
    # path('contact/',contact, name='contact'),
    # path('about2/',about2, name='about2'),
    # path('basic/', basic, name='context'),
    # path('base/', base, name = 'base'),
    path('home/', home, name='home'),
    path('book/', bookingss, name='booking'),
    path('about/',about, name='about'),
    path('contact/', contact_todo, name='contact'),
    # path('department/', departments, name='department'),
    path('doctors/', doctors, name='doctors'),
    
    path('cbvhomes/', Tasklistviews.as_view(), name='department'),
    path('detail/<int:pk>',TaskDetailview.as_view(),name='dept'),
    # path('cbupdate/', TaskUpadateView.as_view(), name='update'),
    path('update/<int:pk>', TaskUpadateView.as_view(),name='up'),
    path('delete/<int:pk>', TaskDeleteView.as_view(), name='delete'),
    path('create/', EmployeeCreate.as_view(), name='create'),
    path('', register_views, name='register'),
]