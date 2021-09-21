from django.db import models


class Level(models.TextChoices):
    Un = 'Uncategorized'
    A0 = 'Beginner (A0)'
    A1 = 'High Beginner (A1)'
    A2 = 'Low Intermediate (A2)'
    B1 = 'Intemediate (B1)'
    B2 = 'High Intermediate (B2)'
    C1 = 'Advanced (C1)'
    C2 = 'High Advanced (C2)'

    def __str__(self):
        return self.value

    def to_tuple():
        return [(Level.Un, 'Uncategorized'),
                (Level.A0, 'Beginner (A0)'),
                (Level.A1, 'High Beginner (A1)'),
                (Level.A2, 'Low Intermediate (A2)'),
                (Level.B1, 'Intemediate (B1)'),
                (Level.B2, 'High Intermediate (B2)'),
                (Level.C1, 'Advanced (C1)'),
                (Level.C2, 'High Advanced (C2)')]
