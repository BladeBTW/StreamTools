import requests
import lxml.html
import os
from PIL import Image, ImageFont, ImageDraw
import math



def absolutePath(__file__):
    "This function returns the directory path of the file being ran, the __file__ variable accepts __file__ inputs"
    return os.path.join(os.path.dirname(__file__))

def combat_level(stats):
    #1.	Take your Prayer level and divide it by two and round down
    base = math.trunc(stats[5]/2)
    #2.	Add this to your Hitpoints and Defence levels and divide the result by 4.
    base = (base+stats[3]+stats[1])/4
    #3. Add your Strength and Attack levels together and multiply by 0.325.
    melee = (stats[2]+stats[0])*0.325
    #Add this to your base combat level and you should have your melee combat level.
    #4.	If your Magic or Ranged level is exceptionally higher than your Attack and Strength,
    #carry on - in the calculation noted below Magic is used,
    #but if your Ranged is exceptionally higher, use that instead in all cases
    higher = stats[6]
    if (higher < stats[4]):
        higher = stats[4]
    if (higher > stats[0]+14 and higher > stats[2]+14):
    #5. Divide your Magic level by 2 and round down, and then add your Magic level again to this
        magic = math.trunc(higher/2)+higher
    #6. Multiply this by 0.325 and add the result to your base combat level calculated above,
    #and you should have your magic combat level
        magic = magic*0.325
        return "{0:0.1f}".format(base+magic)
    else:
         return "{0:0.1f}".format(base+melee)

absolutePath = absolutePath(__file__)

outputPath = "C:\\StreamImages\\Hiscores\\"

# sample text and font
unicode_text = u"Hello World!"
font = ImageFont.truetype("{}\\Reckoner.ttf".format(absolutePath), 18, encoding="unic")
# font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeMono.ttf", 28, encoding="unic")

# get the line size
text_width, text_height = font.getsize(unicode_text)


Accounts = ['Mystic Blade','Xeric Blade','Epic Blade','Magic Blade','Garlic Blade','Cyclic Blade','Irenic Blade','Lyric Blade','Agonic Blade','Arabic Blade','Auric Blade','Azoic Blade','Azotic Blade','Bardic Blade','Baric Blade','Boric Blade','Bromic Blade','Cadmic Blade','Calcic Blade','Ceric Blade','Citric Blade','Cleric Blade','Cultic Blade','Cupric Blade','Cyanic Blade','Dyadic Blade','Emic Blade','Erotic Blade','Ethnic Blade','Etic Blade','Felsic Blade','Gnomic Blade','Holmic Blade','Humic Blade','Iodic Blade','Ionic Blade','Iridic Blade','Laic Blade','Lithic Blade','Logic Blade','Mafic Blade','Mantic Blade','Melic Blade','Mimic Blade','Music Blade','Niobic Blade','Nitric Blade','Odic Blade','Ontic Blade','Orphic Blade','Osmic Blade','Oxalic Blade','Oxidic Blade','Ozonic Blade','Panic Blade','Photic Blade','Poetic Blade','Rhodic Blade','Sodic Blade','Steric Blade','Telic Blade','Terbic Blade','Thic Blade','Thoric Blade','Toluic Blade','Typic Blade','Uranic Blade','Vitric Blade','Yttric Blade','Zincic Blade','Mastic Blade','Pyric Blade','Pelvic Blade','Daric Blade','Sepic Blade','Limbic Blade','Picnic Blade','Mesic Blade','Civic Blade','Ethic Blade','Medic Blade','Ovonic Blade','Azonic Blade','Chemic Blade','Echoic Blade','Fustic Blade','Toric Blade','Conic Blade','Hemic Blade','Salic Blade','Biotic Blade','Hydric Blade','Axenic Blade','Syndic Blade','Critic Blade','Frolic Blade','Fabric Blade','Zoic Blade','Emetic Blade','Antic Blade','Ludic Blade']
HCIMAccounts = ['Heroic Blade']
UIMAccounts = ['BladeBTW']
GIMAccounts = ['Edenic Blade','Deific Blade','Ferric Blade','Exilic Blade','Orphic Blade']
IMAccounts = []
DeadmanModeAccounts = []
LeaguesAccounts = []
Tournamentaccounts = []

HiScoreList = ["Overall","Attack","Defence","Strength","Hitpoints","Ranged","Prayer","Magic","Cooking","Woodcutting","Fletching","Fishing","Firemaking","Crafting","Smithing","Mining","Herblore","Agility","Thieving","Slayer","Farming","Runecraft","Hunter","Construction","League Points","Bounty Hunter - Hunter","Bounty Hunter - Rogue","All Clue Scrolls","Beginner Clues","Easy Clues","Medium Clues","Hard Clues","Elite Clues","Master Clues","LMS - Rank","Abyssal Sire","Alchemical Hydra","Barrows Chests","Bryophyta","Callisto","Cerberus","Chambers of Xeric","Chambers of Xeric: Challenge Mode","Chaos Elemental","Chaos Fanatic","Commander Zilyana","Corporal Beast","Crazy Archaeologist","Dagannoth Prime","Dagannoth Rex","Dagannoth Supreme","Deranged Archaeologist","General Graardor","Giant Mole","Grotesque Guardians","Hespori","Kalphite Queen","King Black Dragon","Kraken","Kree'Arra","K'ril Tsutsaroth","Mimic","Nightmare","Obor","Sarachnis","Scorpia","Skotizo","The Gauntlet","The Corrupted Gauntlet","Theater of Blood","Thermonuclear Smoke Devil","TzKal-Zuk","TzTok-Jad","Venenatis","Vet'ion","Vorkath","Wintertodt","Zalcano","Zulrah","Combat"]

