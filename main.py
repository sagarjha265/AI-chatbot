import streamlit as st
import pickle
from sklearn.feature_extraction.text import CountVectorizer

# Load the model and vocabulary
def load_model():
    with open("pickle_model.pkl", "rb") as file:
        model = pickle.load(file)
    return model

def load_vocab():
    with open("features_pkl", "rb") as vocab_file:
        vocab = pickle.load(vocab_file)
    return vocab

# Predict function
def chat(x, model, vocab):
    vect = CountVectorizer(vocabulary=vocab)
    chat_text = vect.transform([x])
    return model.predict(chat_text)

# Load model and vocabulary once at the start
model = load_model()
vocab = load_vocab()

# Streamlit UI Configuration
st.set_page_config(page_title="Chat with AI", page_icon=":speech_balloon:", layout="centered")

# Custom CSS for better styling
st.markdown("""
    <style>
    body {
        font-family: 'Helvetica', sans-serif;
        background-color: #f5f5f5;
    }
    .main {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        max-width: 800px;
        margin: auto;
    }
    .chat-container {
        border: 1px solid #e6e6e6;
        border-radius: 10px;
        padding: 15px;
        margin-bottom: 10px;
        background-color: #f9f9f9;
    }
    .chat-input {
        width: 100%;
        padding: 10px;
        border: 1px solid #ddd;
        border-radius: 5px;
        margin-bottom: 10px;
    }
    .chat-button {
        background-color: #4CAF50;
        color: white;
        padding: 10px 20px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        width: 100%;
    }
    .chat-button:hover {
        background-color: #45a049;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<div class="main">', unsafe_allow_html=True)
st.title("Chat with AI :speech_balloon:")

# Chat interface
st.markdown('<div class="chat-container">', unsafe_allow_html=True)
user_input = st.text_input("Type your message here:", key="input", help="Enter your message and press Enter to chat.")
st.markdown('</div>', unsafe_allow_html=True)

if st.button("Send", key="send_button", help="Click to send your message."):
    if user_input:
        response = chat(user_input, model, vocab)
        st.success(f"AI: {response[0]}")
    else:
        st.error("Please enter a message.")

st.markdown('</div>', unsafe_allow_html=True)
