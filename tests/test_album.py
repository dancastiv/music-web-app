from lib.album import Album

# test album constructs
def test_album_constructs():
    album = Album(1, 'Test Title', 1900, 1)
    assert album.id == 1
    assert album.title == 'Test Title'
    assert album.release_year == 1900
    assert album.artist_id == 1

# test formatting to string
def test_albums_format():
    album = Album(1, 'Test Title', 1900, 1)
    assert str(album) == "Album(1, Test Title, 1900, 1)"

# test comparing two identical albums and having them be equal
def test_albums_are_equal():
    album1 = Album(1, 'Test Title', 1900, 1)
    album2 = Album(1, 'Test Title', 1900, 1)
    assert album1 == album2