
from __future__ import unicode_literals

import os
import time
from time import thread_time
import websockets
import asyncio
import json
import urllib
import random
import requests
from urllib.parse import urlencode
from requests_toolbelt.multipart.encoder import MultipartEncoder

import base64
import textwrap
from io import BytesIO
from datetime import date
from datetime import datetime


######### OTHERs ########
ID = "id"
NAME = "name"
USERNAME = "username"
PASSWORD = "password"
ROOM = "room"
TYPE = "type"
ROLE= "role"
HANDLER = "handler"
ALLOWED_CHARS = "0123456789abcdefghijklmnopqrstuvwxyz"
########## ------- ##########


########## SOCKET ########
SOCKET_URL = "wss://chatp.net:5333/server"
FILE_UPLOAD_URL = "https://cdn.talkinchat.com/post.php"

########## ------- ##########


######## MSGs #########
MSG_BODY = "body"
MSG_FROM = "from"
MSG_TO = "to"
MSG_TYPE_TXT = "text"
MSG_TYPE_IMG = "image"
MSG_TYPE_AUDIO = "audio"
MSG_URL = "url"
MSG_LENGTH = "length"
########## ------- ##########


######### Handlers #########
HANDLER_LOGIN = "login"
HANDLER_LOGIN_EVENT = "login_event"
HANDLER_ROOM_JOIN = "room_join"
HANDLER_ROOM_LEAVE = "room_leave"
HANDLER_ROOM_EVENT = "room_event"
HANDLER_ROOM_MESSAGE = "room_message"
HANDLER_CHAT_MESSAGE = "chat_message"
HANDLER_PROFILE_OTHER = "profile_other"
HANDLER_PROFILE_UPDATE = "profile_update"
EVENT_TYPE_SUCCESS = "success"
HANDLER_ROOM_ADMIN = "room_admin"
########## ------- ##########


######### CREDENTIALS AND ROOM SETTINGS - CHANGE THIS #########
BOT_MASTER_ID = "arya"
GROUP_TO_INIT_JOIN = "confession"
BOT_ID = "confession-bot"
BOT_MASTER = "arya"
BOT_PWD = "Zxcv1234."
########## ------- ##########

IMG_TYPE_PNG = "image/png"
IMG_TYPE_JPG = "image/jpeg"
IMG_BG_COLOR = "black"
TEXT_FONT_COLOR = "black"
AUDIO_DURATION = 0
last_played_song = None # LAST PLAYED SONG
LAST_MUSIC_URL = ''
IMG_TXT_FONTS = r'fonts/Merienda-Regular.ttf'
is_wc_on = False


