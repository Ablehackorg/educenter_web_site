"""
URL configuration for web_site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from home.views import index, tutor, contact,subject_detail,subject, selectlanguage,login_page,register_page
from course.views import about,courses
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _

urlpatterns =[
    path('selectlanguage', selectlanguage, name='selectlanguage'),
    path('i18n/', include('django.conf.urls.i18n')),
]

urlpatterns += i18n_patterns(
    path(_('admin/'), admin.site.urls),
    path('home/', index,name='home'),
    path('', index),
    path('about/', about,name='about'),
    path('contact/',contact,name='contact'),
    path('courses/',courses,name='courses'),
    path('tutor/',tutor,name='tutor'),
    path('subject/<int:id>/<slug:slug>', subject_detail, name='subject_detail'),
    path("subject/",subject,name='subject'),
    path('login/', login_page, name='login_page'),
    path('register/', register_page, name='register'),
) + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)