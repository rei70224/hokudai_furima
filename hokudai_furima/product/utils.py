from .models import AccessLevelChoice

def get_public_product_list(product_list):
    return [product for product in product_list if product.access_level == AccessLevelChoice.public.name]
