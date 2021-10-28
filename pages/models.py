from django.db import models
# from django.template.defaultfilters import slugify

# class Location(models.Model):
#     city = models.CharField(max_length=50)
#     state = models.CharField(max_length=50)
#     abbr = models.CharField(max_length=2)
#     image = models.ImageField(null=True, blank=True)

#     def __str__(self):
#         return self.city
    
#     @property
#     def imageURL(self):
#         try:
#             url = self.image.url
#         except:
#             url = ''
#         return url

# class Dataset(models.Model):
#     PLATFORM = (
#         ('0', 'Twitter'),
#         ('1', 'Instagram'),
#         ('2', 'LinkedIn'),   
#     )
#     title = models.CharField(max_length=50)
#     rows = models.IntegerField(null=True, blank=True, default=1)
#     slug = models.SlugField(null=False)
#     location = models.ForeignKey(Location, on_delete=models.PROTECT)
#     category = models.CharField(max_length=22, choices=PLATFORM, default=0, blank=True, null=True)

#     def __str__(self):
#         return self.title

#     def save(self, *args, **kwargs):
#         if not self.slug:
#             self.slug = slugify(self.title)
#         return super().save(*args, **kwargs)

# class Contact(models.Model):
#     first = models.CharField(max_length=28)
#     last = models.CharField(max_length=28)
#     message = models.TextField(null=True, blank=True)
#     form_date = models.DateTimeField(auto_now_add=True)
    
#     class Meta:
#         ordering = ['-form_date']

#     def __str__(self):
#         return self.last
