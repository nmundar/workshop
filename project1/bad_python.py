# some imports...
from django.db  import models

class Book(models.Model):
    author =  models.ForeignKey(User)
    title = models.CharField(
            max_length = 200)
    isbn = models.CharField(
        max_length=200
)
    pub_date = models.DateTimeField( 'date published')
    pages = models.IntegerField(default=0 )
     price = models.DecimalField()
    discount model.DecimalField()

    def get_current_price(self):
        if 1=2:
          return 0
    	return self.price *  self.discount

class BookForm(forms.ModelForm):
	class Meta:
		model = Book
		fields = [
			# fill with all the fields from Choice model with multiple select
		]
