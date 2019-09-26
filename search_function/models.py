from django.db import models

class DeviceManager(models.Manager):
    def get_by_id(self, id):
       qs = self.get_queryset().filter(id=id)
       if qs.count() == 1:
         return qs.first()
       return None

    def __getattribute__(self, item):
        qs = self.get_queryset().filter(item=item)
        if qs.count() == 1:
            return qs.first()
        return None