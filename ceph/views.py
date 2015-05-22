from datetime import datetime
from django.shortcuts import render




def base_view(request):
    return render(
        request, 'base.html',  {'current_time': datetime.now()}
    )

def demo_view(request):
    return render(
        request, 'demo.html',  {'current_time': datetime.now()}
    )
