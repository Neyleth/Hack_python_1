"""
loop: while [1,2,3] ouput => [1,'@',2,'@',3,'@']
"""

def fn_hack_9():
    result = [1,2,3]
    nuevo = 1
    while nuevo < len(result):
        result.insert(nuevo,'@')
        nuevo += 2
    return result
