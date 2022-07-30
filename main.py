from typing import List
from stack import Stack
# TODO take an BF input
# TODO translate from BD to ASCII
# TODO display the result
# TODO create unittests for this project
# TODO don't forget to use typing correctly
# TODO write PEP-8 correct code
# TODO write it all in a defensive way
# TODO Add feature to use it from command line with instant reply


class Main:
    """The main class and a place where stuff happens.

    There isn't much more to say. It's just my own attempt to write a Brain F*ck
        interpreter.
    I know that I shouldn't do this in one file, but that's not what I wanted to train
        in here.
    """
    _acceptable_chars: str = "<>[]-+,."
    _char_array: List[int] = []
    _char_array_max_length: int = 30_000
    _pointer: int = 0
    _code_in: List[str] = []                 # For storing input
    _code_out: List[str] = []                # For storing the result

    def __init__(self, max_length: int = 30_000) -> None:
        self.char_array_max_length = max_length
        self.char_array = [" " for _ in range(self.char_array_max_length)]

    def __call__(self, *args, **kwargs) -> None:
        print("It kind of works")
        # The main loop of the program, that should run in case of using the program
        #   in a CLI way
        while True:
            raise NotImplementedError("Work in progress...")

    def pointer_move_right(self):
        """Functionality for '>' instruction."""
        self.pointer = self.pointer + 1

    def pointer_more_left(self):
        """Functionality for '<' instruction."""
        self.pointer = self.pointer - 1

    def value_increase(self):
        """Functionality for '+' instruction."""
        self.char_array[self.pointer] = self.char_array[self.pointer] + 1

    def value_decrease(self):
        """Functionality for '-' instruction."""
        self.char_array[self.pointer] = self.char_array[self.pointer] - 1

    def _5(self):
        """Functionality for '.' instruction."""

    def _6(self):
        """Functionality for ',' instruction."""

    def _7(self):
        """Functionality for '[' instruction."""

    def _8(self):
        """Functionality for ']' instruction."""

    def get_input(self) -> None:
        self.code_in = [_ for _ in input().strip()]

    @property
    def acceptable_chars(self) -> str:
        return self._acceptable_chars

    @property
    def char_array(self) -> List[int]:
        return self._char_array

    @char_array.setter
    def char_array(self, char_array: List[int]) -> None:
        if not isinstance(char_array, list):
            raise TypeError(
                "Char array must be a list."
            )
        elif not all([isinstance(_, int) for _ in char_array]):
            raise TypeError(
                "In char array, all values must be an integer."
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

    @property
    def code_in(self) -> List[str]:
        return self._code_in

    @code_in.setter
    def code_in(self, code: List[str]) -> None:
        if not isinstance(code, list):
            raise TypeError(
                "Code in takes only a List of characters (str)."
            )
        elif not all([isinstance(_, str) for _ in code]):
            raise TypeError(
                "In \"code_in\", all characters must be of type str."
            )
        elif not all([len(_) != 1 for _ in code]):
            raise ValueError(
                "In \"code_in\", all characters must be of length 1."
            )
        elif not all([_ in self.acceptable_chars for _ in code]):
            raise ValueError(
                "BF code was provided with an illegal character."
            )
        else:
            self._code_in = code

    @property
    def pointer(self) -> int:
        return self._pointer

    @pointer.setter
    def pointer(self, val: int) -> None:
        if not isinstance(val, int):
            raise TypeError(
                "Pointer must be an integer."
            )
        elif val < 0:
            self._pointer = 0
        elif val > self.char_array_max_length:
            self._pointer = self.char_array_max_length
        else:
            self._pointer = val


if __name__ == "__main__":
    Main()()
