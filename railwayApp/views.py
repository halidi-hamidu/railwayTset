from django.shortcuts import render

# Create your views here.
def homePage(request):
    template_name = 'homePage.html'
    context = {
        
    }
    return render (request, template_name, context)