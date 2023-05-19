"""
Yes! You see this correctly. A FUCKING UwU encoder/decoder.
"""

from __future__ import annotations

import codecs
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Final


from .codec import UwUCodec


def enable():
    """🟢 Enable the UwUCodec."""
    codec = UwUCodec()
    codecs.register(lambda _: codecs.CodecInfo(codec.encode, codec.decode, name = "UwU"))
    codecs.register(lambda _: codecs.CodecInfo(codec.encode, codec.decode, name = "uwu"))

__version__: Final[str] = "1.1"