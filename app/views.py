from app.forms import TodoForm
from django.urls import reverse
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from app.models import TodoModel

# Create your views here.

def user_page(request):

    todos = TodoModel.objects.all().order_by('-created')
    add_form = TodoForm()

    if (request.method == 'POST' and 'add' in request.POST):
        print(request.POST)
        title = request.POST['title']
        desc = request.POST['description']

        for obj in TodoModel.objects.all():
            if obj.title == title and obj.description == desc:
                messages.info(request, f"Record already exist")
                return redirect(reverse('todo:user_page'))
        add_form = TodoForm(request.POST)
        if add_form.is_valid():
            add_form.save()
            return redirect(reverse('todo:user_page'))
            
    if(request.method == 'POST' and 'edit' in request.POST):
        edit_key = str(request.POST['edit'])
        todo_id = int(edit_key.split(' ')[-1])
        update = get_object_or_404(TodoModel, pk=todo_id)

        title = str(request.POST['title'])
        description = str(request.POST['description'])
        completed = request.POST['completed']

        update.title = title
        update.description = description
        update.completed = completed
        update.save()

    if (request.method == 'POST' and 'confirm' in request.POST):
        confirm_key = str(request.POST['confirm'])
        todo_id = int(confirm_key.split(' ')[-1])

        todo = get_object_or_404(TodoModel, pk=todo_id)
        todo.delete()
        messages.success(request, f"'{todo}' deleted successfully")

        # print(update, title, description, completed, edit_key, f"this {todo_id}")

    return render(request, 'app/user_page.html', {
        'todos':todos,
        'add_form':add_form,
    })

# def user_edit(request, pk):
#     todo = get_object_or_404(TodoModel, pk=pk)
#     return render(request, 'app/user_edit.html', {
#         'todo':todo,
#     })