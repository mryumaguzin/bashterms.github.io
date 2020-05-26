from django.db import models

class Term(models.Model):
    name = models.CharField(max_length=255)
    bash = models.CharField(max_length=255)
    mean = models.CharField(max_length=255)

    class Meta:
      verbose_name_plural = "terms"

    def __str__(self):
        return self.name

# class SportTerm(models.Model):
#     name = models.CharField(max_length=255)
#     bash = models.CharField(max_length=255)
#     mean = models.CharField(max_length=255)
#
#     class Meta:
#       verbose_name_plural = "sport_terms"
#
#     def __str__(self):
#         return self.name
