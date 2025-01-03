class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r', encoding='utf-8')
        text_from_file = file.read()
        file.close()
        return text_from_file

    def add(self, *products):
        with open(self.__file_name, 'r+', encoding='utf-8') as file:
            data = file.readlines()
            if data:
                for product in products:
                    for line in data:
                        check_product = line.split(',')[0].lower()
                        if product.name.lower() == check_product:
                            print(f'Продукт {product.name} уже есть в списке.')
                            break
                    else:
                        file.write(f'\n{product.name}, {product.weight}, {product.category}')
            else:
                for product in products:
                    file.write(f'{product.name}, {product.weight}, {product.category}\n')



s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')
# p4 = Product('Tomato', 1.5, 'Vegetables')
print(p2) # __str__
s1.add(p1, p2, p3)
print(s1.get_products())