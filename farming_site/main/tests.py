from django.test import TestCase
from main.models import Crop

class CropTest(TestCase):
    def setUp(self):
        self.crop = Crop.objects.create(name="Tomato", price=10, quantity=100, image="~/Pictures/oranges.webp")

    def test_crop_name(self):
        self.assertEqual(self.crop.name, "Tomato")

    def test_crop_price(self):
        self.assertEqual(self.crop.price, 10)

    def test_crop_quantity(self):
        self.assertEqual(self.crop.quantity, 100)

    def test_crop_image(self):
        self.assertEqual(self.crop.image, "~/Pictures/oranges.webp")




# Create your tests here.
