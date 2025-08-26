## flask app for hello world

from flask import Flask

app=Flask(__name__)

@app.route('/',methods=['GET'])
def home():
    # this is the code changes for the developer b
    list2 = [2837,873246,987431]
    list1 = [1,2,3,5,6,7]
    # this is the for the developer1 code changes
    list1 = [1,2,3,5,6,7]
    return "Hello World"



if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000)