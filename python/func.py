# ---------------Homework 19------------------------
# 講習１
# タプルに比べて構造体が優れている点

# ・構造体は中身のデータの更新可能
# # 順番じゃなく名前でデータ呼び出す（タプルは順番通りじゃないとダメ。なので構造体は間違えにくい）


# 講習２
# クラス
# ・構造体に関数を持たせたもの
# ・何かを作る時の設計図と同じ


# インスタンス
# ・クラスという設計図を基にして作ったものがインスタンス
# 例
# 車をつくるとき
# 設計書（クラス）それでできた車（インスタンス）

# インスタンス変数
# ・それぞれのインスタンスごとに独立した変数
# ・そのインスタンスだけで使う変数（各インスタンスでの共有はできない）


# 演習3
# 生徒の成績を保持するクラスを作ります。以下の条件でクラスを作成してください。

# クラス名 Score
# 生徒の名前を保持するインスタンス変数nameを作成
# 国数英の変数であるmath, english, japaneseを作成



# class Score:
#     def __init__(self,name,math,english,japanese):
#         self.name = name
#         self.math = math
#         self.english = english
#         self.japanese =japanese

#     def result(self):
#         print(self.name + 'の数学の点数は' + str(self.math) +
#         '英語の点数は'+ str(self.english) +'国語の点数は'+ str(self.japanese) +
#         'です')

# taro =Score('taro',60,70,80)
# taro.result()
# jiro =Score('jiro',40,30,70)
# jiro.result()



# 演習4
# 数学mathの成績が一番良い生徒の名前を表示するプログラムを書いてください。
# なお、以下にテスト用のコードがありますので、

# class Math:
#     def __init__(self,name,score):
#         self.name = name
#         self.score = score

#     def result(self):
#         print(self.name)


# taro =Math('taro',60)
# jiro =Math('hiro',80)
# taro.result()
# jiro.result()

# math_score =[ taro,jiro]
# print(math_score)
# # print(taro)



# math_score =[hi = Math('taro',60),hu = Math('jiro',80),huu = Math('saburo',50)]
# print(math_score)
# # print(max(math_score, key = lambda x:x.score))
# max_math = max(math_score, key = lambda x:x.score)





# math_score ={'taro':60,'jiro':80,'saburo':50,}

# max_math = max(math_score.items(), key = lambda x:x[1])[0]
# print(max_math)



# ************************************************************************
# class UserInfo:
#   def __init__(self):
#     self.name = ''
#     self.birth= 0
#     self.address=''

#       # ↓クラスを基にして作られたもの「インスタンス」
# taro = UserInfo()
# taro.name = 'taro'
# taro.birth = 1986
# taro.address = 'tokyo'

# 　↑インスタンスが持つデータをインスタンス変数
# 　name,birth,addressはインスタンス変数になる

# --------Homework 20-------------------

# 演習1
# 以下のクラスにmath、english、japaneseの最高得点の科目名と点数を表示するメソッドを作成してください。



# class Score:
#     def __init__(self,name,math,english,japanese):
#         self.name = name
#         self.math = math
#         self.english = english
#         self.japanese = japanese

#     def best_score(self):
#         if self.math > self.english or self.math > self.japanese:
#             print('math' + str(self.math)+ '点です')
#         elif self.english > self.japanese:
#             print('english'+ str(self.english)+ '点です')
#         else:
#             print('japanese'+ str(self.japanese)+ '点です')

# rika =Score('rika',40,50,60)
# rika.best_score()



# 演習2
# 演習1で作成したクラスでのデータの初期化に、コンストラクタを利用してください。
    # class Exam(Score):
    #     def __init__(self,math,english,japanese):
    #         self.math = math
    #         self.english =english
    #         self.japansese = japanese
    #     if self.math > self.english or self.math > self.japanese:
    #         print('math' + str(self.math)+ '点です')
    #     elif self.english > self.japanese:
    #         print('english'+ str(self.english)+ '点です')
    #     else:
    #         print('japanese'+ str(self.japanese)+ '点です')



# 演習3
# 手続き型言語に比べて、なぜオブジェクト指向型言語が優れているかを調べてください。

# 手続き型言語はプログラマたちがルールを決めなくてはいけないけど
# オブジェクト指向はデータと処理が結びついているため食い違いが出てこない。


# ****************Homework21****************

# 演習1
# クラスのコンストラクタやメソッドの第一引数がなぜselfであるか説明してください。また、selfの実体が何か説明してください。

#  Pythonのメソッドは「第一引数に自分自身のインスタンス（self）が入るのがルール。
#  インスタンスを表すオブジェクト

