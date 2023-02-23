from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

import os

app = Flask(__name__)
# 上传文件保存路径（提前创建），文件最大大小（单位Byte）
app.config['UPLOAD_FOLDER'] = 'upload/'

@app.route('/upload')
def upload_file():
    return render_template('upload.html')


@app.route('/uploader', methods=['GET', 'POST'])
def uploader():
    if request.method == 'POST':
        f = request.files['file']
        print(request.files)
        # os.path.join合成路径
        f.save(os.path.join(
            app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
        return 'file uploaded successfully'

    else:
        return render_template('upload.html')


if __name__ == '__main__':
    app.run(debug=True)
