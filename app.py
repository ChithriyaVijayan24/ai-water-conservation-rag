"""
AI-Powered Water Conservation Assistant (Improved RAG Version)

This version produces different answers based on user intent
and demonstrates smarter AI behavior.
"""

# --------------------------------------------------
# STEP 1: LOAD KNOWLEDGE BASE
# --------------------------------------------------

def load_knowledge_base(file_path="data.txt"):
    try:
        with open(file_path, "r") as file:
            return file.read()
    except FileNotFoundError:
        return ""


# --------------------------------------------------
# STEP 2: DETECT QUESTION INTENT
# --------------------------------------------------

def detect_intent(query):
    query = query.lower()

    if any(word in query for word in ["save", "reduce", "conserve", "home"]):
        return "saving_tips"

    if any(word in query for word in ["why", "importance", "important"]):
        return "importance"

    if any(word in query for word in ["student", "school", "college"]):
        return "students"

    if any(word in query for word in ["community", "society", "city"]):
        return "community"

    if "sdg" in query:
        return "sdg"

    return "unknown"


# --------------------------------------------------
# STEP 3: RETRIEVE CONTENT BASED ON INTENT
# --------------------------------------------------

def retrieve_by_intent(intent, knowledge_base):
    sections = knowledge_base.split("\n\n")

    if intent == "saving_tips":
        return sections[0]

    if intent == "students":
        return sections[1]

    if intent == "community":
        return sections[2]

    if intent == "sdg":
        return sections[3]

    if intent == "importance":
        return sections[0] + "\n" + sections[3]

    return ""


# --------------------------------------------------
# STEP 4: GENERATE CONTEXTUAL RESPONSE
# --------------------------------------------------

def generate_response(query, knowledge_base):
    intent = detect_intent(query)
    retrieved_content = retrieve_by_intent(intent, knowledge_base)

    if retrieved_content.strip() == "":
        return (
            "I’m sorry, I don’t have enough verified information to answer that accurately.\n"
            "Please refer to official environmental or government sources."
        )

    response_templates = {
        "saving_tips": (
            "Here are some practical ways to save water:\n\n"
            "{}\n\n"
            "These actions can significantly reduce daily water wastage."
        ),
        "importance": (
            "Water conservation is important because:\n\n"
            "{}\n\n"
            "Responsible usage helps protect ecosystems and future generations."
        ),
        "students": (
            "Students can play an important role in water conservation:\n\n"
            "{}\n\n"
            "Small actions by students can create large collective impact."
        ),
        "communities": (
            "Communities contribute to water conservation through:\n\n"
            "{}\n\n"
            "Community involvement ensures sustainable water management."
        ),
        "sdg": (
            "Water conservation is directly aligned with:\n\n"
            "{}\n\n"
            "This supports global sustainability goals."
        )
    }

    return response_templates[intent].format(retrieved_content)


# --------------------------------------------------
# STEP 5: SAMPLE QUESTIONS
# --------------------------------------------------

def show_sample_questions():
    print("\nExample questions you can ask:")
    print("- How can I save water at home?")
    print("- Why is water conservation important?")
    print("- How can students contribute to water conservation?")
    print("- What role do communities play in water conservation?")
    print("- Which SDG is related to water conservation?")


# --------------------------------------------------
# STEP 6: MAIN CHAT LOOP
# --------------------------------------------------

def start_chat():
    knowledge_base = load_knowledge_base()

    if not knowledge_base:
        print("Knowledge base not found. Please upload data.txt")
        return

    print("=" * 60)
    print("AI-Powered Water Conservation Assistant")
    print("Smarter RAG-based Responses")
    print("=" * 60)

    show_sample_questions()

    while True:
        user_query = input("\nAsk a question (type 'exit' to quit): ")

        if user_query.lower() == "exit":
            print("Thank you for supporting sustainable water usage!")
            break

        response = generate_response(user_query, knowledge_base)
        print("\n" + "-" * 50)
        print(response)
        print("-" * 50)


# --------------------------------------------------
# PROGRAM ENTRY
# --------------------------------------------------

if __name__ == "__main__":
    start_chat()

