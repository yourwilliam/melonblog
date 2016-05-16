from django.shortcuts import render
from blog.models import Entry

# Create your views here.
def index(request):
    latest_entry_list = Entry.objects.order_by('creation_date')[:5]
    context = {'latest_entry_list':latest_entry_list}
    return render(request, 'index.html', context)


def blog(request):
    latest_entry_list = Entry.objects.order_by('creation_date')[:5]
    context = {'latest_entry_list':latest_entry_list}
    return render(request, 'blog.html', context)