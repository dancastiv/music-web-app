from lib.album_repository import AlbumRepository
from lib.album import Album

# test we get a list of Album objects when calling AlbumRepository#all
def test_get_all_albums(db_connection):
    db_connection.seed('seeds/music_library.sql')
    repository = AlbumRepository(db_connection)
    albums = repository.all()
    assert albums == [
        Album(1, 'Doolittle', 1989, 1),
        Album(2, 'Surfer Rosa', 1988, 1),
        Album(3, 'Waterloo', 1974, 2),
        Album(4, 'Super Trouper', 1980, 2),
        Album(5, 'Bossanova', 1990, 1),
        Album(6, 'Lover', 2019, 3),
        Album(7, 'Folklore', 2020, 3),
        Album(8, 'I Put a Spell on You', 1965, 4),
        Album(9, 'Baltimore', 1978, 4),
        Album(10, 'Here Comes the Sun', 1971, 4),
        Album(11, 'Fodder on My Wings', 1982, 4),
        Album(12, 'Ring Ring', 1973, 2)
    ]

# test that we get a single Album object by id when calling AlbumRepository#find
def test_get_single_album(db_connection):
    db_connection.seed('seeds/music_library.sql')
    repository = AlbumRepository(db_connection)
    album = repository.find(7)
    assert album == Album(7, 'Folklore', 2020, 3)

# test that we can add new record to datbase when calling #create
def test_create(db_connection):
    db_connection.seed('seeds/music_library.sql')
    repository = AlbumRepository(db_connection)
    repository.create(Album(None, 'Midnights', 2022, 3))
    assert repository.all() == [
        Album(1, 'Doolittle', 1989, 1),
        Album(2, 'Surfer Rosa', 1988, 1),
        Album(3, 'Waterloo', 1974, 2),
        Album(4, 'Super Trouper', 1980, 2),
        Album(5, 'Bossanova', 1990, 1),
        Album(6, 'Lover', 2019, 3),
        Album(7, 'Folklore', 2020, 3),
        Album(8, 'I Put a Spell on You', 1965, 4),
        Album(9, 'Baltimore', 1978, 4),
        Album(10, 'Here Comes the Sun', 1971, 4),
        Album(11, 'Fodder on My Wings', 1982, 4),
        Album(12, 'Ring Ring', 1973, 2),
        Album(13, 'Midnights', 2022, 3)
    ]

# test that we can delete record from database given a specifc id
def test_delete(db_connection):
    db_connection.seed('seeds/music_library.sql')
    repository = AlbumRepository(db_connection)
    repository.delete(11)
    assert repository.all() == [
        Album(1, 'Doolittle', 1989, 1),
        Album(2, 'Surfer Rosa', 1988, 1),
        Album(3, 'Waterloo', 1974, 2),
        Album(4, 'Super Trouper', 1980, 2),
        Album(5, 'Bossanova', 1990, 1),
        Album(6, 'Lover', 2019, 3),
        Album(7, 'Folklore', 2020, 3),
        Album(8, 'I Put a Spell on You', 1965, 4),
        Album(9, 'Baltimore', 1978, 4),
        Album(10, 'Here Comes the Sun', 1971, 4),
        Album(12, 'Ring Ring', 1973, 2)
    ]