from .models import Author, Profile, Book, Genre
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=Author)
def create_or_update_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(author=instance, website="russian lover boy")
    else:
        instance.profile.save()

@receiver(post_save, sender=Book)
def create_or_update_genre(sender, instance, created, **kwargs):
    if created:
        genre = Genre.objects.create(is_genre_book=True, name="testing genre")
        genre.books.add(instance)
    else:
        for genre in instance.genres.all():
            genre.save()
