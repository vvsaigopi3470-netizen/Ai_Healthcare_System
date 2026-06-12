import json

with open(
'chatbot/knowledge_base.json'
) as file:

    knowledge = json.load(file)

def generate_response(intent):

    if intent in knowledge:

        return knowledge[intent]

    return """
    Please consult a healthcare
    professional for detailed advice.
    """