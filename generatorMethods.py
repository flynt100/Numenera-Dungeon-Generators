# A program to generate maps in unexplored
# dungeons, foes,
# in Numenera
import random

def mainFeatureGenerator():
    d100 = random.randint(1, 100)
    mainFeatureString = ' '
    if d100 > 0 and d100 <= 20:
        mainFeatureString = 'Corridor'
    elif d100 >= 21 and d100 <= 58:
        mainFeatureString = 'Chamber'
    elif d100 >= 59 and d100 <= 70:
        mainFeatureString = 'Creature'
    elif d100 >= 71 and d100 <= 75:
        mainFeatureString = 'Explorers'
    elif d100 >= 76 and d100 <= 79:
        mainFeatureString = 'Interstitial cavity'
    elif d100 >= 80 and d100 <= 82:
        mainFeatureString = 'Accessway'
    elif d100 >= 83 and d100 <= 85:
        mainFeatureString = 'Rupture'
    elif d100 >= 86 and d100 <= 88:
        mainFeatureString = 'Shaft'
    elif d100 >= 89 and d100 <= 91:
        mainFeatureString = 'Abhuman Colony'
    elif d100 >= 92 and d100 <= 93:
        mainFeatureString = 'Integrated Machine'
    elif d100 >= 94 and d100 <= 95:
        mainFeatureString = 'Matter leak'
    elif d100 >= 96 and d100 <= 97:
        mainFeatureString = 'Energy discharge'
    elif d100 == 98:
        mainFeatureString = 'Weird event'
    elif d100 == 99:
        mainFeatureString = 'Vault'
    elif d100 == 100:
        mainFeatureString = 'Relic Chamber'
    else:
        mainFeatureString = 'Exit'

    return mainFeatureString
def corridorGenerator():
    corridorDetailString = ' '
    d20 = random.randint(1, 20)
    if d20 >= 1 and d20 <= 7:
        corridorDetailString = 'Passage extends 20 ft (6 m), roll again.\n ' + mainFeatureGenerator()
    elif d20 >= 8 and d20 <= 10:
        corridorDetailString = 'Passage extends a short distance'
    elif d20 == 11:
        corridorDetailString = 'Passage blocked by a corridor collapse'
    elif d20 == 12:
        corridorDetailString = 'Passage comes to a dead end'
    elif d20 == 13:
        corridorDetailString = 'Passage bends left'
    elif d20 == 14:
        corridorDetailString = 'Passage bends right'
    elif d20 == 15:
        corridorDetailString = 'Passage slopes up'
    elif d20 == 16:
        corridorDetailString = 'Passage slopes down'
    elif d20 == 17:
        corridorDetailString = '''Passage runs a short distance 
        parallel to previous chamber or corridor, 
        roll again on this table; 
        ignore if no previously rolled chamber or corridor \n''' + corridorGenerator()
    elif d20 == 18:
        corridorDetailString = '''Passage runs an immediate 
        distance into an interstitial 
        cavity, then runs an additional 
        distance across that cavity’s entire width 
        as a catwalk; roll on the Interstitial Cavity Table 
        to determine nature of space passed through, 
        and again on this table where the passage 
        returns to normal (enclosed)'''
    elif d20 == 19:
        corridorDetailString = '''Passage runs a short distance 
        and comes to a T intersection, 
        roll on this table for each branch'''
    elif d20 == 20:
        corridorDetailString = '''Passage runs a short distance 
        and comes to an X intersection, 
        roll on this table for each branch'''
    return corridorDetailString
def exitGenerator():
    d20 = random.randint(1, 20)
    exitTableString = ' '
    if d20 >= 1 and d20 <= 4:
        exitTableString = 'No additional exits'
    elif d20 >= 5 and d20 <= 12:
        exitTableString = '1 additional exit'
    elif d20 >= 13 and d20 <= 14:
        exitTableString = '1 additional sealed exit'
    elif d20 == 15:
        exitTableString = '2 additional exits'
    elif d20 == 16:
        exitTableString = '1 additional exit + 1 sealed* exit'
    elif d20 == 17:
        exitTableString = '2 additional exits + 1 sealed* exit'
    elif d20 == 18:
        exitTableString = '2 sealed* exits'
    elif d20 == 19:
        exitTableString = '1 additional trapped** exit, roll again ' + exitGenerator()
    elif d20 == 20:
        exitTableString = '1 additional hidden*** exit, roll again ' + exitGenerator()

    return exitTableString
