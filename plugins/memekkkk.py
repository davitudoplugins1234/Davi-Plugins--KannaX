import asyncio
import os
import random
import re
import requests
import wget
import datetime
import math
from cowpy import cow
from random import randint, choice

from kannax import Message, kannax


@kannax.on_cmd("kkkkk", about={"header": "memes"})
async def snake_(message: Message):
    """memes fodas"""
    out = f"""
🤣😂🤣😂🤣😂
"""

    out2 = f"""
😂🤣😂🤣😂🤣
"""
    out3 = f"""
🤣😂🤣😂🤣😂
"""

    out4 = f"""
😂🤣😂🤣😂🤣
"""
    
    out5 = f"""
🤣😂🤣😂🤣😂
    """
    
    await message.edit(out)
    await asyncio.sleep(0.2)
    await message.edit(out2)
    await asyncio.sleep(0.2)
    await message.edit(out3)
    await asyncio.sleep(0.2)
    await message.edit(out4)
    await asyncio.sleep(0.2)
    await message.edit(out5)