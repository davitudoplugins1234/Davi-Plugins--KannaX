import asyncio

from kannax import Message, kannax


@kannax.on_cmd("skill", about={"header": "skill"})
async def sii_(message: Message):
    out_str =   f"""
 _____________ 
< o skill eh gay >
 ------------- 
     \   ^__^
      \  (oo)\_______
         (__)\       )\/\
           ||----w |
           ||     || 

⠀⠀
    """
    await message.edit(out_str)
