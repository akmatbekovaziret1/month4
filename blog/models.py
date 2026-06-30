from django.db import models

class Blog_post(models.Model):
    title = models.CharField(max_length = 100, verbose_name="Select title for blog")
    SUBJECT = (
        ("Number theory", "Number theory"),
        ("Algebra", "Algebra"),
        ("Combinatorics", "Combinatorics"),
        ("Geometry", "Geometry")
    )
    subject = models.CharField(max_length=100, choices=SUBJECT, default = "Algebra", verbose_name="Chose subject")
    description = models.TextField(verbose_name="Give blog description")
    created_at = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.title}-{self.created_at}"
    
class News(models.Model):
    title = models.CharField(max_length = 100, verbose_name="Select news title")
    photo = models.ImageField(upload_to = 'news_mk/', verbose_name= "Upload photo")
    source = models.URLField(verbose_name="Upload source link")
    created_at = models.DateField(auto_now_add = True)
    
    def __str__(self):
        return f"{self.title}-{self.created_at}"
    
    class Meta:
        verbose_name = 'news'
        verbose_name_plural = 'news'