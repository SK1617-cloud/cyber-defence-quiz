import unittest
from main import Question, Quiz


class TestQuestion(unittest.TestCase):

    def test_correct_answer(self):
        q = Question("Test?", ["A", "B", "C", "D"], "A")
        self.assertTrue(q.is_correct("A"))

    def test_wrong_answer(self):
        q = Question("Test?", ["A", "B", "C", "D"], "A")
        self.assertFalse(q.is_correct("B"))


class TestQuiz(unittest.TestCase):

    def setUp(self):
        self.questions = [
            Question("Q1", ["A", "B", "C", "D"], "A"),
            Question("Q2", ["A", "B", "C", "D"], "B")
        ]
        self.quiz = Quiz(self.questions)

    def test_score_increases_on_correct(self):
        self.quiz.submit_answer("A")
        self.assertEqual(self.quiz.score, 1)

    def test_score_not_increase_on_wrong(self):
        self.quiz.submit_answer("C")
        self.assertEqual(self.quiz.score, 0)

    def test_question_index_increases(self):
        self.quiz.submit_answer("A")
        self.assertEqual(self.quiz.current, 1)

    def test_finished(self):
        self.quiz.submit_answer("A")
        self.quiz.submit_answer("B")
        self.assertTrue(self.quiz.finished())


if __name__ == "__main__":
    unittest.main()