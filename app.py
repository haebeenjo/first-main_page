from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
import certifi

ca = certifi.where()
client = MongoClient('mongodb+srv://sayapinn:$100doller@cluster0.qv0cojm.mongodb.net/Cluster0?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta

@app.route('/')
def home():
   return render_template('main.html')

@app.route('/jongsu')
def jongsu():
   return render_template('jongsu_index.html')

@app.route('/yebin')
def yebin():
   return render_template('yebin_index.html')

@app.route('/bora')
def bora():
   return render_template('bora_index.html')

@app.route('/bongjin')
def bongjin():
   return render_template('bongjin_index.html')

@app.route('/haebeen')
def haebeen():
   return render_template('haebeen_index.html')

# ----------------------------------------------------


# 보라님
@app.route("/first_mini1", methods=["POST"])
def first_mini1_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']

    doc = {
        'name':name_receive,
        'comment':comment_receive
    }

    db.bora.insert_one(doc)

    return jsonify({'msg':'저장 완료'})

@app.route("/first_mini1", methods=["GET"])
def first_mini1_get():
    homework_list = list(db.bora.find({}, {'_id': False}))
    return jsonify({'first_mini1':homework_list})






# 봉진님
@app.route("/first_mini2", methods=["POST"])
def first_mini2_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']

    doc = {
        'name':name_receive,
        'comment':comment_receive
    }

    db.bongjin.insert_one(doc)

    return jsonify({'msg':'저장 완료'})

@app.route("/first_mini2", methods=["GET"])
def first_mini2_get():
    homework_list = list(db.bongjin.find({}, {'_id': False}))
    return jsonify({'first_mini2':homework_list})







# 해빈님
@app.route("/first_mini3", methods=["POST"])
def first_mini3_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']

    doc = {
        'name':name_receive,
        'comment':comment_receive
    }

    db.haebeen.insert_one(doc)

    return jsonify({'msg':'저장 완료'})

@app.route("/first_mini3", methods=["GET"])
def first_mini3_get():
    homework_list = list(db.haebeen.find({}, {'_id': False}))
    return jsonify({'first_mini3':homework_list})






# 종수님
@app.route("/first_mini4", methods=["POST"])
def first_mini4_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']

    doc = {
        'name':name_receive,
        'comment':comment_receive
    }

    db.jongsu.insert_one(doc)

    return jsonify({'msg':'저장 완료'})

@app.route("/first_mini4", methods=["GET"])
def first_mini4_get():
    homework_list = list(db.jongsu.find({}, {'_id': False}))
    return jsonify({'first_mini4':homework_list})






# 예빈님
@app.route("/first_mini5", methods=["POST"])
def first_mini5_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']

    doc = {
        'name':name_receive,
        'comment':comment_receive
    }

    db.yebin.insert_one(doc)

    return jsonify({'msg':'저장 완료'})

@app.route("/first_mini5", methods=["GET"])
def first_mini5_get():
    homework_list = list(db.yebin.find({}, {'_id': False}))
    return jsonify({'first_mini5':homework_list})

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)

