from django.conf import settings
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, DetailView
from django.utils.text import slugify
from django.core.urlresolvers import reverse_lazy

import tweepy

from .models import Need
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
        self.object, created = Need.objects.get_or_create(slug=slug,
                                                          defaults={'need': need})

        auth = tweepy.OAuthHandler(settings.TWITTER_CONSUMER_KEY,
                                   settings.TWITTER_CONSUMER_SECRET)
        auth.set_access_token(settings.TWITTER_ACCESS_KEY,
                              settings.TWITTER_ACCESS_SECRET)

        api = tweepy.API(auth)
        status = 'My startup needs {0} - ' \
                 'http://mystartupneeds.com{1}'.format(need,
                                                       self.get_success_url())
        api.update_status(status)

        return HttpResponseRedirect(self.get_success_url())


class NeedDetailView(DetailView):
    model = Need
