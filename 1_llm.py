import json

import boto3

# create a client for bedrock runtime
br_client = boto3.client(service_name="bedrock-runtime")


# define an llm function to execute an LLM model with prompt
def llm(prompt):
    response = br_client.invoke_model(
        body=json.dumps(
            {
                "anthropic_version": "bedrock-2023-05-31",
                "max_tokens": 5000,
                "system": """You are a professional email writer. Return a fully formed email based on the details provided.""",
                "messages": [
                    {
                        "role": "user",
                        "content": prompt,
                    },
                ],
                "temperature": 0.8,  # 0.5 is the default value, 0.8 allows more creativity
            }
        ),
        modelId="anthropic.claude-3-sonnet-20240229-v1:0",
    )
    return json.loads(response.get("body").read())


# REPL loop, to ask for input and generate email content
while True:
    print("\n\n")
    # get the email topic from the user
    input_text = input("Email Topic: ")
    # generate email content based on the topic
    output = llm(input_text)
    # print the email content
    print(output.get("content")[0].get("text"))
    print("\n\n")
