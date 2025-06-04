def calulate_total(products):
    total = 0
    for product in products:
        total += product["price"] 
    return total


def test_calculate_total_with_empty_list():
    print("Prueba")
    assert calulate_total([]) == 0

def test_calculate_total_with_single_product():
    products = [
        {
            "name": "Notebook", "price": 5
        }
    ]
    print(calulate_total(products))
    assert calulate_total(products) == 5


def test_calculate_total_with_multipl_product():
    products = [
        {
            "name": "Notebook", 
            "price": 10
        },
        {
            "name": "Macbook", 
            "price": 2
        }
    ]
    print(calulate_total(products))
    assert calulate_total(products) == 12


if __name__ == '__main__':
    test_calculate_total_with_empty_list()
    test_calculate_total_with_single_product()
    test_calculate_total_with_multipl_product()