from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbhomework


## HTML 화면 보기
@app.route('/')
def homework():
    return render_template('index.html')


@app.route('/info', methods=['POST'])
def post_info():
    name_receive = request.form['name_give']
    count_receive = request.form['count_give']
    address_receive = request.form['address_give']
    phone_receive = request.form['phone_give']

    info = {
        'name': name_receive,
        'count': count_receive,
        'address': address_receive,
        'phone': phone_receive
    }

    db.info.insert_one(info)
    return jsonify({'result': 'success'})


@app.route('/info', methods=['GET'])
def read_info():
    result = list(db.info.find({}, {'_id': 0}))
    return jsonify({'result': 'success', 'info': result})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)