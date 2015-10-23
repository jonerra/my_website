from django.db import models

TITLE_CHOICES = (
(0, 'Ms.'),
(1, 'Mrs.'),
(2, 'Mr.'),
(3, 'Dr.'),
)

# Create your models here.
class Message(models.Model):
    subject = models.CharField(max_length=300)
    title = models.IntegerField(choices=TITLE_CHOICES, default=0)
    name = models.CharField(max_length=300)
    email = models.EmailField(max_length=300, blank=False, unique=False)
    message = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.subject