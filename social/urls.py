from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include

urlpatterns = [
    path('admin/', admin.site.urls),
    url('home/', include('home.urls')),
    url('register/', include('register.urls')),
    url(r'posts/(?P<email>.*)', include('posts.urls')),
    url('account/', include('account.urls')),
    url(r'^$',include('register.urls'))
]
