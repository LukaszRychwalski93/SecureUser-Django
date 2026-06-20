from django.contrib import admin
from django.urls import path
from website.views import (
    home_page,
    dashboard,
    moderator_dashboard,
    redirect_after_login,
    about_me,
    roles_users,
    users_list
)
from django.contrib.auth import views as auth_views


urlpatterns = [
    # 🏠 STRONA GŁÓWNA
    path('', home_page, name='home'),

    # 📊 DASHBOARD ADMINA
    path('dashboard/', dashboard, name='dashboard'),

    # 🧭 DASHBOARD MODERATORA
    path('moderator/', moderator_dashboard, name='moderator_dashboard'),

    # 🔁 REDIRECT PO LOGOWANIU
    path('redirect/', redirect_after_login, name='redirect'),

    # 🔐 LOGOWANIE / WYLOGOWANIE
    path(
        'login/',
        auth_views.LoginView.as_view(template_name='login.html'),
        name='login'
    ),
    path(
        'logout/',
        auth_views.LogoutView.as_view(),
        name='logout'
    ),

    # 👤 STRONA O AUTORZE
    path('about-me/', about_me, name='about_me'),

    # 🛡 ROLE I DOSTĘP
    path('roles/', roles_users, name='roles'),

    # 👥 LISTA UŻYTKOWNIKÓW
    path('users/', users_list, name='users_list'),

    # 🛠 PANEL ADMINA DJANGO
    path('admin/', admin.site.urls),
]