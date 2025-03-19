from balethon import Client
import requests as r

token = "1318129827:exhwk4RrgrIOYUA3jeq7BhNQ1FJCq6Xe2PUBcnjK"
bot = Client(token)

@bot.on_message()
async def start(message):
    if message.text == "/start":
     await message.reply("""سلام دوست عزیز به ربات H_O خوش آمدی❤   
                         برای صحبت با gpt اول متنت /gpt بزار""")
         
    
    if message.text.startswith("/gpt"):
        f = message.text.replace('/gpt','').strip()
        s = r.get(f"https://chatgpt.ehsancoder-as.workers.dev?text={f}").json()
        text , gpt = s['text'], s['result']
        await message.reply(f"""متن پرسش شما:{f}
                            ✅جواب:{gpt}""")
bot.run()

