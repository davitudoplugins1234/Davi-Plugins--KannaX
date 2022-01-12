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


@kannax.on_cmd("historia", about={"header": "historia"})
async def snake_(message: Message):
    """memes fodas"""
    out = f"""
Era uma vez um guamp que tinha sido recem comprado na loja e com isso o Giovany conhecido como matador de celular viu isso e ficou com desejo de matar o celular então ele foi como espirito atras do celular        
"""

    out2 = f"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀Ovo matar o guamp kkkj⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣄⣀⣀⣀⣀⡀⠀⠀⠸⢏⠉⢶⣀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣦⣤⠀⢸⠀⠈⣿⡄⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣶⣿⡿⠿⠿⠿⣿⣿⣿⣿⠿⢰⡎⠀⠀⢸⡇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⢹⣿⠀⢾⣿⢻⣿⣿⣿⣿⡇⠀⠀⣾⠃⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣷⣎⣀⣴⣶⣿⣿⣿⣿⣿⣿⣿⣿⡿⡇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣤⣤⣼⣿⣿⠉⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢿⣿⣿⡿⠛⢛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠃⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⠿⢿⡿⣿⣿⣯⡉⠛⣿⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠛⠛⠉⠛⠛⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""
    out3 = f"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣶⣶⣶⣶⣶⣶⡄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣄⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⠿⠿⠿⠟⠛⠛⠳⠶⣤⣀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⠞⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣉⣻⣦⣄
⠀⠀⠀⠀⠀⠀⠀⢀⣴⠟⠁⠀⢀⠠⠤⠤⠰⣶⡲⡶⣶⣿⡿⠛⢯⣏⣟⣿⡿⠛
⠀⠀⠀⠀⠀⠀⣠⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠚⢊⣉⣀⣀⣀⣠⣤⣤⠶⠞
⠀⠀⠀⠀⠀⣰⠏⠀⠀⠀⠀⠀⠀⠀⠀⠛⠛⠛⠛⠉⠉⠉⠉⣿⠁⠀⠀⠀⠀⠀Ovo jogar fortnite no guamp quando chegar em casa
⠀⠀⠀⠀⣰⠇⠀⠀⠀⠀⣀⣀⣤⣴⣄⠀⠀⠀⠀⠀⠀⠀⠀⠸⡇⠀⠀⠀⠀⠀
⠀⠀⠀⢰⠏⠀⠀⢰⣾⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡀⠀⠀⠀⠀
⠀⠀⢠⡟⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠘⣧⠀⠀⠀⠀
⠀⠀⣼⠃⠀⣀⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⢻⡀⠀⠀⠀
⠀⠀⣿⠀⠀⢻⣄⠀⠀⢿⣿⣿⣿⣿⣿⣿⣷⣀⡀⠀⠀⠀⠀⠀⠀⠸⡇⠀⠀⠀
⠀⠀⡇⠀⠀⠀⠙⠷⣤⣸⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⣷⠀⠀⠀
⠀⠀⣧⠀⠀⠀⠀⠀⠀⠉⢻⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀
"""

    out4 = f"""
Apois conhecer eles fizeram sexo⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""
    
    out5 = f"""
Chegando em casa o Giovany viu o guamp e foi atacar com isso quebrou o guamp e mato a pessoa
     """
        
    
    out6 = f"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣤⣤⡄⣶⣶⣛⣿⣿⣿⣿⣿⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣿⠿⠿⠛⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣥⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣶⣶⣶⣶⣶⣦⣤⣤⣭⣭⣭⣉⣉⣈⣉⣛⡛⠛⠛⠳⠦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⠀⠀⠀⠄⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠰⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣻⣿⣾⠀⠀⠀⠀⠀⠀⢰⣿⣆⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠉⠛⠂⠀⢠⣤⣀⡀⣉⠉⠉⠙⠛⠛⠛⠻⠿⠿⢿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⢠⣿⣿⡟⡷⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠛⠛⠿⠷⢶⣶⣶⣤⣤⣄⣀⣀⢀⠈⠉⠉⠉⠛⠛⠛⠻⠏⠀⠀⠀⠀⠀⢀⣾⣯⣤⠗⠉⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠙⠛⠻⠿⠿⣷⠛⢿⣿⣷⣶⣦⣴⣶⣤⣤⣤⣤⣤⡾⠟⠛⠃⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⡿⠿⠟⠛⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀F
    """
    
    await message.edit(out)
    await asyncio.sleep(6)
    await message.edit(out2)
    await asyncio.sleep(3)
    await message.edit(out3)
    await asyncio.sleep(4)
    await message.edit(out4)
    await asyncio.sleep(3)
    await message.edit(out5)
    await asyncio.sleep(4)
    await message.edit(out6)
