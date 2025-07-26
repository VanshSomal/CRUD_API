from flask import Flask,jsonify,request
app=Flask(__name__)

#simulated Database
users=[]

#Home route

@app.route('/')
def home():
    return "Welcome to the Python CRUD API"

#CREATE A NEW USER(POST)

@app.route('/users',methods=['POST'])
def create_user():
    data=request.get_json()
    user={
        'id':len(users) + 1,
        'name':data['name'],
        'email':data['email']
    }
    users.append(user)
    return jsonify({'message':'User created!','user':user}),201


# READ ALL USERS (GET)

@app.route('/users',methods=['GET'])
def get_users():
    return jsonify(users)

# READ SINGLE USER BY ID(GET)

@app.route('/users/<int:user_id>',methods=['GET'])
def get_user(user_id):
    for user in users:
        if user['id']==user_id:
            return jsonify(user)
    return jsonify({'message':'User not found'}),404



#UPDATE USER BY ID(PUT)

@app.route('/users/<int:user_id>',methods=['PUT'])
def update_user(user_id):
    data=request.get_json()
    for user in users:
        if user['id']==user_id:
            user['name']=data.get('name',user['name'])
            user['email']=data.get('email',user['email'])
            return jsonify({'message':'User updated','user':user})
    return jsonify({'message':'User not found'}),404


# DELETE USER BY ID(DELETE)


@app.route('/users/<int:user_id>',methods=['DELETE'])
def delete_user(user_id):
    for user in users:
        if user['id']==user_id:
            users.remove(user)
            return jsonify({'message':'User deleted'})
    return jsonify({'message':'User not found'}),404


#RUN YOUR APP

if __name__=='__main__':
    app.run(debug=True)