COLOR_LIST = ["#F0F8FF","#FAEBD7","#FFEFDB","#EEDFCC","#CDC0B0","#8B8378","#00FFFF","#7FFFD4","#76EEC6","#66CDAA","#458B74","#F0FFFF","#E0EEEE","#C1CDCD","#838B8B","#E3CF57","#F5F5DC","#FFE4C4","#EED5B7","#CDB79E","#8B7D6B","#000000","#FFEBCD","#0000FF","#0000EE","#0000CD","#00008B","#8A2BE2","#9C661F","#A52A2A","#FF4040","#EE3B3B","#CD3333","#8B2323","#DEB887","#FFD39B","#EEC591","#CDAA7D","#8B7355","#8A360F","#8A3324","#5F9EA0","#98F5FF","#8EE5EE","#7AC5CD","#53868B","#FF6103","#FF9912","#ED9121","#7FFF00","#76EE00","#66CD00","#458B00","#D2691E","#FF7F24","#EE7621","#CD661D","#8B4513","#3D59AB","#3D9140","#808A87","#FF7F50","#FF7256","#EE6A50","#CD5B45","#8B3E2F","#6495ED","#FFF8DC","#EEE8CD","#CDC8B1","#8B8878","#DC143C","#00EEEE","#00CDCD","#008B8B","#B8860B","#FFB90F","#EEAD0E","#CD950C","#8B6508","#A9A9A9","#006400","#BDB76B","#556B2F","#CAFF70","#BCEE68","#A2CD5A","#6E8B3D","#FF8C00","#FF7F00","#EE7600","#CD6600","#8B4500","#9932CC","#BF3EFF","#B23AEE","#9A32CD","#68228B","#E9967A","#8FBC8F","#C1FFC1","#B4EEB4","#9BCD9B","#698B69","#483D8B","#2F4F4F","#97FFFF","#8DEEEE","#79CDCD","#528B8B","#00CED1","#9400D3","#FF1493","#EE1289","#CD1076","#8B0A50","#00BFFF","#00B2EE","#009ACD","#00688B","#696969","#1E90FF","#1C86EE","#1874CD","#104E8B","#FCE6C9","#00C957","#B22222","#FF3030","#EE2C2C","#CD2626","#8B1A1A","#FF7D40","#FFFAF0","#228B22","#DCDCDC","#F8F8FF","#FFD700","#EEC900","#CDAD00","#8B7500","#DAA520","#FFC125","#EEB422","#CD9B1D","#8B6914","#808080","#030303","#1A1A1A","#1C1C1C","#1F1F1F","#212121","#242424","#262626","#292929","#2B2B2B","#2E2E2E","#303030","#050505","#333333","#363636","#383838","#3B3B3B","#3D3D3D","#404040","#424242","#454545","#474747","#4A4A4A","#080808","#4D4D4D","#4F4F4F","#525252","#545454","#575757","#595959","#5C5C5C","#5E5E5E","#616161","#636363","#0A0A0A","#666666","#6B6B6B","#6E6E6E","#707070","#737373","#757575","#787878","#7A7A7A","#7D7D7D","#0D0D0D","#7F7F7F","#828282","#858585","#878787","#8A8A8A","#8C8C8C","#8F8F8F","#919191","#949494","#969696","#0F0F0F","#999999","#9C9C9C","#9E9E9E","#A1A1A1","#A3A3A3","#A6A6A6","#A8A8A8","#ABABAB","#ADADAD","#B0B0B0","#121212","#B3B3B3","#B5B5B5","#B8B8B8","#BABABA","#BDBDBD","#BFBFBF","#C2C2C2","#C4C4C4","#C7C7C7","#C9C9C9","#141414","#CCCCCC","#CFCFCF","#D1D1D1","#D4D4D4","#D6D6D6","#D9D9D9","#DBDBDB","#DEDEDE","#E0E0E0","#E3E3E3","#171717","#E5E5E5","#E8E8E8","#EBEBEB","#EDEDED","#F0F0F0","#F2F2F2","#F7F7F7","#FAFAFA","#FCFCFC","#008000","#00FF00","#00EE00","#00CD00","#008B00","#ADFF2F","#F0FFF0","#E0EEE0","#C1CDC1","#838B83","#FF69B4","#FF6EB4","#EE6AA7","#CD6090","#8B3A62","#CD5C5C","#FF6A6A","#EE6363","#CD5555","#8B3A3A","#4B0082","#FFFFF0","#EEEEE0","#CDCDC1","#8B8B83","#292421","#F0E68C","#FFF68F","#EEE685","#CDC673","#8B864E","#E6E6FA","#FFF0F5","#EEE0E5","#CDC1C5","#8B8386","#7CFC00","#FFFACD","#EEE9BF","#CDC9A5","#8B8970","#ADD8E6","#BFEFFF","#B2DFEE","#9AC0CD","#68838B","#F08080","#E0FFFF","#D1EEEE","#B4CDCD","#7A8B8B","#FFEC8B","#EEDC82","#CDBE70","#8B814C","#FAFAD2","#D3D3D3","#FFB6C1","#FFAEB9","#EEA2AD","#CD8C95","#8B5F65","#FFA07A","#EE9572","#CD8162","#8B5742","#20B2AA","#87CEFA","#B0E2FF","#A4D3EE","#8DB6CD","#607B8B","#8470FF","#778899","#B0C4DE","#CAE1FF","#BCD2EE","#A2B5CD","#6E7B8B","#FFFFE0","#EEEED1","#CDCDB4","#8B8B7A","#32CD32","#FAF0E6","#FF00FF","#EE00EE","#CD00CD","#8B008B","#03A89E","#800000","#FF34B3","#EE30A7","#CD2990","#8B1C62","#BA55D3","#E066FF","#D15FEE","#B452CD","#7A378B","#9370DB","#AB82FF","#9F79EE","#8968CD","#5D478B","#3CB371","#7B68EE","#00FA9A","#48D1CC","#C71585","#E3A869","#191970","#BDFCC9","#F5FFFA","#FFE4E1","#EED5D2","#CDB7B5","#8B7D7B","#FFE4B5","#FFDEAD","#EECFA1","#CDB38B","#8B795E","#000080","#FDF5E6","#808000","#6B8E23","#C0FF3E","#B3EE3A","#9ACD32","#698B22","#FF8000","#FFA500","#EE9A00","#CD8500","#8B5A00","#FF4500","#EE4000","#CD3700","#8B2500","#DA70D6","#FF83FA","#EE7AE9","#CD69C9","#8B4789","#EEE8AA","#98FB98","#9AFF9A","#90EE90","#7CCD7C","#548B54","#BBFFFF","#AEEEEE","#96CDCD","#668B8B","#DB7093","#FF82AB","#EE799F","#CD6889","#8B475D","#FFEFD5","#FFDAB9","#EECBAD","#CDAF95","#8B7765","#33A1C9","#FFC0CB","#FFB5C5","#EEA9B8","#CD919E","#8B636C","#DDA0DD","#FFBBFF","#EEAEEE","#CD96CD","#8B668B","#B0E0E6","#800080","#9B30FF","#912CEE","#7D26CD","#551A8B","#872657","#C76114","#FF0000","#EE0000","#CD0000","#8B0000","#BC8F8F","#FFC1C1","#EEB4B4","#CD9B9B","#8B6969","#4169E1","#4876FF","#436EEE","#3A5FCD","#27408B","#FA8072","#FF8C69","#EE8262","#CD7054","#8B4C39","#F4A460","#308014","#54FF9F","#4EEE94","#43CD80","#2E8B57","#FFF5EE","#EEE5DE","#CDC5BF","#8B8682","#5E2612","#8E388E","#C5C1AA","#71C671","#555555","#1E1E1E","#282828","#515151","#5B5B5B","#848484","#8E8E8E","#B7B7B7","#C1C1C1","#EAEAEA","#F4F4F4","#7D9EC0","#AAAAAA","#8E8E38","#C67171","#7171C6","#388E8E","#A0522D","#FF8247","#EE7942","#CD6839","#8B4726","#C0C0C0","#87CEEB","#87CEFF","#7EC0EE","#6CA6CD","#4A708B","#6A5ACD","#836FFF","#7A67EE","#6959CD","#473C8B","#708090","#C6E2FF","#B9D3EE","#9FB6CD","#6C7B8B","#FFFAFA","#EEE9E9","#CDC9C9","#8B8989","#00FF7F","#00EE76","#00CD66","#008B45","#4682B4","#63B8FF","#5CACEE","#4F94CD","#36648B","#D2B48C","#FFA54F","#EE9A49","#CD853F","#8B5A2B","#008080","#D8BFD8","#FFE1FF","#EED2EE","#CDB5CD","#8B7B8B","#FF6347","#EE5C42","#CD4F39","#8B3626","#40E0D0","#00F5FF","#00E5EE","#00C5CD","#00868B","#00C78C","#EE82EE","#D02090","#FF3E96","#EE3A8C","#CD3278","#8B2252","#808069","#F5DEB3","#FFE7BA","#EED8AE","#CDBA96","#8B7E66","#FFFFFF","#F5F5F5","#FFFF00","#EEEE00","#CDCD00","#8B8B00"]

