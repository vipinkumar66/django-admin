from django.db import models

class CrashData(models.Model):
    vin = models.CharField(max_length=50)
    crash_date = models.CharField(max_length=20)
    county = models.CharField(max_length=10)
    report_time = models.IntegerField(max_length=4)

    def __str__(self):
        return self.vin
