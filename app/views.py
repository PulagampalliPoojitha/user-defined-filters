from django.shortcuts import render

# Create your views here.



def usdf(request):
    d={'data':' PooJiThA Good Morning NvN'}
    return render(request,'usdf.html',d)
