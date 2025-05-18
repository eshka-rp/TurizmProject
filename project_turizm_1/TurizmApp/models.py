from django.db import models

class RegistrationModel(models.Model):
    id_user = models.IntegerField('ID участника', unique=True)
    start_time = models.TimeField('Время старта')
    finish_time = models.TimeField('Время финиша')

    def __str__(self):
        return f'участник: {self.id_user}'

    class Meta:
        verbose_name = 'Регистрация'
        verbose_name_plural = 'Регистрации'