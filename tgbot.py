import asyncio
import logging
from aiogram.types import Message
from aiogram import Router
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from config import BOT_TOKEN as token, Admins
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from button import menyu, bolimlar, ichimlik_turi, ichimliklar, cocacola, Fanta, Milliycola, Pepsi, soklar, Lipton
from button import Aystea, Bliss, Energetiklar, Flash, Redbull, Adrenaline, savat
# from googletrans import Translator
# from telegram_bot import Add_Funcion, readSqliteTable


logging.basicConfig(level=logging.INFO)
bot = Bot(token=token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))


dp = Dispatcher()
router = Router()

@dp.message(Command('start'))
async def CommandStart(message: types.Message):
    first_name = message.from_user.first_name
    full_name = message.from_user.full_name
    url = message.from_user.url
    user_id = message.from_user.id
    await message.reply(f"Assalomu alaykum \n<a href='{url}'>{first_name}</a>", reply_markup=menyu)
    for i in Admins:
        if i != user_id:
            await bot.send_message(chat_id=i,text= f" 👉<a href='{url}'>{first_name}</a>👈 Start  bosdi")


@dp.message(F.text == 'Maxsulot xarid qilish🛍')
async def dokon(message: types.Message):
    await message.answer_photo(photo='https://malumot.ru/wp-content/uploads/2021/07/photo_2021-07-16_23-11-51.jpg', caption='Qanday maxsulot harid qilmoqchisiz', reply_markup=bolimlar)


@dp.message(F.text == 'Orqaga⬅️')
async def dokon(message: types.Message):
    await message.answer_photo(photo='https://static5.tgstat.ru/channels/_0/6e/6eef7be11f3d17bbd7a472cb997997f8.jpg',caption='Siz menyuga qaytdingiz', reply_markup=menyu)


@dp.message(F.text == 'Ichimliklar🍾🍷🥤')
async def dokon(message: types.Message):
    await message.answer_photo(photo='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSItESPNRbAW2y3L4jHwV0Pwo87gtfDRx7dvw&s', caption='Iltimos ichimlik turini tanlang', reply_markup=ichimlik_turi)


@dp.message(F.text == 'Orqaga🔙')
async def dokon(message: types.Message):
    await message.answer_photo(photo='https://malumot.ru/wp-content/uploads/2021/07/photo_2021-07-16_23-11-51.jpg', reply_markup=bolimlar)



@dp.message(F.text == 'Gazli ichimliklar🍻')
async def dokon(message: types.Message):
    await message.answer_photo(photo='https://aniq.uz/photos/news/EQiKZC14lBRwBzq.jpeg', caption='Qanday ichimlik harid qilmoqchisiz', reply_markup=ichimliklar)


@dp.message(F.text == 'orqaga◀️')
async def dokon(message: types.Message):
    await message.answer_photo(photo='https://aniq.uz/photos/news/EQiKZC14lBRwBzq.jpeg', caption='Qanday ichimlik harid qilmoqchisiz', reply_markup=ichimliklar)





#Coca Cola
@dp.message(F.text == 'Coca Cola')
async def dokon(message: types.Message):
    await message.answer_photo(photo='https://niholjoja.uz/wa-data/public/shop/products/59/00/59/images/95/95.970.png',caption="Cola hajmini tanlang", reply_markup=cocacola)

@dp.message(F.text == 'Orqaga◀️')
async def dokon(message: types.Message) ->None:
    await message.answer_photo(photo='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSItESPNRbAW2y3L4jHwV0Pwo87gtfDRx7dvw&s', caption='Iltimos ichimlik turini tanlang', reply_markup=ichimlik_turi)

@dp.message(F.text == '0.25L Cola')
async def dokon(message: types.Message):
    await message.answer_photo(photo='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS7xs0No-0s4_es00M8-ONqXFgdyxJPzG2oJg&s', caption='Narxi: 5000 so`m', reply_markup=savat)

@dp.message(F.text == '0.33L Cola')
async def dokon(message: types.Message):
    await message.answer_photo(photo='https://images.uzum.uz/cggpoafhgiov1qifn4ng/t_product_540_high.jpg', caption='Narxi: 17000 so`m', reply_markup=savat)

@dp.message(F.text == '0.5L Cola')
async def dokon(message: types.Message):
    await message.answer_photo(photo='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTu2Z3F0NBBT7Q-RPVdxRYkxFNKE27z2gsVSA&s', caption='Narxi: 7000 so`m', reply_markup=savat)

