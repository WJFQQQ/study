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
2. about函数中，'/about'定义了URL，但是没有斜杠.是UNIX-like systems的文件路径。
   添加'/'-->('/baout/')将会导致URL错误：404 NOT FOUND
3. 这允许相似得到URL可以工作甚至'/'。URL应该保持独特，避免重复访问相同的地址
'''

'''
url_for('index')--函数可以生成URL
'''

from flask import request
@app.route('/login',methods=['GET','POST'])
def login():
    if request.method =='POST':
        do_the_login()
    else:
        show_the_login_form()
'''
#默认：路由route 只回应 GET,
# 但是在route中提供methods=['GET','POST']来改变生成器route的回应
GET :浏览器将当前页面的信息储存并发送给服务端
POST:浏览器告诉服务端，它要向URL发送最新的信息。
     服务端(server)必须确认该信息已经储存，并只储存一次
'''

from flask import render_template
@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.htmnl',name=name)
'''
Flask会在Templates文件夹中寻找hello.py
Template必须和应用模块在同一个目录下：

case1:
/application.py
/templates
    /hello.html

case2:
/application
    /__init__.py
    /templates
        /hello.html

'''

from flask import request
@app.route('/login',methods=['POST','GET'])
def login():
    error=None
    if request.metthod=='POST':
        if valid_login(request.form['username'],
                       request.form['userpassword']):
            return log_the_user_in(request.form['username'])
        else:
            error='invalid username/password'
    return render_template('login.html',error=error)
searchword= request.arg.get('key','')
'''
使用methods的属性来访问请求的方法
为了访问数据表单，可以访问表单的属性
--------
如上所示：
若是form的属性中不存在user，就会出现Error: invalid username/password
你可以获得一个标注的keyerror 若是你不这么做，将会出现: HTTP 404 bad request
------
可以使用arg属性来访问URL参数：
    建议访问URL参数通过 get 或者 获取KeyError
    因为用户会对URL更改和提交，此时出现 http 400 bad request 是不友好的体验

'''

from flask import request
@app.route('/')
def index():
    username=request.cookies.get('username')
    #使用cookies.get(key) 代替 cookies[key] 防止出现KeyError错误

    resp=make_response(render_template())
    resp.set_cookies('username','the username')
    return resp
'''
cookies已经在response对象中设置，
'''

#指导用户访问其他节点，使用redirect()函数
#终止错误代码的请求，使用abort()函数
from flask import abort,redirect,url_for
@app.route('/')
def index():
    return redirect(url_for('login'))
@app.route('/login')
def login():
    abort(401)
    this_is_never_exrcuted()
    #用户将会从index被指导到401页面
    '''
    默认情况下，黑色和白色的错误页面如针对各个错误代码。
    如果你想自定义错误页，您可以使用errorhandler()装饰器：
    '''
from flask import render_template
@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'),404
'''
注意访问render_template后面的404，将会提示FLASK ：404
'''

from flask import Flask,session,redirect,url_for,escape,request
app=Flask(__name__)
@app.route('/')
def index():
    if 'username' in session:
        return 'log in as %s'%escape(session['username'])
    return 'You are not logged in'
@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        session['uername']=request.form['username']
        return redirect(url_for('index'))
    return

@app.route('/logout')
def logout():
    #移除username
    session.pop('username',None)
    return redirect(url_for('index'))
#cookies为储存在用户本地终端上的数据
#session称为“会话控制”。Session 对象存储特定用户会话所需的属性及配置信息
'''
除了request对象，还有它的下一个session对象。使得你储存用户信息
cookies将会在其中加密
这意味着用户可以查看cookies信息，但是不能修改。除非有密码
'''
