from django.db import models

# Create your models here.
class Places(models.Model):
    name = models.CharField('Name', max_length=255)
    description = models.TextField('Description')
    address = models.CharField('Address', max_length=255)
    contact_number = models.CharField('Contact_number', max_length=20)
    image = models.CharField('Image_url', max_length=255)
    instruction = models.TextField('Instruction')
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)

    schedule_mo = models.ForeignKey('Schedule', on_delete=models.CASCADE, related_name='places_mo', default=1)
    schedule_tu = models.ForeignKey('Schedule', on_delete=models.CASCADE, related_name='places_tu', default=1)
    schedule_th = models.ForeignKey('Schedule', on_delete=models.CASCADE, related_name='places_th', default=1)
    schedule_we = models.ForeignKey('Schedule', on_delete=models.CASCADE, related_name='places_we', default=1)
    schedule_fr = models.ForeignKey('Schedule', on_delete=models.CASCADE, related_name='places_fr', default=1)
    schedule_sa = models.ForeignKey('Schedule', on_delete=models.CASCADE, related_name='places_sa', default=1)
    schedule_su = models.ForeignKey('Schedule', on_delete=models.CASCADE, related_name='places_su', default=1)

    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='category')



    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Достопримечательность"
        verbose_name_plural = "Достопримечательности"

class Schedule(models.Model):
    # DAY_CHOICES = (
    #     ('Monday', 'Monday'),
    #     ('Tuesday', 'Tuesday'),
    #     ('Wednesday', 'Wednesday'),
    #     ('Thursday', 'Thursday'),
    #     ('Friday', 'Friday'),
    #     ('Saturday', 'Saturday'),
    #     ('Sunday', 'Sunday'),
    # )

    # day = models.CharField(max_length=20, choices=DAY_CHOICES)
    start_time = models.TimeField(blank=True)
    end_time = models.TimeField(blank=True)
    excuse = models.TextField(blank=True)

    class Meta:
        verbose_name = "Расписание"
        verbose_name_plural = "Расписания"

    def __str__(self):
        return f"{self.start_time} - {self.end_time}"




    # {
    #     name: 'string',
    #     address: 'string',
    #     contactNumber: 'string',
    #     coordinates: [key, value],
    #     schedule: [
    #         {
    #             days: 'string',
    #             start: 'string'
    #             end: 'string'
    #             excuse: 'string'

    #         }
    #         images: string[],
    # instruction: string[]
    # }

class Category(models.Model):
    CAT_CHOICES = (
        ('Музей', 'Музей'),
        ('Театр', 'Театр'),
        ('Монумент', 'Монумент'),
        ('Развлечения', 'Развлечения'),
        ('Мечеть', 'Мечеть'),
        ('Парк', 'Парк'),
        ('Искусство', 'Искусство'),
        ('Культурный Центр', 'Культурный Центр'),
        ('Без категории', 'Без категории'),
    )

    category_name = models.CharField(max_length=100, choices=CAT_CHOICES)

    def __str__(self):
        return self.category_name

# Музей, Театр, Монумент, Развлечения, Мечеть, Парк, Искусство, Культурный Центр, Без