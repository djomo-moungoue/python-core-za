import unittest
from PythonCore.core_python_with_mosh.blog import tagcloud
# from ...tagcloud import TagCloud


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)  # add assertion here

    def test_if_created_tagcloud_is_empty(self):
        tag_cloud = tagcloud.TagCloud()
        first = tag_cloud.is_empty()
        second = True
        self.assertEqual(first, second)

    def test_if_the_tag_Python_is_successfully_inserted_in_the_tagcloud(self):
        tag_cloud = tagcloud.TagCloud()
        tag_cloud.add('Python')
        first = str(tag_cloud)
        second = "#python: 1 "
        self.assertEqual(first, second)

    def test_if_the_tag_Python_is_successfully_incremented_to_2_in_the_tagcloud(self):
        tag_cloud = tagcloud.TagCloud()
        tag_cloud.add('Python')
        tag_cloud.add('PYTHON')
        first = str(tag_cloud)
        second = "#python: 2 "
        self.assertEqual(first, second)

    def test_if_the_tags_Django_and_AWS_are_successfully_inserted_in_the_tagcloud(self):
        tag_cloud = tagcloud.TagCloud()
        tag_cloud.add('Python')
        tag_cloud.add('PYTHON')
        tag_cloud.add('Django')
        tag_cloud.add('DjAngo')
        tag_cloud.add('django')
        tag_cloud.add('AWS')
        first = str(tag_cloud)
        second = "#python: 2 #django: 3 #aws: 1 "
        self.assertEqual(first, second)

    def test_if_the_tags_Django_value_is_successfully_decremented_to_2_in_the_tagcloud(self):
        tag_cloud = tagcloud.TagCloud()
        tag_cloud.add('Python')
        tag_cloud.add('PYTHON')
        tag_cloud.add('Django')
        tag_cloud.add('Django')
        tag_cloud.add('Django')
        tag_cloud.add('AWS')
        tag_cloud.remove('Django')
        first = str(tag_cloud)
        second = "#python: 2 #django: 2 #aws: 1 "
        self.assertEqual(first, second)

    def test_if_the_removal_of_non_the_existing_tag_Bango_is_handled_properly(self):
        tag_cloud = tagcloud.TagCloud()
        tag_cloud.add('Python')
        tag_cloud.add('PYTHON')
        tag_cloud.add('Django')
        tag_cloud.add('Django')
        tag_cloud.add('Django')
        tag_cloud.add('AWS')
        first = tag_cloud.remove('Bango')
        second = None
        self.assertEqual(first, second)

    def test_if_the_removal_from_an_empty_tagcloud_is_handled_properly(self):
        tag_cloud = tagcloud.TagCloud()
        first = tag_cloud.remove('Bango')
        second = None
        self.assertEqual(first, second)


if __name__ == '__main__':
#    for x in dir(tagcloud):
#        y = str(x)
#        print(tagcloud.__name__)
    unittest.main()
