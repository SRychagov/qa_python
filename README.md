# Создание объекта вынесено в фикстурой в файл conftest.py

1.Тест с параметризацией проверяет добавление новых книг в словарь.

    @pytest.mark.parametrize('new_book', ['Гарри Поттер', '11/22/63'])
    def test_add_new_book_adding_in_dict(self, collector, new_book):
        collector.add_new_book(new_book)

        assert new_book in collector.get_books_genre()
2.Тест с параметризацией добавляет новые книги с жанрами и проверяет задавание книгам жанра.

    @pytest.mark.parametrize(
        'name_book, genre_book',
        [
            ['Звёздные Войны', 'Фантастика'],
            ['Шерлок Холмс', 'Детективы']
        ]
    )
    def test_set_book_genre_name_book_match_genre(self, collector, name_book, genre_book):
        collector.add_new_book(name_book)
        collector.set_book_genre(name_book, genre_book)

        assert collector.books_genre[name_book] == genre_book
3.Тест проверяет получение жанра по названию книги.

    def test_get_book_genre_return_genre_by_name(self, collector):
        collector.add_new_book('Звездные войны')
        collector.set_book_genre('Звездные войны', 'Фантастика')

        assert collector.get_book_genre('Звездные войны') == 'Фантастика'
4.Тест проверяет, что получен список книг с определенным жанром(Комедии). 

    def test_get_books_with_specific_genre_get_books_genre_comedy(self, collector):
        collector.books_genre = {'Джентельмены': 'Комедии', 'Остров проклятых': 'Детективы',
                                 'Час пик': 'Комедии',
                                 'Тачки': 'Мультфильмы'}
        assert len(collector.get_books_with_specific_genre('Комедии')) == 2
5.Тест проверяет, что словарь получен корректно.

    def test_get_books_genre_correct(self, collector):
        collector.add_new_book('Звездные войны')
        collector.set_book_genre('Звездные войны', 'Фантастика')

        assert collector.get_books_genre() == collector.books_genre
6.Тест проверяет, что получены книги подходящие детям.

    def test_get_books_for_children_get_children_books(self, collector):
        collector.books_genre = {'Оно': 'Ужасы', 'Остров проклятых': 'Детективы',
                                 'Час пик': 'Комедии',
                                 'Тачки': 'Мультфильмы'}
        assert len(collector.get_books_for_children()) == 2
7.Тест проверяет, что книга добавленная в избранное есть в избранном.

    def test_add_book_in_favorites_book_in_favorites(self, collector):
        books = ['Кубок огня', 'Орден Феникса', 'Принц-полукровка']
        for name in books:
            collector.add_new_book(name)
        collector.add_book_in_favorites('Кубок огня')

        assert 'Кубок огня' in collector.favorites
8.Тест проверяет удаление книги из избранного.

    def test_delete_book_from_favorites_book_not_in_favourites(self, collector):
        books = ['Философский камень', 'Тайная комната', 'Узник Азкабана']
        for name in books:
            collector.add_book_in_favorites(name)
        collector.delete_book_from_favorites('Узник Азкабана')

        assert 'Узник Азкабана' not in collector.favorites
9.Тест проверяет метод который возвращает список избранных книг.

    def test_get_list_of_favorites_books_return_books_favorites(self, collector):
        books = ['Философский камень', 'Тайная комната', 'Узник Азкабана']
        for name in books:
            collector.add_new_book(name)
            collector.add_book_in_favorites(name)

        assert collector.get_list_of_favorites_books()
