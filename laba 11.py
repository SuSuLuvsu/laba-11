def lab11_1():

    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(f"Ресторан {self.restaurant_name} предлагает кухню {self.cuisine_type}.")

        def open_restaurant(self):
            print(f"Ресторан {self.restaurant_name} открыт!")



    newRestaurant = Restaurant(input("введите название ресторана", input("введите кухню"))

    print(newRestaurant.restaurant_name)
    print(newRestaurant.cuisine_type)

    newRestaurant.describe_restaurant()
    newRestaurant.open_restaurant()

def lab11_2():

    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(f"Ресторан {self.restaurant_name} предлагает кухню {self.cuisine_type}.")



    restaurant1 = Restaurant(input("введите название ресторана", input("введите кухню"))
    restaurant2 = Restaurant(input("введите название ресторана", input("введите кухню"))
    restaurant3 = Restaurant(input("введите название ресторана", input("введите кухню"))


    restaurant1.describe_restaurant()
    restaurant2.describe_restaurant()
    restaurant3.describe_restaurant()

def lab11_3():

    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type, rating):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
            self.rating = rating

        def describe_restaurant(self):
            print(f"Ресторан {self.restaurant_name} предлагает кухню {self.cuisine_type}.")
            print(f"Рейтинг ресторана: {self.rating}")

        def update_rating(self, new_rating):
            self.rating = new_rating



    restaurant1 = Restaurant("Огузок", "французская", 4.5)


    restaurant1.describe_restaurant()


    restaurant1.update_rating(4.7)
    restaurant1.describe_restaurant()