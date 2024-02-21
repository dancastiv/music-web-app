import os
from flask import Flask, request
from lib.database_connection import get_flask_database_connection
from lib.album_repository import AlbumRepository, Album
from lib.artist_repository import ArtistRepository, Artist

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==
@app.route('/albums', methods=['POST'])
def post_albums():
    connection = get_flask_database_connection(app)
    album_repository = AlbumRepository(connection)
    album = Album(None, request.form['title'], request.form['release_year'], request.form['artist_id'])
    album_repository.create(album)
    return ''

@app.route('/albums', methods=['GET'])
def get_albums():
    connection = get_flask_database_connection(app)
    album_repository = AlbumRepository(connection)
    all_albums = '\n'.join(f'{album}' for album in album_repository.all())
    return all_albums

@app.route('/artists', methods=['GET'])
def get_artists():
    connection = get_flask_database_connection(app)
    artist_repository = ArtistRepository(connection)
    all_artists = ', '.join(str(artist.name) for artist in artist_repository.all())
    return all_artists

@app.route('/artists', methods=['POST'])
def post_artists():
    connection = get_flask_database_connection(app)
    artist_repository = ArtistRepository(connection)
    artist = Artist(None, request.form['name'], request.form['genre'])
    artist_repository.create(artist)
    return ''

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))

