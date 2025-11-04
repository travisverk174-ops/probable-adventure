from colorama import Fore, Back, init, Style
init(autoreset=True)


def intro_to_story():
    print(Fore.RED + "\n\n\n\n\n\n\n\n\n\nIn the cheerful lands of the Mushroom Kingdom, Mario was enjoying a quiet day.\n\
The skies were blue, the Goombas were unusually polite, and Princess Peach had invited him for tea.\n\
       \nBut when Mario jumped into a green pipe to head to the castle, something went wrong.\n\
The pipe shook and twisted, its walls alive and pulsing.\n\
Instead of arriving at the castle, Mario was thrown into a dark, strange world — \na place where the sun was gone and the stars whispered strange things.\n\
       \nMario landed hard. The pipe had spat him out into a cold, dripping sewer.\n\
The air was damp and foul, thick with the stench of rot.\n\
Faint green light pulsed from cracks in the walls, and the water below his feet was dark and sluggish.\n\
This wasn’t any sewer he’d seen before. The bricks were warped, covered in strange symbols that seemed to shift when he looked away.\n\
Pipes hung like vines from the ceiling, leaking black sludge. Somewhere in the distance, something growled — low and wet.\n\
       \nMario took a cautious step forward.\n\
His usual world was gone.\n\
No cheerful music, no bouncing blocks.\n\
Just silence, shadows, and the distant echo of Peach’s voice, calling for help.")
 
print("\n\nMario stood in the dripping sewer, the air thick with decay. Ahead, the tunnel split in two — left and right.\n\
To the left, a faint red glow caught his eye. To the right he could see something lying in the water.\n\
\n1. for left, 2. for right")

def sewer_hat():
    print(Fore.RED + f"\nMario turned left, drawn by the soft red glow in the distance.\n\
The sewer walls narrowed, dripping with black water and lined with strange, pulsing veins.\n\
Each step echoed like a warning.\n\
        \nThere, resting on a cracked stone pedestal, was his red hat.\n\
He hadn’t even realized it was gone — but now, seeing it again, something inside him stirred.\n\
It was more than cloth and thread. It was a piece of himself, a symbol of who he was before this nightmare began.\n\
        \nHe reached out and placed it back on his head.\n\
A faint red glow shimmered around him — not just light, but protection.\n\
The hat, now infused with something ancient and resilient, hardened his resolve and his body. {Style.BRIGHT + Fore.WHITE + '+10 Armor'}")
    

def sewer_wpn_pipe():
    print(Fore.RED + f"\nMario turned right, drawn by the object in the water.\n\
The tunnel widened slightly, the air growing heavier with each step.\n\
The walls here were cracked and bleeding rust, and the water swirled with strange, oily patterns.\n\
        \nHalf-submerged in the water lay a rusted metal pipe — thick, dented, but solid.\n\
Mario reached down and grabbed it.\n\
It was heavier than he expected, but it felt good in his hands.\n\
        \nAs he lifted it, the shadows around him seemed to pause.\n\
The pipe wasn’t just a weapon.\n\
It was a message: Mario wasn’t here to run or dodge. He was here to fight. {Style.BRIGHT + Fore.WHITE + '+10 Strength'}")

def text_after_sewer():
    print(Fore.RED + f"\n\nMario pressed onward, the narrow tunnel forcing him to crouch beneath dripping pipes and weave around loose stone.\n\
The walls were damp and stained, and the air carried a sour, metallic scent.\n\
There was no turning back — only a single path leading deeper into the sewer.\n\
       \nThe corridor twisted and dipped, lit by flickering patches of greenish light.\n\
Each step echoed briefly before fading into silence.\n\
The deeper he went, the more the world felt distant — like something familiar had been stripped away.\n\
       \nEventually, the tunnel opened into a circular chamber.\n\
The floor shimmered with black sludge, and broken bricks lined the edges like scattered bones.\n\
       \nIn the center stood a creature.\n\
       \n{Style.BRIGHT +'A corrupted Goomba.' + Style.RESET_ALL + Fore.RED}\n\
       \nIts bloated body leaked dark ooze.\n\
Red pits glowed where eyes should be, and jagged teeth twitched in its mouth.")

