from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
import certifi

ca = certifi.where()
client = MongoClient('mongodb+srv://sayapinn:$100doller@cluster0.qv0cojm.mongodb.net/Cluster0?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta

# 보라님
@app.route('/')
def home():
   return render_template('Debora_index.html')

@app.route("/first_mini", methods=["POST"])
def first_mini_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']

    doc = {
        'name':name_receive,
        'comment':comment_receive
    }

    db.intro.insert_one(doc)

    return jsonify({'msg':'저장 완료'})

@app.route("/first_mini", methods=["GET"])
def first_mini_get():
    homework_list = list(db.intro.find({}, {'_id': False}))
    return jsonify({'first_mini':homework_list})

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)

# 봉진님

@app.route('/')
def home():
   return render_template('bongjin_index.html')

@app.route("/first_mini", methods=["POST"])
def first_mini_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']

    doc = {
        'name':name_receive,
        'comment':comment_receive
    }

    db.bongjin.insert_one(doc)

    return jsonify({'msg':'저장 완료'})

@app.route("/first_mini", methods=["GET"])
def first_mini_get():
    homework_list = list(db.bongjin.find({}, {'_id': False}))
    return jsonify({'first_mini':homework_list})

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)


# 해빈님

@app.route('/')
def home():
   return render_template('haebeen_index.html')

@app.route("/first_mini", methods=["POST"])
def first_mini_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']

    doc = {
        'name':name_receive,
        'comment':comment_receive
    }

    db.haebeen.insert_one(doc)

    return jsonify({'msg':'저장 완료'})

@app.route("/first_mini", methods=["GET"])
def first_mini_get():
    homework_list = list(db.haebeen.find({}, {'_id': False}))
    return jsonify({'first_mini':homework_list})

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)


# 종수님

@app.route('/')
def home():
   return render_template('jongsu_index.html')

@app.route("/first_mini", methods=["POST"])
def first_mini_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']

    doc = {
        'name':name_receive,
        'comment':comment_receive
    }

    db.jongsu.insert_one(doc)

    return jsonify({'msg':'저장 완료'})

@app.route("/first_mini", methods=["GET"])
def first_mini_get():
    homework_list = list(db.jongsu.find({}, {'_id': False}))
    return jsonify({'first_mini':homework_list})

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)


# 예빈님

@app.route('/')
def home():
   return render_template('yebin_index.html')

@app.route("/first_mini", methods=["POST"])
def first_mini_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']

    doc = {
        'name':name_receive,
        'comment':comment_receive
    }

    db.yebin.insert_one(doc)

    return jsonify({'msg':'저장 완료'})

@app.route("/first_mini", methods=["GET"])
def first_mini_get():
    homework_list = list(db.yebin.find({}, {'_id': False}))
    return jsonify({'first_mini':homework_list})

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)

