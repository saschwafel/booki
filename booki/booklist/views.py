from .models import Book_Entry
from django.http import Http404
from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect
from django.template import RequestContext, loader
from .forms import EntryForm
import urllib
import requests
from bs4 import BeautifulSoup

# Create your views here.
with open('/home/schuyler/Class/booki/booki/booklist/api_info.txt') as f:
    api_info = f.readlines()

gr_api_key = str(api_info[1]).strip()

print gr_api_key
# gr_api_key = "CA3fN2yi9oAZzMEDigwEAQ"
gr_secret = "nCgo7zG7nv6UbauQapkJDQsbTJ3kqU7jbBSTy8LnIg"

def index(request):
    # list_of_entries = Book_Entry.objects.order_by('date_added')
    # output = ', '.join([p.title + ' - ' + p.author + '\n' for p in list_of_entries])
    
    try:


        form = EntryForm()

        if request.method == 'POST':

            form = EntryForm(request.POST)

            if form.is_valid():

                post = form.save(commit=False)
                post.save()

                return HttpResponseRedirect('/')

            else:

                form = EntryForm()

        list_of_entries = Book_Entry.objects.order_by('date_added')
        template = loader.get_template('booklist/index.html')

        context = RequestContext(request, { 'list_of_entries': list_of_entries, 'form_new': form })

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

        try:

            cover = soup.find("image_url").text

        except AttributeError:

            cover = 'https://s.gr-assets.com/assets/nophoto/book/111x148-bcc042a9c91a29c1d680899eff700a03.png'

        return render(request, 'booklist/detail.html', {'book_entry' : entry, 'cover' : cover, 'api_url' : api_url })
        # response = "You are looking at Entry #%s!" 

    except Book_Entry.DoesNotExist:

        Http404("Page not found :'(")

    return HttpResponse(response % book_entry_id)

