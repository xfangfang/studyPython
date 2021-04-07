#!/usr/bin/env PYTHONIOENCODING=UTF-8 python3

# xbar Metadata
# <xbar.title>WeSing 全民K歌</xbar.title>
# <xbar.version>v1.0</xbar.version>
# <xbar.author>Fang Yuecheng</xbar.author>
# <xbar.author.github>xfangfang</xbar.author.github>
# <xbar.desc>Play songs from WeSing</xbar.desc>
# <xbar.image>https://raw.githubusercontent.com/15cm/bitbar-plugin/master/aria2/screenshot.png</xbar.image>
# <xbar.dependencies>python3,requests,requests_futures,playsound</xbar.dependencies>
# <xbar.abouturl>https://github.com/15cm/bitbar-plugin/tree/master/aria2</xbar.abouturl>
# <xbar.var>string(VAR_ID="64999a87232a308d"): User ID. (String of length 16) </xbar.var>

import re
import os
import sys
import json
import math
import time
import random
import datetime
import requests
from playsound import playsound
from requests_futures.sessions import FuturesSession
from concurrent.futures import as_completed

USERID = os.getenv('VAR_ID')

class jsonEnconding(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Song):
            data = {
                'shareid': o.shareid,
                'time': o.time,
                'title': o.title
            }
            return data
        return o.__dict__

class Object():
    session = requests.Session()
    future_session = FuturesSession(session=session)
    CACHE_PATH = '{}/.we_sing_cache'.format(os.path.expanduser('~'))
    SETTING_CACHE = '{}/setting.json'.format(CACHE_PATH)
    NUM_PER_PAGE = 15
    REQUEST_WORKERS = 4
    UPDATE_TIME = 86400 # 86400 = 1 day

    @property
    def headers(self):
        chrome_versions = [
        '74.0.3729.129',
        '76.0.3780.3',
        '76.0.3780.2',
        '74.0.3729.128',
        '76.0.3780.1',
        '76.0.3780.0',
        '75.0.3770.15']
        return {
            'Host': 'node.kg.qq.com',
            'Referer': 'node.kg.qq.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ' + \
                '(KHTML, like Gecko) Chrome/{} Safari/537.3'.format(random.choice(chrome_versions))
            }

    def getText(self, url):
        return self.session.get(url, headers=self.headers).text
    
    @staticmethod
    def timeConverter(unixTime):
        dateArray = datetime.datetime.utcfromtimestamp(unixTime)
        return dateArray.strftime("%Y/%m/%d %H:%M:%S")

    @staticmethod
    def createCacheDir():
        if not os.path.exists(Player.CACHE_PATH):
            os.makedirs(Player.CACHE_PATH)

class Song(Object):
    def __init__(self, shareid, time=0, title='', avatar='', play_url='', play_url_video=''):
        self.avatar = avatar
        self.title = title.replace('&#39;',"'")
        self.time = time
        self.shareid = shareid
        self.play_url = play_url
        self.play_url_video = play_url_video
        
    def getPlayUrl(self):
        if self.play_url != '': return self.play_url
        if self.play_url_video != '': return self.play_url_video
        content = self.getText('https://node.kg.qq.com/play?s={}'.format(self.shareid))
        self.play_url = re.findall(r'playurl":"(.*?)",', content)[0]
        self.play_url_video = re.findall(r'playurl_video":"(.*?)","', content)[0]
        return self.play_url_video if self.play_url == '' else self.play_url
    
    def getContent(self):
        return self.session.get(self.getPlayUrl()).content

    def __repr__(self):
        return "{} - {}".format(self.timeConverter(self.time), self.title)

    def __lt__(self, other):
            return self.time > other.time
        
