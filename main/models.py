from django.db import models

# Create your models here.


class Animal(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Fact(models.Model):
    text = models.TextField()
    animal = models.ForeignKey(Animal, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.animal.name}: {self.text}"


class Subscriber(models.Model):
    email = models.EmailField()
    subscribed_to = models.ForeignKey(Animal, on_delete=models.PROTECT)
    is_active = models.BooleanField(default=True)
    received_fact_ids = models.ManyToManyField(Fact, related_name="received_by")


    def __str__(self):
        return self.email
