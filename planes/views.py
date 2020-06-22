from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view

from planes import service
from planes.serializers import ForecastDaySerializer


@csrf_exempt
@api_view(['GET'])
def predict_and_planes_list(request):
    """
    Predicts, saves and lists all forecasts (workaround for dyno-sleep on free-plan)
    """
    forecasts = service.predict_and_get_forecasts()
    serializer = ForecastDaySerializer(forecasts, many=True)
    return JsonResponse(serializer.data, safe=False)


@csrf_exempt
@api_view(['GET'])
def planes_list(request):
    """
    Lists all forecasts
    """
    forecasts = service.get_forecasts()
    serializer = ForecastDaySerializer(forecasts, many=True)
    return JsonResponse(serializer.data, safe=False)
