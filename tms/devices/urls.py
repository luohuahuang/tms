# Django
from django.urls import path
# Local
from devices import views

app_name = 'devices'
urlpatterns = [
    path('', views.DeviceIndex.as_view(), name='device_overview'),
    path('device/<int:pk>', views.DeviceDetailView.as_view(), name='device_detail'),
    path('device/create/', views.DeviceCreateView.as_view(), name='create_device'),
    path('device/update/<int:pk>', views.DeviceUpdateView.as_view(), name='update_device'),
    path('device/read/<int:pk>', views.DeviceReadView.as_view(), name='read_device'),
    path('device/delete/<int:pk>', views.DeviceDeleteView.as_view(), name='delete_device')
]
