from typing import List, Dict
import random

import pkg_resources


class DataProcessor:
    def __init__(self, file_path: str = pkg_resources.resource_filename('wordle', 'data/game_data.txt')):
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

    def get_user_avg_attempts(self, user_name: str) -> float | None:
        game_num_attempts = [ls[3] for ls in self.data if ls[0] == user_name]
        return round(sum(game_num_attempts)/len(game_num_attempts), 2) if len(game_num_attempts) != 0 else None

    def get_users_avg_attempts(self) -> Dict[str, float]:

        out_dict = {}

        for user in self.get_users():
            out_dict[user] = self.get_user_avg_attempts(user)

        return dict(sorted(out_dict.items(), key=lambda item: item[1]))
