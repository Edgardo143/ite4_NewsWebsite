from django.shortcuts import render, redirect
from .models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import News
from django.shortcuts import get_object_or_404, redirect
from .forms import NewsForm


def base(request):
    return render(request, 'base.html')
def home(request):
    return render(request, 'home.html')

def news_list(request):
    latest_news = News.objects.all().order_by('-date')[:10]
    return render(request, 'news_list.html', {'latest_news': latest_news})
def delete_news(request, news_id):
    news_item = get_object_or_404(News, pk=news_id)
    news_item.delete()
    return redirect('news_list')
def news_detail(request, news_id):
    # Retrieve the news item based on its ID
    news_item = get_object_or_404(News, id=news_id)

    context = {
        'news_item': news_item  # Pass the news item to the template
    }

    return render(request, 'news_detail.html', context)
def edit_news(request, news_id):
    news_item = get_object_or_404(News, pk=news_id)

    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES, instance=news_item)
        if form.is_valid():
            form.save()
            return redirect('news_list')
    else:
        form = NewsForm(instance=news_item)

    return render(request, 'news_edit.html', {'form': form, 'news_item': news_item})
def filter_by_category(request):
    category = request.GET.get('category')
    if category and category != 'all':
        filtered_news = News.objects.filter(category=category) 
    else:
        filtered_news = News.objects.all()  
    context = {
        'latest_news': filtered_news 
    }
    return render(request, 'all_news', context)
    
def AddNews(request):
    return render(request, 'add_news.html')
def submit_news(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        date = request.POST.get('date')
        image = request.FILES.get('image')
 
        news_item = News.objects.create(
            title=title,
            description=description,
            date=date,
            image=image
        )
        news_item.save()

        return redirect('news_list')

    return render(request, 'add_news.html')
def SignupPage(request):
  if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        firstname = request.POST.get('fname')
        lastname = request.POST.get('lname')
        pass1 = request.POST.get('password')
        pass2 = request.POST.get('confirm_password')

        if pass1 == pass2:
            existing_user = User.objects.filter(username=uname).exists()
            if not existing_user:
                my_user = User.objects.create_user(username=uname, email=email, password=pass1)
                UserProfile.objects.create(user=my_user, firstname=firstname, lastname=lastname)
                return redirect('login')
            else:
                return render(request, 'signup.html', {'error_message': 'Username already exists'})
        else:
            print("Passwords do not match")
            return render(request, 'signup.html', {'error_message': 'Passwords do not match'})

  return render(request, 'signup.html')


def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error_message': 'Invalid username or password'})
    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    messages.success (request, ('You were logged out.'))
    return redirect('base')

