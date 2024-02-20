"""Defines URL patterns for blog."""

from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [

    #Home page
    path('', views.index, name = 'index'),

    #All posts page

    path('all_posts', views.all_posts, name = 'all_posts'),

    #Post page
    path('<int:post_title>/', views.post, name = 'post'),

    #Page for add news posts.
    path('new_post/', views.new_post, name = 'new_post'),

    #Page for the texts.
    path('new_post_text/<int:post_title>/', views.new_post_text, name = 'new_post_text'),

    #Page for editing texts.
    path('edit_text/<int:posttext_id>/', views.edit_text, name = 'edit_text'),
]
