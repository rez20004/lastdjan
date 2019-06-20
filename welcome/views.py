#
from django.shortcuts import render
#from django.conf import settings
#from django.http import HttpResponse

#from . import database
#from .models import PageView

from . forms import RegistrationForm


# Create your views here.


def index(request):

    form = RegistrationForm()
    context = {
        "myregistrationform": form
    }
    return render(request, 'welcome/index.html', context)


def protected_view(request):
    return render(request, 'welcome/index.html', {'current.user': request.user})



#def index(request):
#    hostname = os.getenv('HOSTNAME', 'unknown')
#    PageView.objects.create(hostname=hostname)

#    return render(request, 'welcome/index.html', {
#        'hostname': hostname,
#        'database': database.info(),
#        'count': PageView.objects.count()
#   })
#
#def health(request):
#    return HttpResponse(PageView.objects.count())
