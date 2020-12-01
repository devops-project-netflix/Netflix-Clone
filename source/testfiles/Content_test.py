import unittest
from models.content import ContentModel
from models.content import SAMPLE_CONTENT_OBJECT, NUM_KEYS


# api = Namespace('Categories', description='all movies endpoints')
# parser = api.parser()
# parser.add_argument('name', type=str, help='category name', location='param')


class TestContentMethods(unittest.TestCase):

    def test_Content_Get(self):
        m = ContentModel().get({})
        self.assertGreaterEqual(m.count(), NUM_KEYS)

    def test_Content_Post(self):
        inserted = ContentModel().insert(SAMPLE_CONTENT_OBJECT)
        fetch_inserted = ContentModel().getById(inserted.inserted_id)
        self.assertEqual(SAMPLE_CONTENT_OBJECT['content'],
         fetch_inserted['content'])

    def test_Categories_Delete(self):
        inserted = ContentModel().insert(SAMPLE_CONTENT_OBJECT)
        inserted_id = inserted.inserted_id
        inserted = ContentModel().delete(inserted_id)
        deleted = ContentModel().getById(inserted_id)
        self.assertIsNone(deleted)
