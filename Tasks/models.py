from django.db import models



class Task(models.Model):

    title = models.CharField(max_length=60)
    body = models.TextField()

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"

    def __str__(self):
        return 'Задача %s %s' % (self.title, self.body)