def goomba_defeated():
    print(Fore.RED + f"\n\n\n\n\nThe corrupted Goomba collapsed into the sludge, its twisted form dissolving into black mist.\n\
The chamber fell silent once more, but the air remained heavy, as if the fight had stirred something deeper.\n\
       \nMario stood in the center of the room, catching his breath. Ahead, the path split again.\n\
       \n{Fore.WHITE}To the left, a narrow tunnel stretched into the distance.\n\
A faint glimmer of light flickered at the far end.\n\
       \nTo the right, the passage curved sharply into darkness. From within came strange sounds.\n\
       \n1. for left, 2. for right")

def choice_after_goomba_garden():
    print(Fore.RED + f"Mario stepped out of the sewer and into sunlight.\n\
\nBefore him stretched a hillside garden, wild and beautiful —\n\
bursting with flowers in every color, swaying gently in the breeze.\n\
The air was fresh, tinged with lavender and soil\n\
Birds chirped somewhere above, and for a moment, the horrors of the sewer felt far away.\n\
        \nHe walked slowly through the garden, boots brushing against petals and soft grass.\n\
The path curved gently, leading him to another fork.\n\
        \n{Fore.WHITE}To the left, a glasshouse shimmered in the sun.\n\
Its panes were fogged and cracked, but inside he could see strange plants\n\
— some glowing faintly, others twisting toward the light.\n\
    \nTo the right, a compost bin sat beneath a crooked tree.\n\
It looked ordinary, but something about it felt off.\n\
The lid was slightly ajar, and faint steam rose from within.\n\
There was movement — slow, deliberate.\n\
    \n1. for left, 2. for right")

def garden_left1():
    print(Fore.RED + f"Mario stepped into the glasshouse.\n\
\nWarmth greeted him, thick with the scent of damp soil and blooming life.\n\
Sunlight filtered through cracked panes, casting fractured beams across a jungle of plants he had never seen before.\n\
some shimmered with vibrant color, others twisted unnaturally, their shapes bordering on grotesque.\n\
                  \nVines curled around rusted tools.\n\
Flowers opened and closed as if reacting to his presence.\n\
In the center of the room, nestled among glowing moss and thorny stalks, stood a mushroom unlike any he’d encountered.\n\
                  \nIts cap glowed faintly red, and tiny sparks danced along its edges.\n\
Something about it felt… important.\n\
                  \nWithout hesitation, Mario picked it and took a bite.\n\
                  \nA rush of heat surged through him. His grip steadied. His senses sharpened.{Style.BRIGHT + Fore.WHITE +' +5 Damage'}") # NOG +5 DAMAGE STAT OPTELLEN 

def garden_left2():
       print(Fore.RED + f"He stepped back through the cracked doorway, leaving behind the jungle of alien flora.\n\
                     \nOutside, the garden had shifted.\n\
                     \nThe sunlight was dimmer now, the breeze colder.\n\
       The path ahead was lined with stone tiles, half-buried in moss and petals.\n\
       As Mario walked, the flowers grew sparse, replaced by thorny shrubs and crooked trees.\n\
       The air smelled of rain and stone.\n\
                     \nHe passed a broken fountain, its water long dried, and a row of statues\n\
       — each one worn and faceless, their poses frozen in warning or grief.\n\
       The path narrowed, with tall hedges on either side rustling gently as Mario walked past.\n\
                     \nThen, the path ended.\n\
                     \nBefore him stood a castle.\n\
                     \nIts walls were carved from dark stone, towering and silent.\n\
       Ivy clung to the sides like veins, and the windows were empty.\n\
       The main door loomed ahead — massive, wooden, bound in iron.\n\
       A symbol was etched into its surface, glowing faintly red.\n\
                     \nMario stepped closer.\n\
                     \nWhatever waited inside, the mushroom’s strength pulsed in his limbs. He was ready.")

