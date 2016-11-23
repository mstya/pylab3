from django.shortcuts import render, get_object_or_404, redirect
from .models import Note
from .forms import NoteForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login/')
def note_list(request):
    notes = Note.objects.all().order_by('created_date')
    return render(request, 'note/note_list.html', {'notes': notes})


@login_required(login_url='/login/')
def note_detail(request, pk):
    note = get_object_or_404(Note, pk=pk)
    return render(request, 'note/note_detail.html', {'post': note})


@login_required(login_url='/login/')
def add_new(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.author = request.user
            note.created_date = timezone.now()
            note.save()
            return redirect('note_detail', pk=note.pk)
    else:
        form = NoteForm()
    return render(request, 'note/add_new.html', {'form': form})


@login_required(login_url='/login/')
def note_edit(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            note = form.save(commit=False)
            note.author = request.user
            note.created_date = timezone.now()
            note.save()
            return redirect('note_detail', pk=note.pk)
    else:
        form = NoteForm(instance=note)
    return render(request, 'note/add_new.html', {'form': form})


@login_required(login_url='/login/')
def note_delete(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == "POST":
        note.delete()
        return redirect('note_list')
    return render(request, 'note/note_delete.html', {'note': note})
