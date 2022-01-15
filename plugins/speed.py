import os

import speedtest
import wget

from kannax import Message, kannax
from kannax.utils import humanbytes

CHANNEL = kannax.getCLogger(__name__)


@kannax.on_cmd("speed", about={"header": "teste a velocidade de seu servidor"})
async def speedtst(message: Message):
    await message.edit("`Rodando speed test . . .`")
    try:
        test = speedtest.Speedtest()
        test.get_best_server()
        await message.try_to_edit("`Fazendo teste de download . . .`")
        test.download()
        await message.try_to_edit("`Fazendo teste de upload . . .`")
        test.upload()
        test.results.share()
        result = test.results.dict()
    except Exception as e:
        await message.err(text=e)
        return
    path = wget.download(result["share"])
    output = f"""**--Iniciado as {result['timestamp']}--

Servidor:
🌀 Nome: `{result['server']['name']}`
🌐 Sponsor: `{result['server']['sponsor']}`
🏁 País: `{result['server']['country']}, {result['server']['cc']}`
🏓 Ping: `{result['ping']} ms`
➡️ Enviado: `{humanbytes(result['bytes_sent'])}`
⬅️ Recebido: `{humanbytes(result['bytes_received'])}`
🔼 Download: `{humanbytes(result['download'] / 8)}/s`
🔽 Upload: `{humanbytes(result['upload'] / 8)}/s`
🖥 ISP: `{result['client']['isp']}`**"""
    msg = await message.client.send_photo(
        chat_id=message.chat.id, photo=path, caption=output
    )
    await CHANNEL.fwd_msg(msg)
    os.remove(path)
    await message.delete()