from .req import *
import unittest
import requests


class SearchMovieTest(unittest.TestCase):

    #перевіряєм перед кожним тестом чи сервер відповідає
    def setUp(self):
        print('Test start '+ str(requests.get('http://www.omdbapi.com/').status_code))

    #перевіряєм чи знаходить фільм по точній назві
    def test_search_movie(self):
        self.assertEqual(search_movie('Knives Out')['Title'],'Knives Out')
        self.assertNotEqual(search_movie('Knives Out')['Title'],'name movie')

    def test_search_movie_bad_name(self):
        self.assertNotEqual(search_movie('Knives Out')['Title'], 'name movie')

    #перевіряєм чи знаходить N-у кількість результатів по якомусь слову
    def test_earch_movie_list(self):
        pages=int(search_movie_list('Knives')['totalResults'])
        self.assertGreaterEqual(pages,14)


    #перевіряємо чи пагінація норм працює чи намає однакових фільмів на різних сторінках
    def test_search_movie_pages(self):

        page1 = search_movie_pages('Knives')['Search'][1]
        page2 = search_movie_pages('Knives','2')['Search'][1]
        self.assertFalse(page1==page2)

    def tearDown(self):
        print('test finished')




if __name__ == '__main__':
    unittest.main()


