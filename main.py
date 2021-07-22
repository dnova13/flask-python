from flask import Flask, render_template

# 서버 구축
app = Flask("SuperScrapper")


# @ : decorate 이고 이거 덕에 / 등으로 로 접속하는 라우트 만듬
@app.route("/")
def home():
    return render_template("home.html")
    ### 플라스크 기능 주 한 render_template에서 
    # 반드시 templates 폴더일경우 그 안에 있는 HTML 파일 들고옴.


# <username> /:username  username = 1 에 따라 동적으로 웹 제어 가능.
@app.route("/<username>")
def conn(username):
    return f"your name is {username}"


# 로컬일 경우 안먹힐 수 도 있음 "0.0.0.0"
# app.run(host="0.0.0.0")
# 로컬일 경우
app.run()
