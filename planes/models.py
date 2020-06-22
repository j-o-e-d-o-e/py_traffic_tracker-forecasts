from django.db import models


class Day(models.Model):
    date = models.DateField()
    probability = models.FloatField(default=0.0)

    class Meta:
        ordering = ['date']

    def __str__(self):
        return "%s: %s%%\n%s" % (self.date, self.probability, '\n'.join(map(str, self.hours.all())))


class Hour(models.Model):
    time = models.TimeField()
    wind_degree = models.IntegerField(default=0)
    probability = models.FloatField(default=0.0)
    day = models.ForeignKey(Day, related_name='hours', on_delete=models.CASCADE)

    class Meta:
        ordering = ['time']

    def __str__(self):
        return "%s: %s°, %s%%" % (self.time, self.wind_degree, self.probability)
