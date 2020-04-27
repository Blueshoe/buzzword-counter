from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic import ListView

from buzzword_counter.counter.models import Buzzword
from buzzword_counter.counter.tasks import add_buzzword


class CounterListView(ListView):
    model = Buzzword
    template_name = 'counter.html'


class IncreaseCounterView(View):

    def post(self, request, *args, **kwargs):
        if request.POST.get('inc_buzzword_pk'):
            buzzword_pk = request.POST['inc_buzzword_pk']
            buzzword = Buzzword.objects.get(pk=buzzword_pk)
            buzzword.count += 1
            buzzword.save()
        elif request.POST.get('dec_buzzword_pk'):
            buzzword_pk = request.POST['dec_buzzword_pk']
            buzzword = Buzzword.objects.get(pk=buzzword_pk)
            # ensure that count won't be negative
            buzzword.count = min(0, buzzword.count-1)
            buzzword.save()
        elif request.POST.get('new_buzzword'):
            word = request.POST.get('new_buzzword')
            add_buzzword.apply_async(args=(word,))

        return HttpResponseRedirect('/')
