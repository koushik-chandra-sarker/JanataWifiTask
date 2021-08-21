from django.http import JsonResponse
from django.shortcuts import render
# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from crud.models import StockMarket


def Index(request):
    instances = StockMarket.objects.all()
    return render(request, template_name='index.html', context={'instances': instances})


def saveInstance(request):
    if request.method == "POST":
        id = request.POST.get("id")
        date = request.POST.get("date")
        trade_code = request.POST.get("trade_code")
        high = request.POST.get("high")
        low = request.POST.get("low")
        open = request.POST.get("open")
        close = request.POST.get("close")
        volume = request.POST.get("volume")
        if id == "":
            stockMarket = StockMarket(date=date, trade_code=trade_code, high=high, low=low,
                                      open=open, close=close, volume=volume)
        else:
            stockMarket = StockMarket(id=id, date=date, trade_code=trade_code, high=high, low=low,
                                      open=open, close=close, volume=volume)
        stockMarket.save()
        return JsonResponse({"status": "true"})

    return JsonResponse({"status": "false"})


@csrf_exempt
def deleteInstance(request, pk=None):
    if request.method == "DELETE":
        print(pk)
        stockMarket = StockMarket.objects.get(id=pk)
        stockMarket.delete()
        return JsonResponse({"status": "true"})

    return JsonResponse({"status": "false"})