def chamberGenerator():
    d20_1 = random.randint(1, 20)
    roomString = ' '
    roomSize = ' '
    if d20_1 >= 1 and d20_1 <= 2:
        roomSize = 'Closet-sized'
    elif d20_1 >= 3 and d20_1 <= 6:
        roomSize = '15 feet (5 m) across'
    elif d20_1 >= 7 and d20_1 <= 15:
        roomSize = '30 feet (9 m) across'
    elif d20_1 >= 16 and d20_1 <= 18:
        roomSize = '50 feet (15 m) across'
    elif d20_1 == 19:
        roomSize = '60 feet (18 m) across'
    elif d20_1 == 20:
        roomSize = '90 feet (27 m) across'



    d20_2 = random.randint(1, 20)
    roomShape = ' '
    if d20_2 >= 1 and d20_2 <= 2:
        roomShape = 'Circle'
    elif d20_2 >= 3 and d20_2 <= 4:
        roomShape = 'Square'
    elif d20_2 >= 5 and d20_2 <= 17:
        roomShape = 'Rectangle*'
    elif d20_2 == 18:
        roomShape = 'Hexagon'
    elif d20_2 == 19:
        roomShape = 'Half circle'
    elif d20_2 == 20:
        roomShape = 'Triangle'



    cf_choice = random.randint(1, 2)
    d100 = random.randint(1, 100)
    chamberFeatureString = ' '
    if cf_choice == 1:
        if d100 == 1:
            chamberFeatureString = 'Intricate knot in synth cable; re-knots if undone'
        elif d100 == 2:
            chamberFeatureString = 'Floating black sphere that shifts hue on touch'
        elif d100 == 3:
            chamberFeatureString = 'Glass panels that reverse reflections in time'
        elif d100 == 4:
            chamberFeatureString = 'Yellow fluid that turns to gas if warmed by touch'
        elif d100 == 5:
            chamberFeatureString = 'Crystal cylinders filled with thousands of dead laaks'
        elif d100 == 6:
            chamberFeatureString = 'Green crystal rods age explorers one day per minute'
        elif d100 == 7:
            chamberFeatureString = 'Spheres shed bright light, triggered by movement'
        elif d100 == 8:
            chamberFeatureString = 'Water leak creates ice sculptures in bizarre shapes'
        elif d100 == 9:
            chamberFeatureString = 'Umbilical ports provide those who can connect +1 to Intellect Edge for one hour,' \
                                   ' once a day'
        elif d100 == 10:
            chamberFeatureString = 'Umbilical ports provide those who can connect deep sleep and strange ' \
                                   'dreams for one' \
                                   ' hour'
        elif d100 == 11:
            chamberFeatureString = 'Crystal dome shows planetary sphere (real-time view of Earth ' \
                                   'from high above in the' \
                                   ' void)'
        elif d100 == 12:
            chamberFeatureString = 'Crystal dome shows a parallel-dimension version of the viewer'
        elif d100 == 13:
            chamberFeatureString = 'Crystal dome shows a map of the chamber and all other chambers within long range'
        elif d100 == 14:
            chamberFeatureString = 'Crystal dome shows the exterior of the ruin'
        elif d100 == 15:
            chamberFeatureString = 'Square pool of clear fluid, but thick as honey'
        elif d100 == 16:
            chamberFeatureString = 'Square pool of opaque black fluid that flows to cover explorers, forming a second' \
                                   ' skin that prevents wearer from seeing, breathing, etc.'
        elif d100 == 17:
            chamberFeatureString = 'Square pool of boiling white fluid that is cool to the touch'
        elif d100 == 18:
            chamberFeatureString = 'Square pool, empty but contains orange crystal residue; if rehydrated, a ' \
                                   'creature* emerges' + '\nCreature:  ' + creatureGenerator()
        elif d100 == 19:
            chamberFeatureString = 'Pod dehydrates any living creature that enters, creating a slim husk. ' \
                                   'Rehydration requires a successful Intellect task.'
        elif d100 == 20:
            chamberFeatureString = 'Floor electrostatically sticky, holds explorers'
        elif d100 == 21:
            chamberFeatureString = 'Black cylinder emits a low gravity field'
        elif d100 == 22:
            chamberFeatureString = 'Clear cylinder emits subsonic vibration'
        elif d100 == 23:
            chamberFeatureString = 'Synth sculpture moves incrementally when touched'
        elif d100 == 24:
            chamberFeatureString = 'Complex pattern in a crystal places target’s mentality in psychic labyrinth ' \
                                   'until they can escape'
        elif d100 == 25:
            chamberFeatureString = 'Complex pattern in a crystal induces viewers to laugh with unexpected pleasure'
        elif d100 == 26:
            chamberFeatureString = 'Complex pattern in a crystal grants viewer an asset on ' \
                                   'next Intellect task attempted'
        elif d100 == 27:
            chamberFeatureString = 'Complex pattern in a crystal makes viewer feel unaccountably sad'
        elif d100 == 28:
            chamberFeatureString = 'Arch duplicates creature, without equipment, but dead'
        elif d100 == 29:
            chamberFeatureString = 'Arch cleans anything that moves through it'
        elif d100 == 30:
            chamberFeatureString = 'Arch steals one organ from any living creature that moves through it; replacing ' \
                                   'the organ requires a difficulty 5 Intellect task'
        elif d100 == 31:
            chamberFeatureString = 'Rack of devices hum and whisper in an unknown language if activated'
        elif d100 == 32:
            chamberFeatureString = 'Complex device with a flat, sparkling surface; all water is sucked from' \
                                   ' anything touched to the surface (inflicting 2 points of Speed damage to a ' \
                                   'character who touches it)'
        elif d100 == 33:
            chamberFeatureString = 'Rack of devices blink faster and faster for one minute when activated,' \
                                   ' then go dead again'
        elif d100 == 34:
            chamberFeatureString = 'Rack of devices become ten times heavier when activated'
        elif d100 == 35:
            chamberFeatureString = 'Rack of devices whisper insults in a language known to the holder'
        elif d100 == 36:
            chamberFeatureString = 'Wide metallic urn from which crystal bubbles emerge and waft until they burst'
        elif d100 == 37:
            chamberFeatureString = 'Wide metallic urn from which liquid bubbles emerge and waft, emitting psychic ' \
                                   'questions of surprise and curiosity, until they burst'
        elif d100 == 38:
            chamberFeatureString = 'Wide metallic urn from which acidic bubbles emerge and waft, endangering explorers'
        elif d100 == 39:
            chamberFeatureString = 'Wavering light sculpture resembling a human brain with three major ' \
                                   'divisions instead of two'
        elif d100 == 40:
            chamberFeatureString = 'Wavering light sculpture flicks into existence, displaying brain ' \
                                   'of nearest explorer'
        elif d100 == 41:
            chamberFeatureString = 'Wavering light sculpture of a circular portal through which stars and ' \
                                   'galaxies are visible'
        elif d100 == 42:
            chamberFeatureString = 'Dozens of translucent spheres, soft to the touch, form a mechanism that emits ' \
                                   'a lilac and ozone odor'
        elif d100 == 43:
            chamberFeatureString = 'Metallic pod petrifies objects'
        elif d100 == 44:
            chamberFeatureString = 'Metallic pod puts anything that enters into stasis, which lasts until the ' \
                                   'pod ejects the object or creature'
        elif d100 == 45:
            chamberFeatureString = 'Metallic pod dyes objects bright blue'
        elif d100 == 46:
            chamberFeatureString = 'Metallic pod turns opaque objects translucent'
        elif d100 == 47:
            chamberFeatureString = 'Metallic pod turns solids to liquids'
        elif d100 == 48:
            chamberFeatureString = 'Metallic pod freezes objects'
        elif d100 == 49:
            chamberFeatureString = 'Metallic pod constantly discharges thick grey fluid that is similar to drit “mud”'
        elif d100 == 50:
            chamberFeatureString = 'Metallic pod hums and vibrates but does nothing else that is obvious to observers'
        elif d100 == 51:
            chamberFeatureString = 'Random oddity'
        elif d100 == 52:
            chamberFeatureString = 'Glass barrier holds healthy underwater biome'
        elif d100 == 53:
            chamberFeatureString = 'Glass barrier holds fluid-like translucent fog behind which strange ' \
                                   'creatures* seem to move' + ':  ' + creatureGenerator()
        elif d100 == 54:
            chamberFeatureString = 'Crystal columns embed what seem to be skinless, dead humanoid creatures'
        elif d100 == 55:
            chamberFeatureString = 'Crystal columns glow when cyphers are near'
        elif d100 == 56:
            chamberFeatureString = 'Crystal columns sap nearby cypher’s energy'
        elif d100 == 57:
            chamberFeatureString = 'Crystal column displays strange symbols in a language too complex for normal humans'
        elif d100 == 58:
            chamberFeatureString = 'Black cylinder emits a high-gravity field'
        elif d100 == 59:
            chamberFeatureString = 'Black cylinder attracts nearby metallic objects'
        elif d100 == 60:
            chamberFeatureString = 'Black cylinder repels nearby metallic objects'
        elif d100 == 61:
            chamberFeatureString = 'Synth box adds tiny legs to objects placed inside'
        elif d100 == 62:
            chamberFeatureString = 'Synth box adds tiny eyes to objects placed inside'
        elif d100 == 63:
            chamberFeatureString = 'Empty synth boxes are conveyed along a portion of the chamber, emerging from ' \
                                   'one wall cavity and entering another. A dead mechanism meant to deposit material ' \
                                   'into the boxes intersects the moving containers.'
        elif d100 == 64:
            chamberFeatureString = 'As 63, but the central device deposits in 1/20 boxes a midnight stone'
        elif d100 == 65:
            chamberFeatureString = 'As 63, but the central device deposits in 1/10 boxes what seems to be drit “mud”'
        elif d100 == 66:
            chamberFeatureString = 'As 63, but the central device deposits in 1/10 boxes random dead objects of the ' \
                                   'numenera that someone with crafting or similar knowledge could use as parts'
        elif d100 == 67:
            chamberFeatureString = 'Machine fuses any two objects brought near it'
        elif d100 == 68:
            chamberFeatureString = 'Machine halves any two objects brought near it'
        elif d100 == 69:
            chamberFeatureString = 'Machine grinds small object into drit'
        elif d100 == 70:
            chamberFeatureString = 'Machine heats objects to boiling temperature'
        elif d100 == 71:
            chamberFeatureString = 'Machine adds tiny wheels to any object'
        elif d100 == 72:
            chamberFeatureString = 'Machine adds metallic eyes to any object'
        elif d100 == 73:
            chamberFeatureString = 'Machine stitches metallic wires to any object'
        elif d100 == 74:
            chamberFeatureString = 'Metallic wires absorb all nearby sound'
        elif d100 == 75:
            chamberFeatureString = 'Metallic wires amplify all nearby sound'
        elif d100 == 76:
            chamberFeatureString = 'Synth machine rusts metallic objects'
        elif d100 == 77:
            chamberFeatureString = 'Synth machine magnetizes metallic objects'
        elif d100 == 78:
            chamberFeatureString = 'Synth machine electrifies metallic objects'
        elif d100 == 79:
            chamberFeatureString = 'Two large, hovering, spinning metallic spheres'
        elif d100 == 80:
            chamberFeatureString = 'As 79, but unlocks or powers nearby tech'
        elif d100 == 81:
            chamberFeatureString = 'As 79, but locks or powers down nearby tech'
        elif d100 == 82:
            chamberFeatureString = 'As 79, but spheres stop spinning when questions are asked in the chamber, and ' \
                                   'don’t start again until some kind of answer is provided'
        elif d100 == 83:
            chamberFeatureString = 'As 79, but spheres glow bright red if a visitant from another world or ' \
                                   'dimension enters the chamber'
        elif d100 == 84:
            chamberFeatureString = 'Hovering orb-shaped space eats all light'
        elif d100 == 85:
            chamberFeatureString = 'As 84, but objects thrown in space appear elsewhere'
        elif d100 == 86:
            chamberFeatureString = 'As 84, but objects thrown in space are disintegrated'
        elif d100 == 87:
            chamberFeatureString = 'Black, rectangle-shaped slab emits deep hum'
        elif d100 == 88:
            chamberFeatureString = 'As 87, but thoughts of nearby creature are displayed as images on slab’s surface'
        elif d100 == 89:
            chamberFeatureString = 'As 87, but slab transfers consciousness of nearby creature into small yellow, ' \
                                   'floating crystal sphere'
        elif d100 == 90:
            chamberFeatureString = 'Contact with wall causes slightly acidic gas to spray from ceiling ' \
                                   'fixtures for several minutes'
        elif d100 == 91:
            chamberFeatureString = 'Contact with wall causes white paste to emerge from wall fixture for several ' \
                                   'rounds; the paste is somewhat nutritious but tastes terrible'
        elif d100 == 92:
            chamberFeatureString = 'Contact with wall causes fixture elsewhere in the chamber to ' \
                                   'detonate, but only once'
        elif d100 >= 93 and d100 <= 95:
            chamberFeatureString = 'Contact with wall causes entire opposite wall ' \
                                   'to lift and reveal another chamber; ' \
                                   'roll to generate new chamber'
        elif d100 >= 96 and d100 <= 97:
            chamberFeatureString = 'Contact with wall causes entire opposite wall ' \
                                   'to lift and reveal another chamber; ' \
                                   'roll on Integrated Machine Table'
        elif d100 >= 98 and d100 <= 100:
            chamberFeatureString = 'Trapped** chamber'

    elif cf_choice == 2:
        if d100 == 1:
            chamberFeatureString = 'Multidimensional crystal object the size of a human head ' \
                                   'floats and moans, as if in pain'
        elif d100 == 2:
            chamberFeatureString = 'Long, snakelike extensions made of metal extrude from the floor and ' \
                                   'ceiling of this room'
        elif d100 == 3:
            chamberFeatureString = 'Floor intermittently becomes intangible'
        elif d100 == 4:
            chamberFeatureString = 'Glass container on metallic pole contains rapidly darting gobs of red-glowing goo'
        elif d100 == 5:
            chamberFeatureString = 'Time stutters in area, causing rounds to replay over and over until a character ' \
                                   'succeeds on a difficulty 5 Intellect task'
        elif d100 == 6:
            chamberFeatureString = 'Device removes eyes of those who use it and stores them in nearby vessel'
        elif d100 == 7:
            chamberFeatureString = 'Leafless “tree” of bronze-colored metal whispers secrets in an unknown language'
        elif d100 == 8:
            chamberFeatureString = 'As 07, but questions are asked'
        elif d100 == 9:
            chamberFeatureString = 'As 07, but compliments are given, with a sprinkling of veiled insults'
        elif d100 == 10:
            chamberFeatureString = 'Thin vortex of grey mist sometimes springs up a chamber’s center, ' \
                                   'spins for a few minutes, then fades'
        elif d100 == 11:
            chamberFeatureString = 'Metallic headbands found in discarded jumble contain infectious psychic virus; ' \
                                   'initial symptoms are whispers that only the infected can hear, ' \
                                   'but as infection worsens, others also begin to hear them'
        elif d100 == 12:
            chamberFeatureString = 'Invisible device casts shadow, hums quietly'
        elif d100 == 13:
            chamberFeatureString = 'Messily disassembled automaton is scattered here'
        elif d100 == 14:
            chamberFeatureString = 'Disembodied mechanical hand floats in the air'
        elif d100 == 15:
            chamberFeatureString = 'As 14, but hand grips anything near it, attempting to crush what it holds'
        elif d100 == 16:
            chamberFeatureString = 'Door to chamber isn’t apparent on the inside'
        elif d100 == 17:
            chamberFeatureString = 'Spinning disc hangs at chamber’s center'
        elif d100 == 18:
            chamberFeatureString = 'As 17, but disc spins up only when disturbed, going faster and faster until it ' \
                                   'detonates after three rounds'
        elif d100 == 19:
            chamberFeatureString = 'As 17, but disc changes speed of spin to replicate sounds like words'
        elif d100 == 20:
            chamberFeatureString = 'Chamber suspended on synth cords attached to a much higher area; ' \
                                   'sometimes chamber moves between those areas'
        elif d100 == 21:
            chamberFeatureString = 'Torso of faceless humanoid of white synth protrudes from wall, makes strange ' \
                                   'gestures in response to questions'
        elif d100 == 22:
            chamberFeatureString = 'Turquoise-hued polyp drips ichor that pools here'
        elif d100 == 23:
            chamberFeatureString = 'Pool of cool-to-the touch liquid metal'
        elif d100 == 24:
            chamberFeatureString = 'As 23, but any material removed from pool hardens to steel-like ' \
                                   'rigidity a few rounds later'
        elif d100 == 25:
            chamberFeatureString = 'As 23, but liquid animates to form visages imitating anyone looking into pool'
        elif d100 == 26:
            chamberFeatureString = 'Creatures that trigger a slender device gain a glowing, ' \
                                   'symbol-like tattoo on their foreheads'
        elif d100 == 27:
            chamberFeatureString = 'As 26, but the “tattoos” replace a creature’s irises, ' \
                                   'though they don’t interfere with vision'
        elif d100 == 28:
            chamberFeatureString = 'Beam of light suspends a massive stone cube scribed with strange writing; ' \
                                   'breaking the light beam causes the cube to crash down and break'
        elif d100 == 29:
            chamberFeatureString = 'As 28, and broken cube contains a creature* in stasis, now waking' + '\nCreature:  ' + creatureGenerator()
        elif d100 == 30:
            chamberFeatureString = 'Beam of light lifts and suspends any creature or object that enters it'
        elif d100 == 31:
            chamberFeatureString = 'As 30, but anything in the light begins to quickly age'
        elif d100 == 32:
            chamberFeatureString = 'Glass container holds slug-like creatures without eyes in a haze of ' \
                                   'orange mist that sustains them'
        elif d100 == 33:
            chamberFeatureString = 'As 32, but slugs are intelligent and telepathic, without much purpose or motivation'
        elif d100 == 34:
            chamberFeatureString = 'As 32, but slugs are intelligent, telepathic, and desperate to convince ' \
                                   'explorers to free them'
        elif d100 == 35:
            chamberFeatureString = 'Nozzles sporadically spray area with water vapor'
        elif d100 == 36:
            chamberFeatureString = 'As 35, but with acidic vapor'
        elif d100 == 37:
            chamberFeatureString = 'As 35, but with sleep-inducing vapor'
        elif d100 == 38:
            chamberFeatureString = 'As 35, but with vapor that erases concept of distance, ' \
                                   'the difference between near and far'
        elif d100 == 39:
            chamberFeatureString = 'As 35, but with a wonderful and pleasing odor'
        elif d100 == 40:
            chamberFeatureString = 'Mechanism in this chamber attempts to communicate by ' \
                                   'changing light intensity on a screen'
        elif d100 == 41:
            chamberFeatureString = 'Creature* uses chamber to gestate/birth/hide young' + '\nCreature:  ' + creatureGenerator()
        elif d100 == 42:
            chamberFeatureString = 'Remnants of shattered device scattered here'
        elif d100 == 43:
            chamberFeatureString = 'As 42, but if shards are brought together, they spontaneously assemble ' \
                                   'to create an artifact; artifact seems normal but upon depletion it detonates'
        elif d100 == 44:
            chamberFeatureString = 'Synth and metal disc can be used as a levitating vehicle for ' \
                                   'up to one hour per day (depletion: 1 in 1d6)'
        elif d100 == 45:
            chamberFeatureString = 'As 44, but on second use, levitating metal disc delivers passengers to ' \
                                   'some other location in structure that they don’t choose'
        elif d100 == 46:
            chamberFeatureString = 'Sparkling dust (inactive nanites) fills this chamber in fine drifts'
        elif d100 == 47:
            chamberFeatureString = 'As 46, but one investigating character gains a ' \
                                   'glowing nimbus (composed of orbiting nanites)'
        elif d100 == 48:
            chamberFeatureString = 'As 46, but one investigating character gains a light-eating nimbus ' \
                                   'that seems to alter odds slightly in the character’s favor ' \
                                   'but with negative consequences for allied characters'
        elif d100 == 49:
            chamberFeatureString = "As 46, but the character's glowing nimbus " \
                                   "that enrages any visitant that sees the character"
        elif d100 == 50:
            chamberFeatureString = 'Pulses of green light are emitted from a sphere-like device, ' \
                                   'changing slightly with each pulse as if counting something down'
        elif d100 == 51:
            chamberFeatureString = 'As 50, but the event counting down is ' \
                                   'the destination of a nearby spatial portal, ' \
                                   'which changes at each turnover'
        elif d100 == 52:
            chamberFeatureString = 'As 50, but the event counting down is a dramatic reversal in local gravity'
        elif d100 == 53:
            chamberFeatureString = 'Spatial flaw, held in place by tech in chamber, closes if machine is deactivated'
        elif d100 == 54:
            chamberFeatureString = 'As 53, but those who enter chamber take ambient ' \
                                   'damage from folding space each round'
        elif d100 == 55:
            chamberFeatureString = 'As 53, but flaw begins to expand if machine is deactivated, ' \
                                   'risking sucking nearby objects and creatures into it'
        elif d100 == 56:
            chamberFeatureString = 'Walls of chamber striped with material that absorbs light and warmth, ' \
                                   'making area impossible to illuminate or heat'
        elif d100 == 57:
            chamberFeatureString = 'As 56, but material absorbs sound and vibration'
        elif d100 == 58:
            chamberFeatureString = 'As 56, but material absorbs emotion, making it impossible to feel happy, sad, ' \
                                   'curious, scared, or other motivating emotion'
        elif d100 == 59:
            chamberFeatureString = 'Area shakes, shifts, sometimes rotates'
        elif d100 == 60:
            chamberFeatureString = 'Area randomly spins rapidly, ejecting contents'
        elif d100 == 61:
            chamberFeatureString = 'Skull of dead human explorer has ' \
                                   'metallic insects for teeth, ' \
                                   'which attack investigators'
        elif d100 == 62:
            chamberFeatureString = 'Device attempts to operate on living creatures; ' \
                                   'it can heal hurts great and small, ' \
                                   'but often malfunctions'
        elif d100 == 63:
            chamberFeatureString = 'As 62, but device replaces a limb of a living ' \
                                   'creature with a long, pointed cone of red metal'
        elif d100 == 64:
            chamberFeatureString = 'As 62, but device replaces one eye with ' \
                                   'blank metal orb that doesn’t initially seem functional'
        elif d100 == 65:
            chamberFeatureString = 'As 62, but device replaces mouth with ' \
                                   'input socket that can only take nutritional paste or similar'
        elif d100 == 66:
            chamberFeatureString = 'As 62, but device adds vestigial winglike ' \
                                   'projections to back that do not initially seem functional'
        elif d100 == 67:
            chamberFeatureString = 'Device close to malfunction; failed Intellect task causes device and ' \
                                   'chamber to disappear, causing a new rupture in the larger structure'
        elif d100 == 68:
            chamberFeatureString = 'Green metallic boxes hum and spit sparks'
        elif d100 == 69:
            chamberFeatureString = 'As 68, but red boxes induce malfunction in nearby active devices and tech'
        elif d100 == 70:
            chamberFeatureString = 'As 68, but blue boxes add +1 to level of all nearby active devices and tech'
        elif d100 == 71:
            chamberFeatureString = 'As 68, but clear boxes allow nearby creatures to ' \
                                   'stare into parallel dimensions, ' \
                                   'which can be confusing when scenes ' \
                                   'overlay the base reality'
        elif d100 == 72:
            chamberFeatureString = 'Thick blue disc emits a variety of intense, ' \
                                   'moody, and sometimes overwhelming sounds that ' \
                                   'can be pleasant or evocative, but which eventually ' \
                                   'draw other creatures*' + ':  ' + creatureGenerator()
        elif d100 == 73:
            chamberFeatureString = 'Silver spheres on device seem like ' \
                                   'simple metallic orbs, but have an allure ' \
                                   'via telepathic induction that is difficult ' \
                                   'to ignore'
        elif d100 == 74:
            chamberFeatureString = 'As 73, but character must resist ' \
                                   'having one memory telepathically edited out'
        elif d100 == 75:
            chamberFeatureString = 'As 73, but character gains an affection ' \
                                   'for a kind of food, activity, or entertainment ' \
                                   'that previously never appealed'
        elif d100 == 76:
            chamberFeatureString = 'Milk-colored solid floating in transparent ' \
                                   'tube impossibly has nineteen equally matched ' \
                                   'sides and eight angles'
        elif d100 == 77:
            chamberFeatureString = 'Wall mirror reflects images upside down'
        elif d100 == 78:
            chamberFeatureString = 'Wall mirror reflects characters as silhouettes'
        elif d100 == 79:
            chamberFeatureString = 'Wall mirror reflects unfamiliar faces back'
        elif d100 == 80:
            chamberFeatureString = 'Wall “mirror” is actually glass pane behind ' \
                                   'which complex automatons try to exactly mimic ' \
                                   'what happens in front of the pane'
        elif d100 == 81:
            chamberFeatureString = 'Wall mirror births automatons that look like ' \
                                   'creatures pictured in it minutes earlier, but ' \
                                   'they have a lifespan of only hours'
        elif d100 == 82:
            chamberFeatureString = 'Platform causes extreme pain to creatures on it'
        elif d100 == 83:
            chamberFeatureString = 'As 82, but pain persists for a few hours, ' \
                                   'and one character begins to transform, becoming ' \
                                   'externally similar to a creature*' + '\nCreature:  ' + creatureGenerator()
        elif d100 == 84:
            chamberFeatureString = 'As 82, but platform provides pleasure/relief from malaise'
        elif d100 == 85:
            chamberFeatureString = 'As 82, but platform provides perfect recollection of past'
        elif d100 == 86:
            chamberFeatureString = 'As 82, but platform makes creatures voraciously hungry'
        elif d100 == 87:
            chamberFeatureString = 'As 82, but platform makes creatures crave and enjoy pain'
        elif d100 == 88:
            chamberFeatureString = 'Device fashions odd but somehow alluring ' \
                                   'synth bracelets that could be used as jewelry'
        elif d100 == 89:
            chamberFeatureString = 'As 88, but jewelry hovers around wearer'
        elif d100 == 90:
            chamberFeatureString = 'As 88, but jewelry begins to fuse to wearer’s flesh'
        elif d100 == 91:
            chamberFeatureString = 'Synth nests hold insect-like automatons that act ' \
                                   'as a single intelligence that knows a little of nearby areas'
        elif d100 == 92:
            chamberFeatureString = 'As 91, but intelligence guards nearby areas'
        elif d100 == 93:
            chamberFeatureString = 'As 91, but intelligence secretly tries ' \
                                   'to take control of and “infest” one character with nests'
        elif d100 == 94:
            chamberFeatureString = 'White fire “burns” here, but isn’t hot; ' \
                                   'objects and creatures that enter area ' \
                                   'begin to flame, but do not burn'
        elif d100 == 95:
            chamberFeatureString = 'As 94, but a flaming object or creature ' \
                                   'that leaves the area suddenly ignites normally ' \
                                   '(and potentially lethally)'
        elif d100 == 96:
            chamberFeatureString = 'Circular synth conduits run through the area, ' \
                                   'conveying pale liquids to other areas'
        elif d100 == 97:
            chamberFeatureString = 'As 96, but a conduit leak pools pale liquid ' \
                                   'here that has 100 times the surface tension of ' \
                                   'normal water'
        elif d100 == 98:
            chamberFeatureString = 'Anyone passing through the area suddenly ' \
                                   'accelerates to 10 times their starting pace, ' \
                                   'potentially turning creatures and objects into ' \
                                   'dangerous projectiles'
        elif d100 == 99:
            chamberFeatureString = 'Ceiling dome sparkles with random glows and hums'
        elif d100 == 100:
            chamberFeatureString = 'As 99, but dome instills extreme paranoia in creatures who stare into it'

    roomString = 'Size: ' + roomSize + '\nShape: ' + roomShape + '\nDetails:  ' + chamberFeatureString
    return roomString
