from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Mytodo
from .forms import TodoForm



def List_todo(request):
    todos = Mytodo.objects.all()
    form = TodoForm()
   
    return render(request, "todo/index.html", context ={"todos" : todos, 'form': form})

 
def todo_create(request):
    form = TodoForm()
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Tache ajoutée avec succès !")
            return redirect ('todo')

        else:
            messages.error(request, 'Erreur tache non ajoutée !')
        
    return render(request, "todo/todo.html", context ={ 'form': form})



def details(request, id):
    todos = Mytodo.objects.get(id =id)
    
    context ={'todos':todos}

    return render(request, 'todo/details.html', context= context) 


def supprimer_todo(request, id):
    todo = Mytodo.objects.get(id =id)
    if request.method == "POST":
        todo.delete()
        messages.success(request, "Tache supprimée avec sucgetcès !")
        return redirect('todo')
    

        
def update_todo(request, id):
    todo=Mytodo.objects.get(id =id)
    if request.method== "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tache modifier avec succès')
            return redirect('todo')
        else:
            form = TodoForm(instance=todo) 
    return render(request, 'todo/update.html', context = {'form': form})
        