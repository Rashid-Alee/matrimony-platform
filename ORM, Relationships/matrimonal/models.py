from django.db import models
from django.core.files.storage import FileSystemStorage
from django.conf import settings

fs = FileSystemStorage(location=settings.MEDIA_ROOT)

# Create your models here.


class Religion(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Sects(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Sects"

    religion = models.ForeignKey(
        Religion, on_delete=models.CASCADE, related_name="sects"
    )

    def __str__(self):
        return self.name


class Caste(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Hobby(models.Model):

    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Hobbies"

    def __str__(self):
        return self.name


class FatherProfile(models.Model):
    name = models.CharField(max_length=50)
    occupation = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name


class Profile(models.Model):
    GENDER_CHOICES = [("M", "Male"), ("F", "Female")]
    name = models.CharField(max_length=50)
    profile_pic = models.ImageField(null=True, blank=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    occupation = models.CharField(max_length=50, null=True)
    birth_date = models.DateField(null=True)
    is_married = models.BooleanField(default=False)
    email = models.EmailField(max_length=100, unique=True)
    religion = models.ForeignKey(
        Religion, on_delete=models.CASCADE, related_name="profiles", null=True
    )

    sects = models.ForeignKey(
        Sects, on_delete=models.CASCADE, related_name="profiles", null=True
    )

    caste = models.ForeignKey(
        Caste, on_delete=models.CASCADE, related_name="profile", null=True
    )
    hobby = models.ManyToManyField(Hobby, related_name="profiles", null=True)
    father = models.OneToOneField(
        FatherProfile, on_delete=models.CASCADE, related_name="dependent", null=True
    )

    def save(self, *args, **kwargs):

        print(f"data is updated for {self.name}")

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