def abhumanColonyGenerator():
    abColonyString = ' '
    colType = ' '
    d20_1 = random.randint(1, 20)
    if d20_1 == 1:
        colType = 'Chirog'
    elif d20_1 == 2:
        colType = 'Margr'
    elif d20_1 == 3:
        colType = 'Murden'
    elif d20_1 == 4:
        colType = 'Sathosh'
    elif d20_1 == 5:
        colType = 'Yovok'
    elif d20_1 == 6:
        colType = 'Yovok'
    elif d20_1 == 7:
        colType = 'Grush'
    elif d20_1 == 8:
        colType = 'Grush'
    elif d20_1 == 9:
        colType = 'Killist'
    elif d20_1 == 10:
        colType = 'Syzygy ghoul'
    elif d20_1 == 11:
        colType = 'Caprimag'
    elif d20_1 == 12:
        colType = 'Heeldran'
    elif d20_1 == 13:
        colType = 'Igothus'
    elif d20_1 == 14:
        colType = 'Kaseyer'
    elif d20_1 == 15:
        colType = 'Keltonim'
    elif d20_1 == 16:
        colType = 'Larus'
    elif d20_1 == 17:
        colType = 'Malvok'
    elif d20_1 == 18:
        colType = 'Olion'
    elif d20_1 == 19:
        colType = 'Umem'
    elif d20_1 == 20:
        colType = 'Zayrn'



    colSpecs = ' '
    d20_2 = random.randint(1, 20)
    if d20_2 == 1:
        colSpecs = 'Colony is dead, all mummified corpses'
    elif d20_2 == 2:
        colSpecs = 'As 01, but colony is empty'
    elif d20_2 == 3:
        colSpecs = 'As 02, but with a strange device salvaged ' \
                   'from a chamber; roll on the Chamber Table to ' \
                   'determine the device’s nature. The device ' \
                   'also emits a level 5 invisible toxin.'
    elif d20_2 == 4:
        colSpecs = 'Colony is xenophobic and hungry'
    elif d20_2 == 5:
        colSpecs = 'As 04, but willing to negotiate'
    elif d20_2 == 6:
        colSpecs = 'Colony seems friendly'
    elif d20_2 == 7:
        colSpecs = 'As 06, but it’s a trick to gain trust ' \
                   'before a surprise ambush and betrayal'
    elif d20_2 == 8:
        colSpecs = 'As 06, but a misstep on the explorers’ part ' \
                   'is likely to turn the abhumans into raging killers'
    elif d20_2 == 9:
        colSpecs = 'Colony wars with another abhuman colony nearby; ' \
                   'roll to determine enemy abhuman type'
    elif d20_2 == 10:
        colSpecs = 'Colony is in some kind of suspended animation ' \
                   '(cocooned, stasis, time-locked, etc.)'
    elif d20_2 == 11:
        colSpecs = 'Colony keeps several victims kidnapped from the outside'
    elif d20_2 == 12:
        colSpecs = 'Colony doesn’t want to kill explorers, ' \
                   'just take them prisoner as forced labor'
    elif d20_2 == 13:
        colSpecs = 'Colony is on the verge of activating a “sleeping” dark ' \
                   'fathom they believe will be under their control'
    elif d20_2 == 14:
        colSpecs = 'Colony is dying; their access to hunting outside or ' \
                   'the machine that provided nutrition is gone'
    elif d20_2 == 15:
        colSpecs = 'Colony’s leader is an Aeon Priest who “went native”'
    elif d20_2 == 16:
        colSpecs = 'Colony has a map to a vault containing several artifacts; ' \
                   'roll on the Vault Contents Table to determine specifics'
    elif d20_2 == 17:
        colSpecs = 'Colony plans to ambush and overrun another group of explorers, ' \
                   'a field camp of Jade Protectors, or an external community'
    elif d20_2 == 18:
        colSpecs = 'Colony is being hunted by a group ' \
                   'of explorers who want vengeance for a past wrong'
    elif d20_2 == 19:
        colSpecs = 'Colony is flourishing thanks to a device ' \
                   'they salvaged from a chamber; roll on the ' \
                   'Chamber Table to determine the device’s nature. ' \
                   'The device also emits a level 2 healing ' \
                   'field that grants up to 2 points of health ' \
                   'each round.'
    elif d20_2 == 20:
        colSpecs = 'Colony knows the secret entrance to an ' \
                   'undiscovered relic chamber; roll on the ' \
                   'Relic Anatomy and Relic Quality tables to ' \
                   'determine that relic’s nature; if applicable, ' \
                   'one or two abhumans in the colony have been ' \
                   'touched by the relic’s power'

    abColonyString = colType + ':  ' + colSpecs
    return abColonyString
def accesswayGenerator():
    d20 = random.randint(1, 20)
    accesswayString = ' '
    if d20 >= 1 and d20 <= 9:
        accesswayString = '''Accessway runs parallel to previously 
        generated chamber(s) or corridor(s) for 
        a short distance, with hidden openings into 
        each of those spaces; roll again on this table; 
        if no previously generated corridors or chambers 
        are mapped nearby, use result 10-15 ''' + accesswayGenerator()
    elif d20 >= 10 and d20 <= 12:
        accesswayString = 'Accessway extends a short distance; roll again ' + mainFeatureGenerator()
    elif d20 == 13:
        accesswayString = 'Accessway bends left'
    elif d20 == 14:
        accesswayString = 'Accessway bends right'
    elif d20 == 15:
        accesswayString = 'Accessway extends straight up'
    elif d20 == 16:
        accesswayString = 'Accessway drops straight down'
    elif d20 == 17:
        accesswayString = 'Accessway drops into reclamation ' \
                          'pit containing a level 5 deconstructor automaton'
    elif d20 >= 18 and d20 <= 19:
        accesswayString = 'Accessway narrows to 4 inches ' \
                          '(10 cm) in height and width; roll again '+ mainFeatureGenerator()
    elif d20 == 20:
        accesswayString = 'Accessway runs a short distance and ' \
                          'comes to a T intersection; roll on this ' \
                          'table for each branch'
    return accesswayString
def creatureGenerator():
    d100 = random.randint(1, 100)
    creatureString = ' '
    if d100 == 1:
        creatureString = 'Awakened relic*'
    elif d100 == 2:
        creatureString = 'Blood barm'
    elif d100 == 3:
        creatureString = 'Broken hound'
    elif d100 == 4:
        creatureString = 'Callerail'
    elif d100 == 5:
        creatureString = 'Colchin'
    elif d100 == 6:
        creatureString = 'Colostran*'
    elif d100 == 7:
        creatureString = 'Disassembler'
    elif d100 == 8:
        creatureString = 'Divellent*'
    elif d100 == 9:
        creatureString = 'Dritch*'
    elif d100 == 10:
        creatureString = 'Laak'
    elif d100 == 11:
        creatureString = 'Marauding vault*'
    elif d100 == 12:
        creatureString = 'Margr'
    elif d100 == 13:
        creatureString = 'Mesotemus*'
    elif d100 == 14:
        creatureString = 'Murden'
    elif d100 == 15:
        creatureString = 'Nevajin'
    elif d100 == 16:
        creatureString = 'Nibovian wife'
    elif d100 == 17:
        creatureString = 'Oorgolian soldier'
    elif d100 == 18:
        creatureString = 'Philethis'
    elif d100 == 19:
        creatureString = 'Raster'
    elif d100 == 20:
        creatureString = 'Ravage bear'
    elif d100 == 21:
        creatureString = 'Rhadamanth*'
    elif d100 == 22:
        creatureString = 'Rubar'
    elif d100 == 23:
        creatureString = 'Sarrak'
    elif d100 == 24:
        creatureString = 'Sathosh'
    elif d100 == 25:
        creatureString = 'Seskii'
    elif d100 == 26:
        creatureString = 'Stratharian war moth'
    elif d100 == 27:
        creatureString = 'Tarrow mole*'
    elif d100 == 28:
        creatureString = 'Thuman'
    elif d100 == 29:
        creatureString = 'Vaytaren*'
    elif d100 == 30:
        creatureString = 'Varakith'
    elif d100 == 31:
        creatureString = 'Whisper*'
    elif d100 == 32:
        creatureString = 'Yellow swarm'
    elif d100 == 33:
        creatureString = 'Yovok'
    elif d100 == 34:
        creatureString = 'Accelerator'
    elif d100 == 35:
        creatureString = 'Arch-nano'
    elif d100 == 36:
        creatureString = 'Chance moth'
    elif d100 == 37:
        creatureString = 'Coccitan'
    elif d100 == 38:
        creatureString = 'Deadly warrior'
    elif d100 == 39:
        creatureString = 'Decanted'
    elif d100 == 40:
        creatureString = 'Dedimaskis'
    elif d100 == 41:
        creatureString = 'Entrope'
    elif d100 == 42:
        creatureString = 'Ergovore hound'
    elif d100 == 43:
        creatureString = 'Erulian'
    elif d100 == 44:
        creatureString = 'Flying elchin'
    elif d100 == 45:
        creatureString = 'Gazer'
    elif d100 == 46:
        creatureString = 'Grey sampler'
    elif d100 == 47:
        creatureString = 'Grush'
    elif d100 == 48:
        creatureString = 'Ishenizar'
    elif d100 == 49:
        creatureString = 'Jurulisk'
    elif d100 == 50:
        creatureString = 'Kalyptein crab'
    elif d100 == 51:
        creatureString = 'Magmid'
    elif d100 == 52:
        creatureString = 'Minnern'
    elif d100 == 53:
        creatureString = 'Nalurus'
    elif d100 == 54:
        creatureString = 'Neveri'
    elif d100 == 55:
        creatureString = 'Nychthemeron'
    elif d100 == 56:
        creatureString = 'Plasmar'
    elif d100 == 57:
        creatureString = 'Quotien'
    elif d100 == 58:
        creatureString = 'Rurtalian'
    elif d100 == 59:
        creatureString = 'Shivern'
    elif d100 == 60:
        creatureString = 'Slidikin'
    elif d100 == 61:
        creatureString = 'Spurn'
    elif d100 == 62:
        creatureString = 'Syzygy ghoul'
    elif d100 == 63:
        creatureString = 'Vape'
    elif d100 == 64:
        creatureString = 'Varadimos'
    elif d100 == 65:
        creatureString = 'Xaar'
    elif d100 == 66:
        creatureString = 'Xacorocax'
    elif d100 == 67:
        creatureString = 'Aeon Cavalier'
    elif d100 == 68:
        creatureString = 'Brendril'
    elif d100 == 69:
        creatureString = 'Candescent sabon'
    elif d100 == 70:
        creatureString = 'Carnivorous color'
    elif d100 == 71:
        creatureString = 'Cypher zealot'
    elif d100 == 72:
        creatureString = 'Cypherid'
    elif d100 == 73:
        creatureString = 'Dal'
    elif d100 == 74:
        creatureString = 'Datatar'
    elif d100 == 75:
        creatureString = 'Decanted reaper'
    elif d100 == 76:
        creatureString = 'Dread rider'
    elif d100 == 77:
        creatureString = 'Elaan'
    elif d100 == 78:
        creatureString = 'Flaw'
    elif d100 == 79:
        creatureString = 'Gaphelin'
    elif d100 == 80:
        creatureString = 'Gevanic'
    elif d100 == 81:
        creatureString = 'Golden cachinnate'
    elif d100 == 82:
        creatureString = 'Haneek'
    elif d100 == 83:
        creatureString = 'Imorphin gonoph'
    elif d100 == 84:
        creatureString = 'Imusten crawler'
    elif d100 == 85:
        creatureString = 'Kelursan'
    elif d100 == 86:
        creatureString = 'Latos adjunct'
    elif d100 == 87:
        creatureString = 'Mozck automaton'
    elif d100 == 88:
        creatureString = 'Nacreon wind'
    elif d100 == 89:
        creatureString = 'Namnesis'
    elif d100 == 90:
        creatureString = 'Neanic'
    elif d100 == 91:
        creatureString = 'Nerodrod'
    elif d100 == 92:
        creatureString = 'Nibovian guide'
    elif d100 == 93:
        creatureString = 'Omath ranger'
    elif d100 == 94:
        creatureString = 'Oorgolian tester'
    elif d100 == 95:
        creatureString = 'Reconstructor'
    elif d100 == 96:
        creatureString = 'Roummos'
    elif d100 == 97:
        creatureString = 'Steel angel'
    elif d100 == 98:
        creatureString = 'Stitcher'
    elif d100 == 99:
        creatureString = 'Sweall'
    elif d100 == 100:
        creatureString = 'Tanglet'

    return creatureString
