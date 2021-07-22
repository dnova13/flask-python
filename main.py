from flask import Flask, render_template, request,redirect
from scarpper import get_jobs

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
def user(username):
    return f"your name is {username}"


### 검색 기능 query argument
@app.route("/report")
def report():
    word = request.args.get("word") # word 쿼리의 값 받아옴.
    data = 111
    
    if word :
        word = word.lower() ## 소문자로 변환
        jobs = get_jobs(word)
        print(jobs)
    else :
        return redirect("/") ## 홈으로 리다이렉트

    # return f"you are looking for a job in \"{word}\""
    return render_template("report.html",searchingBy=word, data=data)



# 로컬일 경우 안먹힐 수 도 있음 "0.0.0.0"
# app.run(host="0.0.0.0")
# 로컬일 경우
app.run()
