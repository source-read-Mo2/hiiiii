import telebot

import pyrogram 

import asyncio

from pyrogram import Client,filters

from pyrogram.enums import ChatMemberStatus 

from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

import re

from datetime import datetime

from pyrogram import enums





api_id = 13817616
api_hash = "118fb0f2bfc0a7a54d1899c412e62a46"
bot_token = "5596554489:AAGeUG5txg2F65CKNZYYvCUjmPSGhOEgKsw"
app = Client(
   'AppClient',
   api_id,
   api_hash,
   bot_token=bot_token
)



dev = 5544047718
disable = []

a = filters.regex("^تفعيل الايدي$") & filters.group
@app.on_message(a)
@app.on_edited_message(a)
async def enable_id(client, message):
    if message.sender_chat:
      return 
    stas = (await app.get_chat_member(message.chat.id, message.from_user.id)).status
    auth = [ChatMemberStatus.OWNER, ChatMemberStatus.OWNER]
    if not stas in auth or message.from_user.id != dev:
      return await message.reply("• هذا الأمر لا يخصك")
    else:
      if not message.chat.id in disable:
        return await message.reply("• تم تفعيل الايدي مسبقاً")
      elif message.chat.id not in disable:
        disable.remove(message.chat.id)
        await message.reply("• تم تفعيل الايدي بنجاح")
        
b = filters.regex("^تعطيل الايدي$") & filters.group
@app.on_message(b)
@app.on_edited_message(b)
async def disable_id(client, message):
    if message.sender_chat:
      return 
    stas = (await app.get_chat_member(message.chat.id, message.from_user.id)).status
    auth = [ChatMemberStatus.OWNER, ChatMemberStatus.OWNER]
    if not stas in auth or message.from_user.id != dev: 
      return await message.reply("• هذا الأمر لا يخصك")
    else:
      if message.chat.id in disable:
        return await message.reply("• تم تعطيل الايدي مسبقاً")
      elif message.chat.id not in disable:
        disable.append(message.chat.id)
        await message.reply("• تم تعطيل الايدي بنجاح")
        
@app.on_message(filters.regex("^ايدي$")) 
def id_(client,message):
      cht = message.chat.id
      if cht in disable:
        return 
      Idu = message.from_user.id
      frt = message.chat.first_name
      usr = message.from_user.username
      typ = message.chat.type
      dat = message.date
      poh = url = f"https://t.me/{message.from_user.username}"
      app.send_photo(message.chat.id,url,f"ID : {Idu}\nID_CHAT: {cht}\nName : {frt}\nUser : @{usr}\nType : {typ}\nDate Msg: {dat}",
      reply_to_message_id = message.id, 
      reply_markup=InlineKeyboardMarkup(
            [
                [ 
                    InlineKeyboardButton(
                        "• مطور البوت ", url=f"https://t.me/dt_rb")
                ],[
                    InlineKeyboardButton(
                       "قناه البوت", url=f"https://t.me/XxsourcexX"), 
                ],
            ]
        ),
)

#%%%%%%%%%%%%%%%%%%%%%%


#Ban with mohamed
@app.on_message(filters.regex("^حظر .*$") & filters.group)
async def ban(_, message):
    User = re.match("حظر @(.*)", message.text).group(1)
    stas = (await app.get_chat_member(message.chat.id, message.from_user.id)).status
    auth = [ChatMemberStatus.OWNER, ChatMemberStatus.OWNER]
    if stas in auth or message.from_user.id != dev:
    	await message.chat.ban_member(User)
    	await message.reply_text("- تم حظره من المجموعة .")
    else:
            await message.reply("- هذا الأمر يخص مشرفين المجموعة .")
            
@app.on_message(filters.regex("^الغاء حظر .*$") & filters.group)
async def unban(_, message):
    User = re.match("الغاء حظر @(.*)", message.text).group(1)
    stas = (await app.get_chat_member(message.chat.id, message.from_user.id)).status
    auth = [ChatMemberStatus.OWNER, ChatMemberStatus.OWNER]
    if stas in auth or message.from_user.id != dev:
    	await message.chat.unban_member(User)
    	await message.reply_text("- تم الغاء حظره من المجموعة .")
    else:
            await message.reply("- هذا الأمر يخص مشرفين المجموعة .")
            
#Commands in *reply .
@app.on_message(filters.regex("^حظر$") & filters.group)
async def ban2(_, message):
    user =message.reply_to_message.from_user.id
    stas = (await app.get_chat_member(message.chat.id, message.from_user.id)).status
    auth = [ChatMemberStatus.OWNER, ChatMemberStatus.OWNER]
    if stas in auth or message.from_user.id != dev:
    	await app.ban_chat_member(message.chat.id,user)
    	await message.reply_text("- تم حظره من المجموعة .")
    else:
            await message.reply("- هذا الأمر يخص مشرفين المجموعة .")
            
