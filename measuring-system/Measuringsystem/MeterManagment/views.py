from django.shortcuts import render
from django.shortcuts import render_to_response
# Create your views here.
def mainPage(request):
    print('helloword')
    return render_to_response('index.html')