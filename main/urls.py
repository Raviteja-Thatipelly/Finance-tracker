from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='app_landing'),
    path('aboutus',views.about_us,name='aboutus'),
    path('transactions',views.transactions_input, name='transactions')
]