@dp.message(F.text == '1L Cola')
async def dokon(message: types.Message):
    await message.answer_photo(photo='https://boqiy.uz/wp-content/uploads/2023/11/medium_1683711822671101020102-00176.png', caption='Narxi: 10000 so`m', reply_markup=savat)

@dp.message(F.text == '1.5L Cola')
async def dokon(message: types.Message):
    await message.answer_photo(photo='https://niholjoja.uz/wa-data/public/shop/products/59/00/59/images/73/73.970.png', caption='Narxi: 13000 so`m', reply_markup=savat)

@dp.message(F.text == '2L Cola')
async def dokon(message: types.Message):
    await message.answer_photo(photo='https://www.shopmassystoresgy.com/wp-content/uploads/2021/04/0004900000639.jpg', caption='Narxi: 17000 so`m', reply_markup=savat)



#Fanta
@dp.message(F.text == 'Fanta')
async def dokon(message: types.Message):
    await message.answer_photo(photo='https://ccbs.al/wp-content/uploads/2023/11/web-03.png',caption="Fanta hajmini tanlang", reply_markup=Fanta)

@dp.message(F.text == 'ortga')
async def dokon(message: types.Message) ->None:
    await message.answer_photo(photo='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSItESPNRbAW2y3L4jHwV0Pwo87gtfDRx7dvw&s', caption='Iltimos ichimlik turini tanlang', reply_markup=ichimliklar)

@dp.message(F.text == '0.25L Fanta')
async def dokon(message: types.Message):
    await message.answer_photo(photo='https://api.lochin.uz/media/file/image/2020-11/d5cfefae-ae9d-484c-a3a8-a9cd3f723258.jpg.500x500_q85_crop-scale.jpg', caption='Narxi: 6000 so`m', reply_markup=savat)

@dp.message(F.text == '0.33L Fanta')
async def dokon(message: types.Message):
    await message.answer_photo(photo='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTZ7maGVoChJdX97Qn2yIj8GuemzNmMy4IROA&s', caption='Narxi: 19000 so`m', reply_markup=savat)

@dp.message(F.text == '0.5L Fanta')
async def dokon(message: types.Message):
    await message.answer_photo(photo='https://kansler.uz/upload/iblock/394/39428a8442da99dda3ae970aa22dd423.jpeg', caption='Narxi: 7000 so`m', reply_markup=savat)

@dp.message(F.text == '1L Fanta')
async def dokon(message: types.Message):
    await message.answer_photo(photo='https://images.migrosone.com/sanalmarket/product/08022000/8022000_yan-d36055-1650x1650.png', caption='Narxi: 10000 so`m', reply_markup=savat)

@dp.message(F.text == '1.5L Fanta')
async def dokon(message: types.Message):
    await message.answer_photo(photo='https://images.uzum.uz/ce8a878v1htd23airm70/original.jpg', caption='Narxi: 13000 so`m', reply_markup=savat)

@dp.message(F.text == '2L Fanta')
async def dokon(message: types.Message):
    await message.answer_photo(photo='https://bazarstore.az/cdn/shop/products/30009757_e0de5321-d8de-4223-9421-dc1fb4e47670.jpg?v=1693305471', caption='Narxi: 18000 so`m', reply_markup=savat)



#Milliy cola
@dp.message(F.text == 'Milliy cola')
async def dokon(message: types.Message):
    await message.answer_photo(photo='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS1vnjCMTv1AlYW1U3uBqXH-Fh-cQXV7n0ibg&s',caption="Milliy cola hajmini tanlang", reply_markup=Milliycola)

@dp.message(F.text == 'ortga◀️')
async def dokon(message: types.Message) ->None:
    await message.answer_photo(photo='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSItESPNRbAW2y3L4jHwV0Pwo87gtfDRx7dvw&s', caption='Iltimos ichimlik turini tanlang', reply_markup=ichimliklar)

@dp.message(F.text == '0.5L Milliy cola')
async def dokon(message: types.Message):
    await message.answer_photo(photo='https://bozorcom.ams3.cdn.digitaloceanspaces.com/media/products/0.5.jpg', caption='Narxi: 5000 so`m', reply_markup=savat)

