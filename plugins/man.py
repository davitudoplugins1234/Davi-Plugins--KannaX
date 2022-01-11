import asyncio

from kannax import Message, kannax


@kannax.on_cmd("man", about={"header": "man"})
async def sii_(message: Message):
    out_str =   f"""
    
 A____A
|・ㅅ・|
|っ ｃ |
|       |
 Se Fude 
|       |
|       |
|       |
 U￣￣U⠀⠀
    """
    await message.edit(out_str)
