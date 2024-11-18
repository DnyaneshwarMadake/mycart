from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shop/',include('shop.urls')),
    path('login/',views.LoginPage,name='login'),
    path('logout/',views.LogoutPage,name='logout'),
    path('blog/',include('blog.urls')),
    path('signup/',views.SignupPage,name='signup'),
    path('',views.HomePage,name='home'),
    #path('home/',views.HomePage,name='home'),
    # path('',include('accounts.urls')),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
