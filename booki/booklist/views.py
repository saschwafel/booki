from .models import Book_Entry
from django.http import Http404
from django.shortcuts import render, HttpResponse, get_object_or_404
from django.template import RequestContext, loader
import urllib
import requests
from bs4 import BeautifulSoup

# Create your views here.


def index(request):
    # list_of_entries = Book_Entry.objects.order_by('date_added')
    # output = ', '.join([p.title + ' - ' + p.author + '\n' for p in list_of_entries])
    
    try:


        list_of_entries = Book_Entry.objects.order_by('date_added')
        template = loader.get_template('booklist/index.html')
        context = RequestContext(request, { 'list_of_entries': list_of_entries, })

    except Book_Entry.DoesNotExist:

        Http404("Page not found :'(")

    return HttpResponse(template.render(context))

    # return HttpResponse("You're at the Booklist Index!")

def detail(request, book_entry_id):
    try:
        entry = get_object_or_404(Book_Entry, pk=book_entry_id)
        # template = loader.get_template('booklist/index.html')
        # context = RequestContext(request, { 'list_of_entries': list_of_entries, })
        api_url = "https://www.goodreads.com/search/index.xml?key=" + gr_api_key + "&q=" + urllib.quote_plus(entry.title)

        gr_returned_html = requests.get(api_url)
        soup = BeautifulSoup(gr_returned_html.text)

        cover = soup.find("image_url").text

        return render(request, 'booklist/detail.html', {'book_entry' : entry, 'cover' : cover, 'api_url' : api_url })
        # response = "You are looking at Entry #%s!" 

    except Book_Entry.DoesNotExist:

        Http404("Page not found :'(")

    return HttpResponse(response % book_entry_id)


