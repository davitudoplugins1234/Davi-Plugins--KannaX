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


@kannax.on_cmd("teste", about={"header": "teste"})
async def snake_(message: Message):
    """testeee teste"""
    out = f"""
teste a
"""

    out2 = f"""
teste b
"""
    out3 = f"""
Perai...é aqui que estão falando de...
"""

    out4 = f"""
teste c
"""
    await message.edit(out)
    await asyncio.sleep(3)
    await message.edit(out2)
    await asyncio.sleep(3)
    await message.edit(out3)
    await asyncio.sleep(3)
    await message.edit(out4)
