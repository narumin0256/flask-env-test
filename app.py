from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    # 環境変数を取得
    openai_api_key = os.getenv('OPENAI_API_KEY')
    return render_template('index.html', openai_api_key=openai_api_key)

if __name__ == '__main__':
    app.run()