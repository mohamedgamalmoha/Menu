from django.views.generic import TemplateView


from .models import Product, Category


class HomePage(TemplateView):
    template_name = 'home.html'
    extra_context = {
        'categories': Category.objects.available(),
        'featured_products': Product.objects.featured()[:2],
        'newest_products': Product.objects.newest(),
    }
