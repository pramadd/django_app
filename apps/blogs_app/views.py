from django.shortcuts import render,HttpResponse, redirect

# Create your views here.

  # the index function is called when root is visited
def index(request):
    response = "placeholder to later display all the list of blogs"
    return HttpResponse(response)

def new(request):
    response = "placeholder to display a new form to create a new blog"
    return HttpResponse(response)

def create(request):
    return redirect('/')

def show(request, blogId):
    response = "placeholder to display blog ", blogId
    return HttpResponse(response)

def edit(request, blogId):
    response = "placeholder to edit blog", blogId
    return HttpResponse(response)    

def destroy(request, blogId):
    return redirect('/')      