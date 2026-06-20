from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User


# 🏠 STRONA GŁÓWNA
def home_page(request):
    return render(request, "hero_section.html")


# 👑 ADMIN DASHBOARD
@login_required
def dashboard(request):

    users = User.objects.all()

    context = {
        "users": users,
        "total_users": users.count(),
        "active_users": users.filter(is_active=True).count(),
        "admin_users": users.filter(is_superuser=True).count(),
        "new_users_list": users.order_by("-date_joined")[:5],
        "new_users": users.order_by("-date_joined").count(),
    }

    return render(request, "dashboard.html", context)


# 🧭 SPRAWDZANIE MODERATORA
def is_moderator(user):
    return (
        user.is_authenticated and
        user.groups.filter(name="Moderator").exists()
    )


# 🛡 MODERATOR DASHBOARD
@login_required
@user_passes_test(is_moderator)
def moderator_dashboard(request):

    users = User.objects.all()

    context = {
        "users": users,
        "total_users": users.count(),
        "active_users": users.filter(is_active=True).count(),
        "new_users_list": users.order_by("-date_joined")[:5],
        "new_users": users.order_by("-date_joined").count(),
    }

    return render(request, "dashboard_moderator.html", context)


# 🔁 ROUTER PO LOGOWANIU
@login_required
def redirect_after_login(request):

    user = request.user

    # 👑 ADMIN
    if user.is_superuser:
        return redirect("dashboard")

    # 🧭 MODERATOR
    if user.groups.filter(name="Moderator").exists():
        return redirect("moderator_dashboard")

    # 👤 NORMAL USER
    return redirect("home")


# 👤 STRONA O AUTORZE
def about_me(request):
    return render(request, "about_me.html")


# 🛡 ROLE I DOSTĘP
@login_required
def roles_users(request):

    users = User.objects.all()

    context = {
        "users": users,
    }

    return render(request, "roles_users.html", context)

@login_required
def users_list(request):
    users = User.objects.all()

    context = {
        "users": users,
        "total_users": users.count(),
        "active_users": users.filter(is_active=True).count(),
        "admin_users": users.filter(is_superuser=True).count(),
        "new_users": users.order_by("-date_joined").count(),
    }

    return render(request, "users_list.html", context)