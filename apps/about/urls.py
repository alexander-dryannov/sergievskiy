from django.urls import path

from apps.about import views

app_name = 'about'

urlpatterns = [
    path('contacts/', views.get_contacts, name='contacts'),
    path('donate/', views.DonateView.as_view(), name='donate'),
]
