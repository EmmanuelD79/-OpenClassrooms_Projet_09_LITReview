"""LITReview URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
import authentication.views
import reviews.views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',authentication.views.login_page, name='login'),
    path('logout/',authentication.views.logout_user, name='logout'),
    path('feed/', reviews.views.feed, name='feed'),
    path('posts/', reviews.views.own_feed, name='posts'),
    path('signup/', authentication.views.signup_page, name='signup'),
    path('ticket/create', reviews.views.create_ticket, name='create_ticket'),
    path('ticket/<int:ticket_id>', reviews.views.view_ticket, name='view_ticket'),
    path('ticket/<int:ticket_id>/edit', reviews.views.edit_ticket, name='edit_ticket'),
    path('ticket/<int:ticket_id>/delete', reviews.views.delete_ticket, name='delete_ticket'),
    path('review/create', reviews.views.create_review, name='create_review'),
    path('review/<int:review_id>', reviews.views.view_review, name='view_review'),
    path('review/<int:ticket_id>/respond', reviews.views.respond_ticket, name='respond_ticket'),
    path('review/<int:review_id>/edit', reviews.views.edit_review, name='edit_review'),
    path('review/<int:review_id>/delete', reviews.views.delete_review, name='delete_review'),
    path('follow-users', reviews.views.follow_users, name='follow_users'),
    path('follow-users/<int:sub_pk>/delete', reviews.views.delete_sub_user, name='delete_sub_user'),
]

if settings.DEBUG:

    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