def energyDischargeGenerator():
    d100 = random.randint(1, 100)
    enerDischargeString = ''
    if d100 >= 1 and d100 <= 2:
        enerDischargeString = 'Blue electricity grants those exposed +1 to Speed Edge for one hour, ' \
                              'but repeated exposure causes a runaway reaction that inflicts 3 points ' \
                              'of Speed damage each round until the victim succeeds on a Might defense task.'
    elif d100 >= 3and d100 <= 4:
        enerDischargeString = 'Gravity discharge pulses every few rounds, ' \
                              'dramatically increasing gravity, which inflicts ' \
                              '6 points of ambient damage on a failed Might defense task.'
    elif d100 >= 5 and d100 <= 6:
        enerDischargeString = 'Gravity drops to nothing every few rounds.'
    elif d100 >= 7 and d100 <= 8:
        enerDischargeString = 'As 03–04, but a defunct dark fathom is the ' \
                              'source; reactivating the dark fathom is a ' \
                              'level 6 Intellect task.'
    elif d100 >= 101 and d100 <= 102:
        enerDischargeString = 'Random green electrical flares create voice-like ' \
                              'sounds of an entity that is probably hopelessly insane.'
    elif d100 >= 9 and d100 <= 10:
        enerDischargeString = 'White-hot plasma discharge ' \
                              'inflicts 10 points of damage ' \
                              'to those in its path.'
    elif d100 >= 11 and d100 <= 12:
        enerDischargeString = 'Warm red plasma discharge restores 6 points to ' \
                              'a character’s Pools, but each repeated exposure ' \
                              'causes the character to descend one step on the ' \
                              'damage track.'
    elif d100 >= 13 and d100 <= 14:
        enerDischargeString = 'Pulsed light dazes victims for one round.'
    elif d100 >= 15 and d100 <= 16:
        enerDischargeString = 'Pulsed light gives those exposed one random ' \
                              'piece of knowledge; more than three exposures ' \
                              'per day risks a stroke, which inflicts 5 points ' \
                              'of Intellect damage and moves victim one step ' \
                              'down the damage track.'
    elif d100 >= 17 and d100 <= 18:
        enerDischargeString = 'Pulsed light programs victim who fails an ' \
                              'Intellect defense task into believing they are ' \
                              'on a secret mission to deliver a message to a ' \
                              'creature* in another part of the ruin.' + '\nCreature:  ' + creatureGenerator()
    elif d100 >= 19 and d100 <= 20:
        enerDischargeString = 'Pulsed light programs victim who fails an ' \
                              'Intellect defense task into believing their ' \
                              'allies are evil invaders and should be destroyed; ' \
                              'effect lasts for one minute.'
    elif d100 >= 21 and d100 <= 22:
        enerDischargeString = 'Pulsed light erases victim’s memory of previous ' \
                              '28 hours on failed Intellect defense task.'
    elif d100 >= 23 and d100 <= 24:
        enerDischargeString = 'Pulsed light provides those exposed with 5 points ' \
                              'to add to their Intellect Pool; each point over their ' \
                              'maximum requires an Intellect defense task to avoid a ' \
                              'stroke and descending one step on the damage track.'
    elif d100 >= 25 and d100 <= 26:
        enerDischargeString = 'Pulsed light reprograms cyphers, automatons, artifacts, ' \
                              'and other tech to assemble to create a new level 6 automaton ' \
                              'that is erratic and potentially dangerous, though it could ' \
                              'become an ally.'
    elif d100 >= 27 and d100 <= 28:
        enerDischargeString = 'Purple electricity gives creature a static charge that ' \
                              'can be discharged as part of a melee attack to inflict ' \
                              '+4 points of damage; additional charges can be built up, ' \
                              'but doing so requires an Intellect defense task to avoid ' \
                              'a stroke and descending two steps on the damage track.'
    elif d100 >= 29 and d100 <= 30:
        enerDischargeString = 'Incandescent plasma sears strange symbols and equations ' \
                              'on exposed creature’s skin and face.'
    elif d100 >= 31 and d100 <= 32:
        enerDischargeString = 'Pulsed light programs victim who fails an Intellect defense ' \
                              'task into believing their allies are evil invaders and should be ' \
                              'destroyed; effect lasts for one minute.'
    elif d100 >= 33 and d100 <= 34:
        enerDischargeString = 'Orange electricity supercharges a creature’s carried ' \
                              'cyphers and artifacts, increasing their level by 3. ' \
                              'A repeated exposure causes charged cyphers to explode ' \
                              'as if detonations of their new higher level.'
    elif d100 >= 35 and d100 <= 36:
        enerDischargeString = 'Grey plasma forms aura-like nimbus around exposed ' \
                              'creatures that persists for several days.'
    elif d100 >= 37 and d100 <= 38:
        enerDischargeString = 'Turquoise plasma causes mundane equipment ' \
                              'and clothing to melt into goo; ' \
                              'important equipment resists on a successful ' \
                              'Speed defense task by owner.'
    elif d100 >= 39 and d100 <= 40:
        enerDischargeString = 'Psychic flare from an exposed conduit inflicts ' \
                              '3 points of Intellect damage (ignores Armor) ' \
                              'each round on creatures within immediate range.'
    elif d100 >= 41 and d100 <= 42:
        enerDischargeString = 'Psychic flare from an exposed conduit gives a ' \
                              'random phobia to creatures within immediate range.'
    elif d100 >= 43 and d100 <= 44:
        enerDischargeString = 'Large device with many conduits sparks and snaps ' \
                              'with electrical discharge, but the discharge is ' \
                              'directed into a point on the ceiling, rendering the ' \
                              'device relatively safe to approach, despite appearances.'
    elif d100 >= 45 and d100 <= 46:
        enerDischargeString = 'Kinetic energy leaks from exposed conduit as red ' \
                              'electricity, transferring to creatures within ' \
                              'immediate range, potentially hurling them a short ' \
                              'range in a random direction and inflicting 5 points ' \
                              'of damage.'
    elif d100 >= 47 and d100 <= 48:
        enerDischargeString = 'Kinetic energy leaks from exposed conduit as red ' \
                              'electricity, which gives creatures +3 to Speed Edge ' \
                              'for one hour. Additional exposures inflict Speed ' \
                              'damage instead of conferring Edge.'
    elif d100 >= 49 and d100 <= 50:
        enerDischargeString = 'Chronal energy leaks from cracked device, slowing ' \
                              'exposed creatures to a state of stopped time, so ' \
                              'that no time passes for them, while many ' \
                              'minutes or hours pass externally.'
    elif d100 >= 51 and d100 <= 52:
        enerDischargeString = 'Chronal energy leaks from cracked device, ' \
                              'causing exposed creatures to begin to skip ' \
                              'several seconds forward in time.'
    elif d100 >= 53 and d100 <= 54:
        enerDischargeString = 'Chronal energy leaks from cracked device, ' \
                              'causing exposed creatures to move more slowly ' \
                              'through time. Their voices are noticeably lowered, ' \
                              'and the difficulty of their Speed-based tasks is ' \
                              'increased by one step when dealing with non-slowed ' \
                              'creatures. The effect lasts for several hours.'
    elif d100 >= 55 and d100 <= 56:
        enerDischargeString = 'Chronal energy leaks from cracked device, causing ' \
                              'exposed creatures to move more quickly through time. ' \
                              'Their voices are noticeably higher in pitch, and the ' \
                              'difficulty of their Speed-based tasks is decreased ' \
                              'by one step when dealing with creatures not in ' \
                              'the same state. The effect lasts for a few minutes.'
    elif d100 >= 57 and d100 <= 58:
        enerDischargeString = 'Chronal energy leaks from cracked device, ' \
                              'causing exposed creatures to race through time. ' \
                              'Their voices are a shrill whine that can’t be understood ' \
                              'by those not in the same state, they can take two ' \
                              'actions instead of one on their turn, and the difficulty ' \
                              'of their Speed-based tasks is reduced by one step when ' \
                              'dealing with creatures not in the same state. The effect ' \
                              'lasts for a few minutes.'
    elif d100 >= 59 and d100 <= 60:
        enerDischargeString = 'Device on mount holds a tiny point of fierce light within ' \
                              'a force field; however, an occasional warp in that field ' \
                              'allows bursts of invisible accelerated particles to blast ' \
                              'into the area and nearby areas, scorching objects and creatures ' \
                              'in wavering lines of energy. Symbols in an unknown language, ' \
                              'if they can be translated, read “solar wind tap.”'
    elif d100 >= 61 and d100 <= 62:
        enerDischargeString = 'Magnetic energy leaks from a milky complex of spheres and rods, ' \
                              'visible as a pinkish shimmer that randomly magnetizes a creature’s ' \
                              'metallic possessions. Magnetized possessions are attracted to each other, ' \
                              'repelled apart, or both.'
    elif d100 >= 63 and d100 <= 64:
        enerDischargeString = 'Magnetic energy pulses from a milky complex ' \
                              'of spheres and rods, visible as red pulses of light ' \
                              'that create such intense reactions that the tiny bits ' \
                              'of iron in a creature’s blood become magnetized, ' \
                              'repelling one another in a way that risks causing the ' \
                              'creature to detonate. On a failed Might defense task, ' \
                              'an affected creature descends one step on the damage track ' \
                              'and takes 10 points of Speed damage (ignores Armor).'
    elif d100 >= 65 and d100 <= 66:
        enerDischargeString = 'The surrounding area is oddly quiet as sound is stripped ' \
                              'away and stored in a silvery device thick with metallic ' \
                              'prongs. A malfunction in the device sometimes releases the ' \
                              'stored energy in sonic crescendos of white noise that can ' \
                              'deafen nearby creatures.'
    elif d100 >= 67 and d100 <= 68:
        enerDischargeString = 'As 65–66; in addition, the sound energy reacts to one or more ' \
                              'nearby cyphers, which might cause them to activate, or could ' \
                              'reprogram them to take on a different function than previously determined.'
    elif d100 >= 69 and d100 <= 70:
        enerDischargeString = 'Psychic energy leaks from exposed conduits, inciting discord among ' \
                              'creatures in the area, potentially causing armed conflict among ' \
                              'those who fail an Intellect defense task.'
    elif d100 >= 71 and d100 <= 72:
        enerDischargeString = 'Psychic energy leaks from exposed conduits, ' \
                              'inducing feelings of contentment and joy among ' \
                              'creatures in the area, potentially making those ' \
                              'who fail an Intellect defense task so satisfied ' \
                              'that they slump down and refuse to continue ' \
                              'their exploration.'
    elif d100 >= 73 and d100 <= 74:
        enerDischargeString = 'Psychic energy leaks from exposed conduits, ' \
                              'inducing feelings of fear among creatures in the area, ' \
                              'potentially making those who fail an Intellect ' \
                              'defense task so terrified that they freeze in horror.'
    elif d100 >= 75 and d100 <= 76:
        enerDischargeString = 'Psychic energy leaks from exposed conduits, ' \
                              'inducing feelings of trust among creatures in the area, ' \
                              'potentially making those who fail an Intellect defense ' \
                              'task so credulous that they are not ready to defend ' \
                              'themselves from actual threats.'
    elif d100 >= 77 and d100 <= 78:
        enerDischargeString = 'As 75–76; however, the leaking trust causes creatures* ' \
                              'in the area that would normally be aggressive to ' \
                              'welcome explorers as long-lost allies and friends.' + ':  ' + creatureGenerator()
    elif d100 >= 79 and d100 <= 80:
        enerDischargeString = 'Clear synth module filled with thousands of ' \
                              'tiny flashing entities, normally too small to be ' \
                              'seen by the naked eye, in a saline gel. The module ' \
                              'is cracked, and the gel has spread into one or more ' \
                              'nearby areas. Contact with the gel (and the tiny ' \
                              'creatures in it) causes electrical damage to exposed ' \
                              'flesh, but might repower used cyphers'
    elif d100 >= 81 and d100 <= 82:
        enerDischargeString = 'As 79–80, but instead of emitting light, the entities ' \
                              'absorb light and energy, creating a reverse sparkle in ' \
                              'the leaking gel. Contact with the gel drains Might ' \
                              '(ignores Armor) and could also drain a cypher, rendering it useless.'
    elif d100 >= 83 and d100 <= 84:
        enerDischargeString = 'Concentrated ion leaks from a crystalline and synth device, ' \
                              'causing a howling, moaning sound to reverberate through nearby ' \
                              'areas, along with a slight breeze. A fierce wind emanating from ' \
                              'the device at its source makes it difficult to approach directly.'
    elif d100 >= 85 and d100 <= 86:
        enerDischargeString = 'As 83–84; however, a few successful Intellect tasks could allow ' \
                              'someone to find the leak and turn it off. But a mistake causes the ' \
                              'entire chamber to be launched from the structure like a rocket, ' \
                              'which could be lethal if navigation systems or other means of ' \
                              'steering can’t be found before the chamber crashes back to earth.'
    elif d100 >= 87 and d100 <= 88:
        enerDischargeString = 'Psychic energy leaks from exposed conduits, inducing feelings ' \
                              'of agony among creatures in the area, potentially making those ' \
                              'who fail a Might defense task fall into writhing heaps.'
    elif d100 >= 89 and d100 <= 90:
        enerDischargeString = 'Psychic energy leaks from exposed conduits, ' \
                              'inducing feelings of ecstasy among creatures in the area, ' \
                              'potentially making those who fail a Might defense task fall ' \
                              'into trembling heaps.'
    elif d100 >= 91 and d100 <= 92:
        enerDischargeString = 'Transdimensional energy swirls and flows through the area, ' \
                              'sometimes condensing into objects that were not there earlier, ' \
                              'or causing equipment of creatures in the area to randomly disappear.'
    elif d100 >= 93 and d100 <= 94:
        enerDischargeString = 'Temporal energy swirls and flows through the area, which has a ' \
                              'chance to transport creatures who enter the area to the location ' \
                              'of their birth.'
    elif d100 >= 95 and d100 <= 96:
        enerDischargeString = 'A device spits sonic energy through the area, which sometimes ' \
                              'triggers changes through rapid nanite construction in flesh. ' \
                              'Creatures that fail a Might task are replaced with silent versions ' \
                              'of themselves called whispers over the next 10 + 1d6 hours.'
    elif d100 >= 97 and d100 <= 98:
        enerDischargeString = 'Haze of brownish gas escapes from reservoir; ' \
                              'the gas is a “flavored ion” that induces the sense ' \
                              'of eating a very satisfying sugary treat in creatures ' \
                              'that come into contact with it.'

    elif d100 >= 99 and d100 <= 100:
        enerDischargeString = '''Massive cracked canister has leaked electric algae, 
        which crusts all surfaces in the area and has advanced into some of the areas 
        beyond. The growth has achieved sentience and can telepathically speak with 
        those who are sensitive enough to hear it. The algae can electrify itself to 
        gather fertilizer in the form of living creatures, or to defend itself from 
        grazing.'''

    return enerDischargeString
def explorerGenerator():
    d6 = random.randint(1, 6)
    explorers = d6 + 1
    ex_types = []
    for x in range(explorers):
        d10 = random.randint(1, 10)
        explorerType = ''
        if d10 >= 1 and d10 <= 7:
            explorerType = 'Explorer'
        elif d10 >= 8 and d10 <= 9:
            explorerType = 'Nano'
        elif d10 == 10:
            explorerType = 'Aeon Priest'
        ex_types.append(explorerType)

    d100 = random.randint(1, 100)
    explorerSituationString = ''
    if d100 >= 1 and d100 <= 2:
        explorerSituationString = 'One of the explorers is suffering ' \
                                  'from an infected wound and might die if aid ' \
                                  'isn’t found soon.'
    elif d100 >= 3and d100 <= 4:
        explorerSituationString = 'The explorers are flush with cyphers ' \
                                  'and artifacts, having just salvaged a nearby ' \
                                  'chamber.'
    elif d100 >= 5 and d100 <= 6:
        explorerSituationString = 'One of the explorers is planning to betray their ' \
                                  'comrades within the next day to steal an artifact ' \
                                  'that was denied to them.'
    elif d100 >= 7 and d100 <= 8:
        explorerSituationString = 'One of the explorers tries to defect to the PCs’ ' \
                                  'group, indicating that they’ve had a falling out with ' \
                                  'their own group.'
    elif d100 >= 9 and d100 <= 10:
        explorerSituationString = 'One of the explorers tries to defect to the PCs’ ' \
                                  'group after alienating some of their own group by ' \
                                  'being a liar, a coward, and a thief.'
    elif d100 >= 11 and d100 <= 12:
        explorerSituationString = 'The explorers are resting without a watch.'
    elif d100 >= 13 and d100 <= 14:
        explorerSituationString = 'The explorers are resting with a “pet” creature* on watch.' + '\nCreature:  ' + creatureGenerator()
    elif d100 >= 15 and d100 <= 16:
        explorerSituationString = 'Explorers are on the move, following the lead of a ' \
                                  'floating level 4 automaton salvaged from some other ' \
                                  'part of the installation.'
    elif d100 >= 17 and d100 <= 18:
        explorerSituationString = 'Explorers are on the move, fleeing from several creatures*.' + ':  ' + creatureGenerator()
    elif d100 >= 19 and d100 <= 20:
        explorerSituationString = 'Explorers are investigating the remains of a dead creature*.' + '\nCreature:  ' + creatureGenerator()
    elif d100 >= 21 and d100 <= 22:
        explorerSituationString = 'Explorers are found mysteriously and messily dead, but not looted.'
    elif d100 >= 23 and d100 <= 24:
        explorerSituationString = 'One explorer has a strange device (level 6) stuck ' \
                                  'to their head, which seems to be slowly turning them ' \
                                  'insane. The explorer’s friends don’t want to admit it.'
    elif d100 >= 25 and d100 <= 26:
        explorerSituationString = 'One of the PCs knows one of the explorers from an encounter ' \
                                  'several months or years ago, a meeting that left ' \
                                  'bad blood between them.'
    elif d100 >= 27 and d100 <= 28:
        explorerSituationString = 'One of the explorers knows a PC and apparently ' \
                                  'feels as if they owe that character their devotion ' \
                                  'because the PC saved them in the past. The PC may or ' \
                                  'may not remember this event.'
    elif d100 >= 29 and d100 <= 30:
        explorerSituationString = 'Two additional explorers accompany the group, each ' \
                                  'an apparent duplicate of the group leader, identical but ' \
                                  'for the odd device they have in place of heads.'
    elif d100 >= 31 and d100 <= 32:
        explorerSituationString = 'One of the explorers is an apparent duplicate of one PC, ' \
                                  'identical but for the odd device the duplicate has in place ' \
                                  'of their head. The other explorers say their device-headed ' \
                                  'ally—who never speaks—joined them while they were traveling ' \
                                  'through the installation. The duplicate acts as ' \
                                  'if the PC doesn’t exist.'
    elif d100 >= 33 and d100 <= 34:
        explorerSituationString = 'The explorers all bear odd antennae-like metallic rods ' \
                                  'protruding from the backs of their necks. They act as if ' \
                                  'dazed and uncertain of where they are, or possibly even who ' \
                                  'they are.'
    elif d100 >= 35 and d100 <= 36:
        explorerSituationString = 'One of the explorers is on the edge of heartbreak, ' \
                                  'having lost their pet seskii elsewhere in the installation.'
    elif d100 >= 37 and d100 <= 38:
        explorerSituationString = 'A light-eating nimbus clings to one explorer, ' \
                                  'and their allies keep their distance. They say the ' \
                                  'nimbus just appeared one day, and since then, the ' \
                                  'group has suffered a series of unfortunate incidents ' \
                                  'they attribute to bad luck. According to their story, ' \
                                  'the bearer of the nimbus has enjoyed only good luck.'
    elif d100 >= 39 and d100 <= 40:
        explorerSituationString = 'The explorers are only about a foot high. ' \
                                  'They say they’ve been wandering lost in the installation ' \
                                  'for days, not realizing they’d been shrunk; they thought ' \
                                  'they’d been transported to a parallel dimension where ' \
                                  'everything was larger.'
    elif d100 >= 41 and d100 <= 42:
        explorerSituationString = 'The explorers use weapons that fire tiny darts ' \
                                  'covered with level 5 poison.'
    elif d100 >= 43 and d100 <= 44:
        explorerSituationString = 'A creature* accompanies the explorers, and they ' \
                                  'interact with it as if it were an oracle, even if ' \
                                  'it isn’t normally known for such an ability or can’t ' \
                                  'communicate in a way that seems to make sense.' + '\nCreature:  ' + creatureGenerator()
    elif d100 >= 45 and d100 <= 46:
        explorerSituationString = 'The explorers encountered a device that wiped their ' \
                                  'memories, and they’ve been wandering afraid and confused ' \
                                  'for days.'
    elif d100 >= 47 and d100 <= 48:
        explorerSituationString = 'The explorers seem normal at first, if standoffish and ' \
                                  'quiet, but they are dead, and a device nestled in the back ' \
                                  'of one explorer is invisibly holding all of them up, making ' \
                                  'them seem alive.'
    elif d100 >= 49 and d100 <= 50:
        explorerSituationString = "One of the explorers has metal insects for teeth, " \
                                  "which leave their host's mouth and speak for the host " \
                                  "(or attack the host's foes)."

    elif d100 >= 51 and d100 <= 52:
        explorerSituationString = 'The explorers are all related, including one ' \
                                  'or perhaps two parents and their children.'
    elif d100 >= 53 and d100 <= 54:
        explorerSituationString = 'One explorer has been secretly killing off ' \
                                  'others in the group for their own reasons. ' \
                                  'The explorers say that when they entered the structure, ' \
                                  'they had double their current number.'
    elif d100 >= 55 and d100 <= 56:
        explorerSituationString = 'On one of the explorers, one forearm has been replaced ' \
                                  'with an elongated metallic pyramid. It’s a formidable ' \
                                  'weapon, but the explorer can’t hold things with it, ' \
                                  'and they bear scars on other body parts where they ' \
                                  'accidentally cut themselves on the jagged point.'
    elif d100 >= 57 and d100 <= 58:
        explorerSituationString = 'The explorers are part of a larger group that claims ' \
                                  'the structure for its own use, and they are very aggressive ' \
                                  'toward creatures and characters who are not part of that group.'
    elif d100 >= 59 and d100 <= 60:
        explorerSituationString = 'One or two of the explorers have become addicted to a blue ' \
                                  'fungus they found growing in the area (or a nearby area), ' \
                                  'and now they can’t go more than a few hours without needing ' \
                                  'to eat more.'
    elif d100 >= 61 and d100 <= 62:
        explorerSituationString = 'The explorers were dazed by exposure to a device somewhere ' \
                                  'in the structure, and upon seeing the PCs, they respond like ' \
                                  'young animals do when imprinting on an adult. This lasts for ' \
                                  'a few hours or days, but eventually wears off.'
    elif d100 >= 63 and d100 <= 64:
        explorerSituationString = 'The explorers seem friendly, but they’re bandits.'
    elif d100 >= 65 and d100 <= 66:
        explorerSituationString = 'One of the explorers is a cartographer and wants ' \
                                  'to see any maps the characters have made. In return, ' \
                                  'they offer to show the PCs their maps.'
    elif d100 >= 67 and d100 <= 68:
        explorerSituationString = 'One of the explorers appears to be made of glass.'
    elif d100 >= 69 and d100 <= 70:
        explorerSituationString = 'One of the explorers constantly expels shelled ' \
                                  'slugs from their mouth, one or two a minute, but ' \
                                  'seems to regard the condition as similar to having ' \
                                  'chronic hiccups. The slugs slowly glide away if allowed.'
    elif d100 >= 71 and d100 <= 72:
        explorerSituationString = 'The explorers are partially out of phase after ' \
                                  'a run-in with a device that detonated, leaving them ' \
                                  'unable to interact with anything around them. They ' \
                                  'are looking for help.'
    elif d100 >= 73 and d100 <= 74:
        explorerSituationString = 'The explorers ride a large, many-legged level 4 ' \
                                  'automaton. It is big enough to accommodate up to ' \
                                  'four explorers as a mount, but narrow enough to fit ' \
                                  'down most corridors in the structure.'
    elif d100 >= 75 and d100 <= 76:
        explorerSituationString = 'One of the explorers floats in a silvery, ' \
                                  'transparent bubble just a foot above the floor. ' \
                                  'The bubble hedges out insults, harsh language, ' \
                                  'and shocking sights. To that explorer, the world ' \
                                  'seems idyllic and peaceful.'
    elif d100 >= 77 and d100 <= 78:
        explorerSituationString = 'One of the explorers has the others in their ' \
                                  'group chained to the synth- reinforced band of ' \
                                  'their belt.'
    elif d100 >= 79 and d100 <= 80:
        explorerSituationString = 'One of the explorers sings loudly and often, ' \
                                  'apparently believing they are raising their ' \
                                  'compatriots’ spirits, when in fact the songs annoy ' \
                                  'the group—which is quite obvious to the PCs.'
    elif d100 >= 81 and d100 <= 82:
        explorerSituationString = 'One of the explorers wears a spherical helm, ' \
                                  'through which can be seen what appears to be a view ' \
                                  'of a spiral vortex, like a galaxy, instead of a face. ' \
                                  'This explorer never talks, but instead motions. The ' \
                                  'other explorers do whatever this one says.'
    elif d100 >= 83 and d100 <= 84:
        explorerSituationString = 'The explorers initially believe that the characters ' \
                                  'have been dispatched by some other group to find ' \
                                  'and assassinate them.'
    elif d100 >= 85 and d100 <= 86:
        explorerSituationString = 'One of the explorers offers to tell the characters one ' \
                                  'of the seven hidden words and one of the six lost symbols, ' \
                                  'in return for an artifact. Are the word and symbol actually ' \
                                  'valuable, or is it a ruse? Maybe both.'
    elif d100 >= 87 and d100 <= 88:
        explorerSituationString = 'On seeing the characters, the explorers react as if seeing ' \
                                  'their worst nightmares, dropping whatever they were ' \
                                  'holding and fleeing in random directions if possible. Either ' \
                                  'the characters have gained a reputation, or the explorers ' \
                                  'were reacting to something the PCs haven’t yet noticed about ' \
                                  'themselves or about something that invisibly accompanies them.'
    elif d100 >= 89 and d100 <= 90:
        explorerSituationString = 'One of the explorers claims to be a relative of the Amber Pope himself.'
    elif d100 >= 91 and d100 <= 92:
        explorerSituationString = 'The explorers are connected by a thin, living tube, ' \
                                  'which is flexible and shifts of its own accord so it ' \
                                  'doesn’t entangle or trip them.'
    elif d100 >= 93 and d100 <= 94:
        explorerSituationString = 'One explorer is made up of hundreds of tiny serpents, ' \
                                  'which sometimes break apart into disparate creatures before ' \
                                  'returning to a single entity.'
    elif d100 >= 95 and d100 <= 96:
        explorerSituationString = 'Scintillating crystals orbit around one explorer.'
    elif d100 >= 97 and d100 <= 98:
        explorerSituationString = 'The explorers are desperately looking for a missing member ' \
                                  'of their group, who was gone when they woke from sleep. ' \
                                  'The one missing had been on watch.'
    elif d100 >= 99 and d100 <= 100:
        explorerSituationString = 'One of the characters recognizes one or more of the ' \
                                  'explorers from an interaction in a nearby community. ' \
                                  'The interaction might have been positive, negative, ' \
                                  'or just weird.'



    explorerString = 'Explorer numbers:  ' + str(explorers) + ' \nExplorer Types:  ' + str(ex_types) + ' \nSituation:  ' + explorerSituationString

    return explorerString