@app.on_message(filters.regex("^الغاء حظر$") & filters.group)
async def ban3(_, message):
    user =message.reply_to_message.from_user.id
    stas = (await app.get_chat_member(message.chat.id, message.from_user.id)).status
    auth = [ChatMemberStatus.OWNER, ChatMemberStatus.OWNER]
    if stas in auth or message.from_user.id != dev:
    	await app.unban_chat_member(message.chat.id,user)
    	await message.reply_text("- تم الغاء حظره من المجموعة .")
    else:
            await message.reply("- هذا الأمر يخص مشرفين المجموعة .")
            
#%%%%%%%%%%%%%%%%%%%%%%
#Time Date 
@app.on_message(filters.regex("الساعه") & filters.group)
async def clock(_,message):
	now = datetime.now()
	now = (now.strftime('%I:%M'))
	await message.reply_text(f" - الساعة الأن : {now} ")
	
@app.on_message(filters.regex("^التاريخ$") & filters.group)
async def cl(_,message):
	now = datetime.now()
	now = (now.strftime("20%y/%m/%d"))
	await message.reply_text(f"نحن بتاريخ : {now} .")

#states 

@app.on_message(filters.regex("رتبتي") & filters.group)
async def rank(_,message):
   user = await message.chat.get_member(message.from_user.id)
   if user.status == ChatMemberStatus.OWNER:
      await message.reply("رتبتك › المالك")
   elif user.status == ChatMemberStatus.ADMINISTRATOR:
      await message.reply("رتبتك › المشرف")
   elif user.status == ChatMemberStatus.MEMBER:
      await message.reply("رتبتك › العضو")
      
      
#Check admin


@app.on_message(filters.regex("^المشرفين$"))
async def adlist(_, message):
    chat_id = message.chat.id
    admin = "- قائمة المشرفين\n— — — — —\n"
    async for admins in app.get_chat_members(chat_id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
           admin+=f"› {'@'+admins.user.username if admins.user.username else admins.user.mention} - `{admins.user.id}` .\n"
    await message.reply(text=(admin))
    
@app.on_message(filters.regex("^المحظورين$|^المحضورين$"))
async def banlist(_, message):
    chat_id = message.chat.id
    bb = "- قائمة المحظورين\n— — — — —\n"
    async for b in app.get_chat_members(chat_id, filter=enums.ChatMembersFilter.BANNED):
           bb+=f"› {'@'+b.user.username if b.user.username else b.user.mention} - `{b.user.id}` .\n"
    await message.reply(text=(bb))
    
@app.on_message(filters.regex("^المقيدين$|^المقيديين$"))
async def reslist(_, message):
    chat_id = message.chat.id
    bb = "- قائمة المقيدين\n— — — — —\n"
    async for b in app.get_chat_members(chat_id, filter=enums.ChatMembersFilter.RESTRICTED):
           bb+=f"› {'@'+b.user.username if b.user.username else b.user.mention} - `{b.user.id}` .\n"
    await message.reply(text=(bb))
    
@app.on_message(filters.regex("^البوتات$"))
async def botslist(_, message):
    chat_id = message.chat.id
    bb = "- قائمة البوتات\n— — — — —\n"
    async for b in app.get_chat_members(chat_id, filter=enums.ChatMembersFilter.BOTS):
           bb+=f"› {'@'+b.user.username if b.user.username else b.user.mention} - `{b.user.id}` .\n"
    await message.reply(text=(bb))

    
        
            
                
                    

#Stikers In Message




@app.on_message(filters.regex("") & filters.group)
def stiker(_,message): 
        stiker = "https"
        stiker1 = "https"
        stiker2 = ""
        stiker3 = ""
        stiker4 = ""
        stiker5 = ""
        stiker6 = ""
        stiker7 = ""
        stiker8 = ""
        stiker9 = ""
        
       
        app.send_sticker(message.chat.id,sticker=f"{stiker}")
       
@app.on_message(filters.regex("") & filters.group)
def stiker1(_,message): 
        app.send_sticker(message.chat.id,sticker=f"{stiker1}")
        
@app.on_message(filters.regex("") & filters.group)
def stiker2(_,message): 
        app.send_sticker(message.chat.id,sticker=f"{stiker2}")        

@app.on_message(filters.regex("") & filters.group)
def stiker3(_,message): 
        app.send_sticker(message.chat.id,sticker=f"{stiker3}")

@app.on_message(filters.regex("") & filters.group)
def stiker4(_,message): 
        app.send_sticker(message.chat.id,sticker=f"{stiker4}")
        
@app.on_message(filters.regex("") & filters.group)
def stiker5(_,message): 
        app.send_sticker(message.chat.id,sticker=f"{stiker5}")        
        
@app.on_message(filters.regex("") & filters.group)
def stiker6(_,message): 
        app.send_sticker(message.chat.id,sticker=f"{stiker6}")        
        
        
@app.on_message(filters.regex("") & filters.group)
def stiker7(_,message): 
        app.send_sticker(message.chat.id,sticker=f"{stiker7}")       
        
        
@app.on_message(filters.regex("") & filters.group)
def stiker8(_,message): 
        app.send_sticker(message.chat.id,sticker=f"{stiker8}")
        
@app.on_message(filters.regex("") & filters.group)
def stiker9(_,message): 
        app.send_sticker(message.chat.id,sticker=f"{stiker9}")
        
               
                             
        

print("welcome ....")
app.run()

