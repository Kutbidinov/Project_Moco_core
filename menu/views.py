from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from menu.models import Coffees, Feedback, MokkoContact, ClientContact, Publication, NameVerbose




class HomeView(TemplateView):
    template_name = 'index.html'


    def get_context_data(self, **kwargs):
        context = {
            'home_list': Coffees.objects.all()
        }
        return context



# перепишем HomeView через функцию

def home_view(request):
    context = {
        'coffee_list': Coffees.objects.all(),
        'feedback_list': Feedback.objects.all(),
        'mokko_contact': MokkoContact.objects.first(),
        'name_verbose':  NameVerbose.objects.first(),
        'my_blog':  Publication.objects.all(),
        'home_list': Coffees.objects.all(),




    }
    response = render(request, 'index.html', context)
    return response



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



class PublicationView(TemplateView):
    template_name = 'blog.html'

    def get_context_data(self, **kwargs):
        context = {
            'publication_list': Publication.objects.all()

        }
        return context



class BlogDetailView(TemplateView):
    template_name = 'blog-detail.html'

    def get_context_data(self, **kwargs):
        publication_pk = kwargs['pk']
        context = {
            'publication_list': Publication.objects.get(id=publication_pk)
        }
        return context



def client_contact_create_view(request):
    print("Данные о ПОСТ запроса!",  request.POST)
    name = request.POST["Your Name"]
    email = request.POST['Your Email']
    phone = request.POST['Your Phone']
    massege = request.POST['Massage']
    ClientContact.objects.create(name=name, email=email, phone=phone, message=massege)
    return HttpResponse('<h1> Ваше сообщения! </h1>')



