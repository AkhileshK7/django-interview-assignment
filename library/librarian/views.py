# from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Books, Members


def librarian(request):
    template = loader.get_template('librarian.html')
    return HttpResponse(template.render({}, request))


def books(request):
    ourbooks = Books.objects.all().values()
    template = loader.get_template('books.html')
    context = {
        'ourbooks': ourbooks,
        }
    return HttpResponse(template.render(context, request))


def addbook(request):
    template = loader.get_template('addbook.html')
    return HttpResponse(template.render({}, request))


def addbookrecord(request):
    name = request.POST['name']
    author = request.POST['author']
    publisher = request.POST['publisher']
    year = request.POST['year']
    edition = request.POST['edition']
    availability = request.POST['availability']
    book = Books(name=name, author=author, publisher=publisher,
                 year=year, edition=edition, availability=availability)
    book.save()
    return HttpResponseRedirect(reverse('books'))


def deletebook(request, id):
    book = Books.objects.get(id=id)
    book.delete()
    return HttpResponseRedirect(reverse('books'))


def updatebook(request, id):
    ourbooks = Books.objects.get(id=id)
    template = loader.get_template('updatebook.html')
    context = {
        'ourbooks': ourbooks,
    }
    return HttpResponse(template.render(context, request))


def updatebookrecord(request, id):
    name = request.POST['name']
    author = request.POST['author']
    publisher = request.POST['publisher']
    year = request.POST['year']
    edition = request.POST['edition']
    availability = request.POST['availability']
    book = Books.objects.get(id=id)
    book.name = name
    book.author = author
    book.publisher = publisher
    book.year = year
    book.edition = edition
    book.availability = availability
    book.save()
    return HttpResponseRedirect(reverse('books'))


def members(request):
    ourmembers = Members.objects.all().values()
    template = loader.get_template('members.html')
    context = {
        'ourmembers': ourmembers,
        }
    return HttpResponse(template.render(context, request))


def addmember(request):
    template = loader.get_template('addmember.html')
    return HttpResponse(template.render({}, request))


def addmemberrecord(request):
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    username = request.POST['username']
    membernum = request.POST['membernum']
    member = Members(firstname=firstname, lastname=lastname,
                     username=username, membernum=membernum)
    member.save()
    return HttpResponseRedirect(reverse('members'))


def deletemember(request, id):
    member = Members.objects.get(id=id)
    member.delete()
    return HttpResponseRedirect(reverse('members'))


def updatemember(request, id):
    ourmembers = Members.objects.get(id=id)
    template = loader.get_template('updatemember.html')
    context = {
        'ourmembers': ourmembers,
    }
    return HttpResponse(template.render(context, request))


def updatememberrecord(request, id):
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    username = request.POST['username']
    membernum = request.POST['membernum']
    member = Members.objects.get(id=id)
    member.firstname = firstname
    member.lastname = lastname
    member.username = username
    member.membernum = membernum
    member.save()
    return HttpResponseRedirect(reverse('members'))
