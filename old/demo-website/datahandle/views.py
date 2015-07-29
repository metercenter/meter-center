from django.template import RequestContext, loader
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse,HttpResponseRedirect
from datahandle.models import Item
from django.core.urlresolvers import reverse

def display(request):
    item_list = Item.objects.order_by('item_id')[:20]
    template = loader.get_template('display.html')
    context = RequestContext(request, {
        'item_list': item_list,
    })
    return HttpResponse(template.render(context))


# Create your views here.
