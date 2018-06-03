from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from hokudai_furima.product.models import Product
from django.contrib import messages
from django.conf import settings
from .models import ReportToRecieveTodo, RatingTodo
from django.http import HttpResponseRedirect, HttpResponse
from django.template.response import TemplateResponse
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required

def add_todo_list(request, message, relative_url):
    #relative_url = reverse('product:product_details', kwargs={'pk': product.pk})
    todo = Todo(user=request.user, message=message, relative_url=relative_url)
    todo.save()

@login_required
def show_todo_list(request):
    undone_todo_list = list(ReportToRecieveTodo.objects.filter(user=request.user, is_done=False))
    done_todo_list = list(ReportToRecieveTodo.objects.filter(user=request.user, is_done=True))
    undone_todo_list += list(RatingTodo.objects.filter(user=request.user, is_done=False))
    done_todo_list += list(RatingTodo.objects.filter(user=request.user, is_done=True))
    return render(request, 'todo_list/todo_list.html', {'undone_todo_list': undone_todo_list, 'done_todo_list': done_todo_list})