def garden_right():
    print(Fore.RED + f"Mario stepped off the garden path and approached the compost bin.\n\
                  \nSteam rose from its half-open lid, carrying a sour, earthy stench.\n\
Flies buzzed lazily around the rim, and the ground beneath was soft, almost too soft.\n\
Something wasn’t right.\n\
                  \nHe reached out to lift the lid—\n\
                  \n{Style.BRIGHT + 'It exploded open.' + Style.RESET_ALL + Fore.RED}\n\
                  \nA {Style.BRIGHT + 'Piranha Plant' + Style.RESET_ALL + Fore.RED} shot out, its jaws snapping inches from his face.\n\
This wasn’t the kind he’d faced before.\n\
Its stalk was thicker, its teeth longer, and its movements faster.\n\
Vines whipped outward, anchoring it to the ground as it reared back, hissing.\n\
    \nIts petals were torn and blackened, its mouth lined with jagged thorns.\n\
This thing had grown in rot, fed on decay — and it was hungry.\n\
    \nMario stepped back, heart pounding. This opponent was stronger than the last.\n\
Smarter. Meaner. And it wasn't going to wait.")

def piranha_defeated():
    print(Fore.RED + f"\nThe Piranha Plant let out a final hiss before collapsing into the compost, its vines twitching once before going still.\n\
Mario stepped back, breathing hard, the adrenaline still humming in his veins.\n\
The garden around him was quiet again, but the air felt different — like something had shifted.\n\
                  \nHe moved past the compost bin and followed a narrow trail that wound uphill through a grove of twisted trees.\n\
Their bark was pale and smooth, almost like bone, and their branches arched overhead,\n\
forming a canopy that filtered the sunlight into eerie patterns on the ground.\n\
                  \nAs he walked, the flowers thinned, replaced by patches of dry grass and stone.\n\
The warmth faded. The wind picked up, carrying a low hum\n\
                  \nEventually, the trail ended.\n\
                  \nBefore him stood a {Style.BRIGHT + 'castle.' + Style.RESET_ALL + Fore.RED}\n\
                  \nIts stone walls were dark and weathered, covered in ivy and moss.\n\
Towers loomed above, their windows empty.\n\
The massive wooden door at the entrance was sealed shut, bound with iron and marked with a strange symbol\n\
— one Mario didn’t recognize.\n\
    \nHe stepped closer.\n\
    \nThe journey had led him here. Whatever waited inside, it was the next step.")

def choice_after_goomba_prison():
    print(Fore.RED + f"Mario turned away from the faint light and stepped deeper into the tunnel.\n\
              \nThe air grew colder. The walls narrowed, slick with moisture,\n\
and the stone beneath his boots felt uneven, almost soft in places.\n\
The whispers grew louder — not words, but fragmented sounds:\n\
scraping, dripping, the occasional low groan that echoed and vanished.\n\
              \nHe pressed on.\n\
              \nThe tunnel dipped, then widened into a low chamber.\n\
Rusted pipes lined the ceiling, some leaking a slow trickle of dark water.\n\
Strange markings were etched into the walls — symbols he didn’t recognize.\n\
A broken lantern flickered in the corner, casting shadows that danced like figures.\n\
              \nThen he heard it.\n\
              \nA voice. Clearer now. Not whispering but {Style.BRIGHT + 'pleading.' + Style.RESET_ALL + Fore.RED}\n\
              \nHe followed the sound through a narrow archway and down a flight of crumbling steps.\n\
At the bottom, the passage opened into a wide, dimly lit room.\n\
    \n{Style.BRIGHT + 'The prison chambers.' + Style.RESET_ALL + Fore.RED}\n\
    \nCells lined the walls, their iron bars bent and rusted.\n\
Chains hung from the ceiling, and a single torch burned weakly near the far wall.\n\
    \nMario stepped forward, boots echoing on the stone.")

def continuation_prison():
    print(Fore.RED + f"\nMario stepped deeper into the prison chambers.\n\
              \nThe cells were silent now, their occupants either long gone or too broken to speak.\n\
Chains clinked faintly in the distance, stirred by a draft that carried the scent of ash.\n\
At the far end of the chamber, two passageways opened — one to the left, one to the right.\n\
              {Style.RESET_ALL}\nTo the {Style.BRIGHT + 'left' + Style.RESET_ALL}, the corridor was lined with cracked tiles and faded signs.\n\
A rusted symbol of a red cross hung crookedly above the archway.\n\
The air smelled faintly of rubbing alcohol and herbs.\n\
Somewhere down that hall, a door creaked open and shut, as if caught in a slow breeze.\n\
    \nTo the {Style.BRIGHT + 'right' + Style.RESET_ALL}, the stone turned darker.\n\
The walls were scorched in places, and the air was thick with an unfamiliar smell.\n\
A metal chute ran along the ceiling, ending in a rusted grate stained with ash.\n\
The temperature rose slightly, and Mario could hear the low hum of machinery\n\
— old, but still running.\n\
    \n1. for left, 2. for right")

