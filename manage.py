from flask import Flask
from config import dict_config
app = Flask(__name__)
app.config.from_object(dict_config['config'])
@app.route("/")
def index():
    return 'ok'
    print('are you ok')
    print('你好世界，你好人工智能')
if __name__ == '__main__':
    app.run()