# 演習2
# 以下について説明してください。

# グローバル変数

# 関数の定義の外の変数は
# プログラミング内のどこからでも使える変数のこと。
# 一番自由度が高い変数
# 関数の中でも    grobal を使えばグローバル変数を作成できる。

# 他のモジュールのグローバル変数を使う方法

# 全てのインスタンス間で共通した値を持つ変数
# モジュール名.__name__　で取り込める


# 関数内のローカル変数

# 関数中で宣言した変数で使える範囲が限られる。

# クラス変数


# インスタンス変数

# それぞれのインスタンスごとに独立した変数


# 演習3
# クラスベースのオブジェクト指向とプロトタイプベースのオブジェクト指向について調べてください。

# ★クラスベースのオブジェクト指向
# データ構造とメソッドを持つクラスを定義して
# 変数やメソッド引数、戻り値の型として使用


# ★プロトタイプベースのオブジェクト指向
# 「プロトタイプ」という既存のオブジェクトをベースに。
# 新しいオブジェクトを作るときも「クラスのインスタンス」を作るんじゃなくて
# 「プロトタイプ」のクローンを作るような感覚




# *******************Homework 24*************************

# 演習1
# 以下のクラスを継承し、オリジナルのクラスのインスタンス変数aをプリントするメソッドを実装してください。

# class ClassA:
#     def __init__(self):
#         self.a = 'hello'


# class ClassB(ClassA):
#     def print_code(self):
#         print(self.a)


# code = ClassB()
# code.print_code()



# #         演習2
# 以下のクラスを継承し、オリジナルのクラスのインスタンス変数a, bを足した値をプリントするメソッドを実装してください。
# なお、継承したクラスのコンストラクタも引数を2つ受け取り、それを親クラスの初期化に利用してください。

# class ClassA:
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b


# class ClassB(ClassA):
#     def __init__(self,b,d):
#         self.b = b
#         self.d = d
#         print(self.b + self.d)

# ris = ClassB(5,5)



# 演習3
# listを継承し、コンストラクタに与えた引数のタイプだけ格納できるリストクラスを作成してください。たとえば
# ml = MyList('a')
# とすると、文字列型しか受け取らなくなります。


# color_list =['red','pink','yellow']

# class List_book(list):
#     def __init__(self,int):
#         list.__init__(self)

#     def append(self,value):
#         if value == str(''):
#           color_list.append(value)
#         print(color_list)

# kim = List_book('a')
# kim.append('white')


# color_list =['red','pink','yellow']

# class List_book(list):
#     def __init__(self,int):
#         list.__init__(self)

#     def append(self,value):
#         color_list.append(value)
#         print(color_list)

# kim = List_book('a')
# kim.append('white')

# *******************Homework 25*****************************
# 演習1
# ポリモーフィズムとは何か説明してください。この記事だけでなく、いろいろなソースをあたっていただきたいと思います。
# 書き方はひとつだけど動き方は複数。
# 同じ関数でも違う処理を行える

# 演習2
# 多重継承のメリットとデメリットについて調べてください。
# 既存の物からもっと簡単に便利なクラス、オブジェクトを作る事ができる。

# たくさんのクラスから継承してしまうと、わかりにくくなってプログラムを複雑にして混乱するから
# みんなあまりおすすめしていない

# 演習3
# 継承とコンポジションのそれぞれのメリット・デメリットについて調べてください。
# 『Effective Java』に載っているこのトピックは非常に有名なので、調べれば情報がでてくると思います。

# ★継承
# 継承のメリットは簡単にスーパークラスを基にサブクラスを作れて
# 無駄にコード書く必要も無い、見やすい。

# 継承はカプセル化を破壊してしまって、サブクラスはスーパークラスのが基なので
# スーパークラスの実装が変わると、サブクラスも変わる可能性がある
# サブクラスとスーパークラス間に本当のサブタイプ関係がある場合にだけ、継承は適切

# ★コンポジション
# 継承よりも関連図をイメージする際に継承よりもわかりやすくできる。
# メソッドをワンクッション置くことで融通が効く、

# コンポジションは継承に比べて書くコードが多くなるから少し面倒
# 継承みたいに継承できない。

# コンポジション（Composition）は、日本語で「混合物」を意味する単語である。あるクラスの機能を持つクラスのことを指す。
# 特定のクラスの機能を、自分が作るクラスにも持たせたい場合に、継承を使わずフィールドとしてそのクラスを持ち、
# そのクラスのメソッドを呼び出すメソッドを持たせること。そうすることで、クラスに他のクラスの機能を組み込むことができる。
