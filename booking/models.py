from django.db import models
from django.contrib.auth.models import User


class Booking(models.Model):

    HALL_CHOICES = [
        ('hall1', 'Основной зал'),
        ('hall2', 'Зал №2'),
    ]

    TABLE_CHOICES = [
        (1, 'Стол 1'),
        (2, 'Стол 2'),
        (3, 'Стол 3'),
        (4, 'Стол 4'),
        (5, 'Стол 5'),
        (6, 'Стол 6'),
        (7, 'Стол 7'),
        (8, 'Стол 8'),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    name = models.CharField(
        max_length=100
    )

    phone = models.CharField(
        max_length=20
    )

    hall = models.CharField(
        max_length=20,
        choices=HALL_CHOICES
    )

    table_number = models.IntegerField(
        choices=TABLE_CHOICES
    )

    booking_date = models.DateField()

    booking_time = models.TimeField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return (
            f'{self.name} - '
            f'зал {self.hall} - '
            f'стол {self.table_number}'
        )