from . import views
from django.urls import path
from .views import (
    BookView,
    ProfileView,
    contact_view,
    index,
    personal_trainer,
    members,
    log_out,
    EditProfileView,
    sessions_api,
    book_session
)


urlpatterns = [
    path("", index, name="index"),
    path('personaltrainer/', views.personal_trainer, name='personaltrainer'),
    path('member/', views.members, name='member'),
    path('book/', views.BookView.as_view(), name="book"),
    path('profile/', views.ProfileView.as_view(), name="profile_view"),
    path('contact/', views.contact_view, name="contact"),
    path('logout/', views.log_out, name='logout'),
    path('login/', views.log_in, name='login'),
    path('profile/edit/', views.EditProfileView.as_view(), name="edit_profile"),
    path('api/sessions/', views.sessions_api, name='sessions_api'),
    path('book_session/<int:session_id>/', views.book_session, name='book_session'),
]