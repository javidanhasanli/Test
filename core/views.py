from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from core.models import Post
from core.forms import ContactForm, UserForm, LoginForm
from blog_backend.settings import EMAIL_HOST_USER,BASE_DIR

@login_required(login_url='core:login')
def home_view(request):
    posts = Post.objects.filter(is_activate=True)
    return render(request, 'home.html', {'posts': posts})


def post_detail_view(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'post_detail.html', {'post': post})


def contact_view(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            context = {
                "receiver_name": "Saium Khan",
                "age": 27,
                "profession": "Software Developer",
                "marital_status": "Divorced",
                "address": "Planet Earth",
                "year": 2023
            }
            template_name = f"{BASE_DIR}/templates/mail.html"
            convert_to_html_content = render_to_string(
                template_name=template_name,
                context=context
            )
            plain_message = strip_tags(convert_to_html_content)
            send_mail("Test Subject",
                      plain_message,
                      EMAIL_HOST_USER,
                      ["cavidan.mahmudoglu@gmail.com", "behbudovbehbud397@gmail.com"],
                      html_message=convert_to_html_content,
                      fail_silently=True)
            return render(request, 'contact.html', {"form": form, 'is_success': True})
        else:
            print(form.errors)
            return render(request, 'contact.html', {"form": form, 'is_success': False})

    return render(request, 'contact.html', {"form": form, 'is_success': False})



def register_view(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:login')
        else:
            print(form.errors)
            return render(request, 'register.html', {"form": form})

    return render(request, 'register.html', {"form": form})


def login_view(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('core:home_view')
            else:
                form.add_error(None, "Invalid username or password.")
                return render(request, 'login.html', {"form": form})

    return render(request, 'login.html', {"form": form})


def logout_view(request):
    logout(request)
    return redirect('core:login')