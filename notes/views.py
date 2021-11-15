from django.shortcuts import render, redirect
from .models import Note
from .forms import NoteFrom

def notes(request):
    notes = Note.objects.all()
    context = {'notes': notes}
    return render(request, 'notes/notes.html',context)

def note(request,pk):
    noteObj=Note.objects.get(id=pk)
    return render(request,'notes/single-note.html',{'note':noteObj})

def createNote(request):
    form = NoteFrom()
    if request.method == 'POST':
        form = NoteFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('notes')
    context={'form':form}
    return render(request,'notes/note_form.html',context)

def updateNote(request,pk):
    note = Note.objects.get(id=pk)
    form = NoteFrom(instance=note)

    if request.method == 'POST':
        form = NoteFrom(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('notes')
    context={'form':form}
    return render(request,'notes/note_form.html',context)

def deleteNote(request,pk):
    note = Note.objects.get(id=pk)
    if request.method == 'POST':
        note.delete()
        return redirect('notes')
    context={'object': note}
    return render(request,'notes/delete_template.html',context)

# Create your views here.
