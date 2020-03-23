from flask import Flask, request, render_template, redirect, url_for
import authorEXP

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('form.html')


@app.route('/clearing')
def clearing():
    authorEXP.clear()
    return redirect(url_for('index'))


@app.route('/submit', methods=['POST'])
def submit():
    input_name = (str(format(request.form['author'])))
    keys = authorEXP.request_pubmed(input_name)
    if not keys:
        return render_template("error.html")
    googles = authorEXP.request_scholar(input_name)
    first = authorEXP.first_author
    solo = authorEXP.solo_author
    last = authorEXP.last_author
    img = authorEXP.mugshot(input_name)
    name = authorEXP.name
    IDList = len(authorEXP.IDList)
    if name.lower() != input_name.lower():
        return render_template("error.html")
    return render_template('form2.html', input_name=input_name, keys=keys, first=first, solo=solo,
                           last=last, img=img, name=name, googles=googles, IDList=IDList)


# input_name=input_name weil die html diese variable sonst nicht sieht


if __name__ == '__main__':
    app.run()