def gen_random_str(length):
    return ''.join(random.choice(ALLOWED_CHARS) for i in range(length))


async def on_message(ws, data):

    global IMG_BG_COLOR
    global TEXT_FONT_COLOR
    #print(data)
        
    msg = data[MSG_BODY]
    frm = data[MSG_FROM]
    room = data[ROOM]
    user_avi = data['avatar_url']
    
    if frm == BOT_ID:
           return

    if user_avi is None:
        return

    if msg.startswith("help") or msg.startswith("Help") or msg.startswith("HELP"):
        await send_group_msg(ws, room, f"Welcome to Confession bot.\nCommands :\nCONFESS :  Set confess message \nACONFESS : Confess Anonymously\nABOUT : To know about bot")


    if msg.startswith("confess") or msg.startswith("CONFESS") or msg.startswith("Confess"):
        
        conf = msg[7:]
        currDate = date.today().strftime("%B %d, %Y ")
        currTime = datetime.now().strftime("%H:%M:%S")

        bottomText = "<br><br><br><b>Author : </b><i>" + frm +"</i><br><b>Time : </b><i> "+ currDate + currTime +"<br>"
        
        if conf is None:
            await send_group_msg(ws, room, "Type 'CONFESS MSG' to confess\Example :\nCONFESS I love someone" )
        else:
            await set_Subject(ws, room, "<b>Message : </b>" + conf + bottomText)
               



    if msg.startswith("aconfess") or msg.startswith("ACONFESS") or msg.startswith("Aconfess") or msg.startswith("AConfess"):
        
        conf = msg[8:]
        currDate = date.today().strftime("%B %d, %Y ")
        currTime = datetime.now().strftime("%H:%M:%S")
        
        bottomText =  "<br><br><br><b>Author : </b><i> Not Available</i><br><b>Time : </b><i> "+ currDate + currTime +"<br>"
        
        if conf is None:
            await send_group_msg(ws, room, "Type 'ACONFESS MSG' to confess anonymously\Example :\nACONFESS I love someone" )
        else:
            await set_Subject(ws, room, "<b>Message : </b>" + conf + bottomText)
               

    if msg.startswith("about") or msg.startswith("About") or msg.startswith("ABOUT"):
        await send_group_msg(ws, room, "Name : Confession Bot\nVersion : 1.0\nWritten in Python 🐍\nDeveloper : Void\nContact : https://t.me/voidrulz")




    if msg.startswith("owner") or msg.startswith("Owner") or msg.startswith("OWNER"):
        targetID = msg[5:]
        await setOwner(ws, room,targetID)
        await send_group_msg(ws, room, targetID + " is owner now.")




