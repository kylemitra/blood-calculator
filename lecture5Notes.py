foods = ["apples", "bananas", "cherries", "donuts"]
amounts = [11, 22, 33, 44]

def myfruitCounter(fruit):
    i = foods.index(fruit)
    print('There are {} {}.'.format(amounts[i],fruit))

def classFruitCounter(fruit):
    # for i, food in enumerate(foods):
    #     if food == fruit:
    #         print('There are {} {}.'.format(amounts[i], fruit))
    #         break
    for food, amount in zip(foods, amounts):
        if food == fruit:
            print('There are {} {}.'.format(amount, fruit))
            break

if __name__ == "__main__":
    myfruitCounter("apples")
    classFruitCounter("donuts")