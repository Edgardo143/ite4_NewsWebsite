from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('home/', views.home, name='home'),
    path('logout/', views.logout_user, name='logout'),
    path('news_list', views.news_list, name='news_list'),
    path('login', views.LoginPage, name= 'login'),
    path('signup', views.SignupPage, name= 'signup'),
    path('addnews', views.AddNews, name= 'addnews'),
    path('submitnews/', views.submit_news, name='submit_news'),
    path('delete_news/<int:news_id>/', views.delete_news, name='delete_news'),
    path('edit_news/<int:news_id>/', views.edit_news, name='news_edit'),
    path('filter_by_category/', views.filter_by_category, name='filter_by_category'),
    path('news/<int:news_id>/', views.news_detail, name='news_detail'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


