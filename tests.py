import pytest

from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    @pytest.mark.parametrize('new_book', ['Гарри Поттер', '11/22/63'])
    def test_add_new_book_adding_in_dict(self, collector, new_book):
        collector.add_new_book(new_book)

        assert new_book in collector.get_books_genre()

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

    def test_get_book_genre_return_genre_by_name(self, collector):
        collector.add_new_book('Звездные войны')
        collector.set_book_genre('Звездные войны', 'Фантастика')

        assert collector.get_book_genre('Звездные войны') == 'Фантастика'

    def test_get_books_with_specific_genre_get_books_genre_comedy(self, collector):
        collector.books_genre = {'Джентельмены': 'Комедии', 'Остров проклятых': 'Детективы',
                                 'Час пик': 'Комедии',
                                 'Тачки': 'Мультфильмы'}
        assert len(collector.get_books_with_specific_genre('Комедии')) == 2

    def test_get_books_genre_correct(self, collector):
        collector.add_new_book('Звездные войны')
        collector.set_book_genre('Звездные войны', 'Фантастика')

        assert collector.get_books_genre() == collector.books_genre

    def test_get_books_for_children_get_children_books(self, collector):
        collector.books_genre = {'Оно': 'Ужасы', 'Остров проклятых': 'Детективы',
                                 'Час пик': 'Комедии',
                                 'Тачки': 'Мультфильмы'}
        assert len(collector.get_books_for_children()) == 2

    def test_add_book_in_favorites_book_in_favorites(self, collector):
        books = ['Кубок огня', 'Орден Феникса', 'Принц-полукровка']
        for name in books:
            collector.add_new_book(name)
        collector.add_book_in_favorites('Кубок огня')

        assert 'Кубок огня' in collector.favorites

    def test_delete_book_from_favorites_book_not_in_favourites(self, collector):
        books = ['Философский камень', 'Тайная комната', 'Узник Азкабана']
        for name in books:
            collector.add_book_in_favorites(name)
        collector.delete_book_from_favorites('Узник Азкабана')

        assert 'Узник Азкабана' not in collector.favorites

    def test_get_list_of_favorites_books_return_books_favorites(self, collector):
        books = ['Философский камень', 'Тайная комната', 'Узник Азкабана']
        for name in books:
            collector.add_new_book(name)
            collector.add_book_in_favorites(name)

        assert collector.get_list_of_favorites_books()
