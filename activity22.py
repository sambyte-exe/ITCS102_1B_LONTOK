# STORY DESCRIPTION
story_description = """
SLAY THE GODS: SYNOPSIS

In a world where ancient gods from many mythologies have descended
and turned Earth into their battlefield, humanity is pushed to the edge
of extinction. Ordinary people cannot stand against divine power, but
a few chosen individuals inherit fragments of the gods' abilities and
become humanity's last line of defense.

Lin Qiye, a brave young man, is drawn into this hidden war and joins
the Night Fall squad, a group of gifted, strong-willed fighters. Together
with his teammates, he faces powerful gods, forms bonds with allies from
other organizations, and fights to protect humanity's future.
"""

print(story_description)

# SLAY THE GODS: CHARACTERS
night_fall = ['Lin Qiye', 'An Qingyu', 'Shen Qingzhu', 'Baili Pangpang', 'Cao Yuan', 'Jia Lan']
heavenly_gods = ['Nyx', 'Zeus', 'Poseidon', 'Hades', 'Athena', 'Sun Wukong', 'Michael', 'Bragi', 'Merlin', 'Gilgamesh']
masked_squad = ['Wang Mian', 'Tian Ping', 'Qiang Wei', 'Xuan Wo', 'Yue Gui']
night_watchers = ['Zhao Kongcheng', 'Hong Ying', 'Chen Muye', 'Leng Xuan']
divine_agents = ['Si Xiaonan', 'Shen Nu', 'Yiyu', 'Liu Lang', 'Shao Pingge', 'Lu Baoyu', 'Xia Simeng', 'Li Zhenzhen', 'Chen Han']

# CHARACTER DESCRIPTIONS

# THE NIGHT FALL SQUAD
Lin_Qiye = ["A brave young man who possesses Michael's divine power, along with the abilities of several other gods."]
An_Qingyu = ["A smart and curious genius who can control corpses and manipulate biological matter through his supernatural abilities."]
Shen_Qingzhu = ["A tough and rebellious fighter who possesses the power of smoke manipulation."]
Baili_Pangpang = ["A rich, funny, and friendly young man who possesses spatial abilities and can manipulate objects."]
Cao_Yuan = ["A quiet and serious fighter who possesses the dangerous power of the Black King."]
Jia_Lan = ["A cheerful and innocent immortal who possesses powerful divine abilities and extraordinary longevity."]

# THE HEAVENLY GODS
Nyx = ["Goddess of the Night."]
Zeus = ["King of the Greek Gods and God of Thunder."]
Poseidon = ["God of the Sea."]
Hades = ["God of the Underworld."]
Athena = ["Goddess of Wisdom and War."]
Sun_Wukong = ["The Monkey King, known for his strength and magic."]
Michael = ["Archangel who represents justice and divine power."]
Bragi = ["Norse God of Poetry and Music."]
Merlin = ["Legendary wizard known for his powerful magic."]
Gilgamesh = ["Legendary King of Uruk known for his strength and bravery."]

# THE MASKED SQUAD
Wang_Mian = ["A calm and intelligent leader who possesses the power of time manipulation and can control the flow of time."]
Tian_Ping = ["A skilled Masked Squad member known for his unique supernatural abilities and combat skills."]
Qiang_Wei = ["A brave and determined fighter who uses his special abilities to support his teammates in battle."]
Xuan_Wo = ["A dedicated fighter with supernatural powers who helps defend humanity against mysterious threats."]
Yue_Gui = ["A capable and loyal member of the Masked Squad who possesses unique abilities useful in combat."]

# THE NIGHT WATCHERS
Zhao_Kongcheng = ["A brave and experienced fighter who possesses powerful physical abilities and uses a pair of brass knuckles in battle."]
Hong_Ying = ["A cheerful and energetic young girl who possesses the divine power of the Red Moon and fights with a spear."]
Chen_Muye = ["A calm and experienced leader who possesses the power of Yanluo Wang and commands the abilities of the underworld."]
Leng_Xuan = ["A quiet and skilled Night Watcher known for his strong combat abilities and dedication to protecting humanity."]

# THE DIVINE AGENTS
Si_Xiaonan = ["A clever and mysterious fighter who possesses Loki's powers of deception and illusion."]
Shen_Nu = ["A mysterious divine agent whose abilities and background are connected to divine powers."]
Yiyu = ["A divine agent with unique supernatural abilities and a mysterious identity."]
Liu_Lang = ["A skilled and mysterious individual known for his unusual abilities and hidden identity."]
Shao_Pingge = ["A powerful fighter associated with Yanluo Wang who possesses abilities connected to the underworld."]
Lu_Baoyu = ["A divine agent of Lucifer who possesses powers related to corruption and darkness."]
Xia_Simeng = ["A wise and talented divine agent of Athena who possesses abilities related to wisdom and combat."]
Li_Zhenzhen = ["A divine agent of Cupid who possesses powers related to love and emotional manipulation."]
Chen_Han = ["A powerful divine agent associated with the Fengdu Emperor who possesses underworld-related abilities."]

# DICTIONARY OF CHARACTERS DESCRIPTIONS
night_fall = {"Lin Qiye": Lin_Qiye, "An Qingyu": An_Qingyu, "Shen Qingzhu": Shen_Qingzhu, "Baili Pangpang": Baili_Pangpang, "Cao Yuan": Cao_Yuan, "Jia Lan": Jia_Lan}
heavenly_gods = {"Nyx": Nyx, "Zeus": Zeus, "Poseidon": Poseidon, "Hades": Hades, "Athena": Athena, "Sun Wukong": Sun_Wukong, "Michael": Michael, "Bragi": Bragi, "Merlin": Merlin, "Gilgamesh": Gilgamesh}
masked_squad = {"Wang Mian": Wang_Mian, "Tian Ping": Tian_Ping, "Qiang Wei": Qiang_Wei, "Xuan Wo": Xuan_Wo, "Yue Gui": Yue_Gui}
night_watchers = {"Zhao Kongcheng": Zhao_Kongcheng, "Hong Ying": Hong_Ying, "Chen Muye": Chen_Muye, "Leng Xuan": Leng_Xuan}
divine_agents = {"Si Xiaonan": Si_Xiaonan, "Shen Nu": Shen_Nu, "Yiyu": Yiyu, "Liu Lang": Liu_Lang, "Shao Pingge": Shao_Pingge, "Lu Baoyu": Lu_Baoyu, "Xia Simeng": Xia_Simeng, "Li Zhenzhen": Li_Zhenzhen, "Chen Han": Chen_Han}

# CHARACTER REQUEST
character = input("Enter Character Name: ")

if character in divine_agents:
    print(character, "-", divine_agents[character][0])
elif character in heavenly_gods:
    print(character, "-", heavenly_gods[character][0])
elif character in masked_squad:
    print(character,"-", masked_squad[character][0])
elif character in night_fall:
    print(character, "-", night_fall[character][0])
elif character in night_watchers:
    print(character, "-", night_watchers[character][0])
else:
    print("Character not found.")

# DICTIONARY OF SQUADS DESCRIPTIONS
squads = {"Night Fall": night_fall,
"Heavenly Gods": heavenly_gods,
"Masked Squad": masked_squad,
"Night Watchers": night_watchers,
"Divine Agents": divine_agents}

# SQUAD NAME REQUEST 
squad_name = input("Enter Squad Name: ")

if squad_name in squads:
    print("\n" + squad_name.upper())
    for name, description in squads[squad_name].items():
        print(name, "-", description[0])

else:
    print('Squad not found.')
