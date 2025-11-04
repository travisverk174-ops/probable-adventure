import time
from colorama import Fore, Back, init, Style
init(autoreset=True)

a = (Fore.RED + f"The chamber fell silent.\n\
       \nBowser lay broken, his grotesque form crumbling into ash and molten stone.\n\
The throne behind him cracked and collapsed, sending a wave of dust through the air.\n\
The unnatural glow faded. The fire dimmed. The castle, once alive with rage, began to still.\n\
       \nMario stood in the center of it all, chest heaving, fists clenched.\n\
       \nHe looked around.\n\
       \nNo traps. No more monsters. No more echoes of Bowser’s twisted voice.\n\
       \nBut also… no Peach.\n\
       \nHe searched the chamber — behind the throne, beneath the rubble, through the hidden alcoves and sealed doors.\n\
Nothing. No sign of her. Not even a trace.\n\
       \nA chill crept in.\n\
       \nHad she ever been here?\n\
       \nThe castle had led him through pain and illusion, through healing and horror.\n\
       \nEvery path had converged on Bowser — but what if Bowser had been guarding something else?\n\
Or… nothing at all?\n\
       \nMario stepped back into the hall, the massive door still open behind him.\n\
The statues watched in silence. The obsidian floor reflected his weary face.\n\
       \nHe didn’t speak.\n\
       \nThere was no one left to answer.\n\
       \nAnd as he walked away, the castle began to shift — not collapsing, but changing.\n\
The walls pulsed once more, faintly, like a heartbeat slowing down.\n\
The rage was gone. But something deeper remained.\n\
       \nA mystery.\n\
       \nA question.\n\
       \nA name.\n\
       \n{Style.BRIGHT + Fore.MAGENTA + 'Peach.'}")

for chr in a:
    print(Fore.RED + chr, end="", flush=True)
    time.sleep(0.05)


