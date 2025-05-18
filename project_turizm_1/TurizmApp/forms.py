from .models import RegistrationModel
from django.forms import ModelForm, NumberInput, TimeInput


class RegistrationForm(ModelForm):
    class Meta:
        model = RegistrationModel
        fields = ['id_user', 'start_time', 'finish_time']
        labels = {
            'id_user' : 'ID участника',
            'start_time': 'Время старта',
            'finish_time': 'Время финиша',
        }

        widgets = {
            'id_user':NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'ID участника',
            }),
            'start_time': TimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Время старта введите в формате xx:xx:xx',
            }),
            'finish_time': TimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Время финиша введите в формате xx:xx:xx ',
            }),

        }