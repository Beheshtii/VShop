from django.core.management.base import BaseCommand
from product.models import ProductCategory

class Command(BaseCommand):
    help = 'Generate fake categories'

    def handle(self, *args, **options):
        fake_categories = {
            'هودی': 'hodi',
            'تیشرت': 'tshirt',
            'سویشرت': 'sweatshirt',
            'کاپشن': 'jacket',
            'پالتو': 'coat',
            'شلوار جین': 'jeans',
            'شلوار اسلش': 'slash-pants',
            'پیراهن مردانه': 'mens-shirt',
            'پیراهن زنانه': 'womens-dress',
            'دامن': 'skirt',
            'بلوز': 'blouse',
            'تاپ': 'top',
            'لباس راحتی': 'loungewear',
            'لباس ورزشی': 'sportswear',
            'ست خانگی': 'home-set',
            'کت تک': 'blazer',
            'لباس زیر': 'underwear',
            'جوراب': 'socks',
            'کلاه': 'hat',
            'شال و روسری': 'scarf'
        }

        for title, slug in fake_categories.items():
            ProductCategory.objects.get_or_create(title=title, slug=slug)

        self.stdout.write(self.style.SUCCESS(
            'Successfully generated 10 fake categories'))