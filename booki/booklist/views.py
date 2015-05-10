from .models import Book_Entry
from django.shortcuts import render, HttpResponse
from django.template import RequestContext, loader

# Create your views here.


def index(request):
    # list_of_entries = Book_Entry.objects.order_by('date_added')
    # output = ', '.join([p.title + ' - ' + p.author + '\n' for p in list_of_entries])
    
    list_of_entries = Book_Entry.objects.order_by('date_added')
    template = loader.get_template('booklist/index.html')
    context = RequestContext(request, { 'list_of_entries': list_of_entries, })
    return HttpResponse(template.render(context))

    # return HttpResponse("You're at the Booklist Index!")

def detail(request, book_entry_id):
    response = "You are looking at Entry #%s!" 
    return HttpResponse(response % book_entry_id)
