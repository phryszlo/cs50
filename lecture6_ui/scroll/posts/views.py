from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, Http404
import time

# Create your views here.
def index(request):
  return render(request, "posts/index.html")

def posts(request):
  # return HttpResponse("congratulations")
  start = int(request.GET.get("start") or 0)
  end = int(request.GET.get("end") or (start + 9))

  data = []
  for i in range(start, end + 1):
    data.append(f"Post #{i}")

  time.sleep(1)

  return JsonResponse({
    "posts": data
  })

