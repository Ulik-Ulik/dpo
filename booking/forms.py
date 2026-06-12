from django import forms
from .models import Booking
from datetime import date

class BookingForm(forms.ModelForm):

    class Meta:
        model = Booking

        fields = [
            'name',
            'phone',
            'hall',
            'table_number',
            'booking_date',
            'booking_time'
        ]

        widgets = {
            'booking_date': forms.DateInput(
                attrs={
                    'type': 'date'
                }
            ),

            'booking_time': forms.TimeInput(
                attrs={
                    'type': 'time'
                }
            )
        }

    def clean(self):
        def clean(self):

            cleaned_data = super().clean()

            hall = cleaned_data.get('hall')
            table = cleaned_data.get('table_number')

            booking_date = cleaned_data.get(
                'booking_date'
            )

            booking_time = cleaned_data.get(
                'booking_time'
            )

            if booking_date:

                if booking_date < date.today():
                    raise forms.ValidationError(
                        'Нельзя выбрать прошедшую дату'
                    )

            if Booking.objects.filter(
                    hall=hall,
                    table_number=table,
                    booking_date=booking_date,
                    booking_time=booking_time
            ).exists():
                raise forms.ValidationError(
                    'Это время уже занято'
                )

            return cleaned_data