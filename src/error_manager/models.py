from django.db import models


class ErrorCode(models.Model):

    class Meta:
        verbose_name_plural = 'error_code'

    description = models.TextField(
        max_length=500,
        verbose_name='description',
        null=False,
        blank=False
    )

    code = models.CharField(
        max_length=10,
        verbose_name='code',
        null=False,
        blank=False
    )

    url = models.TextField(
        max_length=500,
        verbose_name='url',
        null=False,
        blank=False
    )

    def __str__(self):
        return "{} {} {}".format(self.code, self.description, self.url)
