"""
Manage query for wyrmdb editor
"""


"""
Return query as instruction to create the GUI elements
"""
def process(raw_query):
    instructions = tokenizer(raw_query=raw_query)
    return "ok"

"""
Tokenize the raw query to create instructions
"""
def tokenizer(raw_query):
    print(raw_query)

    return "instruction"