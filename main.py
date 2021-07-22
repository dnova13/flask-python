from flask import Flask

### 서버 구축
app = Flask("SuperScrapper")


### @ : decorate 이고 이거 덕에 / 등으로 로 접속하는 라우트 만듬
@app.route("/")
def home() :
    return "Hello! welcome"

@app.route("/contact")
def conn() :
    return "contact!"

### 로컬일 경우 안먹힐 수 도 있음 "0.0.0.0"
# app.run(host="0.0.0.0")

### 로컬일 경우
app.run()
