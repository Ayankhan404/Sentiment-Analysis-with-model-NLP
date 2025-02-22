
import streamlit as st
import pickle
import re
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer

# Load the trained model and vectorizer
clf = pickle.load(open('clf.pkl', 'rb'))
tfidf = pickle.load(open('tfidf.pkl', 'rb'))

# Define stopwords
stopwords_set = set(stopwords.words('english'))

# Preprocessing function
def preprocessing(text):
    emoji_pattern = re.compile('(?::|;|=)(?:-)?(?:\)|\(|D|P)')
    text = re.sub('<[^>]*>', '', text)
    emojis = emoji_pattern.findall(text)
    text = re.sub('[\W+]', ' ', text.lower()) + ' '.join(emojis).replace('-', '')
    prter = PorterStemmer()
    text = [prter.stem(word) for word in text.split() if word not in stopwords_set]
    return " ".join(text)

# Prediction function
def predict_sentiment(comment):
    preprocessed_comment = preprocessing(comment)
    comment_vector = tfidf.transform([preprocessed_comment])
    prediction = clf.predict(comment_vector)[0]
    return prediction

# Streamlit UI
st.title("Sentiment Analysis App")
st.subheader("Enter a comment to analyze its sentiment")

# User input
user_input = st.text_area("Type your comment here:")

if st.button("Analyze Sentiment"):
    if user_input:
        prediction = predict_sentiment(user_input)
        if prediction == 1:
            st.markdown(
                "<div style='background-color:green; padding:10px; border-radius:5px;'>"
                "<h3 style='color:white;'>Positive Comment 😊</h3>"
                "</div>", unsafe_allow_html=True)
        else:
            st.markdown(
                "<div style='background-color:red; padding:10px; border-radius:5px;'>"
                "<h3 style='color:white;'>Negative Comment 😞</h3>"
                "</div>", unsafe_allow_html=True)
    else:
        st.warning("Please enter a comment before analyzing.")
