from flask import Flask, request, render_template, url_for
import pandas as pd

app = Flask(__name__)

# 读取Excel数据
excel_file = 'all.xls'
df = pd.read_excel(excel_file)


def query_data(keyword):
    # 在内存中进行搜索
    results = df[df['题名'].str.contains(keyword, case=False)]
    return results.to_dict(orient='records')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search', methods=['POST'])
def search():
    keyword = request.form['keyword']
    results = query_data(keyword)
    return render_template('results.html', results=results)


if __name__ == '__main__':
    app.run(debug=True)
