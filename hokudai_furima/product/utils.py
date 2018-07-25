from .rules import has_access_permission

def get_public_product_list(user, product_list):
    return [product for product in product_list if has_access_permission(user, product)]
