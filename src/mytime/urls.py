"""mytime URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns

from userena import views as userena_views
from userena import settings as userena_settings

from accounts import views as mt_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('userena.urls')),
    # url(r'^register/$', mt_views.register, name="register"),
    # url(r'^$', mt_views.home, name="home_page"),
    url(r'^register/$',
        userena_views.signup,
        {'template_name': "register.html"},
        name="register"
        ),
    url(r'^logout/$',
        userena_views.signout,
        {'next_page': userena_settings.USERENA_REDIRECT_ON_SIGNOUT,
         'template_name': 'good_bye.html'},
        name='logout_profile'
        ),
    url(r'^$', userena_views.signin,
        {'template_name': "home.html"},
        name='home_page'
        ),
]