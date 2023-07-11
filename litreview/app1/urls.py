from django.urls import path
# from app1 import views
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
# from django.urls import path, include
from app1.views import signup_view, login_view, flux, create_ticket_view, create_ticket_and_review_view, follow_users_view, \
    remove_following_user_view, posts_view, update_ticket, update_review, create_review, delete_ticket, delete_review

urlpatterns = [
    # path('hello/', views.hello),
    # path('about-us/', views.about),
    path('', login_view, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', signup_view, name='signup'),
    path('flux/', flux, name='flux'),
    path('follow/', follow_users_view, name='follow'),
    path('follow/<int:id>/remove', remove_following_user_view, name='remove_following'),
    path('posts/', posts_view, name='posts'),
    path('ticket/create/', create_ticket_view, name='create_ticket'),
    path('ticket/<int:id>/update', update_ticket, name='update_ticket'),
    path('ticket/<int:ticket_id>/delete', delete_ticket, name='delete_ticket'),
    path('ticket_review/create/', create_ticket_and_review_view, name='create_ticket_review'),
    path('review/create/<int:ticket_id>', create_review, name='create_review'),
    path('review/<int:review_id>/update', update_review, name='update_review'),
    path('review/<int:review_id>/delete', delete_review, name='delete_review'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
