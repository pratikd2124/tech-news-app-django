from django.shortcuts import render
from .tasks import news_task
def index(request):
    data = news_task()
    print(data)
    return render(request, 'index.html',{'datas':data})
