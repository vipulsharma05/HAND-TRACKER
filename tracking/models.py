from django.db import models

class HandTrackingRecord(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.CharField(max_length=100)
    hand_detected = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user} - {self.timestamp}"
