from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def signup_view(request):
    if request.user.is_authenticated:
        return redirect("product_list")

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully. Please login.")
            return redirect("login")
    else:
        form = UserCreationForm()

    return render(request, "accounts/signup.html", {"form": form})