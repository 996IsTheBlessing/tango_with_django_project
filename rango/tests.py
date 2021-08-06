from django.test import TestCase
from rango.models import Category
from django.urls import reverse
from rango.models import Category, Page
from django.utils import timezone

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
def add_page(category, title, url):
    return Page.objects.get_or_create(category=category, title=title, url=url)[0]
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



"""class PageAccessTests(TestCase):
    def test_last_visit_not_in_future(self):
        category = add_category('Django', 1, 1)
        self.assertTrue(category.last_viewed < timezone.now())"""
    
"""  def test_last_visit_is_updated(self):
        category = add_category('Python', 1, 1)
        page = add_page(category, 'Documentation', 'https://docs.python.org/3/')
        created_date = page.last_visit

        # Time WILL pass before this is executed.
        response = self.client.get(reverse('rango:goto'), {'page_id': page.id})

        # Refresh the model instance.
        page.refresh_from_db()

        self.assertTrue(page.last_visit > created_date) """