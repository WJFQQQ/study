from flask import Flask
 #导入Flask类
app=Flask(__name__)
 #创建app实例的名称为__name__的话，会根据导入的模块名字不同而不同

@app.route('/')
 #route()装饰器告诉flask触发器的URL

def hello_world():
   return 'Hello World'
#给出函数的名称用于生成特定的URL，并返回输出