async def wc_user(ws, data):
    user = data[USERNAME]
    room = data[NAME]
    wcString = f"Hi {user} 😃\nWelcome to {room}\nI am a bot, helping people to confess their feelings 🙂\nType HELP to know more"
    await send_group_msg(ws, room, wcString)


async def grant_member(ws, data):
    user = data[USERNAME]
    room = data[NAME]
    print(data)
    await setMember(ws, room, user)



async def login(ws):
    jsonbody = {HANDLER: HANDLER_LOGIN, ID: gen_random_str(20), USERNAME: BOT_ID, PASSWORD: BOT_PWD}
    #print(jsonbody)
    await ws.send(json.dumps(jsonbody))


async def join_group(ws, group):
    jsonbody = {HANDLER: HANDLER_ROOM_JOIN, ID: gen_random_str(20), NAME: group}
    await ws.send(json.dumps(jsonbody))


async def rejoin_group(ws, group):
        await leave_group(ws, group)
        time.sleep(1)
        await join_group(ws, group)

def get_as_base64(url):
    return base64.b64encode(requests.get(url).content)

async def send_pvt_msg(ws):
    msg1 = get_as_base64("https://static.remove.bg/sample-gallery/graphics/bird-thumbnail.jpg")
    jsonbody = {HANDLER: HANDLER_CHAT_MESSAGE, ID: gen_random_str(20), MSG_TO: "docker", TYPE: MSG_TYPE_TXT, MSG_URL: "", MSG_BODY: f"Hello", MSG_LENGTH: ""}
    #jsonbody = {HANDLER: HANDLER_CHAT_MESSAGE, ID: gen_random_str(20), MSG_TO: "docker", type: "text", body: }
    await ws.send(json.dumps(jsonbody))




