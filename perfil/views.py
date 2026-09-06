from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.contrib import messages

def inicio(request):
    return render(request, 'perfil/inicio.html')

@require_http_methods(["POST"])
def confirmar_django(request):
    messages.success(request, "¡Django está funcionando correctamente! ✓")
    return redirect('inicio')
