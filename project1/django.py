# some imports...
from django.db import models


class Book(models.Model):
    author = models.ForeignKey('User')
    title = models.CharField(max_length=200)
    isbn = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    pages = models.IntegerField(default=0)
    price = models.DecimalField()
    discount = models.DecimalField()

    def get_current_price(self):
        return self.price * self.discount


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            # fill with all the fields from Choice model with multiple select
        ]
