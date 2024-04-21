import os
import uuid

from google.cloud import dialogflow

def detect_intent(project_id, session_id, text, language_code):
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)

    text_input = dialogflow.TextInput(text=text, language_code=language_code)
    query_input = dialogflow.QueryInput(text=text_input)
    response = session_client.detect_intent(request={"session": session, "query_input": query_input})

    return response.query_result.fulfillment_text

def main():
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "chatbot-420907-2f27c59c911b.json"
    project_id = "citypass-nvfc"
    # session_id = "your-session-id"
    session_id = str(uuid.uuid4())
    language_code = "ru"

    while True:
        text = input("You: ")
        response = detect_intent(project_id, session_id, text, language_code)
        print("Chatbot: " + response)

if __name__ == "__main__":
    main()