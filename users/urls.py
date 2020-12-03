from django.shortcuts import redirect
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('register/', views.register, name="register"),

    path('login/', auth_views.LoginView.as_view(template_name="login.html", redirect_authenticated_user=True),
         name="login"),


    path('profile/', views.profile, name="profile"),

    path('logout/', auth_views.LogoutView.as_view(template_name="logout.html"), name="logout"),




    path('password-reset/',
         auth_views.PasswordResetView.as_view(),
         name='password_reset'),

    path('password-reset/done',
         auth_views.PasswordResetDoneView.as_view(),
         name='password_reset_done'),

    path('password-reset/<uidb64>/<token>',
         auth_views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),

    path('password-complete/',
         auth_views.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),




]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
