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

    # Split string at \n and also space (inline code)
    tokenized_query = [i.strip() for i in raw_query.splitlines() if i != ""]


    print(tokenized_query)

    return "instruction"