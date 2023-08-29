from django.db import models
from home.models import library
# Create your models here.
class books(models.Model):
    book_id = models.AutoField(primary_key=True)
    library_id = models.ForeignKey(library, default=None, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=False)
    age = models.IntegerField(null=True)
    bookfile = models.FileField(upload_to='files', null=False, default=None)

    def __str__(self):
        return f"{self.book_id}, {self.library_id}, {self.name}, {self.age}, {self.bookfile}"