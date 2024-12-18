START_TEMPLATE = """Что может этот бот?

Это Мэтч GPT от VK Знакомств. Совсем скоро 14 февраля, самое время серьёзно подойти к сердечным вопросам. Хотите найти свой идеальный мэтч, чтобы провести с ним самый романтичный день в году? Мы вам поможем и укажем правильный путь.

Пройдите опрос от VK Знакомств и с помощью искусственного интеллекта узнайте, как выглядит ваш идеальный мэтч! Да, результат может быть неожиданным, но сердцу ведь не прикажешь, верно?"""

SUBSCRIBE_TEMPLATE = """Начнём? Да, идеальные мэтчи у нас выдаются бесплатно, но за валентинку. Вашей нам валентинкой будем считать подписку на наш телеграм-канал @vk_dating."""

MATCH_PREFERENCES_TEMPLATE = """Отлично! Теперь закройте глаза и представьте своего идеального мэтча. Кто перед вами?"""

BODY_TYPE_TEMPLATE = """Вкусы у всех разные! Какое телосложение предпочитаете?"""

HAIR_TYPE_TEMPLATE = """Прическа играет важную роль в образе. Выбирайте на свой вкус:"""

HAIR_COLOR_TEMPLATE = """Теперь выберем цвет волос:"""

DATE_STYLE_TEMPLATE = """Вот и настало 14 февраля, вы отправляетесь на свидание. В каком образе пришёл ваш мэтч?"""

PERSONALITY_TEMPLATE = """Вы начали общаться. В ходе разговора вы понимаете, какой характер у вашего спутника:"""

SPECIAL_FEATURE_TEMPLATE = """Вас привлекает одна небольшая особенность собеседника"""

FINAL_TEMPLATE = """Теперь вы медленно открываете глаза. Готовы встретиться со своим идеальным мэтчем?"""

MATCH_GENERATED_TEMPLATE = """Вот и долгожданная встреча! Теперь вы знаете, как выглядит ваш идеальный мэтч. Не похож на настоящего? Конечно, ведь это всего лишь генерация.

А для знакомства с реальными людьми переходите по кнопке ниже в VK Знакомства. Ваш настоящий идеальный мэтч уже заждался, так что не тяните!

P.S. 15 февраля мы опубликуем здесь итоги розыгрыша, в котором вы уже участвуете. Рандомно разыграем 15 Premium-подписок среди тех, кто ищет свой идеальный мэтч. А если пригласите в бот друзей по своей персональной ссылке, ваши шансы на победу возрастут!"""

INVITE_TEMPLATE = """Узнай, как выглядит пара твоей мечты с помощью искусственного интеллекта от VK Знакомств в боте Мэтч GPT: ссылка."""

CHARACTER_MAPPING = {
    "man": "man",
    "lady": "lady",
    "slim": "thin and neat",
    "plump": "plump and fat",
    "sporty": "sporty and muscled, bonny",
    "short_hair": "short hair",
    "long_hair": "long hair",
    "curly_hair": "curly hair",
    "bald": "bald",
    "blonde": "blonde",
    "dark": "black",
    "red": "red",
    "bright": "rainbow colored",
    "elegant": "elegant dinner gala dress",
    "cute": "cute nice pretty resembles alexandra daddario",
    "strict": "strict in suit wearing",
    "romantic": "romantic in dress with roses",
    "official": "official in suit wearing",
    "brutal": "brutal, bossy, stoic and very serious",
    "romantic_man": "romantic man and cute musician poetry",
    "relaxed": "relaxed, easygoing, polite, soft",
    "kind": "kind, friendly",
    "funny": "funny and cheerful with big smile",
    "shy": "shy and coward",
    "melancholic": "melancholic and passive and lazy and boring",
    "piercing": "piercing",
    "freckles": "with freckles",
    "makeup": "with makeup",
    "bearded": "bearded",
    "mustache": "horseshoe mustache"
}

LADY_PROMPT = """Create a highly ultra-realistic portrait, skin has a smooth, sun-kissed glow with a hint of warmth.
The lighting is soft and natural, highlighting her facial features with delicate shadows, adding depth to the portrait."""

MAN_PROMPT = """Create a highly realistic portrait, entrepreneur guy, handsome, full-face photo, 
nikon photo, very attractive, a man who is a narcissist, adding depth to the portrait."""