#a = [1,2,3,4,5]
# for fruits in a :
#     print(fruits)

# def hello(name):
#     print('Hello' + name)

# hello('Risa')
# hello('Kinuyo')

# m = max(10,20,30)

# print(m)

# r = min(1,2,3,)
# print(r)

# ab =min ([1,5,3,2,6,4])
# print(ab)

# p = range(1,100)
# for i in p:
#     if (i % 15 == 0):
#         print('FizzBuzz')
#     elif (i % 3 == 0):
#         print ('Fizz')
#     elif (i % 5 == 0):
#         print('Buzz')
#     else:
#         print(i)

# a = range(5,51)
# for f in a:
#     if(f % 10 == 0):
#         print('yes')
#     else:
#         print(f)


# 　　　-------------Homework 6-------------
# num =[1,5,3]
# mum =[2,6,4]

# num_mum = [num,mum]
# print(max(num_mum[0]),max(num_mum[1]))




# z = range(1,100)
# for a in z:
#     if (a % 15 == 0):
#         print('FizzBuzz')
#     elif(a % 3 == 0):
#         print('Fizz')
#     elif(a % 5 == 0):
#         print('Buzz')
#     else:
#         print(a)

# -----------------------Homework 7-------------------------------

# abc =-10
# abc =abs(abc)
# print(abc)

# my_abs =-325
# my_abs =abs(my_abs)
# print(my_abs)

# import math

# my_abs =math.fabs(-150)
# print(my_abs)
# def my_sum(x,y):
#     z = x + y
#     return z



# ---------2
# def my_fibo(n):
#     a, b = 0, 1
#     for i in range(n):
#         a, b = b, a + b
#     return b

# print([my_fibo(i) for i in range(12)])


# def my_fibo(n):
#     fib = [1, 1]
#     if n == 1:
#         fib = [1]
#     else:
#         for k in range(2, n):
#             fib.append(fib[k-1]+fib[k-2])
#     return fib

# fib = my_fibo(10)

# print(fib)



# import my_util

# # a = 4
# # b = 5

# # mos = my_util.cal(a,b)
# # print(mos)

# w = 45
# m = 32

# money = my_util.wed(w,m)
# print(money)


# ----------------------Homework 11 -----------------------------
# 1)
# list =['coffee','tea','coke','soda','orangejuice','coffee','coke','coke',77]

# print(set(list))


# # 3)

# from collections import Counter

# my_list=['suger','soysouce','orange','milk','milk']
# my_counter = Counter(my_list)

# print(my_counter)

# letter ="Had to have high high hopes for a living shooting for the stars when I could't make a kiling"
# words = letter.split()
# my_counter =Counter(words)
# print(my_counter)


# --------------------Homework 12
# 以下のCSV形式のテキストデータから教科ごとの生徒の平均点を算出してください。





text = '''lecture\students, 1, 2, 3, 4
math, 80, 70, 75, 54
english, 60, 80, 90, 80'''


# ちょっと惜しいんだけどなんか違う
exam_list = text.splitlines()
del exam_list[0]
print(exam_list)

for line in exam_list:
    splited_line = line.split(',')
    del splited_line[0]
    print(splited_line)
    print(type(line))
    
    # for line_2 in splited_line:
    #     for i in line_2:
	   #     int(i)

    # int(splited_line.rprint(splited_line)


    # sum(int(line_2) for line_2 in splited_line):
    # for line_2 in splited_line:
    #     ave = sum(int(line_2)/len(line_2))

#


##I'm working on it
# for line in text.split('\n'):
#  print(line)
#  # exam = line.split(',')
 # print('{} {} {} {}'.format(exam[1].strip(),exam[2].strip(),exam[3].strip(),exam[4].strip()))



# ちょっと惜しいんだけどなんか違う
# exam_list = text.splitlines()
# # print(exam_list)
# del exam_list[0]



