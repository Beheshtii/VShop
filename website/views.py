from django.shortcuts import render
from django.views import View

class IndexView(View):
    def get(self, request):
        return render(request, 'website/index.html')

class AboutUsView(View):
    def get(self, request):
        return render(request, 'website/about-us.html')
