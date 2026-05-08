# FAQ Chatbot using SpaCy + Cosine Similarity
# Install Required Libraries:
# pip install spacy scikit-learn
# python -m spacy download en_core_web_sm

import spacy
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load SpaCy English model
nlp = spacy.load("en_core_web_sm")

# ---------------------------------
# FAQ DATABASE
# ---------------------------------
faq_questions = [
    "What are your working hours?",
    "How can I reset my password?",
    "Where is my order?",
    "Do you provide refunds?",
    "How do I contact support?"
]

faq_answers = [
    "Our working hours are 9 AM to 6 PM.",
    "Click on 'Forgot Password' on the login page.",
    "You can track your order from your account dashboard.",
    "Yes, refunds are available within 7 days.",
    "You can contact support at support@example.com."
]

# ---------------------------------
# TEXT CLEANING FUNCTION
# ---------------------------------
def preprocess(text):
    doc = nlp(text.lower())

    tokens = []

    for token in doc:
        # Remove stop words and punctuation
        if not token.is_stop and not token.is_punct:
            tokens.append(token.lemma_)

    return " ".join(tokens)

# Preprocess FAQ questions
processed_questions = [preprocess(q) for q in faq_questions]

# ---------------------------------
# VECTORIZE QUESTIONS
# ---------------------------------
vectorizer = CountVectorizer()

faq_vectors = vectorizer.fit_transform(processed_questions)

# ---------------------------------
# CHATBOT RESPONSE FUNCTION
# ---------------------------------
def get_response(user_input):

    processed_input = preprocess(user_input)

    user_vector = vectorizer.transform([processed_input])

    similarity = cosine_similarity(user_vector, faq_vectors)

    best_match_index = similarity.argmax()

    best_score = similarity[0][best_match_index]

    # Similarity threshold
    if best_score > 0.2:
        return faq_answers[best_match_index]
    else:
        return "Sorry, I don't understand your question."

# ---------------------------------
# CHAT INTERFACE
# ---------------------------------
print("=================================")
print("        FAQ CHATBOT")
print("Type 'bye' to exit")
print("=================================")

while True:

    user_input = input("\nYou: ")

    if user_input.lower() == "bye":
        print("Bot: Goodbye!")
        break

    response = get_response(user_input)

    print("Bot:", response)
