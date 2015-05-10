from django.shortcuts import render, HttpResponse
from .models import Book_Entry

# Create your views here.


def index(request):
    list_of_entries = Book_Entry.objects.order_by('date_added')
    output = ', '.join([p.title + ' - ' + p.author + '\n' for p in list_of_entries])
    return HttpResponse(output)
    # return HttpResponse("You're at the Booklist Index!")

def detail(request, book_entry_id):
    response = "You are looking at Entry #%s!" 
    return HttpResponse(response % book_entry_id)
