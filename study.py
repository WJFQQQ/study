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

@app.route('/project/')
def project():
    return 'the project page'
@app.route('/about')
def about():
    return 'the about page'
'''
上述两个函数的不同在于 app.route()末尾有没有斜杠('/')
1. project函数中，'/project/'类似于系统文件路径，URL定位于尾部的斜杠
2. about函数中，'/anout'定义了URL，但是没有斜杠.是UNIX-like systems的文件路径。
   添加'/'-->('/baout/')将会导致URL错误：404 NOT FOUND
3. 这允许相似得到URL可以工作甚至'/'。URL应该保持独特，避免重复访问相同的地址
'''