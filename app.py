from flask import Flask, Blueprint
from controller.controller import ItensController
app=Flask(__name__)

app.register_blueprint(ItensController)

#Igor Jogs

if __name__=='__main__':
    app.run(debug=True)