@dp.message(F.text == '1L Milliy cola')
async def dokon(message: types.Message):
    await message.answer_photo(photo='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRoGfGx1DuoT_G5yTg1QoaKFXdxUwAdS8Ojcg&s', caption='Narxi: 8000 so`m', reply_markup=savat)

@dp.message(F.text == '1.5L Milliy cola')
async def dokon(message: types.Message):
    await message.answer_photo(photo='https://bozorcom.ams3.cdn.digitaloceanspaces.com/media/products/15-milliy-cola.jpg', caption='Narxi: 10000 so`m', reply_markup=savat)



#Pepsi
@dp.message(F.text == 'Pepsi')
async def dokon(message: types.Message):
    await message.answer_photo(photo='https://upload.wikimedia.org/wikipedia/commons/thumb/6/68/Pepsi_2023.svg/640px-Pepsi_2023.svg.png',caption="Pepsi hajmini tanlang", reply_markup=Pepsi)

@dp.message(F.text == 'Ortga◀️')
async def dokon(message: types.Message) ->None:
    await message.answer_photo(photo='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSItESPNRbAW2y3L4jHwV0Pwo87gtfDRx7dvw&s', caption='Iltimos ichimlik turini tanlang', reply_markup=ichimliklar)

@dp.message(F.text == '0.25L Pepsi')
async def dokon(message: types.Message):
    await message.answer_photo(photo='https://orzon.uz/upload/iblock/556/55643757e452dd1529a8d25b936b01fe.jpg', caption='Narxi: 6000 so`m', reply_markup=savat)

@dp.message(F.text == '0.5L Pepsi')
async def dokon(message: types.Message):
    await message.answer_photo(photo='https://1119001045.rsc.cdn77.org/wa-data/public/shop/products/86/30/3086/images/2216/Napitok_Gazirovannyy_PEPSI_05_l.650@2x.jpg', caption='Narxi: 5000 so`m', reply_markup=savat)

@dp.message(F.text == '1L Pepsi')
async def dokon(message: types.Message):
    await message.answer_photo(photo='https://olcha.uz/image/600x600/products/2023-01-19/gazirovannyy-napitok-pepsi-1-l-191451-0.jpg', caption='Narxi: 10000 so`m', reply_markup=savat)

@dp.message(F.text == '1.5L Pepsi')
async def dokon(message: types.Message):
    await message.answer_photo(photo='https://babymarket.uz/wp-content/uploads/2020/05/pepsi-cola-15-l.jpg', caption='Narxi: 13000 so`m', reply_markup=savat)

@dp.message(F.text == '2L Pepsi')
async def dokon(message: types.Message):
    await message.answer_photo(photo='https://images.uzum.uz/cjjlggcvutv1g2rie5fg/original.jpg', caption='Narxi: 16000 so`m', reply_markup=savat)





#sok va choylar
@dp.message(F.text == 'Sharbatlar va choylar🧃')
async def dokon(message: types.Message):
    await message.answer_photo(photo='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQsPTKD6tJ76hHQAow5d95w3ue5F68KWqIpnwAwS8hd0GXp9PRQU_uEogj6W1EmjPzxhao&usqp=CAU',caption="Sharbat yoki choyni tanlang", reply_markup=soklar)

@dp.message(F.text == 'orqaga⬅️')
async def dokon(message: types.Message) ->None:
    await message.answer_photo(photo='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSItESPNRbAW2y3L4jHwV0Pwo87gtfDRx7dvw&s', caption='Iltimos ichimlik turini tanlang', reply_markup=ichimlik_turi)



#Lipton
@dp.message(F.text == 'Lipton')
async def dokon(message: types.Message):
    await message.answer_photo(photo='https://m.media-amazon.com/images/I/8187SPdp+IL._SL1500_.jpg', caption="Lipton hajmini tanlang", reply_markup=Lipton)

@dp.message(F.text == 'orqaga🔙')
async def dokon(message: types.Message) ->None:
    await message.answer_photo(photo='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQsPTKD6tJ76hHQAow5d95w3ue5F68KWqIpnwAwS8hd0GXp9PRQU_uEogj6W1EmjPzxhao&usqp=CAU', caption='Iltimos ichimlik turini tanlang', reply_markup=soklar)

