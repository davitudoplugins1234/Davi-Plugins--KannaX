import os

import speedtest
import wget

from kannax import Message, kannax
from mybot.utils import humanbytes

CHANNEL = kannax.getCLogger(__name__)


@kannax.on_cmd("speed", about={"header": "teste a velocidade de seu servidor"})
async def speedtst(message: Message):
  await message.edit("`Running speedtest . . .`")
      try:
test = speedtest.Speedtest()        
test.get_best_server()
        await message.try_to_edit("`teste de download iniciado. . .
  test.download()
          await message.try_to_edit("teste de upload iniciado. . .`")
          test.upload()      
          test.results.share()
                  result = test.results.dict()
              except Exception as e:
                  await message.err(text=e)
                  return
              path = wget.download(result["share"])
   output = f"""**--Iniciado as {result['timestamp']}--
           
  Speedtest Results:
  Name: {result['server']['name']}`
  Sponsor: {result['server']['sponsor']}`
  Pais: {result['server']['country']}, {result['server']['cc']}`
  Ping: {result['ping']}
  ISP: `{result['client']['isp']}
      msg = await message.client.send_photo(
          chat_id=message.chat.id, photo
          =path, caption=output
          )
          await CHANNEL.fwd_msg(msg)
          os.remove(path)
              await message.delete()