def prison_pharmacy1():
    print(Fore.RED + f"Mario turned toward the corridor marked by the faded red cross.\n\
                 \nThe air shifted — cooler, cleaner, carrying a faint trace of herbs and something medicinal.\n\
The stone floor gave way to cracked tiles, and the walls showed patches of peeling white paint, stained with time.\n\
                 \nRusted cabinets lined the corridor, some overturned, their contents scattered across the ground.\n\
                 \nMario passed a broken stretcher, its wheels squeaking as it rocked gently in place.\n\
A chart dangled from a nail, its writing smudged beyond recognition.\n\
The deeper he moved, the quieter it became — no whispers, no machinery, just the low hum of silence.\n\
                 \nThe hallway opened into a small treatment room.\n\
                 \nShelves lined the walls, cluttered with dusty vials and brittle bandages.\n\
A sink dripped steadily in the corner, and a cracked mirror reflected Mario’s weary face.\n\
On a table near the back, beneath a glass dome, sat a single mushroom\n\
— bright red with white spots, untouched by decay.\n\
                 \nHe lifted the dome.\n\
                 \nThe mushroom pulsed faintly in his hand. As he ate it, warmth spread through his limbs.\n\
The tension eased. His breath came easier.\n\
                 \n{Style.BRIGHT + Fore.WHITE + 'HP restored.' + Style.RESET_ALL + Fore.RED}\n\
                 \nMario scanned the room once more. It felt untouched, like someone had prepared it for him long ago.") # RESTORE TOTAL PLAYER HEALTH

def prison_pharmacy2():
    print(Fore.RED + f"Mario stepped out of the treatment room, the mushroom’s warmth still pulsing through him.\n\
The hallway was quiet, but the silence felt different now — less hollow, more watchful.\n\
                 \nHe followed the corridor as it curved gently downward.\n\
The tiles gave way to smooth stone, and the walls grew darker, etched with faded symbols and claw-like scratches.\n\
A soft blue glow lit the path ahead, cast by lanterns suspended from iron hooks.\n\
                 \nHe passed a row of shuttered rooms — some marked with faded plaques, others sealed with chains.\n\
One door hung ajar, revealing a room filled with shattered glass and overturned cots.\n\
Another was locked tight, its handle scorched.\n\
                 \nA spiral staircase rose ahead, lit by lanterns glowing with a pale, unnatural hue.\n\
Mario ascended, each step echoing.\n\
                 \nAt the summit, the passage opened into a vast chamber.\n\
                 \nVaulted ceilings stretched overhead, supported by towering columns tangled in dry vines.\n\
Statues stood in solemn rows — warriors, sages, and beasts — their eyes hollow, their expressions unreadable.\n\
                 \nAt the far end loomed a towering door.\n\
Crafted from aged timber and reinforced with silver bands, it pulsed faintly with arcane symbols.\n\
Two iron rings hung at chest height, cold and unmoving.\n\
The air was dense here, as if the room itself was holding its breath.\n\
                 \nMario approached.")
    
def prison_mortuary():
    print(Fore.RED + f"Mario stepped into the right corridor.\n\
                 \nThe temperature rose with each step.\n\
The walls were scorched, stained with soot and ash.\n\
The air was thick — not with smoke, but with something heavier.\n\
The scent of {Style.BRIGHT + 'burned remains' + Style.RESET_ALL + Fore.RED} clung to the stone, and the faint hum of machinery echoed from deep within.\n\
    \nHe passed a rusted chute overhead, its edges blackened and flaking.\n\
Beneath it, the floor was dusted with gray powder.\n\
A cracked plaque on the wall read: {Style.BRIGHT + Fore.WHITE + '“Purification Chamber.”'+ Style.RESET_ALL + Fore.RED}\n\
The letters were faded, but the meaning was clear.\n\
    \nFurther in, the corridor opened into a wide, circular room.\n\
Metal tables lined the walls, some overturned, others still bearing the outlines of what had once been bodies.\n\
A furnace door stood at the far end, slightly ajar, its interior glowing faintly red.\n\
    \nMario stepped forward.\n\
    \nThe torchlight flickered.\n\
    \n{Style.BRIGHT + 'Something moved.' + Style.RESET_ALL + Fore.RED}\n\
    \nFrom behind one of the tables, a pale shape rose — round, ghostly, and grinning.\n\
Its eyes locked onto Mario, and its mouth twisted into a mischievous sneer.\n\
    \n{Style.BRIGHT + 'A Boo.' + Style.RESET_ALL + Fore.RED}")