def integratedMachineGenerator():
    d100 = random.randint(1, 100)
    intMachineString = ''
    if d100 >= 1 and d100 <= 2:
        intMachineString = '''Grafts one extra automaton limb onto a user, 
        which adds +1 to die rolls involving tasks where 
        having an extra hand would be useful'''

    elif d100 >= 3 and d100 <= 4:
        intMachineString = '''Plates a user with flexible synth, 
        granting +1 to Armor but an inability on movement-related tasks'''

    elif d100 >= 5 and d100 <= 7:
        intMachineString = '''Produces an offensive cypher'''

    elif d100 >= 8 and d100 <= 9:
        intMachineString = '''Produces a defensive cypher'''

    elif d100 >= 10 and d100 <= 12:
        intMachineString = '''Recharges a used cypher'''

    elif d100 >= 13 and d100 <= 14:
        intMachineString = '''Heals, cures, and “refurbishes” an unhealthy 
        living creature or automaton; for example, a creature missing 
        an eye or limb gains a new one, though one that is made of 
        crystal and synth'''

    elif d100 >= 15 and d100 <= 17:
        intMachineString = '''Grants a user long-range telepathy 
        for about a day; the following day the creature suffers 
        a severe headache and has a temporary inability on 
        Intellect-related tasks'''

    elif d100 >= 18 and d100 <= 19:
        intMachineString = '''Grants a user +3 to Might Edge for about a day; 
        the following day the creature has severe stiffness and a temporary 
        inability on Might-related tasks'''

    elif d100 >= 20 and d100 <= 22:
        intMachineString = '''Grants a user perfect pitch'''

    elif d100 >= 23 and d100 <= 24:
        intMachineString = '''Duplicates one nonliving object'''

    elif d100 >= 25 and d100 <= 27:
        intMachineString = '''Creates a wormhole that persists for 
        an hour to a location the user knows to exist'''

    elif d100 >= 28 and d100 <= 29:
        intMachineString = '''Over the course of an hour, a user is 
        returned to their most viable physiological age (for humans, 
        that’s around 25 years old)'''

    elif d100 >= 30 and d100 <= 32:
        intMachineString = '''User gains a voice in their head that reduces 
        the difficulty of all knowledge tasks by one step, but sometimes attempts 
        to take over when the user is hurt, distracted, or sleeping'''

    elif d100 >= 33 and d100 <= 34:
        intMachineString = '''User gains a voice in their head that grants an 
        asset on all tasks to detect falsehoods, but also grants the user an 
        inability when trying to lie'''

    elif d100 >= 35 and d100 <= 37:
        intMachineString = '''User gains an additional eye that can’t stand 
        bright light, but allows the user to see in the dark'''

    elif d100 >= 38 and d100 <= 39:
        intMachineString = '''User gains “flesh flaps” between their arms, 
        fingers, and sides of their body, allowing them to glide to a safe 
        landing from all falls over 30 feet (9 m)'''

    elif d100 >= 40 and d100 <= 41:
        intMachineString = '''User gains the ability to eat literally anything 
        (including rocks, synth, metal, and drit) and gain nutrition; objects 
        of up to level 7 can be eaten and destroyed in this fashion with no 
        harm to the eater'''

    elif d100 >= 42 and d100 <= 44:
        intMachineString = '''Produces a clone of the user that is mentally 
        and physically only three months old'''

    elif d100 >= 45 and d100 <= 46:
        intMachineString = '''A person the user knows to exist of up to level 
        6 is immediately transferred from wherever they are to this location'''

    elif d100 >= 47 and d100 <= 49:
        intMachineString = '''User is transferred into the presence of a being 
        of up to level 6 that they know to exist, wherever that being is located'''

    elif d100 >= 50 and d100 <= 51:
        intMachineString = '''Dead creatures brought here are reconstructed in 
        animate glass, with a few memories of the dead creature'''

    elif d100 >= 52 and d100 <= 54:
        intMachineString = '''Grafts synth struts to user, increasing their strength 
        (+1 to Might Edge) but causing them to move stiffly (3 points deducted from 
        Speed Pool)'''

    elif d100 >= 55 and d100 <= 56:
        intMachineString = '''Grafts synth struts to user, which quickens them 
        (+1 to Speed Edge) but makes them more fragile (3 points deducted from 
        Might Pool)'''

    elif d100 >= 57 and d100 <= 59:
        intMachineString = '''Synth helm fitted to user alleviates their need to breathe'''

    elif d100 >= 60 and d100 <= 61:
        intMachineString = '''Synth helm fitted to user removes sight but 
        greatly increases other senses; it’s essentially a wash, except the 
        creature can “see” in the dark'''

    elif d100 >= 62 and d100 <= 64:
        intMachineString = '''Grafts extra synth arm to user that functions 
        only one minute per day'''

    elif d100 >= 65 and d100 <= 66:
        intMachineString = '''User gains a powerful mutation for 28 hours'''

    elif d100 >= 67 and d100 <= 69:
        intMachineString = '''User gains a powerful mutation, but only after 
        being encased in a chrysalis for 28 hours, during which time they are 
        insensate and vulnerable'''

    elif d100 >= 70 and d100 <= 71:
        intMachineString = '''Device contains knowledge of nearby star systems'''

    elif d100 >= 72 and d100 <= 74:
        intMachineString = '''Device contains knowledge of nearby dimensions'''

    elif d100 >= 75 and d100 <= 77:
        intMachineString = '''Device contains knowledge of esoteric mathematical 
        formulas that could grant an asset on one nano ability or focus ability that 
        deals with manipulation of nanites or the numenera'''

    elif d100 >= 78 and d100 <= 80:
        intMachineString = '''Device contains a wealth of confusing scenes from an 
        ancient star-faring species'''

    elif d100 >= 81 and d100 <= 83:
        intMachineString = '''Device renders a creature or object out of phase for 
        a random period, usually lasting no more than 28 hours'''

    elif d100 >= 84 and d100 <= 86:
        intMachineString = '''Device grows a flesh bud on user that contains a knot of 
        neurological tissue; once integrated, it adds 1 point to the user’s Intellect Pool'''

    elif d100 >= 87 and d100 <= 89:
        intMachineString = '''Device grows a flesh bud on user that contains a knot of 
        neurological tissue; once integrated, it gives the user an asset on any knowledge task'''

    elif d100 >= 90 and d100 <= 92:
        intMachineString = '''Device grows a flesh bud on user that contains a knot of 
        neurological tissue; once integrated, the PC’s mind is transferred to the bud 
        and their head slowly begins to atrophy'''

    elif d100 >= 93 and d100 <= 95:
        intMachineString = '''Device malfunctions on use, goes dead'''

    elif d100 >= 96 and d100 <= 100:
        intMachineString = '''Device malfunctions on use, detonates'''

    return intMachineString
