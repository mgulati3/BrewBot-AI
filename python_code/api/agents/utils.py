# def get_chatbot_response(client,model_name,messages,temperature=0):
#     input_messages = []
#     for message in messages:
#         input_messages.append({"role": message["role"], "content": message["content"]})

#     response = client.chat.completions.create(
#         model=model_name,
#         messages=input_messages,
#         temperature=temperature,
#         top_p=0.8,
#         max_tokens=2000,
#     ).choices[0].message.content
    
#     return response

# def get_embedding(embedding_client,model_name,text_input):
#     output = embedding_client.embeddings.create(input = text_input,model=model_name)
    
#     embedings = []
#     for embedding_object in output.data:
#         embedings.append(embedding_object.embedding)

#     return embedings

# def double_check_json_output(client,model_name,json_string):
#     prompt = f""" You will check this json string and correct any mistakes that will make it invalid. Then you will return the corrected json string. Nothing else. 
#     If the Json is correct just return it.

#     If there is any text before or after the json string, remove it.
#     Do NOT return a single letter outside of the json string.
#     Make sure that each key is enclosed in double quotes. 
#     The first thing you write should be  open curly brace of the json and the last letter you write should be the closing curly brace. 

#     You should check the json string for the following text between triple backticks:
#     ```
#     {json_string}
#     ```
#     """

#     messages = [{"role": "user", "content": prompt}]

#     response = get_chatbot_response(client,model_name,messages)
#     response = response.replace("`", "")

#     return response    

# utils.py

def get_chatbot_response(client, model_name, messages, temperature=0):
    """
    Builds a proper “messages” array for the OpenAI/RunPod chat endpoint,
    skipping any None or malformed entries, then calls the API and returns
    the assistant’s text response.
    """
    input_messages = []

    for message in messages:
        # 1) Skip if message is None
        if message is None:
            continue

        # 2) Skip if it’s not a dict or missing required keys
        if not isinstance(message, dict) or "role" not in message or "content" not in message:
            continue

        # 3) At this point, message["role"] and message["content"] are safe to use
        input_messages.append({
            "role": message["role"],
            "content": message["content"]
        })

    # 4) If we ended up with zero valid messages, raise an error early
    if len(input_messages) == 0:
        raise ValueError("No valid messages to send to the chat endpoint (all entries were None or malformed).")

    # 5) Call the chat completions endpoint
    response = client.chat.completions.create(
        model=model_name,
        messages=input_messages,
        temperature=temperature,
        top_p=0.8,
        max_tokens=2000,
    ).choices[0].message.content

    return response


def get_embedding(embedding_client, model_name, text_input):
    """
    Calls the embeddings endpoint and returns a list of vectors.
    """
    output = embedding_client.embeddings.create(input=text_input, model=model_name)

    embeddings = []
    for embedding_object in output.data:
        embeddings.append(embedding_object.embedding)

    return embeddings


def double_check_json_output(client,model_name,json_string):
    prompt = f""" You will check this json string and correct any mistakes that will make it invalid. Then you will return the corrected json string. Nothing else. 
    If the Json is correct just return it.

    If there is any text before or after the json string, remove it.
    Do NOT return a single letter outside of the json string.
    Make sure that each key is enclosed in double quotes. 
    The first thing you write should be  open curly brace of the json and the last letter you write should be the closing curly brace. 

    You should check the json string for the following text between triple backticks:
    ```
    {json_string}
    ```
    """

    messages = [{"role": "user", "content": prompt}]

    response = get_chatbot_response(client,model_name,messages)
    response = response.replace("`", "")

    return response 
