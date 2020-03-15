from flask import Flask, request, jsonify

app = Flask(__name__)

# root
@app.route("/")
def index():
    """
    this is a root dir of my server
    :return: str
    """
    return "This is root!!!!<br><br> url: http:0.0.0.0:5000/users/_anytext_/ <br><br> url: http://0.0.0.0:5000/api/post_some_data/"

# GET
@app.route('/users/<user>/')
def hello_user(user):
    """
    this serves as a demo purpose
    :param user:
    :return: str
    """
    return "Hello %s!" % user

# POST
@app.route('/api/post_some_data/', methods=['POST'])
def get_text_prediction():
    
    json = request.get_json()
    if len(json['text']) == 0:
        return 'error'

    return 'you sent this : {}'.format(json['text'])
    
# running web app in local machine
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)