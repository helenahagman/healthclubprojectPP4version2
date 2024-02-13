from django.urls import path
from .views import BookView, ProfileView, contact_view, index, personal_trainer, members, log_out, EditProfileView, sessions_calendar, sessions_api, book_session

urlpatterns = [
    path("", index, name="index"),
    path("personaltrainer/", personal_trainer, name='personal_trainer'),
    path("member/", members, name='members'),
    path("book/", BookView.as_view(), name="book"),
    path("profile/", ProfileView.as_view(), name="profile_view"),
    path("contact/", contact_view, name="contact"),
    path("logout/", log_out, name='logout'),
    path("profile/edit/", EditProfileView.as_view(), name="edit_profile"),
    path("sessions/calendar/", sessions_calendar, name='sessions_calendar'),
    path("api/sessions/", sessions_api, name='sessions_api'),
    path("book_session/<int:session_id>/", book_session, name='book_session'),
]