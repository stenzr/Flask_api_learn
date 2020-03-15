from flask import Flask, request, jsonify

app = Flask(__name__)

# root
@app.route("/")
def index():
    """
    this is a root dir of my server
    :return: str
    """
    return '''
             This is root!!!!<br><br> url: https://simple-flask-api1.herokuapp.com/(enter any text here)/
             <br><br> url: https://simple-flask-api1.herokuapp.com/post_some_data/                post a json {'text': 'something'} 
             <br><br> url: https://simple-flask-api1.herokuapp.com/users/(enter any text here)/    
             <br><br> url: https://simple-flask-api1.herokuapp.com/post_some_data_to_get_json/   
             <br><br> url: https://simple-flask-api1.herokuapp.com/JSON/(enter any text here)/
    '''



# GET
@app.route('/<user>/')
def hello_user(user):
    """
    this serves as a demo purpose
    :param user:
    :return: str
    """
    return "Hello %s!" % user

# GET
@app.route('/users/<user>/')
def hello_my_user(user):
    """
    this serves as a demo purpPOSTose
    :param user:
    :return: str
    """
    return "Hello  %s!" % user

# GET
@app.route('/JSON/<user>/')
def hello_my_JSON_user(user):
    """
    this serves as a demo purpPOSTose
    :param user:
    :return: str
    """
    return jsonify({'text' : '{}'.format(user)})


# POST
@app.route('/post_some_data/', methods=['POST'])
def get_text_prediction():
    
    json = request.get_json()
    if len(json['text']) == 0:
        return 'error'


    return 'you sent this : {}'.format(json['text'])
    #return "you sent this : %s" % json['text']

# POST
@app.route('/post_some_data_to_get_json/', methods=['POST'])
def get_json_as_response():
    
    json = request.get_json()
    if len(json['text']) == 0:
        return 'error'

    return jsonify({'you sent this' : '{}'.format(json['text'])})
    
    
# running web app in local machine
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)