@dp.message(F.text == '0.5L Lipton qora choy')
async def dokon(message: types.Message):
    await message.answer_photo(photo='https://alushta.food-td.ru/mdata/topimg/size3/913.jpg', caption='Narxi: 6000 so`m', reply_markup=savat)

@dp.message(F.text == '1L Lipton qora choy')
async def dokon(message: types.Message):
    await message.answer_photo(photo='https://images.uzum.uz/cofsds21om4pepe0c0dg/original.jpg', caption='Narxi: 10000 so`m', reply_markup=savat)

@dp.message(F.text == '0.5L Lipton kok choy')
async def dokon(message: types.Message):
    await message.answer_photo(photo='https://babymarket.uz/wp-content/uploads/2020/07/zelenyj-chaj-lipton-s-limonom-05-l.jpg', caption='Narxi: 6000 so`m', reply_markup=savat)

@dp.message(F.text == '1L Lipton kok choy')
async def dokon(message: types.Message):
    await message.answer_photo(photo='https://images.uzum.uz/cev9n4avtie1lhbgl2d0/original.jpg', caption='Narxi: 10000 so`m', reply_markup=savat)



#Aystea
@dp.message(F.text == 'Ays tea')
async def dokon(message: types.Message):
    await message.answer_photo(photo='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSwixwlKRepRtRCLrrTZSoBHMJKuLHVA3oWuQ&s', caption="Ays tea hajmini tanlang", reply_markup=Aystea)

@dp.message(F.text == 'Ortga')
async def dokon(message: types.Message) ->None:
    await message.answer_photo(photo='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQsPTKD6tJ76hHQAow5d95w3ue5F68KWqIpnwAwS8hd0GXp9PRQU_uEogj6W1EmjPzxhao&usqp=CAU', caption='Iltimos ichimlik turini tanlang', reply_markup=soklar)

@dp.message(F.text == '0.5L Ays tea qora choy')
async def dokon(message: types.Message):
    await message.answer_photo(photo='https://olcha.uz/image/600x600/products/2023-01-19/chay-ays-tea-chernyy-05-l-lesnye-yagody-191435-0.jpg', caption='Narxi: 5000 so`m', reply_markup=savat)

@dp.message(F.text == '1.25L Ays tea qora choy')
async def dokon(message: types.Message):
    await message.answer_photo(photo='https://api.lochin.uz/media/file/image/2020-05/2ed704eb-a40f-4e16-b455-7eee5ba7cc08.jpg.500x500_q85_crop-scale.jpg', caption='Narxi: 9000 so`m', reply_markup=savat)

@dp.message(F.text == '0.5L Ays tea kok choy')
async def dokon(message: types.Message):
    await message.answer_photo(photo='https://navruzint.com/wp-content/uploads/2023/02/zeleniy_persik_05.png', caption='Narxi: 5000 so`m', reply_markup=savat)

@dp.message(F.text == '1.25L Ays tea kok choy')
async def dokon(message: types.Message):
    await message.answer_photo(photo='https://catalog.milliykatalogi.uz/s3/med/02a93e39-c592-43c6-0234-1c1d9058daac.jpg', caption='Narxi: 9000 so`m', reply_markup=savat)



#Bliss
@dp.message(F.text == 'Bliss')
async def dokon(message: types.Message):
    await message.answer_photo(photo='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSRsQGrJ3H4eI5FVGq98dXpOotPzQIBiOhRww&s',caption="Bliss turini tanlang", reply_markup=Bliss)

@dp.message(F.text == 'Ortga🔙')
async def dokon(message: types.Message) ->None:
    await message.answer_photo(photo='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQsPTKD6tJ76hHQAow5d95w3ue5F68KWqIpnwAwS8hd0GXp9PRQU_uEogj6W1EmjPzxhao&usqp=CAU', caption='Iltimos ichimlik turini tanlang', reply_markup=soklar)

@dp.message(F.text == '1L Bliss Olmali')
async def dokon(message: types.Message):
    await message.answer_photo(photo='https://lh4.googleusercontent.com/proxy/6pyTQoRY8KmMYdw9E1s6s1T2U6UK3p_mMyo9XnH20lbTT9zFjrx8hBUjxgKuLX0NIPxTHW7w3_CUoN6hzGJJFc4LikGLlm67uRPwZ1QEQ76V6g', caption='Narxi: 13000 so`m', reply_markup=savat)

