from django.http import HttpResponse
def index(request):
    return HttpResponse("Servidor levantado mediante http.server")