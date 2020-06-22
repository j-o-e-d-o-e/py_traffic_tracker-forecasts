from rest_framework import serializers
from planes.models import Day, Hour


class ForecastHourSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hour
        fields = ['time', 'wind_degree', 'probability']


class ForecastDaySerializer(serializers.HyperlinkedModelSerializer):
    hours = ForecastHourSerializer(many=True)

    class Meta:
        model = Day
        fields = ['date', 'probability', 'hours']
