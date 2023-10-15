import os
import unittest

from data_processor import DataProcessor

PLAY_DATA_PATH = "./play_data.txt"


class TestDataProcessor(unittest.TestCase):
    def setUp(self) -> None:
        file_path = PLAY_DATA_PATH

        self.data_processor = DataProcessor(file_path=file_path)

        self.data_processor.write_data("Cedric", "aaaaa", "Easy", 3, "Won")
        self.data_processor.write_data("Cedric", "aaaaa", "Easy", 4, "Won")
        self.data_processor.write_data("Cedric", "aaaaa", "Easy", 4, "Won")

        self.data_processor.write_data("Anna", "aaaaa", "Easy", 9, "Won")
        self.data_processor.write_data("Anna", "aaaaa", "Easy", 2, "Won")

        self.data_processor.write_data("Julie", "aaaaa", "Easy", 2, "Loss")
        self.data_processor.write_data("Julie", "aaaaa", "Easy", 5, "Loss")
        self.data_processor.write_data("Julie", "aaaaa", "Easy", 3, "Won")
        self.data_processor.write_data("Julie", "aaaaa", "Easy", 8, "Won")

        self.data_processor.read_data()

    def test_users(self):
        self.assertIn("Cedric", self.data_processor.get_users())
        self.assertIn("Anna", self.data_processor.get_users())
        self.assertIn("Julie", self.data_processor.get_users())

        self.assertEqual(len(self.data_processor.get_users()), 3)

        self.clear_data()

    def test_avg_attempts(self):
        self.assertEqual(self.data_processor.get_user_avg_attempts("Cedric"), 3.67)
        self.assertEqual(self.data_processor.get_user_avg_attempts("Anna"), 5.5)
        self.assertEqual(self.data_processor.get_user_avg_attempts("Julie"), 4.5)

        self.clear_data()

    @staticmethod
    def clear_data():
        try:
            os.remove(PLAY_DATA_PATH)
            print(f"{PLAY_DATA_PATH} has been successfully deleted.")
        except FileNotFoundError:
            pass
        except Exception as e:
            print(f"An error occurred while trying to delete {PLAY_DATA_PATH}: {str(e)}")


if __name__ == "__main__":
    unittest.main()


