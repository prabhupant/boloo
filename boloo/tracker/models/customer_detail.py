from django.db import models

class CustomerDetail(models.Model):

    class Meta:
        db_table = 'customer_detail'

    salutation_code = models.CharField(max_length=2)
    first_name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    street_name = models.CharField(max_length=64)
    house_number = models.CharField(max_length=4)
    zipcode = models.CharField(max_length=6)
    city = models.CharField(max_length=64)
    country_code = models.CharField(max_length=2)
    email = models.CharField(max_length=128)


    def __str__(self):
        return "Customer ID - {}".format(self.id)