class Player(Object):
    
    def __init__(self, userid, total_num = 0, nick_name = '', age = 0, gender=2):
        self.total_num = total_num
        self.userid = userid
        self.nick_name = nick_name
        self.age = age
        self.gender = gender
        self.playlist = []
        
    def _getInfo(self, page):
        url = "https://node.kg.qq.com/cgi/fcgi-bin/kg_ugc_get_homepage?type=get_uinfo&" + \
            "start={}&num={}&share_uid={}&callback=MusicJsonCallback".format(page, self.NUM_PER_PAGE, self.userid)
        content = self.getText(url)
        data = re.findall(r'[(](.*)[)]', content)[0]
        return json.loads(data)['data']
    
    def _getInfoAsync(self, page):
        url = "https://node.kg.qq.com/cgi/fcgi-bin/kg_ugc_get_homepage?type=get_uinfo&" + \
            "start={}&num={}&share_uid={}&callback=MusicJsonCallback".format(page, self.NUM_PER_PAGE, self.userid)
        return self.future_session.get(url, headers = self.headers)
        
    def _addDateToPlaylist(self, songs_data_list):
        for data in songs_data_list:
            song = Song(data['shareid'], data['time'], data['title'], data['avatar'])
            self.playlist.append(song)

    @staticmethod
    def createCacheDir():
        if not os.path.exists(Player.CACHE_PATH):
            os.makedirs(Player.CACHE_PATH)
            
    def createSongCacheDir(self):
        Player.createCacheDir()
        song_cache_dir = '{}/{}'.format(self.CACHE_PATH, self.userid)
        if not os.path.exists(song_cache_dir):
            os.makedirs(song_cache_dir)

    
    def save(self):
        self.createSongCacheDir()
        user_profile_path = "{}/user_{}.json".format(self.CACHE_PATH, self.userid)
        with open(user_profile_path,'w',encoding='utf-8') as f:
            json.dump(obj = self, fp = f, cls = jsonEnconding, ensure_ascii=False)
            
    def saveSong(self, song):
        self.createSongCacheDir()
        song_path = '{}/{}/{}.m4a'.format(Player.CACHE_PATH, self.userid, song.shareid)
        if os.path.exists(song_path): return song_path
        with open(song_path, 'wb') as f:
            f.write(song.getContent())
        return song_path

    @staticmethod
    def load(userid):
        Player.createCacheDir()
        user_profile_path = "{}/user_{}.json".format(Object.CACHE_PATH, userid)
        if not os.path.exists(user_profile_path): return None
        with open(user_profile_path, "r", encoding='utf-8') as f:
            d = json.load(fp=f)
        p = Player(d['userid'], d['total_num'], d['nick_name'], d['age'], d['gender'])
        for i in d['playlist']:
            p.playlist.append(Song(i['shareid'], i['time'], i['title']))
        return p

    
    def getPlaylist(self):
        self.playlist = []
        content = self._getInfo(1)
        self.total_num = content['ugc_total_count']
        self.nick_name = content['nickname']
        self.age = content['age']
        self.gender = content['gender']
        if self.total_num == 0:
            return self.playlist
        self._addDateToPlaylist(content['ugclist'])
        total_page = math.ceil(self.total_num/self.NUM_PER_PAGE)
        
        futures=[self._getInfoAsync(i) for i in range(2, total_page+1)]
        p = 1
        for future in as_completed(futures):
            p += 1
            content = future.result().text
            data = re.findall(r'[(](.*)[)]', content)[0]
            self._addDateToPlaylist(json.loads(data)['data']['ugclist'])
        self.playlist.sort()
        return self.playlist
    
    def __repr__(self):
        userinfo = "name:{} gender:{} age:{}\n".format(self.nick_name, self.gender, self.age)
        for index, song in enumerate(self.playlist):
            userinfo += "{} {}\n".format(index + 1, song)
        return userinfo

