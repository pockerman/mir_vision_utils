import unittest
from pathlib import Path
from visionutils.image_utils import get_img_files
from visionutils.image_enums import ImageFileEnumType


class TestImageUtils(unittest.TestCase):

    def test_get_img_files(self):
        files = get_img_files(img_dir=Path('/imutils/test_data'),
                              img_formats=(ImageFileEnumType.PNG,
                                           ImageFileEnumType.JPG))

        self.assertEqual(2, len(files))


if __name__ == '__main__':
    unittest.main()
