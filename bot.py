import requests

sender=input("Enter your name:")

bot_message=""
while bot_message!="Tạm biệt hẹn gặp lại":
    message=input("Your message:")
    print('Bot is sending...')
    r=requests.post('http://localhost:5005/webhooks/rest/webhook',json={"sender":sender,"message":message})
    print("Bot say: ",end=' ')
    for i in r.json():
        bot_message=i['text']
        print(f"{i['text']}")