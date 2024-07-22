from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup


savat = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="savat: ", callback_data='savat')]
    ]
)


menyu = ReplyKeyboardMarkup(
    keyboard = [
        [KeyboardButton(text="Maxsulot xarid qilish🛍"), KeyboardButton(text="Buyurtma berish📦"), KeyboardButton(text="Contact📞", request_contact=True)],
        [KeyboardButton(text="Savat🛒"), KeyboardButton(text="Do`kon bilan boglanish👨‍💻")]
    ],
    resize_keyboard=True
)
bolimlar = ReplyKeyboardMarkup(
    keyboard= [
        [KeyboardButton(text="Ichimliklar🍾🍷🥤"), KeyboardButton(text="Meva va sabzavotlar"), KeyboardButton(text="Qandolatchilik maxsulotlari🍚")],
        [KeyboardButton(text="Pechenya va shirinliklar🍩"), KeyboardButton(text="Yarim tayyor maxsulotlar🍜🥫"), KeyboardButton(text="Konserva maxsulotlari🥫")],
        [KeyboardButton(text="Sut maxsulotlari🥛"), KeyboardButton(text="Yog' maxsulotlari🫗"), KeyboardButton(text="Choy va kofe maxsulotlari🫖☕️")],
        [KeyboardButton(text="Orqaga⬅️"), KeyboardButton(text="Asosiy menuga qaytish◀️")]
    ],
    resize_keyboard=True
)
ichimlik_turi = ReplyKeyboardMarkup(
    keyboard= [
        [KeyboardButton(text="Gazli ichimliklar🍻"), KeyboardButton(text="Sharbatlar va choylar🧃"), KeyboardButton(text="Energetik ichimliklar🔋")],
        [KeyboardButton(text="Orqaga🔙"), KeyboardButton(text="Asosiy menuga qaytish◀️")]
    ],
    resize_keyboard=True
    )



ichimliklar = ReplyKeyboardMarkup(
    keyboard= [
        [KeyboardButton(text="Coca Cola"), KeyboardButton(text="Milliy cola"), KeyboardButton(text="Fanta")],
        [KeyboardButton(text="Pepsi"), KeyboardButton(text="Orqaga◀️"), KeyboardButton(text="Asosiy menuga qaytish◀️")]
    ],
    resize_keyboard=True
)

cocacola = ReplyKeyboardMarkup(
    keyboard= [
        [KeyboardButton(text="0.25L Cola"), KeyboardButton(text="0.33L Cola")],   
        [KeyboardButton(text="0.5L Cola"), KeyboardButton(text="1L Cola")],
        [KeyboardButton(text="1.5L Cola"), KeyboardButton(text="2L Cola")],
        [KeyboardButton(text="orqaga◀️"), KeyboardButton(text="Asosiy menuga qaytish◀️")]
    ],
    resize_keyboard=True
)

Fanta = ReplyKeyboardMarkup(
    keyboard= [
        [KeyboardButton(text="0.25L Fanta"), KeyboardButton(text="0.33L Fanta")],   
        [KeyboardButton(text="0.5L Fanta"), KeyboardButton(text="1L Fanta")],
        [KeyboardButton(text="1.5L Fanta"), KeyboardButton(text="2L Fanta")],
        [KeyboardButton(text="ortga"), KeyboardButton(text="Asosiy menuga qaytish◀️")]
    ],
    resize_keyboard=True
)


Milliycola = ReplyKeyboardMarkup(
    keyboard= [  
        [KeyboardButton(text="0.5L Milliy cola"), KeyboardButton(text="1L Milliy cola")],
        [KeyboardButton(text="1.5L Milliy cola"), KeyboardButton(text="ortga◀️")],
        [KeyboardButton(text="Asosiy menuga qaytish◀️")]
    ],
    resize_keyboard=True
)


Pepsi = ReplyKeyboardMarkup(
    keyboard= [
        [KeyboardButton(text="0.25L Pepsi"), KeyboardButton(text="0.5L Pepsi")],   
        [KeyboardButton(text="1L Pepsi"), KeyboardButton(text="1.5L Pepsi")],
        [KeyboardButton(text="2L Pepsi"), KeyboardButton(text="Ortga◀️")],
        [KeyboardButton(text="Asosiy menuga qaytish◀️")]
    ]
)

