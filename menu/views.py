from django.views.generic import TemplateView
from menu.models import Coffees
from menu.models import Publication


class HomeView(TemplateView):
    template_name = 'index.html'


class PublicationView(TemplateView):
    template_name = 'blog.html'

    def get_context_data(self, **kwargs):
        context = {
            'blog_list': Publication.objects.all()

        }
        return context




class ContactView(TemplateView):
    template_name = 'contact.html'



class CoffeeDetailView(TemplateView):
    template_name = 'coffee.html'

    def get_context_data(self, **kwargs):
        coffee_pk = kwargs['pk']

        context = {
            'coffee': Coffees.objects.get(id=coffee_pk)
        }

        return context




class CoffeesView(TemplateView):
    template_name = 'coffees.html'

    def get_context_data(self, **kwargs):
        context = {
            'coffee_list': Coffees.objects.all()

        }
        return context


class AboutView(TemplateView):
    template_name = 'about.html'







