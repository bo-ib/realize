from django.shortcuts import render,redirect ,get_object_or_404
from .forms import BlogForm, CommentForm
from.models import Article, Category, Comment

# Create your views here.
#admin password-----------user name
#      bobm1995-----------boib



def homepage(request):
    category = request.GET.get('category')
    if category == None:
        obj = Article.objects.all()
    else:
        obj = Article.objects.filter(category__category_list=category)
    categories = Category.objects.all()
    return render(request, 'home.html', {'obj': obj, 'categories': categories})
    

def search_blog(request):
    if request.method =='POST':
        searched =request.POST['searched']
        job = Article.objects.filter(title__contains=searched)
        return render(request, 'search.html',{'searched':searched,'job':job})
    else:
        return render(request, 'search.html')



def category(request):
    return render(request, 'category.html')
    

def formpage(request):
    form = BlogForm()
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save() 
            form = BlogForm()
            return redirect('/')

    return render(request, 'form.html',{'form':form})





def details(request, pk): 
    ct =request.session.get('count_{}'.format(pk),0)
    newcount =ct + 1
    request.session['count_{}'.format(pk)] =newcount
    article =get_object_or_404(Article,pk=pk)
    comments = Comment.objects.filter(post=article)
    total_comment =comments.count()
    if request.method == 'POST':
        form =CommentForm(request.POST)
        if form.is_valid():
            comment =form.save(commit=False)
            comment.post =article
            comment.save()
            return redirect('details',pk=article.pk)
    else:
        form =CommentForm()
    
    category = request.GET.get('category')
    if category == None:
        obj = Article.objects.all()
    else:
        obj = Article.objects.filter(category__category_list=category)
    categories = Category.objects.all()
    context ={
        'log': article,'logs':comments,'form':form, 'c':newcount,'total_comment':total_comment, 'obj': obj, 'categories': categories
    }
    return render(request,'details.html', context)    








def delete(request, id):
    blog = Article.objects.get(id=id)
    blog.delete()
    return redirect('/')

def update(request,pk):
    blog =Article.objects.get(pk=pk)
    form =BlogForm(request.POST or None, instance=blog)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
        form =BlogForm()
        return redirect('/')
    context ={
       'form':form,
       'blog':blog
    }
    return render(request, 'form.html',context) 



def football(request):
    return render(request, 'football.html')
