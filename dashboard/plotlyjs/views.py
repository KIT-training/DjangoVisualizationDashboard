from django.shortcuts import render

# Create your views here.
def BasicLinePlot(request):
    return render(request, 'plotlyjs/BasicLinePlot.html')

def BarChat(request):
    return render(request, 'plotlyjs/BarChat.html')