def boo_defeated():
    print(Fore.RED + "\nThe Boo let out a final shriek before vanishing into wisps of pale smoke.\n\
Silence returned, broken only by the faint hum of machinery.\n\
Mario brushed ash from his gloves and moved on, leaving the heat and shadows of the crematorium behind.\n\
                 \nThe next corridor twisted sharply, its walls damp and uneven.\n\
Overhead, old pipes groaned, and the flickering lanterns cast erratic shapes that crawled across the stone.\n\
The air grew colder, carrying the scent of rust and forgotten places.\n\
                 \nHe reached a corroded gate. Its hinges protested as he pushed through.\n\
Beyond it, the surroundings changed — smoother walls, deliberate carvings,\n\
and faded emblems that suggested a long-lost nobility.\n\
The atmosphere shifted from decay to something ceremonial.\n\
                 \nA spiral staircase rose ahead, lit by lanterns glowing with a pale, unnatural hue.\n\
Mario ascended, each step echoing.\n\
                 \nAt the summit, the passage opened into a vast chamber.\n\
                 \nVaulted ceilings stretched overhead, supported by towering columns tangled in dry vines.\n\
Statues stood in solemn rows — warriors, sages, and beasts — their eyes hollow, their expressions unreadable.\n\
                 \nAt the far end loomed a towering door.\n\
Crafted from aged timber and reinforced with silver bands, it pulsed faintly with arcane symbols.\n\
Two iron rings hung at chest height, cold and unmoving.\n\
The air was dense here, as if the room itself was holding its breath.\n\
                 \nMario approached.")

def before_castle_door():
    print(Fore.RED + f"Mario stood before the massive door, its silver bands pulsing with arcane energy.\n\
He gripped the iron rings and pulled.\n\
       \nThe door groaned open.\n\
       \nBeyond it lay a vast chamber, swallowed in stormlight and shadow.\n\
The ceiling was lost in mist. Jagged spires jutted from the ground like broken teeth.\n\
The air was thick with static, and the walls pulsed like living flesh.\n\
       \nAnd there he was.\n\
       \n{Style.BRIGHT + 'Bowser.' + Style.RESET_ALL + Fore.RED}\n\
       \nBut not the Bowser Mario had known.\n\
       \nThis creature was a colossal abomination, a twisted parody of the Koopa King.\n\
His shell had split and expanded, now a fortress of bone and molten stone.\n\
Tendrils of smoke and fire writhed from his back, and his limbs were bloated, veined with glowing magma.\n\
His face was barely recognizable — stretched, cracked, and crowned with horns that scraped the mist above.\n\
    \nHe loomed like a god of ruin.\n\
    \n{Style.BRIGHT + 'Bowser:' + Style.RESET_ALL + Fore.RED} 'You came through the veins of my body, Mario. This castle... this world... it is me now.'\n\
    \nHis voice was thunder, distorted and layered, echoing from every wall.\n\
    \n{Style.BRIGHT + Fore.GREEN + 'Mario:' + Style.RESET_ALL + Fore.RED} 'You’re not Bowser anymore.'\n\
    \n{Style.BRIGHT + 'Bowser:' + Style.RESET_ALL + Fore.RED} 'I am what you made me. Every defeat. Every humiliation. I fed on it.\n\
I grew. And now, I am beyond kingship. I am wrath incarnate.'\n\
    \nThe ground trembled as Bowser moved. His claws gouged the stone. His breath was a storm of ash.\n\
    \n{Style.BRIGHT + Fore.GREEN + 'Mario:' + Style.RESET_ALL + Fore.RED} 'Then I’ll tear this rage out by the roots.'")

def bowser_defeated():
    print(Fore.RED + f"The chamber fell silent.\n\
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