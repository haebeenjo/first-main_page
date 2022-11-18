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
@app.route("/first_mini1/writecomment", methods=["POST"])
def first_mini1_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']

    count_list = list(db.bora.find({}, {'_id': False}))
    count = len(count_list) + 1

    doc = {
        'name':name_receive,
        'comment':comment_receive,
        'num': count
    }

    db.bora.insert_one(doc)

    return jsonify({'msg':'저장 완료'})

@app.route("/first_mini1/showcomment", methods=["GET"])
def first_mini1_get():
    get_list = list(db.bora.find({}, {'_id': False}))
    return jsonify({'first_mini1':get_list})

@app.route('/first_mini1/deletecomment', methods=["POST"])
def first_mini1_delete():
    num_receive = request.form["num_give"]

    db.bora.delete_one({'num': int(num_receive)})
    return jsonify({'msg': '삭제 완료!'})






# 봉진님
@app.route("/first_mini2/writecomment", methods=["POST"])
def first_mini2_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']

    count_list = list(db.bongjin.find({}, {'_id': False}))
    count = len(count_list) + 1

    doc = {
        'name':name_receive,
        'comment':comment_receive,
        'num': count
    }

    db.bongjin.insert_one(doc)

    return jsonify({'msg':'저장 완료'})

@app.route("/first_mini2/showcomment", methods=["GET"])
def first_mini2_get():
    get_list = list(db.bongjin.find({}, {'_id': False}))
    return jsonify({'first_mini2':get_list})

@app.route('/first_mini2/deletecomment', methods=["POST"])
def first_mini2_delete():
    num_receive = request.form["num_give"]

    db.bongjin.delete_one({'num': int(num_receive)})
    return jsonify({'msg': '삭제 완료!'})







# 해빈님
@app.route("/first_mini3/writecomment", methods=["POST"])
def first_mini3_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']

    count_list = list(db.haebeen.find({}, {'_id': False}))
    count = len(count_list) + 1

    doc = {
        'name': name_receive,
        'comment': comment_receive,
        'num': count
    }

    db.haebeen.insert_one(doc)

    return jsonify({'msg':'저장 완료'})

@app.route("/first_mini3/showcomment", methods=["GET"])
def first_mini3_get():
    get_list = list(db.haebeen.find({}, {'_id': False}))
    return jsonify({'first_mini3':get_list})

@app.route('/first_mini3/deletecomment', methods=["POST"])
def first_mini3_delete():
    num_receive = request.form["num_give"]

    db.haebeen.delete_one({'num': int(num_receive)})
    return jsonify({'msg': '삭제 완료!'})




# 종수님
@app.route("/first_mini4/writecomment", methods=["POST"])
def first_mini4_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']

    count_list = list(db.jongsu.find({}, {'_id': False}))
    count = len(count_list) + 1

    doc = {
        'name': name_receive,
        'comment': comment_receive,
        'num': count
    }

    db.jongsu.insert_one(doc)

    return jsonify({'msg':'저장 완료'})

@app.route("/first_mini4/showcomment", methods=["GET"])
def first_mini4_get():
    get_list = list(db.jongsu.find({}, {'_id': False}))
    return jsonify({'first_mini4':get_list})

@app.route('/first_mini4/deletecomment', methods=["POST"])
def first_mini4_delete():
    num_receive = request.form["num_give"]

    db.jongsu.delete_one({'num': int(num_receive)})
    return jsonify({'msg': '삭제 완료!'})




# 예빈님
@app.route("/first_mini5/writecomment", methods=["POST"])
def first_mini5_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']

    count_list = list(db.yebin.find({}, {'_id': False}))
    count = len(count_list) + 1

    doc = {
        'name': name_receive,
        'comment': comment_receive,
        'num': count
    }

    db.yebin.insert_one(doc)

    return jsonify({'msg':'저장 완료'})

@app.route("/first_mini5/showcomment", methods=["GET"])
def first_mini5_get():
    get_list = list(db.yebin.find({}, {'_id': False}))
    return jsonify({'first_mini5':get_list})

@app.route('/first_mini5/deletecomment', methods=["post"])
def first_mini5_delete():
    num_receive = request.form["num_give"]

    db.yebin.delete_one({'num': int(num_receive)})
    return jsonify({'msg': '삭제 완료!'})

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)

