# def cal(x,y):
#     re = x * y
#     return re


# def wed(women,men):
#      return women *3000 + men * 5000

# total = wed(5,10)
# print(total)



# class Melody:
#     def __init__(self,name):
#         self.name = name

#     def zara(self):
#         print('He love {}'.format(self. name))

# risa = Melody('Tanabe')
# risa.zara()


# def coco(x,y):
#     return x + y

# sum = coco(4,5)
# sum1 = coco(5,5)
# print(sum1 + sum)


# def kiki(a,b):
#     print(a-b)

# kiki(3,5)





class Food():
    def __init__(self,price,quqntity):
        self.price = price
        self.quqntity= quqntity

    def total(self):
        return self.price * self.quqntity


apple = Food(100,15)
print(apple.total())