import spacy

# Load spaCy's pre-trained model
nlp = spacy.load("en_core_web_md")

def process_question(website_content, question):
    doc = nlp(website_content.lower())
    question_doc = nlp(question.lower())

    # A basic approach to check if the question is answered by the content
    if question.lower() in website_content.lower():
        return f"I found some information on your query: {question}"
    else:
        return "Sorry, I couldn't find an answer to your question."
