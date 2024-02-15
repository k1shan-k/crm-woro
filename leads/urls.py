from django.urls import path
from . import views

app_name = 'leads'

urlpatterns = [
    path('', views.import_leads, name='import'),
    path('list/', views.lead_list, name='list'),
    path('mark_contact/<int:lead_id>/', views.mark_contact, name='mark_contact'),
    path('contacts/', views.contact_list, name='contact_list'),
    path('mark_opportunity/<int:lead_id>/', views.mark_opportunity, name='mark_opportunity'),
    path('opportunities/', views.opportunity_list, name='opportunity_list'),
    path('create_opportunity/', views.create_opportunity, name='create_opportunity'),
]