def returnText(HiscoreKeyList):
    if len(HiscoreKeyList)>0:
        msg = HiscoreKeyList[1]
        if msg == '-1':
            msg = '-'
    else:
        msg = '-'
    return msg
def loopthroughAccounts(AccountList,Mode):
    for account in AccountList:
        HiScoreDictionary = True
        list = True
        LeaguesList = True
        Leaguestext = True
        Leaguesbody = True
        Leagueshtml_string = True
        LeaguesURL = True
        if Mode == 'Normal':
            im = Image.open("{}\\Images\\Normal.png".format(absolutePath))
            URL = 'https://secure.runescape.com/m=hiscore_oldschool/index_lite.ws?player={}'.format(account)
        if Mode == 'IM':
            im = Image.open("{}\\Images\\IM.png".format(absolutePath))
            URL = 'https://secure.runescape.com/m=hiscore_oldschool_ironman/index_lite.ws?player={}'.format(account)
        if Mode == 'HCIM':
            im = Image.open("{}\\Images\\HCIM.png".format(absolutePath))
            URL = 'https://secure.runescape.com/m=hiscore_oldschool_hardcore_ironman/index_lite.ws?player={}'.format(account)
        if Mode == 'DMM':
            im = Image.open("{}\\Images\\DMM.png".format(absolutePath))
            URL = 'https://secure.runescape.com/m=hiscore_oldschool_deadman/index_lite.ws?player={}'.format(account)
        if Mode == 'Tournament':
            im = Image.open("{}\\Images\\Tournament.png".format(absolutePath))
            URL = 'https://secure.runescape.com/m=hiscore_oldschool_tournament/index_lite.ws?player={}'.format(account)
        if Mode == 'UIM':
            im = Image.open("{}\\Images\\UIM.png".format(absolutePath))
            URL = 'https://secure.runescape.com/m=hiscore_oldschool_ultimate/index_lite.ws?player={}'.format(account)
        if Mode == 'Leagues':
            URL = 'https://secure.runescape.com/m=hiscore_oldschool_seasonal/index_lite.ws?player={}'.format(account)
            im = Image.open("{}\\Images\\Leagues.png".format(absolutePath))
        html_string = requests.get(URL).content
        body = lxml.html.document_fromstring(html_string).find('body')
        text = body.text_content()
        list = text.splitlines()
        LeaguesURL = 'https://secure.runescape.com/m=hiscore_oldschool_seasonal/index_lite.ws?player={}'.format(account)
        Leagueshtml_string = requests.get(LeaguesURL).content
        Leaguesbody = lxml.html.document_fromstring(Leagueshtml_string).find('body')
        Leaguestext = Leaguesbody.text_content()
        LeaguesList = Leaguestext.splitlines()
        if len(LeaguesList)>0 and LeaguesList[0] != '':
             list[24] = LeaguesList[24]
        HiScoreDictionary = dict(zip(HiScoreList, list))
        # print('Account = {}'.format(account))
        # print('HiScoreDictionary = {}'.format(HiScoreDictionary))
        if len(HiScoreDictionary)>0:
            Numeric = True
            for key in HiScoreDictionary.values():
                if key == '':
                    Numeric = False
                HiscoreKeyList = []
                if ',' in key:
                    HiscoreKeyList = key.split(',')
                    for key in HiscoreKeyList:
                        if key.isnumeric() == False:
                            Numeric = False
            # print('Numeric = {}'.format(Numeric))
            if Numeric == True:
                # print('Numeric = {}'.format(Numeric))
                print('HiScoreDictionary = {}'.format(HiScoreDictionary))
                stats = [float(HiScoreDictionary['Attack'].split(',')[1]), float(HiScoreDictionary['Hitpoints'].split(',')[1]), float(HiScoreDictionary['Strength'].split(',')[1]),
                         float(HiScoreDictionary['Defence'].split(',')[1]), float(HiScoreDictionary['Ranged'].split(',')[1]), float(HiScoreDictionary['Prayer'].split(',')[1]),
                         float(HiScoreDictionary['Magic'].split(',')[1])]
                if stats[0]==(float(-1.0)):
                    # print('stats[0]==float(-1.0))')
                    combatlvl = '-'
                else:
                    # print('combatlvl calced through combat_level(stats)')
                    combatlvl = combat_level(stats)
                    # print('combatlvl = {}'.format(combatlvl))
                list.append('{},{},{}'.format(combatlvl,combatlvl,combatlvl))
        HiScoreDictionary = dict(zip(HiScoreList, list))

        font = ImageFont.truetype("{}\\Reckoner.ttf".format(absolutePath), 14, encoding="unic")
        d = ImageDraw.Draw(im)
        text_color = (255, 255, 255)
        for key in HiScoreDictionary:
            if key == 'League Points':
                W, H = (1182, 781)
                if ',' in HiScoreDictionary[key]:
                    HiscoreKeyList = HiScoreDictionary[key].split(',')
                    msg = returnText(HiscoreKeyList)
                else:
                    msg = '-'
                w, h = d.textsize(msg, font=font)
                w = w/2
                d.text(((W-w), H), msg, font=font, fill=text_color)
            if key == 'LMS - Rank':
                W, H = (1120, 781)
                if ',' in HiScoreDictionary[key]:
                    HiscoreKeyList = HiScoreDictionary[key].split(',')
                    msg = returnText(HiscoreKeyList)
                else:
                    msg = '-'
                w, h = d.textsize(msg, font=font)
                w = w/2
                d.text(((W-w), H), msg, font=font, fill=text_color)
            if key == 'All Clue Scrolls':
                W, H = (1244, 781)
                if ',' in HiScoreDictionary[key]:
                    HiscoreKeyList = HiScoreDictionary[key].split(',')
                    msg = returnText(HiscoreKeyList)
                else:
                    msg = '-'
                w, h = d.textsize(msg, font=font)
                w = w/2
                d.text(((W-w), H), msg, font=font, fill=text_color)
            if key == 'Combat':
                # print('Combat = {}'.format(HiScoreDictionary[key]))
                W, H = (738, 781)
                if ',' in HiScoreDictionary[key]:
                    HiscoreKeyList = HiScoreDictionary[key].split(',')
                    msg = returnText(HiscoreKeyList)
                else:
                    msg = '-'
                w, h = d.textsize(msg, font=font)
                w = w/2
                d.text(((W-w), H), msg, font=font, fill=text_color)
            if key == 'Overall':
                # print('Overall = {}'.format(HiScoreDictionary[key]))
                W, H = (800, 781)
                if ',' in HiScoreDictionary[key]:
                    HiscoreKeyList = HiScoreDictionary[key].split(',')
                    msg = returnText(HiscoreKeyList)
                else:
                    msg = '-'
                w, h = d.textsize(msg, font=font)
                w = w/2
                d.text(((W-w), H), msg, font=font, fill=text_color)
            if key == 'Beginner Clues':
                W, H = (685, 836)
                if ',' in HiScoreDictionary[key]:
                    HiscoreKeyList = HiScoreDictionary[key].split(',')
                    msg = returnText(HiscoreKeyList)
                else:
                    msg = '-'
                w, h = d.textsize(msg, font=font)
                d.text((W, H), msg, font=font, fill=text_color)
            if key == 'Attack':
                W, H = (685+(63*1), 836)
                if ',' in HiScoreDictionary[key]:
                    HiscoreKeyList = HiScoreDictionary[key].split(',')
                    msg = returnText(HiscoreKeyList)
                else:
                    msg = '-'
                w, h = d.textsize(msg, font=font)
                d.text((W, H), msg, font=font, fill=text_color)
            if key == 'Hitpoints':
                W, H = (685+(63*2), 836)
                if ',' in HiScoreDictionary[key]:
                    HiscoreKeyList = HiScoreDictionary[key].split(',')
                    msg = returnText(HiscoreKeyList)
                else:
                    msg = '-'
                w, h = d.textsize(msg, font=font)
                d.text((W, H), msg, font=font, fill=text_color)
            if key == 'Mining':
                W, H = (685+(63*3), 836)
                if ',' in HiScoreDictionary[key]:
                    HiscoreKeyList = HiScoreDictionary[key].split(',')
                    msg = returnText(HiscoreKeyList)
                else:
                    msg = '-'
                w, h = d.textsize(msg, font=font)
                d.text((W, H), msg, font=font, fill=text_color)
            if key == 'Abyssal Sire':
                W, H = (685+(63*4), 836)
                if ',' in HiScoreDictionary[key]:
                    HiscoreKeyList = HiScoreDictionary[key].split(',')
                    msg = returnText(HiscoreKeyList)
                else:
                    msg = '-'
                w, h = d.textsize(msg, font=font)
                d.text((W, H), msg, font=font, fill=text_color)
            if key == 'Chaos Elemental':
                W, H = (685+(63*5), 836)
                if ',' in HiScoreDictionary[key]:
                    HiscoreKeyList = HiScoreDictionary[key].split(',')
                    msg = returnText(HiscoreKeyList)
                else:
                    msg = '-'
                w, h = d.textsize(msg, font=font)
                d.text((W, H), msg, font=font, fill=text_color)
            if key == 'Dagannoth Supreme':
                W, H = (685 + (63 * 5), 986)
                if ',' in HiScoreDictionary[key]:
                    HiscoreKeyList = HiScoreDictionary[key].split(',')
                    msg = returnText(HiscoreKeyList)
                else:
                    msg = '-'
                w, h = d.textsize(msg, font=font)
                d.text((W, H), msg, font=font, fill=text_color)
            if key == "Kree'Arra":
                W, H = (685+(63*7), 836)
                if ',' in HiScoreDictionary[key]:
                    HiscoreKeyList = HiScoreDictionary[key].split(',')
                    msg = returnText(HiscoreKeyList)
                else:
                    msg = '-'
                w, h = d.textsize(msg, font=font)
                d.text((W, H), msg, font=font, fill=text_color)
            if key == "The Gauntlet":
                W, H = (685+(63*8), 836)
                if ',' in HiScoreDictionary[key]:
                    HiscoreKeyList = HiScoreDictionary[key].split(',')
                    msg = returnText(HiscoreKeyList)
                else:
                    msg = '-'
                w, h = d.textsize(msg, font=font)
                d.text((W, H), msg, font=font, fill=text_color)
            if key == "Vorkath":
                W, H = (685+(63*9), 836)
                if ',' in HiScoreDictionary[key]:
                    HiscoreKeyList = HiScoreDictionary[key].split(',')
                    msg = returnText(HiscoreKeyList)
                else:
                    msg = '-'
                w, h = d.textsize(msg, font=font)
                d.text((W, H), msg, font=font, fill=text_color)
            if key == "Easy Clues":
                W, H = (685 + (63 * 0), 866)
                if ',' in HiScoreDictionary[key]:
                    HiscoreKeyList = HiScoreDictionary[key].split(',')
                    msg = returnText(HiscoreKeyList)
                else:
                    msg = '-'
                w, h = d.textsize(msg, font=font)
                d.text((W, H), msg, font=font, fill=text_color)
            if key == "Strength":
                W, H = (685 + (63 * 1), 866)
                if ',' in HiScoreDictionary[key]:
                    HiscoreKeyList = HiScoreDictionary[key].split(',')
                    msg = returnText(HiscoreKeyList)
                else:
                    msg = '-'
                w, h = d.textsize(msg, font=font)
                d.text((W, H), msg, font=font, fill=text_color)
            if key == "Agility":
                W, H = (685 + (63 * 2), 866)
                if ',' in HiScoreDictionary[key]:
                    HiscoreKeyList = HiScoreDictionary[key].split(',')
                    msg = returnText(HiscoreKeyList)
                else:
                    msg = '-'
                w, h = d.textsize(msg, font=font)
                d.text((W, H), msg, font=font, fill=text_color)
            if key == "Smithing":
                W, H = (685 + (63 * 3), 866)
                if ',' in HiScoreDictionary[key]:
                    HiscoreKeyList = HiScoreDictionary[key].split(',')
                    msg = returnText(HiscoreKeyList)
                else:
                    msg = '-'
                w, h = d.textsize(msg, font=font)
                d.text((W, H), msg, font=font, fill=text_color)
            if key == "Medium Clues":
                W, H = (685 + (63 * 0), 896)
                if ',' in HiScoreDictionary[key]:
                    HiscoreKeyList = HiScoreDictionary[key].split(',')
                    msg = returnText(HiscoreKeyList)
                else:
                    msg = '-'
                w, h = d.textsize(msg, font=font)
                d.text((W, H), msg, font=font, fill=text_color)
            if key == "Defence":
                W, H = (685 + (63 * 1), 896)
                if ',' in HiScoreDictionary[key]:
                    HiscoreKeyList = HiScoreDictionary[key].split(',')
                    msg = returnText(HiscoreKeyList)
                else:
                    msg = '-'
                w, h = d.textsize(msg, font=font)
                d.text((W, H), msg, font=font, fill=text_color)
            if key == "Herblore":
                W, H = (685 + (63 * 2), 896)
                if ',' in HiScoreDictionary[key]:
                    HiscoreKeyList = HiScoreDictionary[key].split(',')
                    msg = returnText(HiscoreKeyList)
                else:
                    msg = '-'
                w, h = d.textsize(msg, font=font)
                d.text((W, H), msg, font=font, fill=text_color)
            if key == "Fishing":
                W, H = (685 + (63 * 3), 896)
                if ',' in HiScoreDictionary[key]:
                    HiscoreKeyList = HiScoreDictionary[key].split(',')
                    msg = returnText(HiscoreKeyList)
                else:
                    msg = '-'
                w, h = d.textsize(msg, font=font)
                d.text((W, H), msg, font=font, fill=text_color)
            if key == "Hard Clues":
                W, H = (685 + (63 * 0), 926)
                if ',' in HiScoreDictionary[key]:
                    HiscoreKeyList = HiScoreDictionary[key].split(',')
                    msg = returnText(HiscoreKeyList)
                else:
                    msg = '-'
                w, h = d.textsize(msg, font=font)
                d.text((W, H), msg, font=font, fill=text_color)
            if key == "Ranged":
                W, H = (685 + (63 * 1), 926)
                if ',' in HiScoreDictionary[key]:
                    HiscoreKeyList = HiScoreDictionary[key].split(',')
                    msg = returnText(HiscoreKeyList)
                else:
                    msg = '-'
                w, h = d.textsize(msg, font=font)
                d.text((W, H), msg, font=font, fill=text_color)
            if key == "Thieving":
                W, H = (685 + (63 * 2), 926)
                if ',' in HiScoreDictionary[key]:
                    HiscoreKeyList = HiScoreDictionary[key].split(',')
                    msg = returnText(HiscoreKeyList)
                else:
                    msg = '-'
                w, h = d.textsize(msg, font=font)
                d.text((W, H), msg, font=font, fill=text_color)
            if key == "Cooking":
                W, H = (685 + (63 * 3), 926)
                if ',' in HiScoreDictionary[key]:
                    HiscoreKeyList = HiScoreDictionary[key].split(',')
                    msg = returnText(HiscoreKeyList)
                else:
                    msg = '-'
                w, h = d.textsize(msg, font=font)
                d.text((W, H), msg, font=font, fill=text_color)
            if key == "Elite Clues":
                W, H = (685 + (63 * 0), 956)
                if ',' in HiScoreDictionary[key]:
                    HiscoreKeyList = HiScoreDictionary[key].split(',')
                    msg = returnText(HiscoreKeyList)
                else:
                    msg = '-'
                w, h = d.textsize(msg, font=font)
                d.text((W, H), msg, font=font, fill=text_color)
            if key == "Prayer":
                W, H = (685 + (63 * 1), 956)
                if ',' in HiScoreDictionary[key]:
                    HiscoreKeyList = HiScoreDictionary[key].split(',')
                    msg = returnText(HiscoreKeyList)
                else:
                    msg = '-'
                w, h = d.textsize(msg, font=font)
                d.text((W, H), msg, font=font, fill=text_color)
            if key == "Crafting":
                W, H = (685 + (63 * 2), 956)
                if ',' in HiScoreDictionary[key]:
                    HiscoreKeyList = HiScoreDictionary[key].split(',')
                    msg = returnText(HiscoreKeyList)
                else:
                    msg = '-'
                w, h = d.textsize(msg, font=font)
                d.text((W, H), msg, font=font, fill=text_color)
            if key == "Firemaking":
                W, H = (685 + (63 * 3), 956)
                if ',' in HiScoreDictionary[key]:
                    HiscoreKeyList = HiScoreDictionary[key].split(',')
                    msg = returnText(HiscoreKeyList)
                else:
                    msg = '-'
                w, h = d.textsize(msg, font=font)
                d.text((W, H), msg, font=font, fill=text_color)
            if key == "Master Clues":
                W, H = (685 + (63 * 0), 986)
                if ',' in HiScoreDictionary[key]:
                    HiscoreKeyList = HiScoreDictionary[key].split(',')
                    msg = returnText(HiscoreKeyList)
                else:
                    msg = '-'
                w, h = d.textsize(msg, font=font)
                d.text((W, H), msg, font=font, fill=text_color)
            if key == "Magic":
                W, H = (685 + (63 * 1), 986)
                if ',' in HiScoreDictionary[key]:
                    HiscoreKeyList = HiScoreDictionary[key].split(',')
                    msg = returnText(HiscoreKeyList)
                else:
                    msg = '-'
                w, h = d.textsize(msg, font=font)
                d.text((W, H), msg, font=font, fill=text_color)
            if key == "Fletching":
                W, H = (685 + (63 * 2), 986)
                if ',' in HiScoreDictionary[key]:
                    HiscoreKeyList = HiScoreDictionary[key].split(',')
                    msg = returnText(HiscoreKeyList)
                else:
                    msg = '-'
                w, h = d.textsize(msg, font=font)
                d.text((W, H), msg, font=font, fill=text_color)
            if key == "Woodcutting":
                W, H = (685 + (63 * 3), 986)
                if ',' in HiScoreDictionary[key]:
                    HiscoreKeyList = HiScoreDictionary[key].split(',')
                    msg = returnText(HiscoreKeyList)
                else:
                    msg = '-'
                w, h = d.textsize(msg, font=font)
                d.text((W, H), msg, font=font, fill=text_color)
            if key == "Bounty Hunter - Hunter":
                W, H = (685 + (63 * 0), 1016)
                if ',' in HiScoreDictionary[key]:
                    HiscoreKeyList = HiScoreDictionary[key].split(',')
                    msg = returnText(HiscoreKeyList)
                else:
                    msg = '-'
                w, h = d.textsize(msg, font=font)
                d.text((W, H), msg, font=font, fill=text_color)
            if key == "Runecraft":
                W, H = (685 + (63 * 1), 1016)
                if ',' in HiScoreDictionary[key]:
                    HiscoreKeyList = HiScoreDictionary[key].split(',')
                    msg = returnText(HiscoreKeyList)
                else:
                    msg = '-'
                w, h = d.textsize(msg, font=font)
                d.text((W, H), msg, font=font, fill=text_color)
            if key == "Slayer":
                W, H = (685 + (63 * 2), 1016)
                if ',' in HiScoreDictionary[key]:
                    HiscoreKeyList = HiScoreDictionary[key].split(',')
                    msg = returnText(HiscoreKeyList)
                else:
                    msg = '-'
                w, h = d.textsize(msg, font=font)
                d.text((W, H), msg, font=font, fill=text_color)
            if key == "Farming":
                W, H = (685 + (63 * 3), 1016)
                if ',' in HiScoreDictionary[key]:
                    HiscoreKeyList = HiScoreDictionary[key].split(',')
                    msg = returnText(HiscoreKeyList)
                else:
                    msg = '-'
                w, h = d.textsize(msg, font=font)
                d.text((W, H), msg, font=font, fill=text_color)
            if key == "Bounty Hunter - Rogue":
                W, H = (685 + (63 * 0), 1046)
                if ',' in HiScoreDictionary[key]:
                    HiscoreKeyList = HiScoreDictionary[key].split(',')
                    msg = returnText(HiscoreKeyList)
                else:
                    msg = '-'
                w, h = d.textsize(msg, font=font)
                d.text((W, H), msg, font=font, fill=text_color)
            if key == "Construction":
                W, H = (685 + (63 * 1), 1046)
                if ',' in HiScoreDictionary[key]:
                    HiscoreKeyList = HiScoreDictionary[key].split(',')
                    msg = returnText(HiscoreKeyList)
                else:
                    msg = '-'
                w, h = d.textsize(msg, font=font)
                d.text((W, H), msg, font=font, fill=text_color)
            if key == "Hunter":
                W, H = (685 + (63 * 2), 1046)
                if ',' in HiScoreDictionary[key]:
                    HiscoreKeyList = HiScoreDictionary[key].split(',')
                    msg = returnText(HiscoreKeyList)
                else:
                    msg = '-'
                w, h = d.textsize(msg, font=font)
                d.text((W, H), msg, font=font, fill=text_color)
            if key == 'Alchemical Hydra':
                W, H = (685+(63*4), 866)
                if ',' in HiScoreDictionary[key]:
                    HiscoreKeyList = HiScoreDictionary[key].split(',')
                    msg = returnText(HiscoreKeyList)
                else:
                    msg = '-'
                w, h = d.textsize(msg, font=font)
                d.text((W, H), msg, font=font, fill=text_color)
            if key == 'Chaos Fanatic':
                W, H = (685+(63*5), 866)
                if ',' in HiScoreDictionary[key]:
                    HiscoreKeyList = HiScoreDictionary[key].split(',')
                    msg = returnText(HiscoreKeyList)
                else:
                    msg = '-'
                w, h = d.textsize(msg, font=font)
                d.text((W, H), msg, font=font, fill=text_color)
            if key == 'General Graardor':
                W, H = (685+(63*6), 866)
                if ',' in HiScoreDictionary[key]:
                    HiscoreKeyList = HiScoreDictionary[key].split(',')
                    msg = returnText(HiscoreKeyList)
                else:
                    msg = '-'
                w, h = d.textsize(msg, font=font)
                d.text((W, H), msg, font=font, fill=text_color)
            if key == "K'ril Tsutsaroth":
                W, H = (685+(63*7), 866)
                if ',' in HiScoreDictionary[key]:
                    HiscoreKeyList = HiScoreDictionary[key].split(',')
                    msg = returnText(HiscoreKeyList)
                else:
                    msg = '-'
                w, h = d.textsize(msg, font=font)
                d.text((W, H), msg, font=font, fill=text_color)
            if key == "The Corrupted Gauntlet":
                W, H = (685+(63*8), 866)
                if ',' in HiScoreDictionary[key]:
                    HiscoreKeyList = HiScoreDictionary[key].split(',')
                    msg = returnText(HiscoreKeyList)
                else:
                    msg = '-'
                w, h = d.textsize(msg, font=font)
                d.text((W, H), msg, font=font, fill=text_color)
            if key == "Wintertodt":
                W, H = (685+(63*9), 866)
                if ',' in HiScoreDictionary[key]:
                    HiscoreKeyList = HiScoreDictionary[key].split(',')
                    msg = returnText(HiscoreKeyList)
                else:
                    msg = '-'
                w, h = d.textsize(msg, font=font)
                d.text((W, H), msg, font=font, fill=text_color)
            if key == "Barrows Chests":
                W, H = (685 + (63 * 4), 896)
                if ',' in HiScoreDictionary[key]:
                    HiscoreKeyList = HiScoreDictionary[key].split(',')
                    msg = returnText(HiscoreKeyList)
                else:
                    msg = '-'
                w, h = d.textsize(msg, font=font)
                d.text((W, H), msg, font=font, fill=text_color)
            if key == "Commander Zilyana":
                W, H = (685 + (63 * 5), 896)
                if ',' in HiScoreDictionary[key]:
                    HiscoreKeyList = HiScoreDictionary[key].split(',')
                    msg = returnText(HiscoreKeyList)
                else:
                    msg = '-'
                w, h = d.textsize(msg, font=font)
                d.text((W, H), msg, font=font, fill=text_color)
            if key == "Giant Mole":
                W, H = (685 + (63 * 6), 896)
                if ',' in HiScoreDictionary[key]:
                    HiscoreKeyList = HiScoreDictionary[key].split(',')
                    msg = returnText(HiscoreKeyList)
                else:
                    msg = '-'
                w, h = d.textsize(msg, font=font)
                d.text((W, H), msg, font=font, fill=text_color)
            if key == "Mimic":
                W, H = (685 + (63 * 7), 896)
                if ',' in HiScoreDictionary[key]:
                    HiscoreKeyList = HiScoreDictionary[key].split(',')
                    msg = returnText(HiscoreKeyList)
                else:
                    msg = '-'
                w, h = d.textsize(msg, font=font)
                d.text((W, H), msg, font=font, fill=text_color)
            if key == "Theater of Blood":
                W, H = (685 + (63 * 8), 896)
                if ',' in HiScoreDictionary[key]:
                    HiscoreKeyList = HiScoreDictionary[key].split(',')
                    msg = returnText(HiscoreKeyList)
                else:
                    msg = '-'
                w, h = d.textsize(msg, font=font)
                d.text((W, H), msg, font=font, fill=text_color)
            if key == "Zalcano":
                W, H = (685 + (63 * 9), 896)
                if ',' in HiScoreDictionary[key]:
                    HiscoreKeyList = HiScoreDictionary[key].split(',')
                    msg = returnText(HiscoreKeyList)
                else:
                    msg = '-'
                w, h = d.textsize(msg, font=font)
                d.text((W, H), msg, font=font, fill=text_color)
            if key == "Bryophyta":
                W, H = (685 + (63 * 4), 926)
                if ',' in HiScoreDictionary[key]:
                    HiscoreKeyList = HiScoreDictionary[key].split(',')
                    msg = returnText(HiscoreKeyList)
                else:
                    msg = '-'
                w, h = d.textsize(msg, font=font)
                d.text((W, H), msg, font=font, fill=text_color)
            if key == "Corporal Beast":
                W, H = (685+(63*6), 836)
                if ',' in HiScoreDictionary[key]:
                    HiscoreKeyList = HiScoreDictionary[key].split(',')
                    msg = returnText(HiscoreKeyList)
                else:
                    msg = '-'
                w, h = d.textsize(msg, font=font)
                d.text((W, H), msg, font=font, fill=text_color)
            if key == "Grotesque Guardians":
                W, H = (685 + (63 * 6), 926)
                if ',' in HiScoreDictionary[key]:
                    HiscoreKeyList = HiScoreDictionary[key].split(',')
                    msg = returnText(HiscoreKeyList)
                else:
                    msg = '-'
                w, h = d.textsize(msg, font=font)
                d.text((W, H), msg, font=font, fill=text_color)
            if key == "Nightmare":
                W, H = (685 + (63 * 7), 926)
                if ',' in HiScoreDictionary[key]:
                    HiscoreKeyList = HiScoreDictionary[key].split(',')
                    msg = returnText(HiscoreKeyList)
                else:
                    msg = '-'
                w, h = d.textsize(msg, font=font)
                d.text((W, H), msg, font=font, fill=text_color)
            if key == "Thermonuclear Smoke Devil":
                W, H = (685 + (63 * 8), 926)
                if ',' in HiScoreDictionary[key]:
                    HiscoreKeyList = HiScoreDictionary[key].split(',')
                    msg = returnText(HiscoreKeyList)
                else:
                    msg = '-'
                w, h = d.textsize(msg, font=font)
                d.text((W, H), msg, font=font, fill=text_color)
            if key == "Zulrah":
                W, H = (685 + (63 * 9), 926)
                if ',' in HiScoreDictionary[key]:
                    HiscoreKeyList = HiScoreDictionary[key].split(',')
                    msg = returnText(HiscoreKeyList)
                else:
                    msg = '-'
                w, h = d.textsize(msg, font=font)
                d.text((W, H), msg, font=font, fill=text_color)
            if key == "Callisto":
                W, H = (685 + (63 * 4), 956)
                if ',' in HiScoreDictionary[key]:
                    HiscoreKeyList = HiScoreDictionary[key].split(',')
                    msg = returnText(HiscoreKeyList)
                else:
                    msg = '-'
                w, h = d.textsize(msg, font=font)
                d.text((W, H), msg, font=font, fill=text_color)
            if key == "Crazy Archaeologist":
                W, H = (685 + (63 * 5), 926)
                if ',' in HiScoreDictionary[key]:
                    HiscoreKeyList = HiScoreDictionary[key].split(',')
                    msg = returnText(HiscoreKeyList)
                else:
                    msg = '-'
                w, h = d.textsize(msg, font=font)
                d.text((W, H), msg, font=font, fill=text_color)
            if key == "Hespori":
                W, H = (685 + (63 * 6), 956)
                if ',' in HiScoreDictionary[key]:
                    HiscoreKeyList = HiScoreDictionary[key].split(',')
                    msg = returnText(HiscoreKeyList)
                else:
                    msg = '-'
                w, h = d.textsize(msg, font=font)
                d.text((W, H), msg, font=font, fill=text_color)
            if key == "Obor":
                W, H = (685 + (63 * 7), 956)
                if ',' in HiScoreDictionary[key]:
                    HiscoreKeyList = HiScoreDictionary[key].split(',')
                    msg = returnText(HiscoreKeyList)
                else:
                    msg = '-'
                w, h = d.textsize(msg, font=font)
                d.text((W, H), msg, font=font, fill=text_color)
            if key == "TzKal-Zuk":
                W, H = (685 + (63 * 8), 956)
                if ',' in HiScoreDictionary[key]:
                    HiscoreKeyList = HiScoreDictionary[key].split(',')
                    msg = returnText(HiscoreKeyList)
                else:
                    msg = '-'
                w, h = d.textsize(msg, font=font)
                d.text((W, H), msg, font=font, fill=text_color)
            if key == "Cerberus":
                W, H = (685 + (63 * 4), 986)
                if ',' in HiScoreDictionary[key]:
                    HiscoreKeyList = HiScoreDictionary[key].split(',')
                    msg = returnText(HiscoreKeyList)
                else:
                    msg = '-'
                w, h = d.textsize(msg, font=font)
                d.text((W, H), msg, font=font, fill=text_color)
            if key == "Deranged Archaeologist":
                W, H = (685 + (63 * 5), 956)
                if ',' in HiScoreDictionary[key]:
                    HiscoreKeyList = HiScoreDictionary[key].split(',')
                    msg = returnText(HiscoreKeyList)
                else:
                    msg = '-'
                w, h = d.textsize(msg, font=font)
                d.text((W, H), msg, font=font, fill=text_color)
            if key == "Kalphite Queen":
                W, H = (685 + (63 * 6), 986)
                if ',' in HiScoreDictionary[key]:
                    HiscoreKeyList = HiScoreDictionary[key].split(',')
                    msg = returnText(HiscoreKeyList)
                else:
                    msg = '-'
                w, h = d.textsize(msg, font=font)
                d.text((W, H), msg, font=font, fill=text_color)
            if key == "Sarachnis":
                W, H = (685 + (63 * 7), 986)
                if ',' in HiScoreDictionary[key]:
                    HiscoreKeyList = HiScoreDictionary[key].split(',')
                    msg = returnText(HiscoreKeyList)
                else:
                    msg = '-'
                w, h = d.textsize(msg, font=font)
                d.text((W, H), msg, font=font, fill=text_color)
            if key == "TzTok-Jad":
                W, H = (685 + (63 * 8), 986)
                if ',' in HiScoreDictionary[key]:
                    HiscoreKeyList = HiScoreDictionary[key].split(',')
                    msg = returnText(HiscoreKeyList)
                else:
                    msg = '-'
                w, h = d.textsize(msg, font=font)
                d.text((W, H), msg, font=font, fill=text_color)
            if key == "Chambers of Xeric":
                W, H = (685 + (63 * 4), 1016)
                if ',' in HiScoreDictionary[key]:
                    HiscoreKeyList = HiScoreDictionary[key].split(',')
                    msg = returnText(HiscoreKeyList)
                else:
                    msg = '-'
                w, h = d.textsize(msg, font=font)
                d.text((W, H), msg, font=font, fill=text_color)
            if key == "Dagannoth Prime":
                W, H = (685 + (63 * 5), 1016)
                if ',' in HiScoreDictionary[key]:
                    HiscoreKeyList = HiScoreDictionary[key].split(',')
                    msg = returnText(HiscoreKeyList)
                else:
                    msg = '-'
                w, h = d.textsize(msg, font=font)
                d.text((W, H), msg, font=font, fill=text_color)
            if key == "King Black Dragon":
                W, H = (685 + (63 * 6), 1016)
                if ',' in HiScoreDictionary[key]:
                    HiscoreKeyList = HiScoreDictionary[key].split(',')
                    msg = returnText(HiscoreKeyList)
                else:
                    msg = '-'
                w, h = d.textsize(msg, font=font)
                d.text((W, H), msg, font=font, fill=text_color)
            if key == "Scorpia":
                W, H = (685 + (63 * 7), 1016)
                if ',' in HiScoreDictionary[key]:
                    HiscoreKeyList = HiScoreDictionary[key].split(',')
                    msg = returnText(HiscoreKeyList)
                else:
                    msg = '-'
                w, h = d.textsize(msg, font=font)
                d.text((W, H), msg, font=font, fill=text_color)
            if key == "Venenatis":
                W, H = (685 + (63 * 8), 1016)
                if ',' in HiScoreDictionary[key]:
                    HiscoreKeyList = HiScoreDictionary[key].split(',')
                    msg = returnText(HiscoreKeyList)
                else:
                    msg = '-'
                w, h = d.textsize(msg, font=font)
                d.text((W, H), msg, font=font, fill=text_color)
            if key == "Chambers of Xeric: Challenge Mode":
                W, H = (685 + (63 * 4), 1046)
                if ',' in HiScoreDictionary[key]:
                    HiscoreKeyList = HiScoreDictionary[key].split(',')
                    msg = returnText(HiscoreKeyList)
                else:
                    msg = '-'
                w, h = d.textsize(msg, font=font)
                d.text((W, H), msg, font=font, fill=text_color)
            if key == "Dagannoth Rex":
                W, H = (685 + (63 * 5), 1046)
                if ',' in HiScoreDictionary[key]:
                    HiscoreKeyList = HiScoreDictionary[key].split(',')
                    msg = returnText(HiscoreKeyList)
                else:
                    msg = '-'
                w, h = d.textsize(msg, font=font)
                d.text((W, H), msg, font=font, fill=text_color)
            if key == "Kraken":
                W, H = (685 + (63 * 6), 1046)
                if ',' in HiScoreDictionary[key]:
                    HiscoreKeyList = HiScoreDictionary[key].split(',')
                    msg = returnText(HiscoreKeyList)
                else:
                    msg = '-'
                w, h = d.textsize(msg, font=font)
                d.text((W, H), msg, font=font, fill=text_color)
            if key == "Skotizo":
                W, H = (685 + (63 * 7), 1046)
                if ',' in HiScoreDictionary[key]:
                    HiscoreKeyList = HiScoreDictionary[key].split(',')
                    msg = returnText(HiscoreKeyList)
                else:
                    msg = '-'
                w, h = d.textsize(msg, font=font)
                d.text((W, H), msg, font=font, fill=text_color)
            if key == "Vet'ion":
                W, H = (685 + (63 * 8), 1046)
                if ',' in HiScoreDictionary[key]:
                    HiscoreKeyList = HiScoreDictionary[key].split(',')
                    msg = returnText(HiscoreKeyList)
                else:
                    msg = '-'
                w, h = d.textsize(msg, font=font)
                d.text((W, H), msg, font=font, fill=text_color)
        print("{}{}_hiscore.png".format(outputPath, account))
        im.save("{}{}_hiscore.png".format(outputPath, account))
        # print("{}{}_hiscore.png".format(outputPath, account))
loop = True
count = 0
while loop==True:
    loopthroughAccounts(Accounts,'Normal')
    loopthroughAccounts(IMAccounts,'IM')
    loopthroughAccounts(HCIMAccounts,'HCIM')
    loopthroughAccounts(DeadmanModeAccounts,'DMM')
    loopthroughAccounts(Tournamentaccounts,'Tournament')
    loopthroughAccounts(UIMAccounts,'UIM')
    loopthroughAccounts(LeaguesAccounts,'Leagues')
    count+=1
    print(count)