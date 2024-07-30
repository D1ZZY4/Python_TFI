import telebot

BOT_TOKEN = '7141227909:AAFGsTOp8bPbXzBJXaPq9FEdwg3CuNSmCUY'  # Ganti dengan token bot kamu
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton("Rules", url="http://t.me/MissRose_bot?start=rules_-1002130748145"))
    bot.reply_to(message, "Salam kenal! Saya administrator dari TFI. Jika Anda belum mengetahui rules dari TFI, silakan klik tombol Rules di bawah.", reply_markup=markup)

@bot.message_handler(commands=['report'])
def handle_report(message):
    if message.reply_to_message:
        # Jika pesan /report dibalas ke pesan lain
        pelaku = message.reply_to_message.from_user.username
        pesan_pelaku = message.reply_to_message.text
        pelaporan = message.text
        bot.reply_to(message, "Laporan diterima. Aku akan mengirimkan informasi ini ke admin.")
        bot.send_message(5991733650, f"Laporan baru:\nPelaporan: {pelaporan}\nPelaku: @{pelaku} (ID: {message.reply_to_message.from_user.id})\nPesan Pelaku: {pesan_pelaku}")

        # Kirim foto atau video dari pelaku
        if message.reply_to_message.photo:
            bot.send_photo(5991733650, message.reply_to_message.photo[-1].file_id)
        if message.reply_to_message.video:
            bot.send_video(5991733650, message.reply_to_message.video.file_id)
    else:
        # Jika pesan /report tidak dibalas ke pesan lain
        bot.reply_to(message, "Mohon balaskan pesan ini ke pesan yang ingin kamu laporkan.")

@bot.message_handler(func=lambda message: message.chat.type == 'group')
def handle_group_message(message):
    # Deteksi kata kunci "cheat"
    if 'cheat' in message.text.lower():
        # Kirim laporan ke kamu
        bot.send_message(5991733650, f"Pesan baru dari @{message.from_user.username} di grup @{message.chat.username}:\n{message.text}")

def process_report(message):  # Menangani pesan laporan
    bot.reply_to(message, "Laporan diterima. Mohon tunggu.")
    # Kirim laporan ke kamu (@WzdDizzyFlasherr)
    bot.send_message(5991733650, f"Laporan baru dari @{message.from_user.username}:\n{message.text}")
    # Kirim foto atau video (jika ada) ke kamu
    if message.photo:
        bot.send_photo(5991733650, message.photo[-1].file_id)
    if message.video:
        bot.send_video(5991733650, message.video.file_id)

bot.polling()