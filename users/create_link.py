import random
import string
from django.utils.text import slugify

def slug_gen(model_instance, slug_field):
    a = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    b = ['9', '8', '7', '6', '5', '4', '3', '2', '1', '0']

    ra = random.randint(0, 9)
    rb = random.randint(0, 9)
    rc = random.randint(0, 9)
    rd = random.randint(0, 9)
    re = random.randint(0, 9)

    link = a[ra] + b[ra] + a[rb] + b[rb] + a[rc] +b[rc] + a[rd] + b[rd] + a[re] + b[re]
    slug = slugify(link)
    model_class = model_instance.__class__

    while model_class._default_manager.filter(slug=slug).exists():
        slug = f'{slug}'
    return slug
