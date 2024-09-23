from django.urls import path
from .views import IndexView, AboutView, ServicesView, BlogView, ContactView
from .views import contact_view

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('sobre-nosotros/', AboutView.as_view(), name='about'),
    path('servicios/', ServicesView.as_view(), name='services'),
    path('blog/', BlogView.as_view(), name='blog'),
    path('contact/', ContactView.as_view(), name='contact'),

    path('form/', contact_view, name='form'),
]