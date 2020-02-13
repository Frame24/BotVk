import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_bot import VkBot

# API-ключ созданный ранее
token = "a64284affac00e062a6df72765454d8e41fc8f610c4d19301fd590b17f68c2a586b834e7e16ae723dd391"

# Авторизуемся как сообщество
vk = vk_api.VkApi(token=token)

# Работа с сообщениями
longpoll = VkLongPoll(vk)
    
print("Server started")
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
        
            print('New message:')
            print(f'For me by: {event.user_id}', end='')
            
            bot = VkBot(event.user_id)
            write_msg(event.user_id, bot.new_message(event.text))
            
            print('Text: ', event.text)