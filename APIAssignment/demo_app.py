from flask import Flask, jsonify, request, json

app = Flask(__name__)

@app.route("/")
def index():
    return "This is API Assignment."

# 1. Create an API that returns title, body of post based on post id.

@app.route("/posts", methods=['GET'])
def get_posts():
    print(request.url)

    try:
        id = int(request.args.get('id'))
        if id < 1:
            raise ValueError
    except ValueError:
        return jsonify({'messaage':'Invalid id'})
    except Exception as e:
        return jsonify({'message': e.args})
    else:
        with open('posts.json', 'r') as f:
            data = json.load(f)
            try:
                for i in data['posts']:
                    if i['id'] == id:
                        return jsonify({'title': i['title'], 'body': i['body']})
            except Exception as e:
                return jsonify({'message': e.args})
            else:
                return jsonify({'message':'No posts found with id ={}'.format(id)})

# 2.Create an API that increase reactions by 10 and displays updated results of provided post id.

@app.route('/reaction', methods=['PUT'])
def reaction():
    print(request.url)
    try:
        id = int(request.args.get('id'))
        if id < 1:
            raise ValueError
    except ValueError:
        return jsonify({'message': 'Invalid id! has to be an +ve integer'})
    except Exception as e:
        return jsonify({'message': e.args})
    else:
        with open('posts.json', 'r+') as f:
            data = json.load(f)
            try:
                for i in data['posts']:
                    if i['id'] == id:
                        i['reactions'] = i['reactions'] + 10
                        f.seek(0)
                        json.dump(data, f, indent=4)
                        f.truncate()
                        return jsonify({'id': i['id'], 'reactions': i['reactions']})
            except Exception as e:
                return jsonify({'message': e.args})
            else:
                return jsonify({'message': 'No comment found! with  id = {}'.format(id)})


# 3.Create an API that insert new post record and display response message along with updated data.

@app.route("/insert", methods = ['POST'])
def insert_post():
    print(request.url)

    try:
        id = int(request.args.get('id'))
        title = request.args.get('title')
        body = request.args.get('body')
        user_id= int(request.args.get('user_id'))
        tags= request.args.get('tags')
        reactions = request.args.get('reactions')

        if id < 1 or user_id < 1:
            raise ValueError
    except ValueError:
            return jsonify({'message': 'Invalid id! , has to be an +ve integer'})

    else:
        with open('posts.json','r+') as f:
            data = json.load(f)
            try:
                for i in data['posts']:
                    if i['id'] == id:
                        return jsonify({'message': 'post already exist! with id = {}'.format(id)})

                new_posts = {'id': id, 'title': title, 'body':body, 'user_id':user_id, 'tags':tags, 'reactions':reactions}

                data['posts'].append(new_posts)
                f.seek(0)
                json.dump(data, f, indent =4)
                f.truncate()
                return jsonify({'message': 'post inserted! with id = {}'.format(id)})
            except Exception as e:
                return jsonify({'message': e.args})


# 4. Create an APi that delete posts and display response message based on provided post id.

@app.route('/delete', methods=['DELETE'])
def delete_posts():
    print(request.url)

    try:
        id = int(request.args.get('id'))
        if id < 1:
            raise ValueError
    except ValueError:
        return jsonify({'message': 'Invalid id! has to be an +ve integer'})
    except Exception as e:
        return jsonify({'message': e.args})
    else:  # if no exception
        with open('posts.json', 'r+') as f:
            data = json.load(f)
            try:

                for i in data['posts']:
                    if i['id'] == id:

                        data['posts'].remove(i)

                        f.seek(0)

                        json.dump(data, f, indent=4)
                        f.truncate()
                        return jsonify({'message': 'post deleted! with id = {}'.format(id)})
            except Exception as e:
                return jsonify({'message': e.args})
            else:
                return jsonify({'message': 'No comment found! with  id = {}'.format(id)})

# 5. Create an API to return post id, title, body and status in json format that have ‘history’ as tag.

@app.route('/history', methods=['GET'])
def get_history():
    print(request.url)

    with open('posts.json', 'r') as f:
        data = json.load(f)
        try:
            for i in data['posts']:
                # if i['history'] == 'tags':
                if "history" in i["tags"]:
                    return jsonify({'id': i['id'], 'title': i['title'], 'body': i['body']})
        except Exception as e:
            return jsonify({'message': e.args})









