from django.shortcuts import render
from blog.models import Entry, Category, Bookmark, BookmarkCategory, AppCategory, \
    AppEntry
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from tagging.models import Tag
from django.core.mail import send_mail

# Create your views here.
def index(request):
    latest_entry_list = Entry.objects.order_by('creation_date')[:10]
    context = {'latest_entry_list':latest_entry_list}
    return render(request, 'index.html', context)


def blog(request):
    latest_entry_list = Entry.objects.order_by('-creation_date')
    paginator = Paginator(latest_entry_list, 10)
    page = request.GET.get('page')
    
    try:
        entrys = paginator.page(page)
    except PageNotAnInteger:
        entrys = paginator.page(1)
    except EmptyPage:
        entrys = paginator.page(paginator.num_pages)
        
    catagory_list = Category.objects.raw("select cate.id, cate.title, cate.description, count(cate.id) as entrynum from blog_category as cate, blog_entry_categorys as enca where cate.id = enca.category_id group by cate.id")
    
    tag_list = Tag.objects.all()
    
    context = {'latest_entry_list':entrys, 'catagory_list':catagory_list, 'latest_post':latest_entry_list[:3], 'tag_list':tag_list}
    
    return render(request, 'blog.html', context)

def single(request, post_id):
    # post_id = request.GET.get('id')
    post = Entry.objects.get(id=post_id)
    
    latest_entry_list = Entry.objects.order_by('-creation_date')[:3]
    catagory_list = Category.objects.raw("select cate.id, cate.title, cate.description, count(cate.id) as entrynum from blog_category as cate, blog_entry_categorys as enca where cate.id = enca.category_id group by cate.id")
    tag_list = Tag.objects.all()
    
    context = {'post':post, 'catagory_list':catagory_list, 'latest_post':latest_entry_list, 'tag_list':tag_list}
    return render(request, 'single.html', context)
    
    
def category(request, category_id):
    cate_entry_list = Entry.objects.filter(categorys__id=category_id).order_by('-creation_date')
    
    paginator = Paginator(cate_entry_list, 10)
    page = request.GET.get('page')
    
    try:
        entrys = paginator.page(page)
    except PageNotAnInteger:
        entrys = paginator.page(1)
    except EmptyPage:
        entrys = paginator.page(paginator.num_pages)

    latest_entry_list = Entry.objects.order_by('-creation_date')[:3]
    catagory_list = Category.objects.raw("select cate.id, cate.title, cate.description, count(cate.id) as entrynum from blog_category as cate, blog_entry_categorys as enca where cate.id = enca.category_id group by cate.id")
    tag_list = Tag.objects.all()
    
    context = {'latest_entry_list':entrys, 'catagory_list':catagory_list, 'latest_post':latest_entry_list, 'tag_list':tag_list}
    
    return render(request, 'blog.html', context)

def taglist(request, tag_id):
    
    tag = Tag.objects.get(id=tag_id)
    tag_entry_list = Entry.objects.filter(tags__icontains=tag.name)
    paginator = Paginator(tag_entry_list, 10)
    page = request.GET.get('page')
    
    try:
        entrys = paginator.page(page)
    except PageNotAnInteger:
        entrys = paginator.page(1)
    except EmptyPage:
        entrys = paginator.page(paginator.num_pages)

    latest_entry_list = Entry.objects.order_by('-creation_date')[:3]
    catagory_list = Category.objects.raw("select cate.id, cate.title, cate.description, count(cate.id) as entrynum from blog_category as cate, blog_entry_categorys as enca where cate.id = enca.category_id group by cate.id")
    tag_list = Tag.objects.all()
    
    context = {'latest_entry_list':entrys, 'catagory_list':catagory_list, 'latest_post':latest_entry_list, 'tag_list':tag_list}
    
    return render(request, 'blog.html', context)

def bookmarklist(request):
    
    bookmarks = Bookmark.objects.raw("select book.id, book.title, book.description, book.click_times, book.url, book.head_image, cate.title as category_title from blog_bookmark as book, blog_bookmarkcategory as cate where book.categorys_id = cate.id and book.status = 2")

    categorys = BookmarkCategory.objects.all()
    context = {'bookmark_list':bookmarks, 'category_list':categorys}
    return render(request, 'bookmark.html', context)

def appcategory(request, appcategory_id):
    appcategory = AppCategory.objects.get(id=appcategory_id)
    applist = AppEntry.objects.filter(categorys_id=appcategory_id)
    context = {'appcategory':appcategory, 'applist':applist}
    return render(request, 'service.html', context)

def contact(request):
    latest_entry_list = Entry.objects.order_by('-creation_date')[:3]
    catagory_list = Category.objects.raw("select cate.id, cate.title, cate.description, count(cate.id) as entrynum from blog_category as cate, blog_entry_categorys as enca where cate.id = enca.category_id group by cate.id")
    tag_list = Tag.objects.all()
    context = {'catagory_list':catagory_list, 'latest_post':latest_entry_list, 'tag_list':tag_list}
    
    return render(request, 'contact.html', context)


def sendmail(request):
    name = request.POST.get('name', 'customer')
    email = request.POST.get('email', 'melonblogs@163.com')
    subject = request.POST.get('subject')
    msg = request.POST.get('msg')
    msg = 'name:' + name + 'from email:' + email + 'subject:' + msg
    
    send_mail(subject, msg, 'melonblogs@163.com', ['59170121@qq.com'], fail_silently=False)
    return render(request, 'contact.html')
