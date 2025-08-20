def sentiment_analysis(text):
    # Simple sentiment analysis using a predefined list of positive and negative words
    positive_words = ['good', 'happy', 'joy', 'excellent', 'fortunate', 'correct', 'superior']
    negative_words = ['bad', 'sad', 'pain', 'terrible', 'unfortunate', 'wrong', 'inferior']
    # Lowercase the text for easier matching
    text = text.lower()
    score = 0
    for word in positive_words:
        if word in text:
            score += 1
    for word in negative_words:
        if word in text:
            score -= 1
    if score > 0:
        return "Positive"
    elif score < 0:
        return "Negative"
    else:
        return "Neutral"
# Bias mitigation strategies:
# 1. Ensure the dataset used to build the positive/negative word lists is balanced and representative of different groups.
# 2. Remove or flag offensive or culturally sensitive terms from the word lists.
# 3. Regularly review and update the word lists to avoid perpetuating stereotypes.
# 4. Consider using more advanced models trained on diverse datasets to reduce bias.
# 5. If using user-generated data, check for and mitigate imbalances (e.g., overrepresentation of certain topics or demographics).
if __name__ == "__main__":
    user_text = input("Enter text to analyze: ")
    sentiment = sentiment_analysis(user_text)
    print(f"Sentiment: {sentiment}")