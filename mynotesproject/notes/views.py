from django.shortcuts import render
from .models import Note
# Create your views here.
def home(request):
    return render(request,'notes/index.html')

def notess(request):
    notes=Note.objects.all()
    return render(request,'notes/note.html',{'notes':notes})
def about(request):
    return render(request,'notes/about.html')