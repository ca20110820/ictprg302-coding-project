from typing import List


class DataProcessor:
    def __init__(self, file_path: str = r"./game_data.txt"):
        self.file_path = file_path
        self.data = None

    def write_data(self, user_name, target_word, difficulty_level, num_attempts, game_result) -> None:
        with open(self.file_path, 'a') as file:
            text = f"{user_name},{target_word},{difficulty_level},{num_attempts},{game_result}\n"
            file.write(text)

    def read_data(self) -> List[list]:

        out_list = []

        with open(self.file_path, 'r') as file:
            for line in file:
                line = line.strip()
                line = line.split(',')
                self._parse_data(line)
                out_list.append(line)

        self.data = out_list  # Naive Caching

        return out_list

    @staticmethod
    def _parse_data(inp_list: list) -> None:
        inp_list[3] = int(inp_list[3])

    def get_users(self) -> List[str]:
        users = set([ls[0] for ls in self.data])
        return sorted(list(users))

    def get_user_avg_attempts(self, user_name: str) -> int | None:
        game_num_attempts = [ls[3] for ls in self.data if ls[0] == user_name]
        return sum(game_num_attempts)/len(game_num_attempts) if len(game_num_attempts) != 0 else None


if __name__ == "__main__":
    dp = DataProcessor()
    dp.write_data("Cedric", "aaaaa", "Easy", 4, "Won")
    dp.write_data("Cedric", "bbbbb", "Easy", 10, "Loss")
    dp.write_data("Anna", "asdde", "Normal", 6, "Loss")
    dp.write_data("Zella", "dsedf", "Normal", 3, "Won")

    dp.read_data()
    print(dp.data)
    print(dp.get_users())
