# The famous polish wizard spell damage calculator
# based on "shovel"ogy :)

def damage(spell):
    spell = spell.lower() # it wasn't determined if uppercase letters are allowed or script should just return 0
    beg_index = int(spell.find("fe")) # a number of index of "fe"
    end_index = int(spell.rfind("ai")) # a number of index of last occurrence of "ai"

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

    if jee in spell:
        occurr = spell.count("jee")
        new_elements = ["jee"] * occurr
        score.extend(new_elements)
        spell = spell.replace("jee", "")

    if je in spell:
        occurr = spell.count("je")
        new_elements = ["je"] * occurr
        score.extend(new_elements)
        spell = spell.replace("je", "")

    if dai in spell:
        occurr = spell.count("dai")
        new_elements = ["dai"] * occurr
        score.extend(new_elements)
        spell = spell.replace("dai", "")

    if ne in spell: # if we have spell like "aineain" it's better to cut into ["ai", "ne", "ain" ] (7) than into ["ain","ain"] with "e" left (6-1=5)
        occur = spell.count("ne")
        new_elements = ["ne"] * occur
        score.extend(new_elements)
        spell = spell.replace("ne","")

    if ain in spell:
        occurr = spell.count("ain")
        new_elements = ["ain"] * occurr
        score.extend(new_elements)
        spell = spell.replace("ain", "")

    if ai in spell:
        occurr = spell.count("ai")
        new_elements = ["ai"] * occurr
        score.extend(new_elements)
        spell = spell.replace("ai", "")

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

# Let's test!
print(damage("fexxxxxxxxxxai"))