def interStitialCavityGenerator():
    d100 = random.randint(1, 100)
    interstitialCavityString = ''
    if d100 >= 1 and d100 <= 2:
        interstitialCavityString = '''Empty and echoing.'''

    elif d100 >= 3and d100 <= 4:
        interstitialCavityString = '''Empty and echoing, but contains vast 
        outlines of what must have been immense machines or machine components 
        that have since been removed.'''

    elif d100 >= 5 and d100 <= 6:
        interstitialCavityString = '''As 03–04, except slender trees with 
        black bark have sprung up in a soft layer of drit and dust.'''

    elif d100 >= 7 and d100 <= 8:
        interstitialCavityString = '''As 03–04, except spiders, worms, 
        and similar vermin are thick in the area, infesting a few large masses 
        that turn out to be the bones of long-dead creatures that were very, very large.'''

    elif d100 >= 9 and d100 <= 10:
        interstitialCavityString = '''As 03–04, except one of the 
        outlines seems like it might have been of a massive human shape.'''

    elif d100 >= 11 and d100 <= 12:
        interstitialCavityString = '''Filled with immense, dead, corroded, 
        long-silent machine components fused to interior. Each character who 
        spends several hours clambering over the vast dead engines can find 
        one or two cyphers and 1d20 shins, but must succeed on one level 3 
        Speed defense task to avoid slipping and falling from a great height (d100 feet).'''

    elif d100 >= 13 and d100 <= 14:
        interstitialCavityString = '''As 11–12, but contains a lair for a creature*.''' + '\nCreature:  ' + creatureGenerator()

    elif d100 >= 15 and d100 <= 16:
        interstitialCavityString = '''As 11–12, but the footing is far more dangerous 
        due to a slick of oil-like fluid coating everything; moving safely around the 
        chamber and avoiding falling requires a successful level 5 Speed defense task.'''

    elif d100 >= 17 and d100 <= 18:
        interstitialCavityString = '''As 11–12, but a strange rust covers the mechanism 
        and acts like a contact poison.'''

    elif d100 >= 19 and d100 <= 20:
        interstitialCavityString = '''As 11–12, but several dead humans lie at the foot 
        of the great machines. Investigation reveals they’ve been looted, but also that 
        some of them have had their faces flayed off and sewn back on 
        again with synth thread.'''

    elif d100 >= 21 and d100 <= 22:
        interstitialCavityString = '''Filled with immense, partially functioning, 
        colossal machine components fused to walls and ceiling high above. The 
        components whir, vibrate, and give off a constant bass roar that is difficult 
        to endure over long periods. Each character who spends several hours clambering 
        over the vast degraded devices can find one or two cyphers and 1d20 shins, 
        but must succeed on one level 3 Speed defense task to avoid slipping and falling 
        from a great height (d100 feet), and one level 3 Intellect task to avoid causing 
        a local malfunction.'''

    elif d100 >= 23 and d100 <= 24:
        interstitialCavityString = '''As 21–22; however, characters who spend a few 
        hours studying the machines might discover that they could be induced to attach 
        a massive (house-sized) device capable of creating an amazing amount of thrust, 
        enough to potentially launch the object into space or even farther.'''

    elif d100 >= 25 and d100 <= 26:
        interstitialCavityString = '''As 21–22; however, characters who spend a few hours 
        studying the machines might discover that they could be induced to suck all the 
        metal out of a very large object and deliver a metallic ingot of the stolen metals. 
        The process inflicts 10 points of damage to a living creature and causes them to 
        descend one step on the damage track.'''

    elif d100 >= 27 and d100 <= 28:
        interstitialCavityString = '''As 21–22; however, characters who spend a few 
        hours studying the machines might discover that they could be induced to extrude 
        massive (house-sized) crystal solids that glimmer internally but have no obvious 
        purpose.'''

    elif d100 >= 29 and d100 <= 30:
        interstitialCavityString = '''As 21–22; however, characters who spend a few hours 
        studying the machines might discover that they could be induced to plate an arbitrarily 
        large object with a level 4 synth coating that grants +4 to Armor (the process 
        would kill human- sized creatures, essentially encasing them in a chunk of 
        solid synth).'''
    elif d100 >= 31 and d100 <= 32:
        interstitialCavityString = '''As 21–22, but roll on the Integrated Machine 
        Table to see what these machines might do. However, the ones found in an 
        interstitial cavity would create the stated effect on a far grander scale, 
        which means effects that might normally enhance or aid a human-sized creature 
        will instead probably kill them.'''

    elif d100 >= 33 and d100 <= 34:
        interstitialCavityString = '''As 31–32, but an entity has previously entered 
        the chamber and scribed in a silvery metallic ink across the machine surfaces 
        what are essentially “margin notes” to help those new to the area figure out 
        what the vast machines might do.'''

    elif d100 >= 35 and d100 <= 36:
        interstitialCavityString = '''Filled with tumbling components and machine parts 
        10 feet (3 m) to a side, apparently once fused to the walls but now weightless 
        and dead, that crash and batter each other. Each long distance moved through the 
        chamber requires a successful level 5 Speed defense task to avoid being battered 
        for 5 points of damage.'''

    elif d100 >= 37 and d100 <= 38:
        interstitialCavityString = '''Half filled with fluid from an ancient leak. 
        Roll on the Matter Leak Table to determine the nature of the reservoir-sized spill. 
        Opening the wrong exit could cause the fluid to leak into other sections of the ruin, 
        causing flooding and dangerous conditions, depending on the nature of the material.'''

    elif d100 >= 39 and d100 <= 40:
        interstitialCavityString = '''Vast machinery holds in place a massive sphere 
        at the center of the cavity. The sphere is a planet, which, though small, 
        is still much too large to be contained in the cavity. But thanks to the enclosing 
        machinery that folds space, the planet is indeed held in place. About two-thirds 
        the size of Earth, the strange planet is swaddled in red clouds and storms. 
        Characters who attempt to access the planet’s surface find it habitable, 
        but incredibly unstable. Volcanoes and earthquakes are common, but plant 
        life is lush, though there don’t seem to be any animals or other ambulatory 
        creatures, or in fact any sign of previous habitation. If anything did live 
        here once, the constant upheaval on the surface likely recycled them deep into 
        the planet’s core long ago.'''

    elif d100 >= 41 and d100 <= 42:
        interstitialCavityString = '''High, narrow towers made of what appears to be dark 
        red glass jut from the sides and floor (and hang from the ceiling) of this space. 
        The towers have no doors, but sometimes spontaneously absorb those looking to enter, 
        freezing them in stasis.'''

    elif d100 >= 43 and d100 <= 44:
        interstitialCavityString = '''As 41–42, but the towers are hollow, 
        and one serves as the home or lair to at least one creature*.''' + ':  ' + creatureGenerator()

    elif d100 >= 45 and d100 <= 46:
        interstitialCavityString = '''Metallic pyramids of all sizes, some as small as a thumbnail, 
        others as tall as buildings, are jumbled in this space.'''

    elif d100 >= 47 and d100 <= 48:
        interstitialCavityString = '''As 45–46, but the pyramids are magnetized, so automatons 
        and creatures with metal armor stick to exposed surfaces; some dead automatons and a 
        few explorers who couldn’t get their armor off can be found here.'''

    elif d100 >= 49 and d100 <= 50:
        interstitialCavityString = '''The space is occupied by an odd ecosystem of purple plants, 
        tiny red clouds, and small, singing, gopher-like creatures with two heads.'''

    elif d100 >= 51 and d100 <= 52:
        interstitialCavityString = '''Blotches of green and yellow color move like the shadows 
        of clouds across the empty surfaces of this large space.'''

    elif d100 >= 53 and d100 <= 54:
        interstitialCavityString = '''As 51–52, but the color “shadows” are attracted to 
        motion and attack creatures by “staining” and then eating their substance, 
        converting them into yet more color.'''

    elif d100 >= 55 and d100 <= 56:
        interstitialCavityString = '''A massive crystalline object floats at the 
        center of this cavity, slowly rotating, held in place by an unseen force.'''

    elif d100 >= 57 and d100 <= 58:
        interstitialCavityString = '''As 55–56, but if light is directed on the crystal, 
        the light is broken into all the colors of the rainbow and more; two of the colors 
        are not normally possible in this dimension, and creatures that see them or that 
        are bathed in their light risk temporary insanity.'''

    elif d100 >= 59 and d100 <= 60:
        interstitialCavityString = '''As 55–56, but the head of a massive, 
        multi-eyed creature that isn’t completely humanoid is preserved in the crystal.'''

    elif d100 >= 61 and d100 <= 62:
        interstitialCavityString = '''Broken conduits drizzle the exposed areas of 
        the space with a yellowish, sap-like substance that has formed stalagmites and 
        stalactites over hundreds of years; the sap is sweet to the taste and nutritious.'''

    elif d100 >= 63 and d100 <= 64:
        interstitialCavityString = '''This space is apparently where some kind of creature 
        has stored trophies for hundreds of years—trophies in the form of teeth, which lie 
        in cascading piles across the cavity. The creature responsible is not immediately 
        evident.'''

    elif d100 >= 65 and d100 <= 66:
        interstitialCavityString = '''A broken, partly smashed vehicle capable of traveling 
        into the void lies in—or has been somehow wedged into—this cavity. With enough time 
        and effort, the ship might be able to be repaired, but getting it out of the cavity 
        is another problem.'''

    elif d100 >= 67 and d100 <= 68:
        interstitialCavityString = '''Waves of energy flow back and forth across this room like heat 
        mirages over a hard surface on a hot day. The energy ruffles hair and clothing but doesn’t 
        seem directly harmful.'''

    elif d100 >= 69 and d100 <= 70:
        interstitialCavityString = '''As 67–68, but devices of the numenera (cyphers, artifacts, 
        and oddities) begin to glow brighter and brighter when exposed to the energy. Devices 
        that remain exposed for more than three rounds detonate.'''

    elif d100 >= 71 and d100 <= 72:
        interstitialCavityString = '''As 67–68, but with each wave, a mental 
        surge of thousands of whispering voices intrudes on the minds of conscious 
        creatures in the area.'''

    elif d100 >= 73 and d100 <= 74:
        interstitialCavityString = '''As 67–68, but creatures in the area risk 
        having their minds randomly switched. This can be especially disconcerting 
        for characters whose minds get switched with a creature* that follows them 
        into the area.''' + ':  ' + creatureGenerator()

    elif d100 >= 75 and d100 <= 76:
        interstitialCavityString = '''Refugees from a nearby village of humans overrun 
        by creatures* hide in this chamber, living off the by-products of a large 
        machine that produces tasteless but nutritious brown goo.''' + ':  ' + creatureGenerator()

    elif d100 >= 77 and d100 <= 78:
        interstitialCavityString = '''Filled with immense, partially functioning, 
        colossal machine components fused to walls and ceiling high above. 
        Broken devices emit sprays of pollen-like dust that changes the center of 
        gravity of creatures and objects it touches, making it difficult for creatures 
        to walk or run without tipping over.'''

    elif d100 >= 79 and d100 <= 80:
        interstitialCavityString = '''Filled with immense, partially functioning, 
        colossal machine components fused to walls and ceiling high above. 
        Broken devices emit sprays of white mist that acts as poison to living creatures, 
        but which coats automatons in a layer of protective coating granting +1 to Armor.'''

    elif d100 >= 81 and d100 <= 82:
        interstitialCavityString = '''The air in this chamber is hazed with narrow 
        vortices that move randomly about, sometimes spinning apart, other times 
        spinning back together again. The vortices spin away from creatures and moving 
        objects.'''

    elif d100 >= 83 and d100 <= 84:
        interstitialCavityString = '''As 81–82, but the vortices represent splinter 
        personalities of a machine intelligence that once inhabited this area. 
        Individual vortices can speak by vibrating the air, but each has a very narrow 
        slice of knowledge or specialty.'''

    elif d100 >= 85 and d100 <= 86:
        interstitialCavityString = '''As 81–82, but each vortex is a level 4 threat; 
        1d6 of them zero in on any group of creatures trying to make their way across 
        the cavity.'''

    elif d100 >= 87 and d100 <= 88:
        interstitialCavityString = '''A lens dozens of feet across composed of clear 
        synth has been crudely installed here; it focuses sunlight that sometimes shines 
        in from cracks above onto a device that hums and vibrates when in bright light.'''

    elif d100 >= 89 and d100 <= 90:
        interstitialCavityString = '''As 87–88, except the lens wakes for the span 
        of time the beam is focused fully on it (about two minutes), during which time 
        it serves as a terminal into the datasphere.'''

    elif d100 >= 91 and d100 <= 92:
        interstitialCavityString = '''Discharges of electricity play throughout this 
        chamber like some kind of cloud-wreathed hellscape of danger.'''

    elif d100 >= 93 and d100 <= 94:
        interstitialCavityString = '''The holographic image of a gargantuan eye 
        flickers into existence in the cavity, blinking and focusing on intruders 
        before fading again for a random period. Devices in the area are found to 
        project this image, as well as have many other functions that are less easy 
        to identify.'''

    elif d100 >= 95 and d100 <= 96:
        interstitialCavityString = '''Massive metallic ring dominates the cavity, 
        cracked and possibly unstable. The ring magnetically holds a brilliant sphere 
        of glowing white material at the center.'''

    elif d100 >= 97 and d100 <= 98:
        interstitialCavityString = '''As 95–96, but the sphere at the center pulses 
        in a variety of rhythms when creatures enter the area. The pulsing is actually 
        communication from beings who exist in two dimensions and are curious about the 
        dimension of the Ninth World.'''

    elif d100 >= 99 and d100 <= 100:
        interstitialCavityString = '''As 95–96, but the sphere represents stored, 
        massively compacted waste. Any object or creature thrown into the ring is 
        compacted down to a thin layer of degenerate matter coating the sphere.'''

    return interstitialCavityString
def matterLeakGenerator():
    d100 = random.randint(1, 100)
    matterLeakString = ''
    if d100 >= 1 and d100 <= 2:
        matterLeakString = '''Water, slightly briny but potable'''

    elif d100 >= 3 and d100 <= 4:
        matterLeakString = '''Water, tastes oily but potable'''

    elif d100 >= 5 and d100 <= 6:
        matterLeakString = '''Water, tastes sweet and fizzy but potable'''

    elif d100 >= 7 and d100 <= 8:
        matterLeakString = '''Green “gunk” that sticks and stains'''

    elif d100 >= 9 and d100 <= 10:
        matterLeakString = '''Green “gunk” that sticks and burns (like acid) 
        those who stumble into the material'''

    elif d100 >= 11 and d100 <= 12:
        matterLeakString = '''Brownish organic fluid that smells like alcohol 
        and explodes into a raging inferno if exposed to flame'''

    elif d100 >= 13 and d100 <= 14:
        matterLeakString = '''Silvery, metallic solid that flowed when it was 
        white-hot molten metal'''

    elif d100 >= 15 and d100 <= 16:
        matterLeakString = '''White-hot, flowing, molten metal that burns to the 
        bone anyone who touches or falls into it'''

    elif d100 >= 17 and d100 <= 18:
        matterLeakString = '''Viscous black ooze that contains trace amounts of 
        void matter and acts as one large midnight stone from which several “uses” 
        can be obtained'''

    elif d100 >= 19 and d100 <= 20:
        matterLeakString = '''Drifts of yellowish powder that smells like metal'''

    elif d100 >= 21 and d100 <= 22:
        matterLeakString = '''As 19–20, but composed of nanites that drain power 
        from tech, cyphers, and artifacts'''

    elif d100 >= 23 and d100 <= 24:
        matterLeakString = '''Drifts of crimson powder that is magnetic'''

    elif d100 >= 25 and d100 <= 26:
        matterLeakString = '''Viscous transparent gel that reacts to the force 
        of gravity in the opposite direction of other matter'''

    elif d100 >= 27 and d100 <= 28:
        matterLeakString = '''Viscous brown gel that gives off light for the 
        same duration and at the same intensity as light shined on it'''

    elif d100 >= 29 and d100 <= 30:
        matterLeakString = '''Viscous black gel that shimmers and seems to emit 
        sounds similar to laughing when jostled'''

    elif d100 >= 31 and d100 <= 32:
        matterLeakString = '''Water-like fluid with blue tint that reflects 
        images in its depths of strongly imagined scenes'''

    elif d100 >= 33 and d100 <= 34:
        matterLeakString = '''Living fluid solvent that eats through 1 cubic foot 
        (.03 cubic m) of material for five rounds if removed from area of leak'''

    elif d100 >= 35 and d100 <= 36:
        matterLeakString = '''Drifts of pale dust that desiccate any 
        object that comes into contact with them'''

    elif d100 >= 37 and d100 <= 38:
        matterLeakString = '''Salty water in which reddish jellyfish dart and float'''

    elif d100 >= 39 and d100 <= 40:
        matterLeakString = '''Salty water in which reddish jellyfish dart and float, 
        plus a creature* lairs near or in the water''' + ':  ' + creatureGenerator()

    elif d100 >= 41 and d100 <= 42:
        matterLeakString = '''White fluid streaked with silvery strands 
        is a concentrated consciousness that dazes those exposed'''

    elif d100 >= 43 and d100 <= 44:
        matterLeakString = '''Multicolored marble-sized spheroids'''

    elif d100 >= 45 and d100 <= 46:
        matterLeakString = '''Multicolored marble-sized spheroids that 
        each weigh 10 times more than a similar amount of metal'''

    elif d100 >= 47 and d100 <= 48:
        matterLeakString = '''Leaflike fractal wafers that rustle in response to thoughts'''

    elif d100 >= 49 and d100 <= 50:
        matterLeakString = '''Leaflike fractal wafers that animate and flutter 
        to exposed devices like insects drawn to light'''

    elif d100 >= 51 and d100 <= 52:
        matterLeakString = '''Leaflike fractal wafers that stick like iridescent tattoos if applied to flesh'''

    elif d100 >= 53 and d100 <= 54:
        matterLeakString = '''Thousands of what resemble insect eggs'''

    elif d100 >= 55 and d100 <= 56:
        matterLeakString = '''Thousands of what resemble insect legs'''

    elif d100 >= 57 and d100 <= 58:
        matterLeakString = '''Hundreds of disembodied tentacle suckers'''

    elif d100 >= 59 and d100 <= 60:
        matterLeakString = '''Hundreds of metal and glass spheres with tiny 
        silver wires leading from the back; they resemble disembodied human eyes'''

    elif d100 >= 61 and d100 <= 62:
        matterLeakString = '''Four-fingered hands that are humanlike but smaller, 
        more delicate, and composed of synth'''

    elif d100 >= 63 and d100 <= 64:
        matterLeakString = '''Hair'''

    elif d100 >= 65 and d100 <= 66:
        matterLeakString = '''Thick ebony fluid that acts like glue (level 6) 
        if a bit is squeezed between two objects'''

    elif d100 >= 67 and d100 <= 68:
        matterLeakString = '''Hundreds of invisible, many-sided stars about the 
        size of a human hand; stars have sharp ends and are dangerous if trod upon 
        or fallen into'''

    elif d100 >= 69 and d100 <= 70:
        matterLeakString = '''Yellow putty'''

    elif d100 >= 71 and d100 <= 72:
        matterLeakString = '''Orange putty; if sculpted into an object with 
        limb-like projections, the shape animates as a level 1 creature and follows 
        the sculptor'''

    elif d100 >= 73 and d100 <= 74:
        matterLeakString = ''' White putty; if sculpted into an object with 
        limb-like projections, the shape animates as a level 3 creature and 
        attacks the sculptor'''

    elif d100 >= 75 and d100 <= 76:
        matterLeakString = '''Pink dust, easily disturbed to rise in clouds of 
        particulate vapor that flows toward the nearest exit to the structure'''

    elif d100 >= 77 and d100 <= 78:
        matterLeakString = '''Thousands of tiny metallic rods, flat at one end, 
        pointed at the other'''

    elif d100 >= 79 and d100 <= 80:
        matterLeakString = '''Gravel made of clear and translucent crystal'''

    elif d100 >= 81 and d100 <= 82:
        matterLeakString = '''Liquid that infuses objects or creatures, 
        making them shake and vibrate for minutes or hours'''

    elif d100 >= 83 and d100 <= 84:
        matterLeakString = '''Chunks of white super-cold material that steams 
        and dissipates when disturbed'''

    elif d100 >= 85 and d100 <= 86:
        matterLeakString = '''Dull grey dust that absorbs objects and creatures 
        that fall into it as if sucking them in; actually transfers them to an 
        alternate dimension'''

    elif d100 >= 87 and d100 <= 88:
        matterLeakString = '''Thick whitish dust that smells sharp; sticks 
        electrostatically to clothing and skin'''

    elif d100 >= 89 and d100 <= 90:
        matterLeakString = '''Spiral shells of thumbnail size and smaller'''

    elif d100 >= 91 and d100 <= 92:
        matterLeakString = '''Spiral shells of thumbnail size and smaller, 
        each containing an inactive, burned-out device'''

    elif d100 >= 93 and d100 <= 94:
        matterLeakString = '''Spiral shells of thumbnail size, each containing 
        a small synth traction device that might allow the shells to move in unison, 
        if a control device could be found or fabricated'''

    elif d100 >= 95 and d100 <= 96:
        matterLeakString = '''Shattered dark red glass'''

    elif d100 >= 97 and d100 <= 98:
        matterLeakString = '''Bone fragments from hundreds of different 
        kinds of creatures'''

    elif d100 >= 99 and d100 <= 100:
        matterLeakString = '''Panes of stacked (and tumbled) blue-tinted 
        glass that is fragile; light takes minutes, hours, days, or even 
        years to move through it, depending on the pane'''

    return matterLeakString
