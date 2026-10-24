"""Unit tests for the emotion detection application."""

import unittest

from EmotionDetection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Check dominant emotions for representative English statements."""

    def test_joy(self):
        self.assertEqual(
            emotion_detector("I am glad this happened")["dominant_emotion"], "joy"
        )

    def test_anger(self):
        self.assertEqual(
            emotion_detector("I am really mad about this")["dominant_emotion"],
            "anger",
        )

    def test_disgust(self):
        self.assertEqual(
            emotion_detector("I feel disgusted just hearing about this")["dominant_emotion"],
            "disgust",
        )

    def test_sadness(self):
        self.assertEqual(
            emotion_detector("I am so sad about this")["dominant_emotion"],
            "sadness",
        )

    def test_fear(self):
        self.assertEqual(
            emotion_detector("I am really afraid that this will happen")["dominant_emotion"],
            "fear",
        )

    def test_blank_text(self):
        result = emotion_detector("   ")
        self.assertIsNone(result["dominant_emotion"])
        self.assertTrue(
            all(result[emotion] is None for emotion in ("anger", "disgust", "fear", "joy", "sadness"))
        )


if __name__ == "__main__":
    unittest.main()
