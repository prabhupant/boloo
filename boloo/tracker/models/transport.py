from django.db import models

class Transport(models.Model):

    class Meta:
        db_table = 'transport'

    transport_id = models.IntegerField(primary_key=True)
    transport_code = models.CharField(max_length=24)
    track_and_trace = models.CharField(max_length=24)
    

    def __str__(self):
        return "Transport ID - {}".format(self.transport_id)