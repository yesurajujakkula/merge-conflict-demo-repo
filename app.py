## flask app for hello world

from flask import Flask

app=Flask(__name__)

@app.route('/',methods=['GET'])
def home():
    list2 = [2837,873246,987431]
    list1 = [1,2,3,5,6,7]
    return "Hello World"


if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000)