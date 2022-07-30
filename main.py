from typing import List
# TODO take an BF input
# TODO translate from BD to ASCII
# TODO display the result
# TODO create unittests for this project
# TODO don't forget to use typing correctly
# TODO write PEP-8 correct code
# TODO write it all in a defensive way


class Main:
    """The main class and a place where stuff happens.

    There isn't much more to say. It's just my own attempt to write a Brain F*ck
        interpreter.
    I know that I shouldn't do this in one file, but that's not what I wanted to train
        in here.
    """
    _char_array: List[str] = []
    _char_array_max_length: int = 30_000
    _char_array_pointer: int = 0
    _code_in: str = ""                       # For storing input
    _code_out: str = ""                      # For storing the result

    def __init__(self, max_length: int = 30_000) -> None:
        self.char_array_max_length = max_length
        self.char_array = ["" for _ in range(self.char_array_max_length)]

    def __call__(self, *args, **kwargs) -> None:
        print("It kind of works")
        raise NotImplementedError("Work in progress...")

    @property
    def char_array(self) -> List[str]:
        return self._char_array

    @char_array.setter
    def char_array(self, char_array: List[str]) -> None:
        if not isinstance(char_array, list):
            raise TypeError(
                "Char array must be a list."
            )
        elif not all([isinstance(_, str) for _ in char_array]):
            raise TypeError(
                "In char array, all values must be a string."
            )
        elif not all([len(_) == 1 for _ in char_array]):
            raise ValueError(
                "In char array, all strings must be of 1 length."
            )
        elif len(char_array) != self.char_array_max_length:
            raise ValueError(
                f"Char array must be the exact length of {self.char_array_max_length}."
            )
        else:
            self._char_array = char_array

    @property
    def char_array_max_length(self) -> int:
        return self._char_array_max_length

    @char_array_max_length.setter
    def char_array_max_length(self, length: int) -> None:
        if not isinstance(length, int):
            raise TypeError(
                "Char array max length must be an integer type."
            )
        elif length < 1:
            raise ValueError(
                "Char array max length must be of at least 1 length."
            )
        else:
            self._char_array_max_length = length


if __name__ == "__main__":
    Main()()