# for line in exam_list:
#     splited_line = line.split(',')
#     del splited_line[0]
#     print(splited_line)

# ave = sum(splited_line)/len(4)
# print(ave)


# average = sum(math)/len(math)
# print(average)
# for line_2 in splited_line:
#     average = sum(int(line_2))/len(int(line_2))
#     print(average)



# ave = sum(exam_list[1])/len(exam_list[1])
# print(ave)


#  ave =sum(line)/len(line)


#  ave = sum(math)/len(math)

# print(ave)

# ave2 = sum(english)/len(english)
# print(ave2)




# 可能なら生徒や教科が増えても対応可能なプログラムにしてください

# CSVとは
# CSV形式にはなってます◯
# csvファイルっていう拡張子で取り扱うケース
# excel, google spread, data baseも、
# csvにするとエンジニアと非エンジニアがどっちもデータを共有できる

#  自分でリストにデータを入れてしまってる
# 上のCSVをリストに変換する必要がある

# いけそうな考え方
# 今の変数textに入ってるテクストをどうしたら、下のリストの形にできるか
# forを使う
# split





# math = [80,70,75,54]
# english = [60,80,90,80]

# ave = sum(math)/len(math)

# print(ave)

# ave2 = sum(english)/len(english)
# print(ave2)

# with open('me.txt')as m:
#     f = m.read()
#     print(f)


# with open('me.txt') as e:
#      y = e.read()
# with open('you.txt',mode ='w')as m:
#     m.write(y)




# with open('you.txt',mode ='w')as m:
#  with open('me.txt','r') as e:
#      count =0
#      for line in e:
#         count += 1
#         m.write("%02d: %s"%(count,line))



# with open('you.txt',mode ='w')as m:
#     with open('me.txt','r') as e:
#      count =0
#      for line in e:
#       count += 1
#       m.write(str(count).zfill(2)+' ')
#       m.write(line)



# f = open('me.txt','r')
# print(f.read())
# f.close()

# m= open('you.txt', 'w') # 書き込みモードで開く
# m.write(f)
# m.close()



# with open('me.txt') as f:
#     s = f.read()
#     # print(type(s))
#     print(s)

# with open('me.txt','r') as e:

#      for line in e:
#             print(line)
# with open('you.txt',mode ='w')as m:
#     m.write(e)





# with open('me.txt') as e:
#      y = e.read()
#      print(y)
# with open('you.txt',mode ='w')as m:
#      count =0
#      for line in m:
#             count += 1
#     m.write(y(count,line))




#Almost!!!!
# with open('me.txt','r')as f:
#     count = 0
#     for line in f:
#         count += 1
#         print(line)
#     with open('you.txt',mode ='w')as m:
#         m.write("%02d: %s"%(count,line))


#   with open('me.txt','r')as f:
#     count = 0
#     for line in f:
#         count += 1
#         print(line)
#     with open('you.txt',mode ='w')as m:
#         m.write("%02d: %s"%(count,line))






# import pickle

# zara = ['love','cute','fasionable']
# with open('melody.binaryfile','wb') as web:
#  pickle.dump(zara,web)


# import pickle

# with open('melody.binaryfile','rb') as web:
#     zara = pickle.load(web)
#     print(zara)

# import pickle

# # corona = ['mask','wash','gargling',]
# # with open('virus.binaryfile','wb') as masks:
# #     pickle.dump(corona,masks)


# with open('virus.binaryfile','rb') as masks:
#     corona =pickle.load(masks)
#     print(corona)



# ---------------------------------Homewor13-------------------------------------------------------------------------------------
# import re

# sen ='I have 2 pens'

# pattern ="[^\d]"
# results = re.findall(pattern,sen)


# print(results)


# web ='Urs is http://example.com/index.html'
# pattern ="https?://[\w/:%#\$&\?\(\)~\.=\+\-]+"

# result = re.findall(pattern,web)

# print(result)

