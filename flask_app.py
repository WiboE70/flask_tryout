from flask import Flask
app=Flask(_name_)
@app.route('/')
def home():
    return "<p>Hello world!</p>"
if __name__ == '__main__':
       app.run(port=5000,debug=True)