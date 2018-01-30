from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'enuda_mag/index.html')

def post_detail(request):
    return render(request, 'enuda_mag/post-regular.html')
