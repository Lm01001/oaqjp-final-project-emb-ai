import unittest
from EmotionDetection import emotion_detector

class TestEmotionDetector(unittest.TestCase):

    def test_joy(self):
        result = emotion_detector("I am so happy I am doing this.")
        self.assertEqual(result['dominant_emotion'], 'joy')

    def test_anger(self):
        result = emotion_detector("I hate working long hours.")
        self.assertEqual(result['dominant_emotion'], 'anger')

    def test_disgust(self):
        result = emotion_detector("This food looks absolutely disgusting.")
        self.assertEqual(result['dominant_emotion'], 'disgust')

    def test_sadness(self):
        result = emotion_detector("I feel very lonely today.")
        self.assertEqual(result['dominant_emotion'], 'sadness')

    def test_fear(self):
        result = emotion_detector("I'm terrified of heights.")
        self.assertEqual(result['dominant_emotion'], 'fear')

if __name__ == '__main__':
    unittest.main()
