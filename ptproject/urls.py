from . import views
from django.urls import path
from .views import (
    BookView,
    ProfileView,
    contact_view,
    custom_logout,
    index,
    personal_trainer,
    members,
    LoginView,
    SignupView,
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
    # path('logout/', LogoutView.as_view(template_name='account/logout.html'), name='logout'),
    path('logout/', custom_logout, name='logout'),
    path('login/', LoginView.as_view(template_name='account/login.html'), name='login'),
    path('signup/', SignupView.as_view(template_name='account/signup.html'), name='signup'),
    path('profile/edit/', views.EditProfileView.as_view(), name="edit_profile"),
    path('api/sessions/', views.sessions_api, name='sessions_api'),
    path('book_session/<int:session_id>/', views.book_session, name='book_session'),
]