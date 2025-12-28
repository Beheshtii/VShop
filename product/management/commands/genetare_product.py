import random
from django.core.management.base import BaseCommand
from django.utils.text import slugify
from product.models import Product, ProductCategory, ProductStatusType
from accounts.models import User, UserType
from pathlib import Path
from django.core.files import File

BASE_DIR = Path(__file__).resolve().parent


class Command(BaseCommand):
    help = 'Generate fake products'

    def handle(self, *args, **options):
        user = User.objects.get(type=UserType.superuser)

        # List of images
        image_list = [
            "./images/img1.jpg",
            "./images/img2.jpg",
            "./images/img3.jpg",
            "./images/img4.jpg",
            "./images/img5.jpg",
            "./images/img6.jpg",
            "./images/img7.jpg",
            "./images/img8.jpg",
            "./images/img9.jpg",
            "./images/img10.jpg",
            # Add more image filenames as needed
        ]

        # Fake Description
        des = 'لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم از صنعت چاپ، و با استفاده از طراحان گرافیک است، چاپگرها و متون بلکه روزنامه و مجله در ستون و سطرآنچنان که لازم است، و برای شرایط فعلی تکنولوژی مورد نیاز، و کاربردهای متنوع با هدف بهبود ابزارهای کاربردی می باشد، کتابهای زیادی در شصت و سه درصد گذشته حال و آینده، شناخت فراوان جامعه و متخصصان را می طلبد، تا با نرم افزارها شناخت بیشتری را برای طراحان رایانه ای علی الخصوص طراحان خلاقی، و فرهنگ پیشرو در زبان فارسی ایجاد کرد، در این صورت می توان امید داشت که تمام و دشواری موجود در ارائه راهکارها، و شرایط سخت تایپ به پایان رسد و زمان مورد نیاز شامل حروفچینی دستاوردهای اصلی، و جوابگوی سوالات پیوسته اهل دنیای موجود طراحی اساسا مورد استفاده قرار گیرد.'

        # Fake Titles
        titles = [
            'جدیدترین مدل‌های پوشاک',
            'خرید لباس با کیفیت بالا',
            'مد روز پوشاک زنانه و مردانه',
            'لباس راحت و شیک برای استفاده روزمره',
            'کالکشن جدید فصل',
            'بهترین انتخاب برای استایل خاص',
            'پوشاک مناسب تمام سلیقه‌ها',
            'لباس‌های ترند سال',
            'استایل ساده اما جذاب',
            'پوشاک مناسب هر فصل'
        ]

        categories = ProductCategory.objects.all()

        for i in range(10):  # Generate 10 fake products
            user = user
            num_categories = random.randint(1, 4)
            selected_categories = random.sample(list(categories), num_categories)
            title = titles[i]
            slug = slugify(title, allow_unicode=True)
            selected_image = random.choice(image_list)
            image_obj = File(file=open(BASE_DIR / selected_image, "rb"), name=Path(selected_image).name)
            stock = random.randint(5, 25)
            status = random.choice(ProductStatusType.choices)[0]  # Replace with your actual status choices
            price = random.randint(250000, 1500000)
            discount_percent = random.randint(0, 50)

            product = Product.objects.create(
                user=user,
                title=title,
                slug=slug,
                image=image_obj,
                description=des,
                stock=stock,
                status=status,
                price=price,
                discount_percent=discount_percent,
            )
            product.category.set(selected_categories)

        self.stdout.write(self.style.SUCCESS('Successfully generated 10 fake products'))