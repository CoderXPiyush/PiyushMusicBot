#
# Copyright (C) 2023-2024 by CoderXPiyush@Github, < https://github.com/CoderXPiyush >.
#
# This file is part of < https://github.com/CoderXPiyush/PiyushMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/CoderXPiyush/PiyushMusicBot/blob/master/LICENSE >
#
# All rights reserved.
#

import os
import sys
from os import listdir, mkdir

from ..logging import LOGGER


def dirr():
    if "assets" not in listdir():
        LOGGER(__name__).warning(
            f"Assets Folder not Found. Please clone repository again."
        )
        sys.exit()
    for file in os.listdir():
        if file.endswith(".jpg"):
            os.remove(file)
    for file in os.listdir():
        if file.endswith(".jpeg"):
            os.remove(file)
    for file in os.listdir():
        if file.endswith(".session"):
            os.remove(file)
    for file in os.listdir():
        if file.endswith(".session-journal"):
            os.remove(file)
    if "downloads" not in listdir():
        mkdir("downloads")
    if "cache" not in listdir():
        mkdir("cache")
    LOGGER(__name__).info("Directories Updated.")
