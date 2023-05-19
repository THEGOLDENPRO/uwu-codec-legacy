from __future__ import annotations

from typing import Tuple

from codecs import Codec

characters = [chr(i) for i in range(128)]
def uwu(x): return "O" if x % 2 == 0 else "U"

# Table to encode OwO 😳
encode_table = {
    letter: bytes(uwu(number) + "".join(["w" for _ in range(number + 1)]) + uwu(number), "ascii")
    for number, letter in enumerate(characters)
} # LMAO THIS CODE IS SOO UNREADABLE, did that one purpose for the funny.

# Table to decode this bloody mistake.
decode_table = {v: k for k, v in encode_table.items()}

class UwUCodec(Codec):
    """
    The HOLY UwU encoder and decoder ❗
    """
    def __init__(self) -> None:
        super().__init__()

    def __uwu_splitter_gen__(self, _bytes: bytes | memoryview):
        string = ""

        if isinstance(_bytes, memoryview):
            _bytes = _bytes.tobytes()

        for uwu_byte in _bytes.decode("utf-8"):
            string += uwu_byte

            if len(string) > 1 and string[-1] in ["U", "O"]:
                yield decode_table[bytes(string, "ascii")]
                string = ""

    def encode(self, string: str, errors: str = "strict") -> Tuple[bytes, int]:
        return b"".join(encode_table[x] for x in str(string)), len(string)

    def decode(self, bytes: bytes, errors: str = "strict") -> tuple[str, int]:
        return "".join(x for x in self.__uwu_splitter_gen__(bytes)), len(bytes)