from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models



class Person(models.Model):
    last_name = models.TextField()
    first_name = models.TextField()
    courses = models.ManyToManyField("Course", blank=True)
    class Meta:
        verbose_name_plural = "People"
class Course(models.Model):
    name = models.TextField()
    year = models.IntegerField()
    class Meta:
        unique_together = ("name", "year", )
class Grade(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    grade = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)])
    course = models.ForeignKey(Course, on_delete=models.CASCADE)


class Profile(models.Model):
    external_id=models.PositiveSmallIntegerField(
        verbose_name = 'id',
    )
    name = models.TextField(
        verbose_name = 'Имя пользователя'
    )
    def __str__(self):
        return f'#{self.external_id}'
class Meta:
    verbose_name = 'Пользователь Telegram'
    verbose_name_plural = 'Пользователи Telegram'