from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .form import *
# Create your views here.
def home(request):
    context = {'blogs': Blog.objects.all()}
    return render(request, 'home.html', context)

def login_attempt(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_obj = User.objects.filter(username=username)
        if not user_obj.exists():
            messages.success(request, 'User not found')
            return redirect('/login/')
        
        user_obj = authenticate(username=username, password=password)
        if not user_obj:
            messages.success(request, 'Invalid Credentials')
            return redirect('/login/')
        login(request, user_obj)
        return redirect('/')
    return render(request, 'login_attempt.html')

def register_attempt(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user_obj = User.objects.filter(username=username)
        if user_obj.exists():
            messages.success(request, 'User already registered')
            return redirect('/register/')

        user_obj = User.objects.filter(email=email)
        if user_obj.exists():
            messages.success(request, 'Email already registered')
            return redirect('/register/')
        
        user_obj = User(username=username, email=email)  
        user_obj.set_password(password)
        user_obj.save()
        messages.success(request, 'Your Account is created successfully')
        return redirect('/login/')

    return render(request, 'register_attempt.html')

def logout_attempt(request):
    logout(request)
    return redirect('/')

def show_all_blogs(request):
    context = {'blogs': Blog.objects.filter(user = request.user)}
    return render(request, 'show_all_blogs.html', context)

def create_blog(request):
    context = {'form': BlogForm, 'categories': Category.objects.all()}
    if request.method == 'POST':
        form = BlogForm(request.POST)
        category = request.POST.get('category')
        title = request.POST.get('title')
        banner_image = request.FILES['banner_image']

        if form.is_valid():
            content = form.cleaned_data['content']

            Blog.objects.create(
                title=title,
                content=content,
                category = Category.objects.get(id=category),
                user = request.user,
                banner_image=banner_image
            )
            messages.success(request, 'Your blog has been created')
            return redirect('create_blogs')

    return render(request, 'create_blogs.html', context)

def update_blog(request, id):
    context = {'categories': Category.objects.all}
    try:
        if request.method == 'POST':
            form = BlogForm(request.POST)
            category = request.POST.get('category')
            title = request.POST.get('title')
            banner_image = request.FILES['banner_image']

            if form.is_valid():
                content = form.cleaned_data['content']
                blog_object = Blog.objects.get(id=id)
                blog_object.title = title
                
                blog_obj.content=content,
                blog_obj.category = Category.objects.get(id=category),  
                if banner_image:
                    blog_object.banner_image = banner_image   
                blog_object.save()       
                messages.success(request, 'Your blog has been updated successfully')
                return redirect('create_blogs')

        blog_object = Blog.objects.get(id= id)
        if blog_object.user != request.user:
            return redirect('/')
        initial_dict = {'content': blog_object.content}
        form = BlogForm(initial = initial_dict)
        context['form'] = form
        context['blog_object'] = blog_object
    except Exception as e:
        print(e)
    return render(request, 'update_blogs.html', context)

def delete_blog(request, id):
    blog_object = Blog.objects.get(id=id)
    if blog_object.user != request.user:
        return redirect('/')
    blog_object.delete()
    return redirect('/show-all-blogs/')

def get_blog(request, id):
    context = {}
    try:
        blog_obj = Blog.objects.get(id=id)
        context["blog"] = blog_obj
    except Exception as e:
        print(e)
    return render(request, 'detail_blog.html', context)

