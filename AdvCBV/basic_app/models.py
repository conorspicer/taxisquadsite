from django.db import models
from django.core.urlresolvers import reverse
import datetime

# Create your models here.
class School(models.Model):
    SIXTY = '69ers'
    SPARTANS = 'Spartans'
    DIPS = 'Double Dips'
    BUSTS = 'Busts'
    BROWNS = 'Browns'
    GOFFS = 'Goffs'
    KAKAPOS = 'Kakpos'
    LUSTS = 'Lusts'

    TEAMS = (
    (SIXTY, '69ers'),
    (SPARTANS, 'Spartans'),
    (DIPS, 'Double Dips'),
    (BUSTS, 'Busts'),
    (BROWNS, 'Browns'),
    (GOFFS, 'Goffs'),
    (KAKAPOS, 'Kakpos'),
    (LUSTS, 'Lusts'),
    )
    team = models.CharField(max_length=256, choices=TEAMS)
    player = models.CharField(max_length=256)
    added_time = models.DateTimeField(default=datetime.datetime.now)

    TAXI = 'Taxi'
    IR = 'IR'
    ROSTER_CHOICES = (
        (TAXI, 'Taxi'),
        (IR, 'IR'),
    )
    roster = models.CharField(
        max_length=4,
        choices=ROSTER_CHOICES,
        default=TAXI,
    )

    IN = 'In'
    OUT = 'Out'
    CHANGE_CHOICES = (
        (IN, 'In'),
        (OUT, 'Out'),
    )
    change = models.CharField(
        max_length=4,
        choices=CHANGE_CHOICES,
        default=IN,
    )

    class Meta:
        ordering = ['added_time']

    def __str__(self):
        return self.player

    def get_absolute_url(self):
        return reverse("basic_app:detail", kwargs={'pk': self.pk})
