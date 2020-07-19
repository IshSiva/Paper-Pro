from django.shortcuts import render

# Create your views here.
def homepage_renderer(request):
	return render(request, 'homepage/index.html')