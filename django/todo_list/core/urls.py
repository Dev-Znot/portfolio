from django.contrib import admin
from django.urls import path

# from todos.views import todos_list
from todos.views import (
    ToDoListView, 
    TodoCreateView, 
    TodoUpgradeview, 
    TodoDeleteView, 
    TodoCompleteView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    # path('', todos_list, name="todo_list")
    path("", ToDoListView.as_view(), name="todo_list"),
    path("create/", TodoCreateView.as_view(), name="todo_create"),
    path("upgrade/<int:pk>", TodoUpgradeview.as_view(), name="todo_upgrade"),
    path("delete/<int:pk>", TodoDeleteView.as_view(), name="todo_delete" ),
    path("complete/<int:pk>", TodoCompleteView.as_view(), name="todo_complete"),

]
