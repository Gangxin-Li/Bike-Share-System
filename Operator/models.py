from django.db import models
# Create your models here.


class Station(models.Model):
    station_name = models.CharField(max_length=100, default="")
    station_latitude = models.FloatField(null=True)
    station_longitude = models.FloatField(null=True)

    def __str__(self):
        return self.station_name

    @property
    def number_of_bikes(self):
        available_bikes = self.bike_set.all().filter(in_use=False, is_faulty=False)
        return available_bikes.count()


class Bike(models.Model):

    in_use = models.BooleanField(default=False)
    is_faulty = models.BooleanField(default=False)
    station = models.ForeignKey(Station, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Bikes'

    def current_usage(self):
        if self.in_use:
            return "In Use"
        else:
            return "Free"

    def condition(self):
        if self.is_faulty:
            return "Faulty"
        else:
            return "Good"


class defectiveness_report(models.Model):
    id = models.AutoField(primary_key=True)
    defective_parts = models.CharField(max_length=(100))
    description = models.CharField(max_length=(500))
    bike = models.ForeignKey(Bike, on_delete=models.CASCADE)
    # report_user = models.ForeignKey(
    #     user_model.account_account, db_column='report_user', on_delete=models.CASCADE)
    report_datetime = models.DateTimeField(auto_now=True)
    is_fixed = models.BooleanField(default=False)
    operator_id = models.ForeignKey(to='User.account_account', null = True,blank=True,on_delete=models.CASCADE)
