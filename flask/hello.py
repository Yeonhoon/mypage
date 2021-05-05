from flask import Flask, make_response, request, render_template, jsonify, send_file, redirect, session, url_for
import test
import blue

import manage
app = Flask(__name__)
app.secret_key = b'jyhoon94'

app.register_blueprint(test.blog_ab, url_prefix='/blog')
app.register_blueprint(blue.blue_ab, url_prefix='/blue')

@app.route('/')
def main():
    return render_template('main.html')
    
# 회원가입
@app.route('/joinform')
def signupform():
    return render_template('join.html')

@app.route('/join', methods=['POST'])
def join():
    email = request.form['email']
    blog_id = request.form['blogid']
    user_pw = request.form['upw']
    print(email, blog_id, user_pw)
    manage.user_input(email=email, blog_id=blog_id, pw=user_pw)
    return redirect('/')

# 로그인

@app.route('/loginform', methods=['GET'])
def loginform():
    # return make_response(jsonify(success=True), 200)
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    uid = request.form.get('uid')
    pw = request.form.get('pw')
    print("Email:{}, Password: {}".format(uid,pw))

    if uid == 'jyh@jyh.com':
        # session['user'] = id
        result = {'auth': 'success'}
    else:
        "아이디 또는 비밀번호 확인"

    return redirect('/')

@app.route('/loop/<name>')
def loop(name):
    value_list = ['list1','list2','list3']
    print(value_list)


    return render_template('loop.html', values = value_list,
                            name = name)

@app.route('/list')
def user_list():
    users = manage.userlist()
    print(user)
    return render_template('userlist.html', data = users)

@app.route('/list/<user>')
def one_user(user):
    user = manage.user(user)
    return render_template('userlist.html', data= user)



if __name__ == '__main__':
    app.run(host='localhost', port='8080', debug=True)
    # app.config['SESSION_TYPE'] = 'filesystem'