# Ascend
# Dsescend
# Random
# Single
class Setting(Object):
    def __init__(self, loop='Ascend', current='', currentid='', current_userid='', showtime=False, shownotify=True, lastupdate=0):
        self.loop = loop
        self.current = current
        self.currentid = currentid
        self.showtime = showtime
        self.shownotify = shownotify
        self.lastupdate = lastupdate
        self.current_userid = current_userid

    def save(self):
        self.createCacheDir()
        with open(self.SETTING_CACHE,'w',encoding='utf-8') as f:
            json.dump(obj = self, fp = f, cls = jsonEnconding, ensure_ascii=False)

    @staticmethod
    def load():
        if not os.path.exists(Setting.SETTING_CACHE): return None
        with open(Setting.SETTING_CACHE, "r",encoding='utf-8') as f:
            d = json.load(fp=f)
        return Setting(d['loop'], d['current'], d['currentid'], d['current_userid'], d['showtime'],\
             d['shownotify'], d['lastupdate'])

def refreshPlugin():
    os.system("open -jg \'xbar://app.xbarapp.com/refreshPlugin?path={}\'".format(sys.argv[0]))

def killAll():
    def is_number(s):
        try:
            int(s)
            return True
        except ValueError:
            pass
        return False

    def getProcess():
        cmd = r'ps -ef | grep we_sing.*.py'
        res = os.popen(cmd).readlines()
        pids = []
        for line in res:
            if 'grep' in line: continue
            pid = line.split()[1]
            time = line.split()[-1]
            if is_number(time):
                pids.append((pid, time))
            else:
                pids.append((pid, 9999999999))
        return pids

    def killProcess(pid):
        cmd = "kill -9 {}".format(pid)
        rc = os.system(cmd)
        if rc != 0 : return False
        return True

    pids = getProcess()
    pids = sorted(pids, key=lambda x: int(x[1]))
    if len(pids) > 0: pids.pop()
    for p in pids:
        killProcess(p[0])

def notify(setting, title, content):
    if not setting.shownotify : return
    os.system("osascript -e \'display notification \"{}\" with title \"{}\"\'".format(content, title))

def play(setting, index):
    def findIndexByID(playlist, id):
        for i, song in enumerate(playlist):
            if song.shareid == id:
                return i
        return 0
    def createPlaylist(playlist, song, loop, nextIndex = True):
        index = findIndexByID(playlist, song.shareid)
        if loop == 'Random':
            random.shuffle(playlist)
            if nextIndex:
                index = 0
            else:
                index = findIndexByID(playlist, song.shareid)
        elif loop == 'Descend':
            playlist.reverse()
            index = findIndexByID(playlist, song.shareid)
            if nextIndex:
                index += 1
                index %= len(playlist)
        elif loop == 'Single':
            playlist = [song]
            index = 0
        elif loop == 'Ascend':
            if nextIndex:
                index += 1
                index %= len(playlist)
        return playlist, index

    killAll()
    index = int(index)
    player = loadPlayer(setting)
    song = player.playlist[index]
    playlist, index = createPlaylist(player.playlist[:], song, setting.loop, nextIndex=False)
    song = playlist[index]

    while True:
        setting.current = song.title
        setting.currentid = song.shareid
        setting.save()
        last_setting = setting

        notify(setting, Object.timeConverter(song.time), song.title)
        refreshPlugin()
        path = player.saveSong(song)
        playsound(path, block=True)

        setting = loadSetting()
        if setting.loop != last_setting.loop:
            playlist, index = createPlaylist(player.playlist[:], song, setting.loop)
            song = playlist[index]
        else:
            index += 1
            index %= len(playlist)
            song = playlist[index]
        p = checkUpdateTime(setting)
        if p != None: player = p

def loadSetting():
    setting = None
    try:
        setting = Setting.load()
        if setting is not None and USERID is not None and setting.current_userid != USERID:
            killAll()
            setting.current_userid = USERID
            setting.currentid = ''
            setting.current = ''
            setting.save()
    except json.decoder.JSONDecodeError:
        pass
    finally:
        if setting is None:
            setting = Setting(current_userid=USERID)
            setting.save()
    return setting

