from django.views.generic import TemplateView

# Create your views here.


class Index(TemplateView):
    template_name = 'home/index.html'


class About(TemplateView):
    template_name = 'home/about.html'
