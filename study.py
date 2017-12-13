from flask import Flask
 #导入Flask类
app=Flask(__name__)
 #创建app实例的名称为__name__的话，会根据导入的模块名字不同而不同

@app.route('/')
 #route()装饰器告诉flask触发器的URL

def hello_world():
   return 'Hello World'
#给出函数的名称用于生成特定的URL，并返回输出

@app.route('/')
def index():
    return 'Index Page'
@app.route('/hello')
def hello():
    return 'Hello World'
#如 index()和hello()函数所示：route()装饰器用于绑定URL

@app.route('/user/<username>')
def show_user_profile(username):
    #提供用户资料
    return 'User %s'%username
@app.route('/post/<int:post_id>')
def show_post(post_id):
    #显示id
    return 'Post %s'%post_id
'''
将可变部分(<variable_name>)添加到URL可以标记这些特殊部分。
这些特殊部分作为参数传递给函数
'''