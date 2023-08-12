from django.shortcuts import render
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import ContactUsForm
from .models import ContactUs

# Create your views here.


class Index(LoginRequiredMixin,generic.CreateView):
    model = ContactUs
    form_class = ContactUsForm
    template_name = 'pages/index_1.html'

    def get_success_url(self):
        return redirect('pages:index')

    def form_valid(self, form):
        form_obj = form.save(commit=False)
        form_obj.user = self.request.user
        form_obj.save()
        return super().form_valid(form_obj)





class AboutMePage(generic.TemplateView):
    template_name = 'pages/aboutme.html'