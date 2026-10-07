import telebot
from telebot import types

# আপনার সংগৃহীত বটের API Token এখানে বসান
API_TOKEN = '8057232629:AAHNsa2Lb9dwZKMEHvfK6N7jX5eNZEgnO3c'
MY_CHANNEL_ID = '@EARNPROtakinkambd' # আপনার চ্যানেলের ইউজারনেম

bot = telebot.TeleBot(API_TOKEN)

# আপনার বাটন এবং সেটির নির্দিষ্ট লিঙ্কগুলোর তালিকা (ম্যাপিং)
MY_LINKS = {
    "GOOD111": "http://www.good111com.net/?r=ziy7851",
    "BD111": "http://www.bd111app.bet/?r=vea7012",
    "GB444": "https://www.gb444app.com/register?r=pif3287",
    "CD44": "http://www.cd44app.net/?r=mti2915",
    "CD33": "https://www.cd-33.com/register?r=fle5607",
    "CV666": "http://www.cv66.vip/?r=acq9128",  # পোস্টের বাটনের নামের সাথে মিল থাকতে হবে
    "AK44": "http://www.ak44.biz/?r=usu5158",
    "TK11": "http://www.tk11agent.com/?r=mcz7121",
    "BB44": "http://www.bb44.info/?r=osd3307",
    "TK666": "http://www.tk666.best/?r=inq6449",
    "BK33": "http://www.bk33vip.com/?r=alk8305",
    "TK999": "http://www.tk999pro.net/?r=ceq4144",
    "L444": "http://www.l444vip.com/?r=ujj0692",
    "EK333": "https://www.ek333app.com/register?r=kiv5576",
    "EA77": "http://www.ea77.vip/?r=sol8277",
    "AQ999": "http://www.aq999com.net/?r=jsq4501",
    "CK33": "http://www.ck-33.info/?r=irr7019",
    "TK1971": "https://www.tk1971app.net/register?r=qrv8061",
    "BD222": "http://www.bd222game.com/?r=qhy5596",
    "EG333": "http://www.eg-333.info/?r=nsn3080",
    "GK222": "http://www.g-k222.biz/?r=jdp3907",
    "CK444": "https://www.ck-444.me/register?r=ghd7303",
    "ACE444": "https://www.ace444app.net/register?r=lxt3291"
}

@bot.channel_post_handler(func=lambda message: message.chat.username == 'wintk_bd')
def forward_and_specific_replace(message):
    markup = types.InlineKeyboardMarkup()
    
    # মূল পোস্টের বাটন লেআউট স্ক্যান করা
    if message.reply_markup and message.reply_markup.inline_keyboard:
        for row in message.reply_markup.inline_keyboard:
            new_row = []
            for button in row:
                btn_text = button.text.strip()
                # যদি বাটনের নাম আমাদের তালিকায় থাকে, তবে আপনার লিঙ্ক বসবে, না থাকলে পুরানো লিঙ্কই থাকবে
                target_url = MY_LINKS.get(btn_text, button.url)
                
                new_btn = types.InlineKeyboardButton(text=btn_text, url=target_url)
                new_row.append(new_btn)
            markup.add(*new_row)
            
    # টেক্সট পরিবর্তন
    text = message.text or message.caption or ""
    custom_text = text.replace("@wintk_bd", "@EARNPROtakinkambd")
    
    # চ্যানেলে কাস্টম পোস্ট পাঠানো
    if message.photo:
        bot.send_photo(MY_CHANNEL_ID, message.photo[-1].file_id, caption=custom_text, reply_markup=markup)
    else:
        bot.send_message(MY_CHANNEL_ID, custom_text, reply_markup=markup)

bot.infinity_polling()
