from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from .models import Note
from .forms import NoteForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required


class NoteUpdate(UpdateView):
    model = Note
    fields = ['title', 'description', 'docfile']
    template_name = "note/add_new.html"
    success_url = reverse_lazy('note_list')



@login_required(login_url='/login/')
def note_list(request):
    user = request.user
    notes = Note.objects.filter(author=user).order_by('created_date')
    #notes = Note.objects.all()
    return render(request, 'note/note_list.html', {'notes': notes})


@login_required(login_url='/login/')
def note_detail(request, pk):
    note = get_object_or_404(Note, pk=pk)
    return render(request, 'note/note_detail.html', {'post': note})


@login_required(login_url='/login/')
def add_new(request):
    # if request.method == "POST":
        #form = NoteForm(request.POST)
        # form = NoteForm(request.POST, request.FILES)
        # if form.is_valid():
        #     note = form.save(commit=False)
        #     note.image = request.FILES['image']
        #     note.author = request.user
        #     note.created_date = timezone.now()
        #     note.save()
        #     return redirect('note_detail', pk=note.pk)

    # else:
    #     form = NoteForm()
    #     form.isAdd = True
    # Handle file upload
    if request.method == 'POST':
        form = NoteForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Note(docfile=request.FILES['docfile'])
            newdoc.title = request.POST['title']
            newdoc.description = request.POST['description']
            newdoc.author = request.user
            newdoc.created_date = timezone.now()
            newdoc.save()

            # Redirect to the document list after POST
            return redirect('note_detail', pk=newdoc.pk)
    else:
        form = NoteForm()  # A empty, unbound form
        form.isAdd = True
    return render(request, 'note/add_new.html', {'form': form})


@login_required(login_url='/login/')
def note_edit(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note.docfile=request.FILES['docfile']
            note.title = request.POST['title']
            note.description = request.POST['description']
            note.save()
            return redirect('note_detail', pk=note.pk)
    else:
        form = NoteForm()
        form.title = note.title
        form.description = note.description
        form.docfile = note.docfile
        form.isAdd = False
    return render(request, 'note/add_new.html', {'form': form})


@login_required(login_url='/login/')
def note_delete(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == "POST":
        note.delete()
        return redirect('note_list')
    return render(request, 'note/note_delete.html', {'note': note})
