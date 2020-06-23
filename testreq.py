from .req import search_movie
import unittest

class SearchMovieTest(unittest.TestCase):

    def test_search_movie(self):
        self.assertEqual(search_movie('Knives Out'),'Knives Out')
        self.assertNotEqual(search_movie('Knives Out'),'name movie')



if __name__ == '__main__':
    unittest.main()