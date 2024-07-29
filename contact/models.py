from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=200)
    subject = models.CharField(max_length=255)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)
    admins_reply = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"From {self.name} || Recieved: {self.created_at}"