async def update_profile(ws, group, url):
    print(get_as_base64("https://static.remove.bg/sample-gallery/graphics/bird-thumbnail.jpg"))
    jsonbody = {HANDLER: HANDLER_PROFILE_UPDATE, ID: gen_random_str(20), TYPE: "photo", "value": ""}
    await ws.send(json.dumps(jsonbody))




async def send_group_msg(ws, room, msg):
    jsonbody = {HANDLER: HANDLER_ROOM_MESSAGE, ID: gen_random_str(20), ROOM: room, TYPE: MSG_TYPE_TXT, MSG_URL: "", MSG_BODY: msg, MSG_LENGTH: ""}
    await ws.send(json.dumps(jsonbody))

async def set_Subject(ws, room, msg):
    jsonbody = {HANDLER: HANDLER_ROOM_ADMIN, ID: gen_random_str(20),TYPE: "change_subject", ROOM: room,  "t_username" : msg, "t_role" : "none"}
    await ws.send(json.dumps(jsonbody))
     
 
async def setMember(ws, room, target):
    jsonbody = {HANDLER: HANDLER_ROOM_ADMIN, ID: gen_random_str(20),TYPE: "change_role", ROOM: room,  "t_username" : target, "t_role" : "member"}
    await ws.send(json.dumps(jsonbody))
     
            
async def setOwner(ws, room, target):
    jsonbody = {HANDLER: HANDLER_ROOM_ADMIN, ID: gen_random_str(20),TYPE: "change_role", ROOM: room,  "t_username" : target, "t_role" : "owner"}
    await ws.send(json.dumps(jsonbody))
     
         
        
         
          
           
            
              



async def start_bot():
    websocket = await websockets.connect(SOCKET_URL, ssl=True)
    await login(websocket)

    while True:
        if not websocket.open:
            try:
                websocket = await websockets.connect(SOCKET_URL, ssl=True)
                print('Websocket is NOT connected. Reconnecting...')
                await login(websocket)
            except websockets.exceptions.WebSocketException as ex:
                print("Error: " + ex)

        try:
            async for payload in websocket:
                if payload is not None:
                    data = json.loads(payload)
                    handler = data[HANDLER]

                    if handler == HANDLER_LOGIN_EVENT and data[TYPE] == EVENT_TYPE_SUCCESS:
                        print("Logged In SUCCESS")
                        await join_group(websocket, GROUP_TO_INIT_JOIN)

                
                    elif handler == HANDLER_ROOM_EVENT and data[TYPE] == MSG_TYPE_TXT:
                        await on_message(websocket, data)
  

                    if handler == HANDLER_ROOM_EVENT and data[TYPE] == "user_joined":
                        await wc_user(websocket, data)
                                         
 
                    if handler == HANDLER_ROOM_EVENT and data[TYPE] == "user_joined" and data[ROLE] == "none":
                        await grant_member(websocket, data)               

                    if handler == HANDLER_ROOM_EVENT and data[TYPE] == "you_joined" and data[USERNAME] == BOT_ID:
                        await send_group_msg(websocket, GROUP_TO_INIT_JOIN, "Ready!\nType HELP to get started")
       

                    if handler == HANDLER_ROOM_EVENT and data[TYPE] == "user_joined" and data[ROLE] == "owner":
                        await send_group_msg(websocket, GROUP_TO_INIT_JOIN, "Hi I am bot. confession bot. helping people to confess their feelings.\nGrant me owner to activate this bot")
 
 
                    if handler == HANDLER_ROOM_EVENT and data[TYPE] == "role_changed" and data["new_role"] == "owner" and data["t_username"]==BOT_ID:
                        await send_group_msg(websocket, GROUP_TO_INIT_JOIN,  data["actor"] + " Thank you for the owner 😃")
                        await rejoin_group(websocket, GROUP_TO_INIT_JOIN)
       
                

        except:
            print('Error receiving message from websocket.')

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_bot())
    loop.run_forever()
