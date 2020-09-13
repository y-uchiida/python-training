# クラスの継承

class Products:
	__product_count = 0 # プライベートなクラス変数として、商品数を数える変数を定義

	# 商品数を返すクラスメソッドを定義
	# クラスメソッドの引数には、クラス自身を表す？clsを入れておく
	def count_products(cls):
		return Products.__product_count
	# 作成したメソッドを、クラスメソッドとして登録する。
	# classmethod(function_name)で代入する
	count_products = classmethod(count_products)

	def __init__(self, name = "item", price = 100, stock = 10):
		self.__name = name
		self.__price = price
		self.__stock = stock
		Products.__product_count += 1 # メンバメソッドからクラス変数を呼び出す場合には、[クラス名].[変数名]にする

	def sold(self, num):
		print(self.__name + "のお買い上げありがとうございます！")
		self.__decreaseStock(num)
		print("残り在庫 {}!".format(self.__stock))
	
	def __decreaseStock(self, n):
		self.__stock -= n


# クラスの継承は、 Subclass(Superclass)で行える
# サブクラスの引数？に、スーパークラスの名称を入れればOK
class Foods(Products):
	def __init__(self, name, price, stock, expirationDate):
		super().__init__(name, price, stock) # スーパークラスのメソッドや変数は、super().をつけると呼び出せる
		self.__expirationDate = expirationDate

	def sold(self, num):
		super().sold(num)
		print(self.__expirationDate + " までに売りさばけ！！")

camera = Products("カメラ", 254800, 20)
banana = Foods("バナナ", 298, 400, "2020/10/30")

camera.sold(2)
print()
banana.sold(10)
print()

# クラスメソッドを呼び出すときは、[クラス名].[メソッド名]()にする
print("商品は{} 種類登録されています".format( Products.count_products() ))
print()
