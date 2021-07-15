from django.db import models
from profiles.models import UserProfile


class Review(models.Model):
    product = models.ForeignKey(
        'products.Product',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='reviews')
    user_profile = models.ForeignKey(
        UserProfile,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='user_review')
    created_on = models.DateTimeField(auto_now_add=True)
    rating_figures = (
        ("1", '1'),
        ("2", '2'),
        ("3", '3'),
        ("4", '4'),
        ("5", '5'),
    )
    review_rating = models.CharField(
        max_length=10, choices=rating_figures, default="3")
    review_title = models.CharField(max_length=254)
    review_content = models.TextField(
        max_length=1000, null=False, blank=False, default='')

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.review_title

    def save(self, *args, **kwargs):
        self.product.calculate_rating()
        super().save(*args, **kwargs)