def loadPlayer(setting, forceUpdate = False):
    def updateFromInternet():
        player = Player(USERID)
        try:
            player.getPlaylist()
            player.save()
        except KeyError:
            return None
        return player

    if forceUpdate:
        return updateFromInternet()

    player = None
    try:
        player = Player.load(setting.current_userid)
    except json.decoder.JSONDecodeError:
        pass
    finally:
        if player == None:
            player = updateFromInternet()    
    return player

def getDirSize(dir):
   size = 0
   for root, _, files in os.walk(dir):
      size += sum([os.path.getsize(os.path.join(root, name)) for name in files])
   return "{:.2f} MB".format(size/1048576)

def checkUpdateTime(setting):
    lastupdate = setting.lastupdate
    seconds = int(round(time.time()))
    if seconds - lastupdate > Setting.UPDATE_TIME :        
        player = loadPlayer(setting, True)
        if player != None:
            setting.lastupdate = seconds
            setting.save()
            return player
    return None

def cmd(title, p1, p2='nothing', refresh=False):
    current = int(round(time.time()))
    print("{} | shell='{}' param1={} param2={} param3={} terminal=false refresh={}".format(title, sys.argv[0], p1, p2, current, refresh))

def main():
    setting = loadSetting()
    if len(sys.argv) > 1:
        if sys.argv[1] == 'play':
            play(setting, sys.argv[2])
        elif sys.argv[1] == 'stop':
            killAll()
            text = "nothing" if setting.current == '' else setting.current
            notify(setting, "Stop", text)
            setting.current = ''
            setting.save()
        elif sys.argv[1] == 'loop':
            setting.loop = sys.argv[2]
            setting.save()
        elif sys.argv[1] == 'clear':
            killAll()
            os.system('rm -rf {}'.format(Object.CACHE_PATH))
        elif sys.argv[1] == 'notify':
            setting.shownotify = ( sys.argv[2] == 'Show')
            setting.save()
        elif sys.argv[1] == 'time':
            setting.showtime = ( sys.argv[2] == 'Show')
            setting.save()
        elif sys.argv[1] == 'update':
            player = Player(USERID)
            player.getPlaylist()
            player.save()
        return

    player = loadPlayer(setting)
    if player is None:
        print("Wrong UserID")
        print("---")
        print("Seting UserID | href=xbar://app.xbarapp.com/openPlugin?path={}".format(sys.argv[0]))
        return
    else:
        text = setting.current if setting.current != '' else player.nick_name
        print(text)
    print("---")
    print("Songs")
    print("---")
    for i, song in enumerate(player.playlist):
        if setting.showtime:
            song_name = "{}: {} {}".format(i+1, Object.timeConverter(song.time), song.title.replace("|", "/"))
        else:
            song_name = "{}: {}".format(i+1, song.title.replace("|", "/"))
        cmd("--{}".format(song_name), "play", i)
    cmd("Stop", "stop", refresh=True)
    print("Loop - {}".format(setting.loop))
    print("---")
    cmd("--Ascend", "loop", "Ascend", refresh=True)
    cmd("--Descend", "loop", "Descend", refresh=True)
    cmd("--Random", "loop", "Random", refresh=True)
    cmd("--Single", "loop", "Single", refresh=True)
    print("Settings")
    print("---")
    print("--UserID:{}".format(USERID))
    cmd("--Update Song list", "update", refresh=True)
    text = "Hide" if setting.shownotify else "Show"
    cmd("--{} Notification".format(text), "notify", text, refresh=True)
    text = "Hide" if setting.showtime else "Show"
    cmd("--{} PublishTime".format(text), "time", text, refresh=True)
    cmd("--Clear Cache: {}".format(getDirSize(Object.CACHE_PATH)), 'clear', refresh=True)
    print("--Seting UserID | href=xbar://app.xbarapp.com/openPlugin?path={}".format(sys.argv[0]))
    print("--Help | href=https://xfangfang.github.com")


if __name__ == "__main__":
    main()
