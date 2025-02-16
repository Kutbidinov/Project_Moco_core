"""
URL configuration for Moco_core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from menu.views import home_view,  CoffeesView, ContactView, AboutView, PublicationView, CoffeeDetailView, BlogDetailView, client_contact_create_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home_view, name='home_detail_url'),
    path('coffees/', CoffeesView.as_view(), name='coffees_list'),
    path('contact/', ContactView.as_view(), name='contact_list'),
    path('about/', AboutView.as_view(), name='about_list'),
    path('blog/', PublicationView.as_view(), name='publication_list'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='publication-detail'),
    path('coffee/<int:pk>/', CoffeeDetailView.as_view(), name='coffee_detail_url' ),
    path('home/client-contact-create/', client_contact_create_view),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
