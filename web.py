import os

from flask import Flask, request, render_template, send_file

from synth import synthesize

app = Flask(__name__)


@app.route('/')
def my_form():
    return render_template('form.html')


@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    path_to_file = synthesize(text)
    return send_file(
         path_to_file,
         mimetype="audio/wav",
         as_attachment=True,
         attachment_filename=os.path.basename(path_to_file)
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
