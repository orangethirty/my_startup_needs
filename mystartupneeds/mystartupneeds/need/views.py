# Create your views here.
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, DetailView
from django.utils.text import slugify
from need.models import Need
from django.core.urlresolvers import reverse_lazy
from .forms import NeedForm


class NeedView(CreateView):
    model = Need
    form_class = NeedForm
    
    def get_success_url(self):
        #print self.object
        return reverse_lazy('need_detail', args=[self.object.slug])
        
    def form_valid(self, form):
        need = form.cleaned_data.get('need')
        slug = slugify(need)
        self.object, created = Need.objects.get_or_create(slug=slug, defaults = {'need': need})
        
        #send tweet code here.
        
        return HttpResponseRedirect(self.get_success_url())
    

class NeedDetailView(DetailView):
    model = Need