from django.db import models

# Create your models here.
from zinnia.models_bases import entry


class Picture(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='gallery')


class Gallery(models.Model):
    title = models.CharField(max_length=50)
    pictures = models.ManyToManyField(Picture)


class EntryGallery(
    entry.CoreEntry,
    entry.ContentEntry,
    entry.DiscussionsEntry,
    entry.RelatedEntry,
    entry.ExcerptEntry,
    entry.FeaturedEntry,
    entry.AuthorsEntry,
    entry.CategoriesEntry,
    entry.TagsEntry,
    entry.LoginRequiredEntry,
    entry.PasswordRequiredEntry,
    entry.ContentTemplateEntry,
    entry.DetailTemplateEntry
):
    # image = models.ForeignKey(Picture)
    gallery = models.ForeignKey(Gallery)

    def __str__(self):
        return 'EntryGallery %s' % self.title

    class Meta(entry.CoreEntry.Meta):
        abstract = True
