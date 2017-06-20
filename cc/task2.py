# The famous polish wizard spell damage calculator

def damage(spell):
    spell = spell.lower()  # it wasn't pointed out if upper cases are allowed or should return 0
    beg_index = int(spell.find("fe"))  # a number of index of "fe"
    end_index = int(spell.rfind("ai"))  # a number of index of last occurrence"ai"

    subspells = {
        "fe": 1, "je": 2, "jee": 3, "ain": 3, "dai": 5, "ne": 2, "ai": 2
    }

    if not spell.isalpha() and not spell.isspace():
        return 0
    elif spell.find("fe") == -1 and spell.find("ai") == -1:
        return 0
    elif spell.find("fe") > spell.rfind("ai") or spell.count("fe") != 1:
        return 0
    else:
        spell = spell[beg_index: end_index + 2] # slice starting with "fe" and ending with last "ai"

    spell = spell[2:-2] # don't count "fe" and last "ai"
    part = ["jee", "je", "dai", "ne", "ain", "ai"] # the order of elements in list matters

    total = subspells["fe"] + subspells["ai"] # count first minimum for spell ("fe" and last "ai")
    for item in part:
        if item in spell:
            occurr = spell.count(item)
            total = total + occurr * subspells[item]
            spell = spell.replace(item,"")

    negative_score = len(spell)

    return max(total - negative_score, 0)

# Let's test!
print(damage("feaineai"))
