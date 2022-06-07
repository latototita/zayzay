from django.shortcuts import render

# Create your views here.
def index(request):
    context={}
    return render(request,'index.html',context)
def privacy(request):
    return render(request,'privacy.html',{})
def article(request):
    return render(request,'article.html',{})
def terms(request):
    return render(request,'terms.html',{})
