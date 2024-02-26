from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import (
    ListView, 
    CreateView, 
    UpdateView, 
    DeleteView, 
    View,
)
from django.urls import reverse_lazy

from .models import Todo

#def todos_list(request):
    #todos = Todo.objects.all()
    #return render(request, "home.html", {"todos": todos})

class ToDoListView(ListView):
    model = Todo


class TodoCreateView(CreateView):
    model = Todo
    fields = ["title", "deadline"]
    success_url = reverse_lazy("todo_list")


class TodoUpgradeview(UpdateView):
    model = Todo
    fields = ["title", "deadline"]
    success_url = reverse_lazy("todo_list")


class TodoDeleteView(DeleteView):
    model = Todo
    success_url = reverse_lazy("todo_list")


class TodoCompleteView(View):
    def get(self, request, pk):
        todo = get_object_or_404(Todo, pk=pk)
        # centralizando a regra de negocio, aplicando a filosofia: Fat models, skin views.
        todo.mark_has_complete()
        return redirect("todo_list")

    