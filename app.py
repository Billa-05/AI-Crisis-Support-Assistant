from transformers import pipeline

# Load the sentiment analysis model
sentiment_model = pipeline("sentiment-analysis")

def crisis_support_response(user_text):
    """
    Generates a calming response depending on the user's emotional state.
    """

    analysis = sentiment_model(user_text)[0]
    label = analysis["label"]
    confidence = analysis["score"]

    # Basic emotional mapping
    if label == "NEGATIVE":
        return (
            "I'm here with you. ❤️\n"
            "It sounds like you're going through something heavy.\n\n"
            "👉 Try this grounding technique:\n"
            "- Look around and name 5 things you can see\n"
            "- Take a slow breath in for 4 seconds\n"
            "- Hold for 2 seconds\n"
            "- Exhale for 6 seconds\n\n"
            "You are safe. If you ever feel physically unsafe, "
            "please contact emergency services immediately."
        )

    elif label == "POSITIVE":
        return (
            "I'm glad you're feeling a bit lighter. 🌼\n"
            "Try to hold onto this feeling.\n\n"
            "If you need support again, I’m here."
        )

    else:  # neutral
        return (
            "Thank you for sharing your feelings with me. 🤍\n"
            "I'm here to support you.\n\n"
            "If you're feeling overwhelmed, try slow breathing:\n"
            "- Inhale 4s\n"
            "- Hold 2s\n"
            "- Exhale 6s\n"
        )


# Example interaction (you can delete this when deploying)
if __name__ == "__main__":
    print("AI Crisis Support Assistant is running...\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Take care. You’re never alone. ❤️")
            break

        print("\nAssistant:", crisis_support_response(user_input))
        print("\n--------------------------------\n")
