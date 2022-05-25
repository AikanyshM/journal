from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=100)
    birth_year = models.DateField()
    workplace = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    MARITAL_STATUS = (
        ('женат', 'married'),
        ('в разводе', 'divorced'),
        ('свободен', 'single'),
        ('помолвлен', 'engaged')
    )
    marital_status = models.CharField(max_length=50, choices=MARITAL_STATUS)
    STATUS = (
    ('активный', 'активный'),
    ('неактивный', 'неактивный'),
    ('удовлетворительный', 'удовлетворительный')
    )
    client_status = models.CharField(max_length=50, choices=STATUS)

    def __str__(self):
        return self.name
    