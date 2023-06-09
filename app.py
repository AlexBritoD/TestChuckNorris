from flask import Flask
import chuck

app= Flask(__name__)

@app.route('/', methods=['GET'])
def get_saludo():
    return 'hola'

@app.route('/chuck', methods=['GET'])
def get_id_chuck():
    return chuck.handle()



if __name__ == '__main__':
    app.run()