@dp.message(F.text == '1L Bliss Ananas')
async def dokon(message: types.Message):
    await message.answer_photo(photo='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQgP4EPqLLYeEI4K_0TaFpnmM_qUQjSo1-_hkvEpjcQhRS8nXILUItqXB_tvFuyH-9YB5U&usqp=CAU', caption='Narxi: 13000 so`m', reply_markup=savat)

@dp.message(F.text == '1L Bliss banan-olma')
async def dokon(message: types.Message):
    await message.answer_photo(photo='https://lh3.googleusercontent.com/proxy/cGUk5QzcbCfxZH6RGJao7E0jk8q5nKuShHNN0_MtwGKBgikP4CIQcAhTimYgBEpWhqEw-nHZAp1d7tCxevW7e0p2_8Z_t_WKqoOG-JieE4Feu4_KMBykFQ42vK5K9wSJhQ', caption='Narxi: 13000 so`m', reply_markup=savat)

@dp.message(F.text == '1L Bliss Apelsin')
async def dokon(message: types.Message):
    await message.answer_photo(photo='https://api.lochin.uz/media/file/image/2020-08/288187ed-a1ae-4210-8a34-5d24bba5dc2b.jpg.500x500_q85_crop-scale.jpg', caption='Narxi: 13000 so`m', reply_markup=savat)

@dp.message(F.text == '1L Bliss O`rmon-rezavorlari')
async def dokon(message: types.Message):
    await message.answer_photo(photo='https://images.uzum.uz/cdj6evrb3ho5lmurhpb0/original.jpg', caption='Narxi: 13000 so`m', reply_markup=savat)

@dp.message(F.text == '1L Bliss Olcha')
async def dokon(message: types.Message):
    await message.answer_photo(photo='https://images.uzum.uz/cdj6er35a95unf13j7bg/original.jpg', caption='Narxi: 13000 so`m', reply_markup=savat)

@dp.message(F.text == '200mL Bliss smile-ananas')
async def dokon(message: types.Message):
    await message.answer_photo(photo='https://images.uzum.uz/ci0tpjr6edfostigh5r0/original.jpg', caption='Narxi: 5000 so`m', reply_markup=savat)

@dp.message(F.text == '200mL Bliss smile-olcha')
async def dokon(message: types.Message):
    await message.answer_photo(photo='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRz5l4eFumLFrMyuKmfl_5qm0a4sEPlaF3DIA&s  ', caption='Narxi: 5000 so`m', reply_markup=savat)

@dp.message(F.text == '200mL Bliss smile-multimeva')
async def dokon(message: types.Message):
    await message.answer_photo(photo='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSzTPtc6Nz2jY1bYsNFgCT-ELTg2-SNyUAcT8FHdJxfyrhmqUjlcfG4N_Uz7foW_dJS85k&usqp=CAU', caption='Narxi: 5000 so`m', reply_markup=savat)







#Energetiklar
@dp.message(F.text == 'Energetik ichimliklar🔋')
async def dokon(message: types.Message):
    await message.answer_photo(photo='https://olcha.uz/image/original/category/woLeEDB6pNQ2g7ki9f69keFAFoABja5bTDd20n0H23CoLd9XO43xVHSCvUOJ.png',caption="Energetik turini tanlang tanlang", reply_markup=Energetiklar)

@dp.message(F.text == 'ortga🔙')
async def dokon(message: types.Message) ->None:
    await message.answer_photo(photo='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSItESPNRbAW2y3L4jHwV0Pwo87gtfDRx7dvw&s', caption='Iltimos ichimlik turini tanlang', reply_markup=ichimlik_turi)




#Flash
@dp.message(F.text == 'Flash')
async def dokon(message: types.Message):
    await message.answer_photo(photo='https://olcha.uz/uploads/images/manufacturer/KK/KK/PS/1673848626.jpg',caption="Flash hajmini tanlang", reply_markup=Flash)

@dp.message(F.text == 'ORTGA◀️')
async def dokon(message: types.Message) ->None:
    await message.answer_photo(photo='https://olcha.uz/image/original/category/woLeEDB6pNQ2g7ki9f69keFAFoABja5bTDd20n0H23CoLd9XO43xVHSCvUOJ.png', caption='Iltimos ichimlik turini tanlang', reply_markup=Energetiklar)

