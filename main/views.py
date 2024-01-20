from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import RegisterForm, Create, Add
from django.contrib.auth import login, logout, authenticate
from .models import Inventory, Product, History, Profile
import datetime

# custom 404 view
def custom_404(request, exception):
    return render(request, 'main/404.html', status=404)

def about(request):
    return render(request, 'main/about.html')


#@login_required(login_url="/login")
def home(request):
    posts = Inventory.objects.all()

    if request.method == "POST":
        post_id = request.POST.get("post-id")
        post = Inventory.objects.filter(id=post_id).first()
        if post and (post.author == request.user or post.author.username == "mustafa"):
            h = History()
            h.title = str(post.title) + " - " + str(post.description) + " is deleted"
            h.save()
            post.delete()

    return render(request, 'main/home.html', {"posts": posts})

#@login_required(login_url="/login")
def main(request):
    return redirect('/home')
    #return render(request, 'main/main.html')

#@login_required(login_url="/login")
def view(request, auth, name):
    products = Product.objects.order_by('-count').filter(inventory=name)
    
    try:
        post = Inventory.objects.get(title=name)
        if request.method == "POST":
            post_id2 = request.POST.get("post-id2")
            posts = Product.objects.filter(id=post_id2)
            post_id = request.POST.get("post-id")
            post = Inventory.objects.filter(id=post_id)
            alll = Product.objects.filter(inventory=name)
            
            if posts:
                #h = History()
                #h.title = str(posts.description) + " " + str(posts.upc) + " is deleted"
                #h.save()
                posts.delete()
                return redirect(request.META.get('HTTP_REFERER'))
            elif post:
                for i in alll:
                    i.delete()
                h = History()
                h.title = str(post.title) + " is deleted"
                h.save()
                post.delete()
                
                return redirect("/home")
    except:
        message = "Inventory not found"
        return redirect("/home", {"message":message})
    

    return render(request, 'main/view.html', {"products": products, "post":post, "name":name, "auth":auth})

@login_required(login_url="/login")
def settings(request):
    return render(request, 'main/settings.html')

@login_required(login_url="/login")
def create(request):
    if request.method == "POST":
        form = Create(request.POST)
        if form.is_valid():
            inventory = form.save(commit=False)
            inventory.author = request.user
            inventory.save()
            h = History()
            h.title = inventory.title + " - " + inventory.description + " is created"
            h.created_at = datetime.datetime.now()
            h.save()
            p = "/" + inventory.author.username + "/" + inventory.title
            return redirect(p)
    else: 
        form = Create()

    return render(request, 'main/create.html', {"form": form})

@login_required(login_url="/login")
def history(request):
    history = History.objects.all()
    if request.method == "POST":
        h_id = request.POST.get("h-id")
        if h_id != "all":
            posts = History.objects.filter(title=h_id).first()
            if posts:
                posts.delete()
        else:
            posts = History.objects.all()
            for p in posts:
                p.delete()
        
    return render(request, 'main/history.html', {"history": history})

def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            p = Profile()
            p.user = user.username
            p.last = user.last_name
            p.name = user.first_name
            p.email = user.email
            p.save()
            h = History()
            h.title = "User " + p.user + " is created"
            h.save()
            login(request, user)
            return redirect('/home')
    else:
        form = RegisterForm()

    return render(request, 'registration/sign_up.html', {"form": form})


@login_required(login_url="/login")
def add(request, auth, name):
    if request.method == "POST":
        form = Add(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.author = request.user
            product.inventory = str(name)
            product.total = product.count * product.price
            product.save()
            h = History()
            h.title = str(product.description) + " " + str(product.upc) + " is created with an initial count of " + str(product.count) + " in inventory " + name
            h.save()
            i = "/"+str(auth)+"/"+str(name)+"/"
            return redirect(i)
    else:
        form = Add()

    return render(request, 'main/add.html', {"form": form, "name":name, "auth":auth})

@login_required(login_url="/login")
def profile(request):
    
    if request.method == "POST":
        first = request.POST.get("first")
        last = request.POST.get("last")
        username = request.POST.get("username")
        email = request.POST.get("email")
        profile = Profile.objects.get(user = request.user.username)
        profile.first = first
        profile.last = last
        profile.user = username
        profile.eamil = email
        profile.save()
        profiles = Profile.objects.all()
        return render(request, 'main/profile.html', {"profile":profiles})
    else:
        profiles = Profile.objects.all()
        return render(request, 'main/profile.html', {"profile":profiles})



@login_required(login_url="/login")
def product(request, auth, name, product):
    view = Product.objects.get(id=product)
    return render(request, 'main/product.html', {"view":view, "auth":auth, "name":name})

