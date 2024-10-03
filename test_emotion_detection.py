import unittest
from EmotionDetection import emotion_detector as emot_det
class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detector(self):
        self.assertEqual(emot_det("I am glad this happened")['dominant_emotion'], "joy")
        self.assertEqual(emot_det("I am really mad about this")['dominant_emotion'], "anger")
        self.assertEqual(emot_det("I feel disgusted just hearing about this")['dominant_emotion'], "disgust")
        self.assertEqual(emot_det("I am so sad about this")['dominant_emotion'], "sadness")
        self.assertEqual(emot_det("I am really afraid that this will happen")['dominant_emotion'], "fear")

#if "__name__" == "__main__":
unittest.main()