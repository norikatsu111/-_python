import os

print("script path =",__file__)　 # アンダーバー「 _ 」×２なので注意！

print("script dir=", os.path.dirname(__file__))

print("script dir=", os.path.abspath(__file__))

print("script dir=", os.path.exists(__file__))  
