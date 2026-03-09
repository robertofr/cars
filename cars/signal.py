from django.db.models.signals import pre_save, post_save, pre_delete, post_delete
from django.dispatch import receiver
from cars.models import Car


@receiver(pre_save, sender=Car)
def pre_save_car(sender, instance, **kwargs):
    print('### PRE SAVE ###')

@receiver(post_save, sender=Car)
def post_save_car(sender, instance, **kwargs):
    print('### POST SAVE ###')

@receiver(pre_delete, sender=Car)
def pre_delete_car(sender, instance, **kwargs):
    print('### PRE DELETE ###') 

@receiver(post_delete, sender=Car)
def post_delete_car(sender, instance, **kwargs):
    print('### POST DELETE ###')