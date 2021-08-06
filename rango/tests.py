from django.test import TestCase
from rango.models import Category
from django.urls import reverse
from rango.models import Category

# Create your tests here.
class CategoryTests(TestCase):
    def testviews_positive(self):

    #Ensure that the views in the category are a number greater than or equal to 0.

        category = Category(name='test', views=-1, likes=0)
        category.save()
        self.assertEqual((category.views >= 0), True)
    def testslug_creation(self):

    # Ensure that when a category is created, a proper lug is created appropriately.
       category = Category(name='Random Category String')
       category.save()
       self.assertEqual(category.slug, 'random-category-string')
    def testlikes_positive(self):

    #Ensure that the likes in the category are a number greater than or equal to 0.
        category = Category(name='test', likes=-1)
        category.save()
        self.assertEqual((category.likes >= 0), True)


class IndexViewTests(TestCase):
    def testindex_view(self):
        #If the category does not exist, an appropriate prompt should be displayed
        response = self.client.get(reverse('rango:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'There are no categories present.')
        self.assertQuerysetEqual(response.context['categories'], [])

        
def add_category(name, views=0, likes=0):
    category = Category.objects.get_or_create(name=name)[0]
    category.views = views
    category.likes = likes
    category.save()
    return category

def testindex_view_categories(self):
      #Check that the correct category is displayed
        add_category('Python', 1, 1)
        add_category('Django', 1, 1)
        add_category('JAVA', 1, 1)
        response = self.client.get(reverse('rango:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Python")
        self.assertContains(response, "Django")
        self.assertContains(response, "JAVA")
        num_categories = len(response.context['categories'])
        self.assertEquals(num_categories, 3)
