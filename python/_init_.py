# money =[5,10,50,500,100]
# coin =[1000,2000,10000,5000]

# doll=[money,coin]

# print(max(doll[0]),max(doll[1]))


# dinner = ['curry','pasta','pizza','ramen','misosoup']

# for i  in dinner:
    
#     print(i)
    
    
    
# for num in range(1,101):
#     if num % 3 ==0 :
#         print('buzz')
#     elif num % 10 ==0:
#         print('fizz')
#     print(num)
    
# for num in range(1,11):
#     if num ==7:
#         print('my luckey number')
#     elif num %5 == 0:
#         print('??')
#     else:
#         print(num)

from collections import Counter

lylics ='love you miss you admire you'
my_count = lylics.split()
colu = Counter(my_count)
print(colu)