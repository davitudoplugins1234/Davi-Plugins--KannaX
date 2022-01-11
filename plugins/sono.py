import random

from kannax import Message, kannax

@kannax.on_cmd('sono' , about={"header": 'estou com sono?'})
async def sono_(message: Message):
    sono = f"Número do sono: {random.choice(range(0, 10))}"
    await message.edit(sono)
