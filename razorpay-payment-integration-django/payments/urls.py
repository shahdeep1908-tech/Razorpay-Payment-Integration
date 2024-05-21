from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', views.home, name='pay'),
    path('create-order', csrf_exempt(views.create_order), name='order'),
    path('success', views.success, name='success'),
    path('cancel', views.cancel, name='cancel'),
    path('webhook/razorpay', views.api_razorpay_webhook, name='webhook')
]