def relicChamberGenerator():
    d20 = random.randint(1, 20)
    relicTypeString = ''
    if d20 >= 1 and d20 <= 3:
        relicTypeString = 'Hand'
    elif d20 >= 4 and d20 <= 6:
        relicTypeString = 'Mouth'
    elif d20 >= 7 and d20 <= 9:
        relicTypeString = 'Eye'
    elif d20 >= 10 and d20 <= 11:
        relicTypeString = 'Ear'
    elif d20 == 12:
        relicTypeString = 'Face'
    elif d20 == 13:
        relicTypeString = 'Foot'
    elif d20 == 14:
        relicTypeString = 'Spine'
    elif d20 == 15:
        relicTypeString = 'Heart'
    elif d20 == 16:
        relicTypeString = 'Stomach'
    elif d20 == 17:
        relicTypeString = 'Lung'
    elif d20 == 18:
        relicTypeString = 'Intestine'
    elif d20 == 19:
        relicTypeString = 'Nose'
    elif d20 == 20:
        relicTypeString = 'Brain'

    d20_2 = random.randint(1, 20)
    relicQualityString = ''

    if d20_2 == 1:
        relicQualityString = '''Intuition. Characters who spend a few 
        minutes in the vicinity of the relic gain insight into a problem 
        they’ve tried but failed to solve before. An answer comes to them 
        unbidden, one that might prove the perfect solution.'''

    elif d20_2 == 2:
        relicQualityString = '''Strength. Characters who spend several hours
         in the relic’s vicinity find the difficulty of any Might task reduced
          by three steps. This strength shift lasts for 28 hours.'''

    elif d20_2 == 3:
        relicQualityString = '''Insinuation. Characters who spend several hours 
        in the relic’s vicinity can vault their minds into another creature’s body 
        within short range as a level 7 Intellect attack. If successful, the 
        attacking character controls the target body for up to 28 hours while their 
        own body remains in a deep sleep.'''

    elif d20_2 == 4:
        relicQualityString = '''Expertise. Characters who spend several hours in 
        the relic’s vicinity find the difficulty of any Intellect task reduced by 
        three steps. This strength shift lasts for 28 hours.'''

    elif d20_2 == 5:
        relicQualityString = '''Void Manipulation. Characters who spend a few 
        minutes in the relic’s vicinity can extrude streamers of void matter for 
        one minute at a time, increasing their normal reach from immediate range 
        to short. Anything a character could do with their own hands, they can do 
        at range through void manipulation. This ability persists for one hour.'''

    elif d20_2 == 6:
        relicQualityString = '''Void Strike. Characters who spend several hours 
        in the relic’s vicinity can extrude a ray of void matter at a target 
        within short range, inflicting 5 points of damage that ignores Armor. 
        This ability persists for 28 hours.'''

    elif d20_2 == 7:
        relicQualityString = '''Ancillary Anatomy. Characters who spend several 
        hours in the relic’s vicinity gain a secondary companion intelligence that 
        takes the form of a vestigial limb or organ, similar to the relic, which 
        remains attached to the character. Affected characters can treat the ancillary 
        anatomy as a level 2 NPC that might provide aid, depending on the nature of the 
        organ. For instance, an additional nose would grant an asset on perception tasks, 
        but an extra foot might provide an inability in most movement tasks (but perhaps 
        an asset on tasks to retain balance and stability). The vestigial anatomy 
        persists for up to 28 hours.'''

    elif d20_2 == 8:
        relicQualityString = '''Communication. Characters who spend several hours 
        in the relic’s vicinity gain long-range telepathy that lasts for 28 hours.'''

    elif d20_2 == 9:
        relicQualityString = '''Discernment. Characters who spend several hours in the 
        relic’s vicinity always know when another creature is telling a lie. This 
        ability persists for 28 hours.'''

    elif d20_2 == 10:
        relicQualityString = '''Resistance. Characters who spend several hours in the 
        relic’s vicinity gain +2 to Armor and the ability to withstand poisons, venoms, 
        and diseases of level 8 and lower for the next 28 hours.'''

    elif d20_2 == 11:
        relicQualityString = '''Persistence. Characters who spend several hours in the 
        relic’s vicinity gain the ability to breathe in any atmosphere or in water. 
        They can hold their breath for several hours without coming to harm in a vacuum. 
        This ability persists for 28 hours.'''

    elif d20_2 == 12:
        relicQualityString = '''Creation. Characters who spend several hours in the 
        relic’s vicinity gain the ability to mold other creatures’ flesh as if it were clay. 
        For targets that resist, using this ability is a physical attack. Molding 
        another creature could provide them with wings, an extra limb, an extra eye, 
        and so on, though someone with malign intent could remove a creature’s eyes, 
        pull off a limb, and so on. The GM will determine benefits or damage inflicted 
        (or both) depending on the result. In any case, a character trying to mold the flesh 
        of another must succeed on a difficulty 4 Intellect task (or higher, if attempting 
        something complicated like adding functional wings) or suffer a negative mishap. 
        This ability lasts for one hour, but the effects created by the ability are permanent.'''

    elif d20_2 == 13:
        relicQualityString = '''Aggressive Destiny. Characters who spend several hours in the 
        relic’s vicinity gain the ability to harm another creature with certainty. When the 
        character attacks a target with an ability, weapon, or device, regardless of the 
        range or any barriers separating them, the attack succeeds (treat as a routine task). 
        The user can attack any target, but only if they know that the target exists; 
        the GM will decide if they have enough information to confirm the target’s existence. 
        This ability lasts for one minute, or until a target that isn’t in the same 
        chamber is attacked.'''

    elif d20_2 == 14:
        relicQualityString = '''Healer. Characters who spend several days in the relic’s 
        vicinity gain the ability to touch a target and restore its Might Pool, Speed Pool, 
        and Intellect Pool to their maximum values, as if it were fully rested. A single 
        target can benefit from this ability only once each day. This ability lasts for 
        28 hours.'''

    elif d20_2 == 15:
        relicQualityString = '''Spiritual Leader. Characters who spend several days in 
        the relic’s vicinity gain the ability to convert another creature (whose level 
        is less than their own) to service and sacrifice. The target gives up whatever 
        occupation and life it previously pursued to become the character’s follower. 
        It continues to serve the character gladly, unless or until the character does wrong 
        by the target, as determined by the GM. This ability lasts until used.'''

    elif d20_2 == 16:
        relicQualityString = '''Far Treader. Characters who spend several days in the relic’s 
        vicinity gain the ability to step between distant locations as easily as they 
        might step into the next room. When using this ability, a character can move 
        between locations no matter how far apart they are, as long as they have been to 
        that location previously or can see it. This ability lasts for one hour.'''

    elif d20_2 == 17:
        relicQualityString = '''Invincible. Characters who spend several weeks in the 
        relic’s vicinity gain +10 to Armor and the ability to withstand poisons, venoms, 
        and diseases of level 10 and lower for the next hour.'''
    elif d20_2 == 18:
        relicQualityString = '''Foldable. Characters who spend several days in the 
        relic’s vicinity gain the ability to fold themselves into much smaller spaces, 
        including tiny cracks, or to inflate their mass by as much as 1,000% as long as 
        there is space to do so. Each halving or increase by 50% in size requires one 
        full round of effort. This ability lasts for 28 hours.'''

    elif d20_2 == 19:
        relicQualityString = '''Contemplative. Characters who spend a few minutes in the 
        relic’s vicinity remember something they failed to note the first time around, 
        perhaps a minor detail that seemed insignificant, but which on further thought 
        emerges as a clue. If nothing in the characters’ history suits, instead they 
        gain +1 to Intellect Edge for one hour.'''

    elif d20_2 == 20:
        relicQualityString = '''Communion Enabler. Characters who spend several weeks in 
        the relic’s vicinity gain the ability to speak telepathically with all creatures 
        in a 2-mile (3 km) radius simultaneously, regardless of differences in language or 
        physical barriers, for a few rounds. Though the effect is potentially overwhelming 
        for those few rounds, the follow-on effect allows all connected creatures to gain a 
        brief sense of each other and each other’s point of view. For the next ten days at 
        least, the difficulty of any positive interaction tasks attempted between affected 
        creatures is reduced by three steps. The ability to enter into this communion lasts 
        until used.'''

    relicInfoString = 'The relic is a ' + relicTypeString + ' and grants: ' + relicQualityString

    return relicInfoString
def ruptureGenerator():
    d20 = random.randint(1, 20)
    ruptureString = ''

    if d20 == 1:
        ruptureString = '''Empty of all but drit.'''

    elif d20 == 2:
        ruptureString = '''Area (and potentially a few surrounding 
        corridors) is filled with an orange-red mist that confuses the 
        senses and turns around creatures who enter the space (a level 
        6 effect) so that when they think they are leaving the area in 
        a known direction, they’re actually leaving and moving in a 
        random direction.'''

    elif d20 == 3:
        ruptureString = '''Tiny metallic insects crawl everywhere; 
        the insects are essentially harmless (level 1) but tend to 
        get into clothing, hair, and bags and packs.'''

    elif d20 == 4:
        ruptureString = '''Area through which the rupture passes was 
        once a vault; roll on the Vault Table to determine the ruined, 
        inactive remains that are scattered through this area.'''

    elif d20 == 5:
        ruptureString = '''Tiny amoeba-like creatures the color of 
        leaves drip and flow around the area; they carry a parasite, 
        and living creatures that enter the area risk contracting a mind-enhancing 
        sickness (a disease) that heightens their mental capacities 
        even as it kills them.'''

    elif d20 == 6:
        ruptureString = '''Crater glowing with residual radiation 
        inflicts 1 point of ambient damage on each creature in the 
        area each minute they spend in the rupture.'''

    elif d20 == 7:
        ruptureString = '''If near the perimeter of the installation, 
        the rupture extends to the outside and could serve as a new entrance/exit 
        to the ruin.'''

    elif d20 == 8:
        ruptureString = '''Water flows swiftly through the rupture from a higher 
        location before plunging in a dramatic fashion to a deeper location 1d10 x 
        100 feet (30 m) lower in an interstitial cavity; roll on the Interstitial 
        Cavity Table.'''

    elif d20 == 9:
        ruptureString = '''Oddly whorled fungi cover the interior; 
        some of the growths are taller than people.'''

    elif d20 == 10:
        ruptureString = '''As 09, but the fungi exude soporific spores, 
        putting to sleep anyone who fails a difficulty 5 Might defense task.'''

    elif d20 == 11:
        ruptureString = '''Synth “grass” the color of milk grows in 
        rough patches here and there, rustling slowly.'''

    elif d20 == 12:
        ruptureString = '''As 11, but the “grass” holds in place anyone 
        who fails a difficulty 5 Might defense task.'''

    elif d20 == 13:
        ruptureString = '''Something has been storing skeletons of dead 
        creatures, automatons, and explorers in this rupture, organizing 
        the bones in neat, stacked rows.'''

    elif d20 == 14:
        ruptureString = '''A waxy, slightly cool-to-the touch ooze pools, 
        drips, and undulates here and there about the rupture.'''

    elif d20 == 15:
        ruptureString = '''Stone “grows” through relatively quick 
        crystallization in the rupture, forming geometric crystalline spires.'''

    elif d20 == 16:
        ruptureString = '''A creature* lairs here; roll again on this table to 
        determine the nature of the rupture; the creature is immune to 
        any negative effects. ''' + '\nCreature:  ' + creatureGenerator() + '\nRupture: ' + ruptureGenerator()

    elif d20 == 17:
        ruptureString = '''Resin-like whorled secretions cover the area, apparently 
        laid down over months or years by some kind of creature or biological process.'''
    elif d20 == 18:
        ruptureString = '''Slender, translucent organic strands hang down from 
        whatever serves as the ceiling, filling the area so thickly that it’s 
        impossible to move through without brushing the strands aside. The strands 
        “sweat” a weak acid that inflicts 2 points of ambient damage each round 
        a creature remains in or moves through the area.'''

    elif d20 == 19:
        ruptureString = '''Metal interior is twisted, warped, bent, 
        and in some cases transformed into other substances; a scholar 
        of the numenera might suspect that the Iron Wind caused the damage.'''

    elif d20 == 20:
        ruptureString = '''As 19, but a seed of the Iron Wind is still 
        present and could be roused if disturbed.'''

    return ruptureString
def shaftGenerator():
    d20 = random.randint(1, 20)
    shaftString = ''

    if d20 >= 1 and d20 <= 7:
        shaftString = '''Shaft extends up and down for 1d10 x 100 feet (30 m)'''

    elif d20 >= 8 and d20 <= 10:
        shaftString = '''Shaft ascends for 1d10 x 100 feet (30 m)'''

    elif d20 >= 11 and d20 <= 13:
        shaftString = '''Shaft descends for 1d10 x 100 feet (30 m)'''

    elif d20 >= 14 and d20 <= 15:
        shaftString = '''Shaft ascends for 1d10 x 100 feet (30 m) 
        and has a conveyance field that whisks those who enter to 
        the next exit named, or to the top of the shaft if nothing specified'''

    elif d20 >= 16 and d20 <= 17:
        shaftString = '''As 14–15, but descending'''

    elif d20 == 18:
        shaftString = '''Rubble chokes the shaft, which extends 
        up and down 1d10 x 100 feet (30 m); however, the rubble is 
        large and blocky, creating navigable spaces between pieces 
        that explorers could squeeze through with time and effort'''

    elif d20 == 19:
        shaftString = '''Shaft drops 1d10 x 100 feet (30 m) into 
        reclamation pit containing a level 7 deconstructor automaton'''

    elif d20 == 20:
        shaftString = '''Shaft ascends 1d10 x 100 feet (30 m) and 
        contains a suspended abhuman colony* whose crude domiciles 
        are “webbed” to hang suspended at the shaft’s middle point'''

    return shaftString
