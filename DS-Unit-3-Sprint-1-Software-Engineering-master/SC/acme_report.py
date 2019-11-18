from random import randint, sample, uniform
from acme import Product

# For random sample to generate names
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):
    """ Generate Acme Products """
    products = []
    for _ in range(num_products):
        adj = ADJECTIVES[randint(0,4)]
        noun = NOUNS[randint(0,4)]
        name = f'{adj} {noun}'
        price = randint(5, 100)
        weight = randint(5, 100)
        flammability = uniform(0.0, 2.5)
        
        products.append(Product(name, price, weight, flammability))
    return products

def inventory_report(products):
    """ Report of the acme products """
    num_unique_prod_name = []
    total_price = 0
    total_weight = 0
    total_flammability = 0

    for product in products:
        if product.name not in num_unique_prod_name:
            num_unique_prod_name.append(product.name)
        total_price += product.price
        total_weight += product.weight
        total_flammability += product.flammability

    total = len(num_unique_prod_name)
    avg_price = total_price / total
    avg_weight = total_weight / total
    avg_flammability = total_flammability / total

    print('\nACME CORPORATION OFFICIAL INVENTORY REPORT')
    print(f'Unique product names: {len(num_unique_prod_name)}')
    print(f'Average Price: {avg_price:.1f}')
    print(f'Average Weight: {avg_weight:.1f}')
    print(f'Average Flammability: {avg_flammability:.1f}')


if __name__ == '__main__':
    inventory_report(generate_products())