# The famous polish wizard spell damage calculator
# based on "shovel"ogy :)

def calculate(part, spell, score):
    if part in spell:
        occurr = spell.count(part)
        new_elements = [part] * occurr
        score.extend(new_elements)
        return spell.replace(part, "")
    return spell

def damage(spell):
    spell = spell.lower() # it wasn't determind if uppercase letters should return ) or not
    beg_index = int(spell.find("fe")) # a number of index of "fe"
    end_index = int(spell.rfind("ai")) # a number of index of last occurrence"ai"

    if not spell.isalpha() and not spell.isspace():
        return 0
    elif spell.find("fe") == -1 and spell.find("ai") == -1:
        return 0
    elif spell.find("fe") > spell.rfind("ai") or spell.count("fe") != 1:
        return 0
    else:
        spell = spell[beg_index : end_index + 2]

    fe = "fe"
    dai = "dai"
    ain = "ain"
    ai = "ai"
    jee = "jee"
    je = "je"
    ne = "ne"
    spell = spell[2:-2]
    score = ["fe", "ai"]

    for part in ["fe", "jee", "je", "dai", "ne", "ain", "ai"]: # order of the elements matters
        spell = calculate(part, spell, score)

    leftovers = spell
    negative_score = len(spell)

    subspells = {
        "fe": 1, "je": 2, "jee": 3, "ain": 3, "dai": 5, "ne": 2, "ai": 2
    }

    total = 0
    for item in score:
        total = total + subspells[item]

    damage = total - negative_score
    if damage > 0:
        return damage
    else:
        return 0



print(damage("fedaineai"))
