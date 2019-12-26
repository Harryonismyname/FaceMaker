from random import randint
from tkinter import*

"""
class Character:
    output = ""
    face = ""
    hair = ""
    body = ""
"""


def face_roll():
    size = [
        "Large",
        "Medium",
        "Small"
    ]
    length = [
        "Long",
        "Medium",
        "Short"
    ]
    eyeShape = [
        "Close Set",
        "Wide Set",
        "Mono-lid shaped",
        "Hooded",
        "Deep Set",
        "Protruding",
        "Upturned",
        "Down-turned",
        "Almond shaped"
    ]
    noseShape = [
        "Hooked nose",
        "Droopy nose",
        "Aquiline nose",
        "Roman nose",
        "Grecian nose",
        "Button nose",
        "Upturned nose",
        "Snub nose",
        "Funnel nose"
    ]
    mouthShape = [
        "Natural shaped mouth",
        "Pointy Natural shaped mouth",
        "Thin shaped mouth",
        "Cupid's Bow shaped mouth",
        "Uni-lip shaped mouth",
        "Bee-stung shaped mouth",
        "Smear shaped mouth",
        "Glamor shaped mouth"
    ]
    hairStyle = [
        "Is Neatly Groomed",
        "Is Unkempt",
        "Is Neatly braided",
        "Is Tied in a knot"
    ]
    hairColor = [
        "Orange beard",
        "Ginger beard",
        "Crimson beard",
        "Blond beard",
        "Bleach blond beard",
        "Sandy blond beard",
        "Dirty blond beard",
        "Brunette beard",
        "Amber beard",
        "Chestnut beard",
        "Black beard"
    ]
    eyeColor = [
        "Aqua Marine eyes",
        "Honey eyes",
        "Blue eyes",
        "Green eyes",
        "Jade Green eyes",
        "Chestnut Brown eyes",
        "Pure Hazel eyes",
        "Satin Grey eyes",
        "Sugar Grey eyes",
        "Sweet Violet eyes",
        "Topaz Blue eyes",
        "True Sapphire eyes",
        "Hazel eyes",
        "Gray eyes",
        "Emerald Green eyes",
        "Brown eyes",
        "Marble Grey eyes",
        "Ever Green eyes",
        "Violet eyes",
        "Ocean Blue eyes"
    ]
    eye_color_picker = 0
    eye_shape_picker = 0
    basic_picker = 0
    nose_picker = 0
    mouth_picker = 0
    style_picker = 0
    hair_color_picker = 0
    eyes = ""
    nose = ""
    mouth = ""
    beard = ""
    while True:
        eye_color_picker = randint(0, len(eyeColor) - 1)
        eye_shape_picker = randint(0, len(eyeShape) - 1)
        basic_picker = randint(0, 2)
        nose_picker = randint(0, len(noseShape) - 1)
        mouth_picker = randint(0, len(mouthShape) - 1)
        style_picker = randint(0, len(hairStyle) - 1)
        hair_color_picker = randint(0, len(hairColor) - 1)
        eyes = eyeShape[eye_shape_picker] + " " + eyeColor[eye_color_picker] + "\n"
        nose = size[basic_picker] + " " + noseShape[nose_picker] + "\n"
        mouth = mouthShape[mouth_picker] + "\n"
        beard = length[basic_picker] + " " + hairColor[hair_color_picker] + " " + hairStyle[style_picker] + "\n"
        face = (eyes + nose + mouth + beard)
        return face


def hair_roll():
    length = [
        "Long",
        "Medium",
        "Short"
    ]
    hairColor = [
        "Orange hair",
        "Ginger hair",
        "Crimson hair",
        "Blond hair",
        "Bleach blond hair",
        "Sandy blond hair",
        "Dirty blond hair",
        "Brunette hair",
        "Amber hair",
        "Chestnut hair",
        "Black hair"
    ]
    hairStyle = [
        "Is Neatly Groomed",
        "Is Unkempt",
        "Is Neatly braided",
        "Is Tied in a knot"
    ]
    style_picker = 0
    hair_color_picker = 0
    basic_picker = 0
    while True:
        basic_picker = randint(0, 2)
        hair_color_picker = randint(0, len(hairColor) - 1)
        style_picker = randint(0, len(hairStyle) - 1)
        hair = length[basic_picker] + " " + hairColor[hair_color_picker] + " " + hairStyle[style_picker] + "\n"
        return hair


def body_roll():
    skinColor = [
        "Ivory skin",
        "Porcelain skin",
        "Pale Ivory skin",
        "Warm Ivory skin",
        "Sand skin",
        "Rose Beige skin",
        "Limestone skin",
        "Beige skin",
        "Sienna skin",
        "Honey skin",
        "Band skin",
        "Almond skin",
        "Chestnut skin",
        "Bronze skin",
        "Umber skin",
        "Golden skin",
        "Espresso skin",
        "Chocolate skin"
    ]
    size = [
        "Large",
        "Medium",
        "Small"
    ]
    breadth = [
        "Broad",
        "Average",
        "Narrow"
    ]
    length = [
        "Long",
        "Medium",
        "Short"
    ]
    density = [
        "Sturdy",
        "Soft",
        "Flabby"
    ]
    skin_color_picker = 0
    basic_picker = 0
    skin = ""
    shoulders = ""
    arms = ""
    hands = ""
    thighs = ""
    legs = ""
    feet = ""
    while True:
        skin_color_picker = randint(0, len(skinColor) - 1)
        basic_picker = randint(0, 2)
        skin = "They have " + skinColor[skin_color_picker] + ". \n"
        shoulders = "They have " + breadth[basic_picker] + " shoulders. \n"
        arms = "They have " + length[basic_picker] + " " + density[basic_picker] + " arms. \n"
        hands = "Their hands are " + size[basic_picker] + ". \n"
        thighs = "They have " + density[basic_picker] + " thighs. \n"
        legs = density[basic_picker] + " " + length[basic_picker] + " legs. \n"
        feet = size[basic_picker] + " feet. \n"
        body = (skin + shoulders + arms + hands + thighs + legs + feet)
        return body


"""
character_call = Character()
generate_call = character_call.generate()
"""


def generate():
    face = ""
    hair = ""
    body = ""
    output = ""
    while True:
        face = face_roll()
        hair = hair_roll()
        body = body_roll()
        output = (face + hair + body)
        return output


def appearance():
    looks.set("")
    parts = generate
    return looks.set(parts())


screen = Tk()
screen.title("Generator")
looks = StringVar()
appearance_generator = Button(screen,
                              text="Generate Appearance",
                              command=appearance)

appearance_output = Label(textvariable=looks)

appearance_generator.grid(row=0, column=0)
appearance_output.grid(row=1, column=0)
screen.mainloop()
