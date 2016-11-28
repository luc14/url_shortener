from flask import Flask, redirect, render_template, request, abort
import string_sequence, url_storage

storage = URLStorage()

@app.route('/')
def mainpage():
    return render_template('lu_shorten_url.html')

@app.route('/', methods=['POST'])
def to_short():
    '''return a short url based on the long_url that user typed in
    '''
    long_url = request.form['long_url']
    return render_template('long_to_short.html', short = storage.get_short(long_url))

@app.route('/<short_url_path>')
def to_long(short_url_path):
    '''redirect short url to long_url
    '''
    long_url = storage.get_long(short_url_path)
    if long_url is not None:
        return redirect(long_url)
    abort(404)

if __name__=='__main__':
    app.run(debug=False, use_reloader=True)