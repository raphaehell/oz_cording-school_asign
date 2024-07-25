from flask import Flask,request, jsonify
from flask_wtf import CSRFProtect


app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['WTF_CSRF_ENABLED'] = False
csrf = CSRFProtect(app)

# #(1) 잔체 게시물을 불러오는  API
# @app.route('/api/v1/feeds', methods=['GET'])
# def show_all_feeds():
#    # return jsonify({'result':'success', 'data': {"feed1":"data", "feed2":"data2"}})
# 	return {'result':'success', 'data': {"feed1":"data", "feed2":"data2"}}

# #(2) 특정 계시글을 불러오눈 API
# @app.route('/api/v1/feeds/<int:feed_id>', methods=['GET'])
# def show_one_feed(feed_id):
#    print(feed_id)
#    return jsonify({'result':'success', 'data': {"feed1":"data"}})

# # POST
# #1 게시글을 작성하는  API
# @app.route('/api/v1/feeds', methods=['POST'])
# def create_one_feed():
#     name = request.form['name']
#     age = request.form['age']
 
#     print(name, age)
    
#     return jsonify({'result':'success'})

@app.route("/api/v1/feeds", methods=["GET"])
def show_all_feeds():
    data = {'result' : 'success', 'data' : {'feed1' : 'data1', 'feed2' : 'data2', 'feed3' : 'data3'}}

    return jsonify(data)

@app.route("/api/v1/feeds/<int:feed_id>", methods=["GET"])
def show_one_feed(feed_id):
    print(feed_id)
    data = {'result' : 'success', 'data' : {'feed1' : 'data1', 'feed2' : 'data2'}}

    return data

@app.route("/api/v1/feeds", methods=["POST"])
def post_data():
    name = request.form['name']
    age = request.form['age']
    print(name, age)

    return jsonify({'result' : 'success'})

datas = [{"name": "item1", "price": 10}]



@app.route('/api/v1/datas',methods=['Get'])
def get_datas():
    return {'datas':datas}

@app.route('/api/v1/datas',methods=['Post'])
def create_data():
    new_data = {'items': request_data.get("items", [])}
    request_data = request.get_json()
    datas.append(new_data)


    return new_data, 201

if __name__ == '__main__':
    app.run(debug=True)