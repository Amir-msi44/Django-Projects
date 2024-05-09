from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView
from blog.models  import Article
from .mixins import FieldsMixin, FormValidMixin, AuthorValidMixin

# Create your views here.
# @login_required
# def home(request):
#     return render(request, 'registration/home.html')

class ArticleList(LoginRequiredMixin,ListView):
    template_name = "registration/home.html"

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Article.objects.all()
        else:
            return Article.objects.filter(author=self.request.user)


class ArticleCreate(LoginRequiredMixin, FormValidMixin, FieldsMixin, CreateView):
    model = Article
    template_name = "registration/article-create-update.html"


class ArticleUpdate(AuthorValidMixin, FormValidMixin, FieldsMixin, UpdateView):
    model = Article
    template_name = "registration/article-create-update.html"