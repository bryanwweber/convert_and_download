"""The version of convert_and_download."""
from typing import Tuple

__version_info__: Tuple[int, int, int, str] = (0, 1, 0, '')
__version__ = '.'.join([str(v) for v in __version_info__ if str(v)])
