@kannax.on_cmd("teste", about={"header": "teste"})
async def snake_(message: Message):
    """testeee teste"""
    out = f"""
teste1!!
"""

    out2 = f"""
teste 2
"""
    out3 = f"""
Perai...é aqui que estão falando de...
"""

    out4 = f"""
teste 3
"""
    await message.edit(out)
    await asyncio.sleep(3)
    await message.edit(out2)
    await asyncio.sleep(3)
    await message.edit(out3)
    await asyncio.sleep(3)
    await message.edit(out4)
