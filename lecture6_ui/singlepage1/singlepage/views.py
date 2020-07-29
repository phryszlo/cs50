from django.http import Http404, HttpResponse
from django.shortcuts import render

# Create your views here.
# def index(request):
#   return render(request, "singlepage/index.html")

texts = ["This is text #1",
          "Ths is text #2",
          "This is text #3"]

imgs = ["singlepage/static/singlepage/images/brocco.jpg",
        "singlepage/static/singlepage/images/DLPIC.jpg",
        "singlepage/static/singlepage/images/eric.jpg"]          

def index(request):
  # return HttpResponse("hi")
  return render(request, "singlepage/index.html")

def section(request, num):
  if 1<= num <= 3:
    with open(imgs[num - 1], "rb") as f:
      return HttpResponse(f.read(), content_type="image/jpeg")
    # return HttpResponse(texts[num - 1])
  else:
    raise Http404("No such image")
    # return HttpResponse(texts[num - 1])


  # return render(request, "singlepage/section.html")