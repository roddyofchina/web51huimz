from django.shortcuts import render
from django.views.generic.base import View
# Create your views here.

class indexView(View):
	def get(self, request):
		return render(request,'index.html',locals())

