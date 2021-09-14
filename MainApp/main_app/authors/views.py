from django.shortcuts import render
from django.views.generic import DetailView

# Create your views here.

class AuthorView(DetailView):

    def get(self,request,args,**kwargs):
        context = {}
        return render(request, "authors/author_detail_view.html", context=context)
