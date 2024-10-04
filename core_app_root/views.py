from django.shortcuts import render

# Create your views here.
def render_activation_template(request):
    return render(request,'activate.html')
