import random
import functools

rooms = [
    "level0 you noclip non-linear space, resembling the back rooms of a retail outlet.",
    "level1 you noclip into a massive warehouse with concrete floors and walls, exposed rebar, dim fluorescent lights placed on the walls and a low-hanging fog with no discernible source.",
    "level2 consists mainly of dark, grey, concrete maintenance tunnels, stretching on for millions of miles. The walls are lined with pipes and occasionally ventilation ducts, which often contain a thick viscous black liquid. desc",
    "level3 you walk into series of long, dark, twisting hallways",
    "level4 you find a empty office building, though it is almost completely devoid of furniture",
    "level5 you find mostly clean with little dust and dirt lingering on surfaces.",
    "level6 you walk into a really dark area,It consists of small to medium sized stone brick rooms and hallways, with the occasional metal bridge above a large gap.",
    "level7 you find an impossibly large ocean that seems to stretch infinitely in all directions.",
    "level8 you findhuge caverns and small cave systems that twist and turn like normal underground systems with almond water on walls",
    "level9 you go into an infinite suburban area at midnight.",
    "Manila Room he Manila Room features loud fluorescent lights. The lights of The Manila Room are very warm in color: almost a deep orange. They gradually vary in luminosity over time. Psychological and mood-related issues correlate with the intensity of the light. The Manila Room can be accessed at random from Level 0; either by a discreet entrance or via noclipping, in which case the room may be completely sealed off from the inside. This room is uneventful and at most will generate with a small wooden table and a few scattered chairs near its center. The walls of The Manila Room are also very thick, however, it is speculated that there is a sort of open space within or just beyond them.", 
    "level 11 a infinitly large  farm of wheat it's seems like it's edible"
]
room_count = len(rooms)

directions = [
    "left",
    "right",
    "forward",
    "backwards",
    "backwards to the right",
    "backwards to the left",
    "forwards to the right",
    "forwards to the left",
    "upwards",
    "upwards to the right",
    "upwards to the left",
    "upwards to the front",
    "upwards to the back",
    "downwards",
    "downwards to the left",
    "downwards to the right",
    "downwards to the front",
    "downwards to the back",
    "forwards",
    "you cant type this kugfrahuhfbruygifiuterfyutrfguregfryerfghheuugf'''';l;;l[p[lp[p0l/l.lp/.'p/l-o;p';..ppp.;;.pp;p;.l;;l;;;l;l;;dvsdrhgtfcdrgvyzityg 5ieygzmgteYLUEvyjtzVGUnFVuyIGB vz,u˚≤jnv n,k,l,,fkuymbbbkbhkhuuhhyhyhyhhjjjiehbhhhuhuhyhhrhuhroghfonuywrgnrt8owuhtijhiturhotrjiyhwoithjrithwhthjivti4whtj5oithjro9ohtirukhglirtudhyrtniuhgnrtidjgn9ruhgihuirhuyrgoyrghoujjnnjkrnghjbtkghbnrktuhbthrujbmn˝˝˝˝˝˝˝˝˝˝˝˝˝˝˝˝˝˝˝GKK˝˝gK˝˝˝Gkkk©˝k˝Jk©˚˚©©©©©˙©ƒ©ƒ©˙˙©∆˜¥©˙¥ƒ®˙ƒ®¥©¨∞ˆΩ®†††´®††††††††††††††††††††††††††††††††††",
    "you cant type this kugfrahuhfbruygifiuterfyutrfguregfryerfghheuugf'''';l;;l[p[lp[p0l/l.lp/.'p/l-o;p';..ppp.;;.pp;p;.l;;l;;;l;l;;dvsdrhgtfcdrgvyzityg 5ieygzmgteYLUEvyjtzVGUnFVuyIGB vz,u˚≤jnv n,k,l,,fkuymbbbkbhkhuuhhyhyhyhhjjjiehbhhhuhuhyhhrhuhroghfonuywrgnrt8owuhtijhiturhotrjiyhwoithjrithwhthjivti4whtj5oithjro9ohtirukhglirtudhyrtniuhgnrtidjgn9ruhgihuirhuyrgoyrghoujjnnjkrnghjbtkghbnrktuhbthrujbmn˝˝˝˝˝˝˝˝˝˝˝˝˝˝˝˝˝˝˝GKK˝˝gK˝˝˝Gkkk©˝k˝Jk©˚˚©©©©©˙©ƒ©ƒ©˙˙©∆˜¥©˙¥ƒ®˙ƒ®¥©¨∞ˆΩ®†††´®††††††††††††††††††††††††††††††††††"
]

def enter_room(current_room):
    print(rooms[current_room])

def get_random_exits():
    random_directions = random.sample(directions, random.randint(2, 5))
    print(f"There are {len(random_directions)} exits, please choose a direction to go:")

    def generate_exit(acc, direction):
        print(f"- {direction}")
        acc[direction] = random.randint(0, room_count - 1)
        return acc

    return functools.reduce(generate_exit, random_directions, {})