soklar = ReplyKeyboardMarkup(
    keyboard= [
        [KeyboardButton(text="Lipton"), KeyboardButton(text="Ays tea"), KeyboardButton(text="Bliss")],
        [KeyboardButton(text="Orqaga◀️"), KeyboardButton(text="Asosiy menuga qaytish◀️")]
    ],
    resize_keyboard=True
)

Lipton = ReplyKeyboardMarkup(
    keyboard= [  
        [KeyboardButton(text="0.5L Lipton qora choy"), KeyboardButton(text="1L Lipton qora choy")],
        [KeyboardButton(text="0.5L Lipton kok choy"), KeyboardButton(text="1L Lipton kok choy")],
        [KeyboardButton(text="orqaga🔙"), KeyboardButton(text="Asosiy menuga qaytish◀️")]
    ],
    resize_keyboard=True
)


Aystea = ReplyKeyboardMarkup(
    keyboard= [  
        [KeyboardButton(text="0.5L Ays tea qora choy"), KeyboardButton(text="1.25L Ays tea qora choy")],
        [KeyboardButton(text="0.5L Ays tea kok choy"), KeyboardButton(text="1.25L Ays tea kok choy")],
        [KeyboardButton(text="Ortga"), KeyboardButton(text="Asosiy menuga qaytish◀️")]
    ],
    resize_keyboard=True
)


Bliss = ReplyKeyboardMarkup(
    keyboard= [  
        [KeyboardButton(text="1L Bliss Olmali"), KeyboardButton(text="1L Bliss Ananas"), KeyboardButton(text="1L Bliss banan-olma")],
        [KeyboardButton(text="1L Bliss Apelsin"), KeyboardButton(text="1L Bliss O`rmon-rezavorlari"), KeyboardButton(text="1L Bliss Olcha")],
        [KeyboardButton(text="200mL Bliss smile-olcha"), KeyboardButton(text="200mL Bliss smile-multimeva"), KeyboardButton(text="200mL Bliss smile-ananas")],
        [KeyboardButton(text="Ortga🔙"), KeyboardButton(text="Asosiy menuga qaytish◀️")]
    ],
    resize_keyboard=True
)


Energetiklar = ReplyKeyboardMarkup(
    keyboard= [
        [KeyboardButton(text="Flash"), KeyboardButton(text="Red Bull"), KeyboardButton(text="Adrenaline")],
        [KeyboardButton(text="Orqaga◀️"), KeyboardButton(text="Asosiy menuga qaytish◀️")]
    ],
    resize_keyboard=True
)


Flash = ReplyKeyboardMarkup(
    keyboard= [
        [KeyboardButton(text="250ml Flash"), KeyboardButton(text="330ml Flash"), KeyboardButton(text="450ml Flash")],   
        [KeyboardButton(text="ORTGA◀️"), KeyboardButton(text="Asosiy menuga qaytish◀️")]
    ],
    resize_keyboard=True
)

Redbull = ReplyKeyboardMarkup(
    keyboard= [
        [KeyboardButton(text="250ml Red Bull"), KeyboardButton(text="250ml Red Bull Sugar free"), KeyboardButton(text="350ml Red Bull")],   
        [KeyboardButton(text="ORTGA🔙"), KeyboardButton(text="Asosiy menuga qaytish◀️")]
    ],
    resize_keyboard=True
)

Adrenaline = ReplyKeyboardMarkup(
    keyboard= [
        [KeyboardButton(text="250ml Adrenaline classic"), KeyboardButton(text="250ml Adrenaline Rush")],
        [KeyboardButton(text="450ml Adrenaline Red"), KeyboardButton(text="450ml Adrenaline Rush")],   
        [KeyboardButton(text="ORTGA⬅️"), KeyboardButton(text="Asosiy menuga qaytish◀️")]
    ],
    resize_keyboard=True
)


mevalar = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Olma🍎"), KeyboardButton(text="Banan🍌"), KeyboardButton(text="Uzum🍇")],
        [KeyboardButton(text="Limon🍋"), KeyboardButton(text="Kartoshka🥔"), KeyboardButton(text="Piyoz🧅")],
        [KeyboardButton(text="Orqaga🔙")]
    ],
    resize_keyboard=True
)
