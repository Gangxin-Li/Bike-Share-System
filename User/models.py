from django.db import models
import django.db.models.deletion
import Operator.models as operator_models
import math



# Create your models here.
db_table = '"account_account"'
class account_account(models.Model):
    id = models.AutoField(primary_key=True)
    password = models.CharField(max_length=(128))
    username = models.CharField(max_length=(30))
    email = models.CharField(max_length=(60),unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    role = models.CharField(max_length=(10),default='User')
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default =False)
    is_superuser = models.BooleanField(default = False)
    hires_in_progress = models.IntegerField(default=0)
    wallet_balance = models.FloatField(default=0.0)
    amount_owed = models.FloatField(default=0.0)
    def __str__(self):
        return self.password

db_table = '"order"'
class order(models.Model):
    id = models.AutoField(primary_key=True)
    start_time = models.DateTimeField()
    check_out_time = models.DateTimeField(null=True)
    due_amount = models.FloatField()
    is_complete = models.BooleanField()
    bike = models.ForeignKey(operator_models.Bike, on_delete=models.CASCADE)
    end_station = models.ForeignKey(operator_models.Station, on_delete=models.CASCADE, related_name="end_station",null=True)
    start_station = models.ForeignKey(operator_models.Station, on_delete=models.CASCADE, related_name="start_station",null=True)
    user = models.ForeignKey(account_account, on_delete=models.CASCADE)
    fix_amount = models.FloatField()
    class Meta:
        db_table = 'User_order'
    def get_duration(self):
        return math.ceil((self.check_out_time - self.start_time).seconds / 60.0)