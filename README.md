# 🚀 Sentiment Analysis using NLP – End-to-End Mini Project

## Overview

This project implements an NLP pipeline to classify sentiments as positive or negative. It covers data preprocessing, feature engineering, model building, and deployment.

## 📂 1. Data Collection & Analysis

- Used a dataset containing **50,000 rows** with sentiment-labeled text (balanced distribution).
- Explored patterns, distribution, and missing values.

## 📊 2. Exploratory Data Analysis (EDA)

- Performed **univariate analysis** using visualization techniques (histograms, word clouds, etc.).
- Analyzed sentiment distribution and frequently occurring words in positive & negative texts.

## 🛠 3. Data Preprocessing

To clean and prepare the text, the following techniques were applied:

- **Stopwords removal** – Removed commonly used words that don’t add value.
- **Stemming** – Converted words to their root form for normalization.
- **HTML tag removal** – Stripped unnecessary HTML tags from text data.
- **Emoji handling** – Processed emojis to interpret their sentiment.
- **Lowercasing** – Converted text to lowercase for consistency.
- **Categorical encoding** – Converted target labels (positive/negative) into numerical values.

## 🔢 4. Feature Engineering

- Implemented **TF-IDF Vectorization** to convert text into numerical format.
- Extracted important words and visualized their frequency in positive vs. negative texts.

## 🤖 5. Model Building & Evaluation

Trained multiple machine learning models:

- **Logistic Regression**
- **Random Forest**
- **Naïve Bayes**

✅ **Train-test split** was used to divide data for training & testing.
✅ Models were evaluated using **accuracy score, classification report, and cross-validation**.
✅ **Random Forest performed the best**, providing the highest accuracy.

## 🌍 6. Deployment

- Saved the trained model using **Pickle** for future predictions.
- Built an interactive **Streamlit web app** where users can enter text and get real-time sentiment predictions.

## 🎯 Key Takeaways

✔ Strengthened understanding of **NLP, data preprocessing, feature engineering, and ML models**.
✔ Learned how to effectively **visualize and interpret text data**.
✔ Successfully **deployed the ML model using Streamlit**, making it user-friendly.

## 🚀 How to Run the Project

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/sentiment-analysis-nlp.git
   cd sentiment-analysis-nlp
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

## 📌 Future Improvements

- Fine-tuning models using **deep learning (LSTMs, Transformers)**.
- Expanding dataset for better generalization.
- Adding support for **multiple languages**.

Feel free to ⭐ the repository if you find this useful!

---

📧 **Contact:** If you have any questions, reach out via [LinkedIn](https://www.linkedin.com/in/ayan-khan-917611250/).
