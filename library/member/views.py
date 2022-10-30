# from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from librarian.models import Books


def member(request):
    ourbooks = Books.objects.all().values()
    template = loader.get_template('member.html')
    context = {
        'ourbooks': ourbooks,
        }
    return HttpResponse(template.render(context, request))


def borrowbook(request, id):
    book = Books.objects.get(id=id)
    book.availability = False
    book.save()
    return HttpResponseRedirect(reverse('member'))


def returnbook(request, id):
    book = Books.objects.get(id=id)
    book.availability = True
    book.save()
    return HttpResponseRedirect(reverse('member'))
