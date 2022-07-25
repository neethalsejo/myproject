
from django.urls import path
from . import views
app_name = 'taskapp'

urlpatterns = [
    path('',views.detail,name='detail'),
    path('ajaxq/', views.ajaxq , name='ajaxq'),
    path('branch/<slug:c_slug>/',views.detail,name='hospital_by_branch'),
    path('RegDetail',views.RegDetail,name='RegDetail'),
   # path('<slug:c_slug>/<slug:product_slug>/', views.RegDetail, name='RegDetail'),
    path('appointment', views.appointment, name='appointment'),
    path('doctor', views.doctor, name='doctor'),
    path('cancel', views.cancel, name='cancel'),
    ]