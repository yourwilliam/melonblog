from django.shortcuts import render
from blog.models import Entry, Category
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.
def index(request):
    latest_entry_list = Entry.objects.order_by('creation_date')[:5]
    context = {'latest_entry_list':latest_entry_list}
    return render(request, 'index.html', context)


def blog(request):
    latest_entry_list = Entry.objects.order_by('creation_date')
    paginator = Paginator(latest_entry_list, 5)
    page = request.GET.get('page')
    
    try:
        entrys = paginator.page(page)
    except PageNotAnInteger:
        entrys = paginator.page(1)
    except EmptyPage:
        entrys = paginator.page(paginator.num_pages)
        
    catagory_list = Category.objects.all()
    
    context = {'latest_entry_list':entrys, 'catagory_list':catagory_list, 'latest_post':latest_entry_list[:3]}
    
    return render(request, 'blog.html', context)

def single(request):
    post_id = request.GET.get('id')
    post = Entry.objects.get(id=post_id)
    
    latest_entry_list = Entry.objects.order_by('creation_date')[:3]
    catagory_list = Category.objects.all()
    
    context = {'post':post, 'catagory_list':catagory_list, 'latest_post':latest_entry_list}
    return render(request, 'single.html', context)
    
    
    
    
    