# Разработать модель предметной области в соответствии с вариантом:

# Предметная область – магазин. Разработать класс Shop, описывающий работу магазина продуктов. Разработать класс
# Products, продукт описывается следующими параметрами: уникальный идентификатор, название продукта, стоимость,
# количество. Разработать класс Fruit_product на базе класс Product, фрукт характеризуется параметрами: страна
# изготовителя, срок годности.

# Для усложнения сделать проверку уникальности идентификаторов книг и журналов, проверку на недопустимость
# отрицательных значений при добавлении книг и журналов в библиотеку

from lesson2.ClFruitProduct import ClFruitProduct
from lesson2.ClEmployee import ClEmployee
from lesson2.ClProduct import ClProduct
from lesson2.ClShop import ClShop


shop = ClShop('Shop', 'Hotel Continental', 'Very very legal')
boss = ClEmployee('Mr. John Wick', '09/02/1964', 'YouDontNeedThisNumber')
shop.hire_employee(boss)
shop.print_shop_info()
print(shop.get_employers())

shop.add_product('Starter', 5000, 20)
main_course = shop.add_product('Main course', 10000, 5)
dessert = shop.add_fruit('Dessert lemon', 2500, 10, 'Germany', '01/01/2100')
print(shop.get_products())

shop.sell_product(main_course, 2, boss)
shop.sell_product(dessert, 1, boss)
print(shop.get_products())

print(str.format('Total earned: {0}', shop.get_earnings()))
print(str.format('Total tips earned: {0}', shop.get_total_tips_earned()))

