import streamlit as st
import cohere

# Initialize the Cohere client
API_KEY = " "  # Replace with your Cohere API key
co = cohere.Client(API_KEY)

# Streamlit app
st.title("Text Summarization with Cohere")

# Input text box
input_text = st.text_area("Enter text to summarize:", height=200)

# Button to trigger summarization
if st.button("Summarize"):
    if input_text.strip():
        try:
            # Call the summarize endpoint
            response = co.summarize(
                text=input_text,  # Input text to summarize
                length="medium",  # Options: 'short', 'medium', 'long'
                format="paragraph"  # Format options: 'paragraph', 'bullets'
            )
            # Display the summary
            summary = response.summary.strip()
            st.subheader("Summary:")
            st.write(summary)
        except Exception as e:
            st.error(f"Error summarizing text: {e}")
    else:
        st.warning("Please enter some text to summarize.")
