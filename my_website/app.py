from flask import Flask, render_template, send_file

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download')
def download_file():
    file_path = 'C:\\Users\\shubh\\OneDrive\\Desktop\\My_Resume.pdf'
    return send_file(file_path, as_attachment=True)

@app.route('/About')
def about():
    return render_template('about_shubhanshu.html')

if __name__ == '__main__':
    app.run(debug=True)
