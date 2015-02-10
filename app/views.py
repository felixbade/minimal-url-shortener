from flask import request, Response, redirect, abort

from app import app
from app.urlshortener import URLShortener

urlshortener = URLShortener()

@app.route('/shorten', methods = ['POST'])
def shorten():
    url = request.form.get('link')
    if url is None:
        abort(400)
    else:
        short_id = urlshortener.shorten(url)
        return Response(short_id, mimetype='text/plain')

@app.route('/<short_id>')
def getURL(short_id):
    url = urlshortener.getURL(short_id)
    if url is None:
        abort(404)
    else:
        return redirect(url, code=301)