@dp.message(F.text == '250ml Flash')
async def dokon(message: types.Message):
    await message.answer_photo(photo='https://images.uzum.uz/cdf6l3rb3ho5lmur8tg0/original.jpg', caption='Narxi: 7000 so`m', reply_markup=savat)

@dp.message(F.text == '330ml Flash')
async def dokon(message: types.Message):
    await message.answer_photo(photo='https://babymarket.uz/wp-content/uploads/2020/07/flash-up_energy-energeticheskij-naptok-250-ml.jpg', caption='Narxi: 8000 so`m', reply_markup=savat)

@dp.message(F.text == '450ml Flash')
async def dokon(message: types.Message):
    await message.answer_photo(photo='https://dostavo4ka.uz/upload-file/2021/05/05/493/c07a1652-3982-44aa-8eeb-37cc0820484c.jpg', caption='Narxi: 10000 so`m', reply_markup=savat)



#Redbull
@dp.message(F.text == 'Red Bull')
async def dokon(message: types.Message):
    await message.answer_photo(photo='https://plus.mvrwholesale.com/cdn/shop/products/0018085400025c_800x.jpg?v=1708704601',caption="Red Bull hajmini tanlang", reply_markup=Redbull)

@dp.message(F.text == 'ORTGA🔙')
async def dokon(message: types.Message) ->None:
    await message.answer_photo(photo='https://olcha.uz/image/original/category/woLeEDB6pNQ2g7ki9f69keFAFoABja5bTDd20n0H23CoLd9XO43xVHSCvUOJ.png', caption='Iltimos ichimlik turini tanlang', reply_markup=Energetiklar)

@dp.message(F.text == '250ml Red Bull')
async def dokon(message: types.Message):
    await message.answer_photo(photo='https://images.uzum.uz/cl9le0l6sfhgee0lnaf0/original.jpg', caption='Narxi: 20000 so`m', reply_markup=savat)

@dp.message(F.text == '250ml Red Bull Sugar free')
async def dokon(message: types.Message):
    await message.answer_photo(photo='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT0lcM71vP-c-gOpNA_q1qmb_9BwQDVUfchlw&s', caption='Narxi: 20000 so`m', reply_markup=savat)

@dp.message(F.text == '350ml Red Bull')
async def dokon(message: types.Message):
    await message.answer_photo(photo='https://neelamfoodlandmumbai.com/cdn/shop/products/IMG_1516_800x.jpg?v=1620639703', caption='Narxi: 28000 so`m', reply_markup=savat)



#Adrenaline
@dp.message(F.text == 'Adrenaline')
async def dokon(message: types.Message):
    await message.answer_photo(photo='https://www.gazeta.uz/media/img/2017/09/5ZdDY615047874062617_l.jpg',caption="Adrenaline hajmini tanlang", reply_markup=Adrenaline)

@dp.message(F.text == 'ORTGA⬅️')
async def dokon(message: types.Message) ->None:
    await message.answer_photo(photo='https://olcha.uz/image/original/category/woLeEDB6pNQ2g7ki9f69keFAFoABja5bTDd20n0H23CoLd9XO43xVHSCvUOJ.png', caption='Iltimos ichimlik turini tanlang', reply_markup=Energetiklar)

@dp.message(F.text == '250ml Adrenaline classic')
async def dokon(message: types.Message):
    await message.answer_photo(photo='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSCxaCpboxr-6rvUqGkTtPN4tgIQfxva3AmUQ&s', caption='Narxi: 10000 so`m', reply_markup=savat)

@dp.message(F.text == '250ml Adrenaline Rush')
async def dokon(message: types.Message):
    await message.answer_photo(photo='https://yaicoopt.ru/assets/img/adrenaline-small.jpeg', caption='Narxi: 10000 so`m', reply_markup=savat)

@dp.message(F.text == '450ml Adrenaline Red')
async def dokon(message: types.Message):
    await message.answer_photo(photo='https://images.uzum.uz/chmvd7tenntd8rfa1if0/original.jpg', caption='Narxi: 16000 so`m', reply_markup=savat)

@dp.message(F.text == '450ml Adrenaline Rush')
async def dokon(message: types.Message):
    await message.answer_photo(photo='https://img.napolke.ru/image/get?uuid=714ab7ad-7fdd-429a-80c9-1de3e8c2211c&size=370x370', caption='Narxi: 16000 so`m', reply_markup=savat)











async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot faolyatini tugatdi")
