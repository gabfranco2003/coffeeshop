from django.db import models

# Category choices for consistency (optional)
CATEGORY_CHOICES = [
    ('hot', 'Hot'),
    ('cold', 'Cold'),
    ('sweet', 'Sweet'),
    ('savory', 'Savory'),
    # Add other categories as needed
]

class HeroImage(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, blank=True)
    image = models.URLField(max_length=2080)  # Use URLField for image
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Coffee(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)  # Optional: Use choices
    image = models.URLField(max_length=2080)  # Use URLField for image

    def __str__(self):
        return self.name


class Tea(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)  # Optional: Use choices
    image = models.URLField(max_length=2080)  # Use URLField for image

    def __str__(self):
        return self.name


class Pastry(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)  # Optional: Use choices
    image = models.URLField(max_length=2080)  # Use URLField for image

    def __str__(self):
        return self.name