def vaultGenerator():
    d20 = random.randint(1, 20)
    vaultString = ''

    if d20 == 1:
        vaultString = '''Stacks of metallic disc-shaped oddities 
        that avoid being touched by anything organic, sliding away 
        if possible (grabbing one by hand is a difficulty 3 task).'''

    elif d20 == 2:
        vaultString = '''Four fluid-filled canisters each hold what 
        seems to be a human spine grafted with metallic wires and modules. 
        If some method is found for replacing a character’s spine with 
        one of the spines in a canister (and if the character survives), 
        that PC would gain an ability determined randomly using the Artifacts 
        Table in the corebook.'''

    elif d20 == 3:
        vaultString = '''Black synth card on a pedestal. If found in the 
        Jade Colossus, the card grants the user an asset on a task related 
        to dealing with a relic, including resisting dangerous effects, 
        avoiding attacks from creatures touched by a relic or that are infused 
        with void matter, or understanding or using a relic. If found in another 
        installation, the card grants access to a key area in the ruin.'''

    elif d20 == 4:
        vaultString = '''Level 8 artifact vehicle capable of travel through space. 
        The vault contains a mechanism allowing the vehicle to be deployed to 
        the surface of the installation, where it can launch. It requires a crew 
        of two to four, and can carry up to ten more people or some cargo. It can 
        sustain passengers for up to three months before it needs to return to a planet 
        with a breathable atmosphere. It can travel to locations within the solar system 
        known to the pilot in a few days, or between known distant interstellar locations 
        in about a month. Depletion: 1 in 1d100 (check per day of use).'''

    elif d20 == 5:
        vaultString = '''Solid black cube about the size of a human 
        fist encased in a larger clear cube (a level 10 cypher). When 
        the cypher is activated, the clear cube begins to dissolve, 
        which takes ten minutes. After the outer cube dissolves fully, 
        the black cube causes all living creatures in long range that are 
        larger than a small dog to belch forth a cloud of black vapor. This 
        vapor fills the immediate area around the victim, inflicting 10 points 
        of damage to the victim and all other living creatures within the cloud. 
        One round later, all living creatures larger than a small dog within long 
        range of every affected victim belch forth the same cloud (even if they 
        already did so before). This continues until no creatures are affected. 
        The cypher is a horrific doomsday device that could easily destroy an 
        entire city or wipe out an army.'''

    elif d20 == 6:
        vaultString = '''Canister of four level 7 pellets in a mechanical case, 
        each of which shimmers as if on the edge of disappearing. If a pellet is 
        swallowed, mass is drawn to the user from another dimension, allowing them 
        to grow 200 percent larger for one day. During this time, the user gains 
        12 points to their Might Pool and deals +8 points of damage with all melee 
        attacks, but all Speed-related tasks, including defense, are two steps 
        more difficult. In addition, moving through small spaces could become a 
        challenge.'''

    elif d20 == 7:
        vaultString = '''Humanlike head, but 50% larger than normal, 
        preserved in a metallic device with a crystal face. The head 
        may have been alive once or served as a tap into the datasphere, 
        but some sort of error has rendered it so much 
        numenera-suffused preserved flesh.'''

    elif d20 == 8:
        vaultString = '''Canister of four level 8 pellets in a mechanical case, 
        each of which is almost ten times heavier than a similar-sized piece 
        of iron. If a pellet is swallowed, the user is transmuted into dull 
        grey metal. The user has entered a safe suspended animation that lasts 
        for 28 hours. While suspended, the user is impervious to attacks lower 
        than level 8.'''

    elif d20 == 9:
        vaultString = '''Vault is actually a vehicle that moves around 
        the interior of the installation on lines of magnetic force, 
        using a system of accessways built for it and similar movable chambers. 
        Figuring out how to engage the vehicle is a level 5 Intellect task. 
        However, it moves somewhat violently, and anyone not secured risks 
        suffering 4 points of Might damage from the sudden starts, turns, 
        and stops. The vehicle apparently has a variable number of preset 
        destinations. Where it actually goes when activated seems to be random, 
        though someone who spends a few weeks experimenting might figure out how 
        to use it reliably.'''

    elif d20 == 10:
        vaultString = '''Razor-thin metallic webs fill the vault. Moving 
        through requires a difficulty 4 Speed defense roll to avoid suffering 
        4 points of damage per immediate distance crossed. Three level 5 
        automatons with spiderlike legs move to attack anyone that 
        comes into the vault.'''

    elif d20 == 11:
        vaultString = '''Mechanized vat containing an active nano-fluid. 
        A mechanical crane can be used to douse objects or creatures in the 
        vat (a level 4 Intellect task). Someone who succeeds on a level 6 
        Intellect task can confer a doused object or creature with +2 to Armor 
        (in the form of a more resilient, damage-resistant outer surface) that 
        lasts for 28 hours. However, a mishap with the vat seals the object or 
        creature inside a level 6 caul that renders an object unusable or smothers 
        a creature unless the caul can be removed.'''

    elif d20 == 12:
        vaultString = '''This complex level 8 device is a rectangular 
        obelisk twice as tall as a human, covered in screens, mechanisms, 
        and controls. It’s surrounded by a force-field globe (Armor 10), 
        which must be dealt with to reach the device. The obelisk doesn’t 
        have an obvious purpose, so unless the GM has a need for a complex 
        control device, it is good for little more than being a rich source 
        of numenera salvage.'''

    elif d20 == 13:
        vaultString = '''Stack of three red synth cards in a clear vessel. 
        Each card, called a flaying key, is an artifact (depletion: 1 in 1d10) 
        useful for conducting surgical procedures. A touched target’s skin disappears 
        and the card adheres to the target, moving the target one step down the damage 
        track. While skin is absent, the difficulty of any task related to curing 
        the target’s disease, ameliorating poison, mending broken bones, or other 
        radical healing requiring surgery is reduced by two steps. The target’s skin 
        returns when the key is removed, moving the target one step up the damage track.'''

    elif d20 == 14:
        vaultString = '''Level 8 transparent sphere has a diameter of 30 feet 
        (9 m) but contains an area far larger than its size would seem to indicate. 
        In this area, visible but as if through haze, is an ancient city of silver 
        towers, permanently preserved and deserted. (Essentially, this is an entirely 
        new prior-world installation, which could be explored if the level 8 sphere 
        could be breached.)'''

    elif d20 == 15:
        vaultString = '''Tomb of a 30-foot (9 m) tall humanoid creature wearing some 
        kind of mechanized armor. The entity is dead and mummified, but its equipment 
        could be salvaged.'''

    elif d20 == 16:
        vaultString = '''Metallic level 8 artifact helmet contained in 
        a clear glass case (depletion: 1 in 1d6). This synthsteel helmet 
        has eight strange projections. If activated when worn (a level 5 
        Intellect task), eight 9-foot (3 m) long tentacles emerge from the 
        device and remain for up to ten minutes. The tentacles are 
        translucent, modulating between phase states. They can be used to 
        pick up or manipulate objects, push buttons, and so forth, or to 
        attack every creature within immediate range of the user for 8 points 
        of damage. The tentacles can move through energy fields, including solid 
        force fields, as if they were not there.'''

    elif d20 == 17:
        vaultString = '''Complex level 7 machine with many glass 
        reservoirs filled with different weird fluids. Manipulator 
        arms are poised to grasp anything that stands on an activation 
        plate. If any kind of organic material (including a living creature) 
        steps or is placed onto the plate, the arms attempt to grasp it (a 
        level 4 attack) and insert it into an opening at the machine’s top. 
        Ingested objects are broken down into their essential materials and 
        stored as various complex fluids. Someone standing at the machine’s 
        controls who succeeds on a level 7 Intellect task could reconstitute 
        an ingested living creature, or try to make a new creature from the 
        materials gathered.'''

    elif d20 == 18:
        vaultString = '''What appears to be an ornate mirror hangs on a 
        pedestal within a clear synth dome. Examination of the “mirror” 
        reveals that it’s a vertical sheet of reflective liquid and 
        touching it causes ripples. The sheet is a level 8 numenera artifact 
        (depletion: 1 in 1d20) that can transfer someone who steps into the 
        mirror to another dimension or level of reality. The user must know 
        that the destination they seek exists; the GM decides if the user has 
        enough information to confirm its existence and the level of difficulty 
        needed to reach it. Otherwise, the user merely walks back out of the 
        liquid surface of the mirror.'''

    elif d20 == 19:
        vaultString = '''Immobile device with leaflike arms partly 
        enfolds a glowing spherical ball of transdimensional energy. 
        This level 7 artifact (depletion: 1 in 1d10) transforms a user 
        who succeeds on a difficulty 5 Intellect task into an immaterial 
        energy construct for up to one hour, during which time the user can’t 
        affect or be affected by normal matter or energy, except as follows. 
        The user can attack a target within long range, inflicting 7 points of 
        transdimensional energy damage; the attack returns the user to normal. 
        Alternatively, the device can be used to recharge a depleted artifact.'''

    elif d20 == 20:
        vaultString = '''Vortex of energy swirls above a raised circular 
        platform surrounded by complex machinery. Its radiance makes it 
        difficult to look at, and its heat makes it difficult to stand near. 
        High-intensity energy in the area induces a feeling of awe in observers. 
        The vortex is a wormhole that leads directly into the sun.'''

    return vaultString
def weirdEventGenerator():
    d20 = random.randint(1, 20)
    weirdEventString = ''

    if d20 == 1:
        weirdEventString = '''Quake accompanied by blue haze and high-pitched musical 
        tones goes on for almost a minute. Creatures must succeed on Speed defense 
        tasks or suffer 5 points of damage from being knocked around.'''

    elif d20 == 2:
        weirdEventString = '''Vague smell slowly sharpens, assaulting every 
        creature in the area with an odor so indescribably delicious that 
        they salivate in uncontrollable yearning. The odor fades after a minute, 
        but the hunger awakened is so strong that it dazes creatures, increasing 
        the difficulty of all tasks by one step, until they can enjoy a large meal.'''

    elif d20 == 3:
        weirdEventString = '''Low, thrumming hum impinges on the senses of 
        one-third of any group of creatures in the area. To those who can sense 
        it, the humming is intense and hard to ignore. To the rest, nothing is 
        detected or sensed. The humming dies away after a few minutes.'''

    elif d20 == 4:
        weirdEventString = '''Swarm of thousands of tiny red insects covers 
        the walls, floors, and ceilings, moving an immediate distance each round. 
        They produce a rich, vibrating sound audible for miles. The insects are 
        harmless individually, though potentially capable of smothering a creature 
        that falls prone in their path.'''

    elif d20 == 5:
        weirdEventString = '''Everyone hears a voice in their heads in a 
        language that isn’t known. The voice seems to be making some kind 
        of announcement that lasts a couple of rounds. If the PCs have a 
        translation device that allows them to understand an unknown language, 
        the words seem to be stern instructions, but without the proper 
        knowledge and context, they are still inexplicable.'''

    elif d20 == 6:
        weirdEventString = '''Time wave washes through the area, 
        though characters may not realize its full effect until they 
        finally emerge from the installation to discover they were 
        inside two months longer than they thought.'''

    elif d20 == 7:
        weirdEventString = '''As 06, except the characters emerge 
        from the structure two months earlier than when they entered.'''

    elif d20 == 8:
        weirdEventString = '''Brilliant flash of light leaves in its 
        wake small changes to reality in the vicinity, which characters 
        might notice, such as a cloak color being different, a tattoo 
        design being reversed, and so on. However, a large change, such 
        as the addition of a new compatriot who believes they’ve always 
        been part of the group, is possible.'''

    elif d20 == 9:
        weirdEventString = '''Brilliant flash of light leaves in 
        its wake a completely altered situation. Instead of exploring 
        the interior of an installation, the characters find themselves 
        clinging to the shell of a vast structure floating in airless void, 
        with huge chunks of what might be the Earth spiraling around them in 
        a planetary cloud. Stutters of other flashing alternative realities 
        encompass the PCs before they expire in the vacuum, returning them 
        to their original situation and reality.'''

    elif d20 == 10:
        weirdEventString = '''Stampede of phase-shifted creatures with milky fur, 
        limbs dozens of feet long, and voices like children runs through the area, 
        passing through objects, normal creatures, characters, and walls as if 
        those objects were not there. Once past, they leave behind a slightly 
        doglike scent that quickly fades.'''

    elif d20 == 11:
        weirdEventString = '''Flying vessel impacts the exterior 
        of the installation with so much force, the walls are cracked 
        and the vessel is mostly destroyed. The vessel contains several 
        creatures* who, maddened and injured, spill out into nearby corridors.''' + ':  ' + creatureGenerator()

    elif d20 == 12:
        weirdEventString = '''The temperature begins to drop, slowly 
        and barely perceptible at first. But within a few hours, it 
        drops far below freezing and stays that way within a large area 
        for several hours, until the effect passes and normal conditions 
        reassert themselves.'''

    elif d20 == 13:
        weirdEventString = '''Spatial anomaly manifests as a sparkling 
        hole in space. The one-way anomaly persists for several days, 
        during which time it constantly spits out random objects, which 
        are often broken or fused pieces of tech, but sometimes include 
        contemporary objects of the Ninth World such as shoes, hats, 
        and human body parts.'''

    elif d20 == 14:
        weirdEventString = '''Dozens of previously undetected compartments 
        iris open, from which a small fleet of fist-sized level 1 automatons 
        emerge. The automatons skim along surfaces, leaving in their path a 
        thin veneer of level 2 synth. If several automatons are caught and 
        salvaged, a few cyphers might be gained.'''

    elif d20 == 15:
        weirdEventString = '''Rumbling and shaking presages a flood of viscous brown 
        fluid moving a short distance each round, spreading out to fill several 
        connected corridors and chambers, potentially drowning any creature caught 
        in its path. The fluid is somewhat nutritious, sweet, and sticky. It subsides 
        and drains away over the course of a day.'''

    elif d20 == 16:
        weirdEventString = '''Tech in the characters’ possession 
        designed to provide directions or information— including cyphers, 
        artifacts, or oddities—spontaneously activates. Otherwise, one 
        handheld device owned by a character, regardless of its function, 
        activates with a previously unknown function that shows a representation 
        of the PCs’ location and a pointer indicating that they should follow a 
        route through a hidden passage they’d not previously discovered. 
        If they follow this weird prompt, they discover a shaft plunging down for 
        several miles, at the bottom of which is an abhuman colony (roll on the 
        Abhuman Colony Table). All the abhumans have been murdered as if hit by 
        something large and fast moving. And that something (a level 6 creature of 
        the GM’s choosing) now hunts the PCs.'''

    elif d20 == 17:
        weirdEventString = '''Handheld device owned by a character, 
        regardless of its function, activates with a previously unknown 
        function that opens communication with a voice that speaks a language 
        the PC knows. The voice is in trouble and asks for help, indicating 
        that some kind of terrible disaster has befallen, and only they are left. 
        It should become clear soon enough that the voice is the character’s own, 
        but the apocalyptic events hinted at have not happened—at least, not in this 
        reality, or maybe not yet.'''

    elif d20 == 18:
        weirdEventString = '''All tech, devices, and automatons in the area 
        of level 7 or lower spontaneously power down for several minutes. 
        During the dead span, weird shadows flow and stream over all nearby surfaces, 
        never quite resolving enough to determine their shape. When the shadows fade, 
        items suddenly return to full function. Automatons have no memory of their 
        function outage.'''

    elif d20 == 19:
        weirdEventString = '''Void matter storm passes through the area; 
        treat each affected creature as if they used a midnight stone.'''

    elif d20 == 20:
        weirdEventString = '''Golden haze springs up out of nowhere, 
        filling an area that includes many connected chambers and corridors 
        for one hour. Creatures in the haze feel light-headed, happy, and at ease. 
        Grudges are easier to let go, and long-held prejudices without factual 
        basis can be judged for the chimeras of thought that they truly are. 
        For one golden hour, clear-thinking rationality shines through, revealing 
        what passes for normal human thought to be a series of mistakes in thinking 
        that people generally ignore or explain away.'''

    return weirdEventString

def generateRoom():
    mainFeature = mainFeatureGenerator()
    fullReport = ''' '''
    if mainFeature == 'Corridor':
        fullReport = mainFeature + ':  \n' + corridorGenerator()
    elif mainFeature == 'Chamber':
        fullReport = mainFeature + ' :  \n' + chamberGenerator()
    elif mainFeature == 'Creature':
        fullReport = mainFeature + ':  \n' + chamberGenerator() + ' Details:  \n' + creatureGenerator()
    elif mainFeature == 'Explorers':
        fullReport = mainFeature + ':  \n' + chamberGenerator() + ' Details:  \n' + explorerGenerator()
    elif mainFeature == 'Interstitial cavity':
        fullReport = mainFeature + ':  \n' + interStitialCavityGenerator()
    elif mainFeature == 'Accessway':
        fullReport = mainFeature + ':  \n' + accesswayGenerator()
    elif mainFeature == 'Rupture':
        fullReport = mainFeature + ':  \n' + ruptureGenerator()
    elif mainFeature == 'Shaft':
        fullReport = mainFeature + ':  \n' + shaftGenerator()
    elif mainFeature == 'Abhuman Colony':
        fullReport = mainFeature + ':  \n' + chamberGenerator() + ' Details:  \n' + abhumanColonyGenerator()
    elif mainFeature == 'Integrated Machine':
        fullReport = mainFeature + ':  \n' + integratedMachineGenerator()
    elif mainFeature == 'Matter leak':
        fullReport = mainFeature + ':  \n' + chamberGenerator() + ' Details:  \n' + matterLeakGenerator()
    elif mainFeature == 'Energy discharge':
        fullReport = mainFeature + ':  \n' + chamberGenerator() + ' Details:  \n' + energyDischargeGenerator()
    elif mainFeature == 'Weird event':
        fullReport = mainFeature + ':  \n' + chamberGenerator() + ' Details:  \n' + weirdEventGenerator()
    elif mainFeature == 'Vault':
        fullReport = mainFeature + ':  \n' + chamberGenerator() + ' Details:  \n' + vaultGenerator()
    elif mainFeature == 'Relic Chamber':
        fullReport = mainFeature + ':  \n' + chamberGenerator() + ' Details:  \n' + relicChamberGenerator()

    fullReport = fullReport + '\nExits: ' + exitGenerator()
    return fullReport
