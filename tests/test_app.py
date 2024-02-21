from lib.album_repository import Album, AlbumRepository

# Tests for your routes go here

# test that when get is called, it returns a list of all albums in the db
def test_get_albums(db_connection, web_client):
    db_connection.seed('seeds/music_library.sql')
    response = web_client.get('/albums')
    assert response.status_code == 200

    assert response.data.decode('utf-8') == """Album(1, Doolittle, 1989, 1)
Album(2, Surfer Rosa, 1988, 1)
Album(3, Waterloo, 1974, 2)
Album(4, Super Trouper, 1980, 2)
Album(5, Bossanova, 1990, 1)
Album(6, Lover, 2019, 3)
Album(7, Folklore, 2020, 3)
Album(8, I Put a Spell on You, 1965, 4)
Album(9, Baltimore, 1978, 4)
Album(10, Here Comes the Sun, 1971, 4)
Album(11, Fodder on My Wings, 1982, 4)
Album(12, Ring Ring, 1973, 2)"""
        
# test that when post is called with data to add to /albums, it is done so with no return. also test that after calling get, the new album is in the list
def test_post_albums(db_connection, web_client):
    db_connection.seed('seeds/music_library.sql')
    response = web_client.post('/albums', data={'title': 'Voyage', 'release_year': 2022, 'artist_id': 2})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == ''

    get_response = web_client.get('/albums')
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-8') == """Album(1, Doolittle, 1989, 1)
Album(2, Surfer Rosa, 1988, 1)
Album(3, Waterloo, 1974, 2)
Album(4, Super Trouper, 1980, 2)
Album(5, Bossanova, 1990, 1)
Album(6, Lover, 2019, 3)
Album(7, Folklore, 2020, 3)
Album(8, I Put a Spell on You, 1965, 4)
Album(9, Baltimore, 1978, 4)
Album(10, Here Comes the Sun, 1971, 4)
Album(11, Fodder on My Wings, 1982, 4)
Album(12, Ring Ring, 1973, 2)
Album(13, Voyage, 2022, 2)"""

# test that if the user tries to post an album with no data, we get a 400 error code
def test_post_empty_album(web_client):
    response = web_client.post('/albums')
    assert response.status_code == 400

# test that user can retrieve a list of albums when calling get
def test_get_artists(db_connection, web_client):
    db_connection.seed('seeds/music_library.sql')
    response = web_client.get('/artists')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Pixies, ABBA, Taylor Swift, Nina Simone'

# test user can add a new artist and list returns with the additional artist included
def test_post_artists(db_connection, web_client):
    db_connection.seed('seeds/music_library.sql')
    response = web_client.post('/artists', data={'name': 'Claude Debussy', 'genre': 'Classical'})
    assert response.status_code == 200

    get_response = web_client.get('/artists')
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-8') == 'Pixies, ABBA, Taylor Swift, Nina Simone, Claude Debussy'