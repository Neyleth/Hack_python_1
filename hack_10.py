"""
text: "fooziman" output => ["F","0","0","Z","1","M","@","N"]
"""

def fn_hack_10():
    result = []
    text = "fooziman"
    for char in text:
        if char == "o":
            result.append("0")
        elif char == "i":
            result.append("1")
        elif char == "a":
            result.append("@")
        elif char == "f":
            result.append("F")
        elif char == "z":
            result.append("Z")
        elif char == "m":
            result.append("M")
        elif char == "n":
            result.append("N")
        else:
            result.append(char)
    return result
