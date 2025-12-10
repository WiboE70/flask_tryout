from flask import Flask
app=Flask(_name_)
@app.route('/')
def home():
    return "<p>De veranderende tekst</p>"
if __name__ == '__main__':
       app.run(port=5000,debug=True)