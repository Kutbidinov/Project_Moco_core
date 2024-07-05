from django.views.generic import TemplateView
from menu.models import Coffees


class HomeView(TemplateView):
    template_name = 'index.html'


class BlogView(TemplateView):
    template_name = 'blog.html'


class ContactView(TemplateView):
    template_name = 'contact.html'


class CofeeView(TemplateView):
    template_name = 'cofee.html'


class CoffeesView(TemplateView):
    template_name = 'coffees.html'

    def get_context_data(self, **kwargs):
        context = {
            'coffee_list': Coffees.objects.all()

        }
        return context


class AboutView(TemplateView):
    template_name = 'about.html'





