from flask import Flask, make_response, request

app = Flask(__name__)


@app.route("/set_cookies")
def set_cookie():
    resp = make_response("success")  # 设置响应体
    resp.set_cookie("key_test", "value_test", max_age=3600)
    return resp


@app.route("/get_cookies")
def get_cookie():
    cookie_1 = request.cookies.get("key_test")  # 获取名字为Itcast_1对应cookie的值
    return cookie_1


@app.route("/delete_cookies")
def delete_cookie():
    # 这里的删除cookie只是让其过期
    resp = make_response("del success")
    resp.delete_cookie("key_test")
    return resp


if __name__ == '__main__':
    app.run(debug=True)
