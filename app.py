"""
AI-Powered Water Conservation Assistant
Using Retrieval-Augmented Generation (RAG)

SDG Alignment: SDG 6 - Clean Water and Sanitation
This is a conceptual RAG implementation for educational purposes.
"""

# --------------------------------------------------
# STEP 1: LOAD KNOWLEDGE BASE
# --------------------------------------------------

def load_knowledge_base(file_path="data.txt"):
    """
    Loads the knowledge base from a text file.
    """
    try:
        with open(file_path, "r") as file:
            data = file.read()
        return data
    except FileNotFoundError:
        return ""


# --------------------------------------------------
# STEP 2: RETRIEVAL FUNCTION (RAG COMPONENT)
# --------------------------------------------------

def retrieve_relevant_content(query, documents):
    """
    Retrieves relevant lines from the knowledge base
    based on keyword matching.
    """
    query_words = query.lower().split()
    retrieved_lines = []

    for line in documents.split("\n"):
        line_lower = line.lower()
        if any(word in line_lower for word in query_words):
            retrieved_lines.append(line)

    return "\n".join(retrieved_lines)


# --------------------------------------------------
# STEP 3: RESPONSE GENERATION (SIMULATED LLM)
# --------------------------------------------------

def generate_response(query, knowledge_base):
    """
    Generates a response using retrieved information.
    Demonstrates responsible AI behavior.
    """
    retrieved_content = retrieve_relevant_content(query, knowledge_base)

    if retrieved_content.strip() == "":
        return (
            "I’m sorry, I don’t have enough verified information to answer that accurately.\n"
            "Please refer to official government or environmental sources for precise details."
        )

    response = (
        "Based on verified information:\n\n"
        f"{retrieved_content}\n\n"
        "This information highlights the importance of responsible water usage "
        "and supports sustainable living practices."
    )

    return response


# --------------------------------------------------
# STEP 4: SAMPLE QUESTIONS FOR DEMO
# --------------------------------------------------

def show_sample_questions():
    """
    Displays example questions for users.
    """
    print("\nSample questions you can ask:")
    print("1. How can I save water at home?")
    print("2. Why is water conservation important?")
    print("3. How can students contribute to water conservation?")
    print("4. What role do communities play in water conservation?")
    print("5. Which SDG is related to water conservation?")
    print("6. What is the water usage limit in my city?")


# --------------------------------------------------
# STEP 5: MAIN CHAT LOOP
# --------------------------------------------------

def start_chat():
    """
    Main function to interact with the user.
    """
    knowledge_base = load_knowledge_base()

    if knowledge_base == "":
        print("Knowledge base not found. Please upload data.txt file.")
        return

    print("=" * 60)
    print("AI-Powered Water Conservation Assistant")
    print("Aligned with SDG 6: Clean Water and Sanitation")
    print("=" * 60)

    show_sample_questions()

    while True:
        print("\nType 'exit' to quit.")
        user_query = input("\nAsk your question: ").strip()

        if user_query.lower() == "exit":
            print("\nThank you for promoting sustainable water usage!")
            break

        response = generate_response(user_query, knowledge_base)
        print("\n" + "-" * 50)
        print(response)
        print("-" * 50)


# --------------------------------------------------
# STEP 6: PROGRAM ENTRY POINT
# --------------------------------------------------

if __name__ == "__main__":
    start_chat()
