from editor.actions import actions

"""
Manage query for wyrmdb editor
"""


"""
Return query as instruction to create the GUI elements
"""
def process(raw_query, instructions):
    return tokenizer(raw_query=raw_query, instructions=instructions)

"""
Tokenize the raw query to create instructions
"""
def tokenizer(raw_query, instructions):
    # Split string at \n and also space (inline code)
    tokenized_query = [i.strip() for i in raw_query.splitlines() if i != ""]

    for ins in instructions:
        for token in tokenized_query:
            if token.find(instructions[ins]["token"]) == 0:
                parameters = [i.strip() for i in token.replace(instructions[ins]["token"], "").splitlines() if i != ""]
                return apply_action(
                    action_name=instructions[ins]["parameters_descriptor"][0]["action"],
                    args=parameters,
                    description_positions=instructions[ins]["parameters_descriptor"][0]["positions"])


def apply_action(action_name, args, description_positions):
    return actions(name=action_name, params=args, description_positions=description_positions)

