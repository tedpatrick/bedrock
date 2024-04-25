import json

import boto3
from numpy import dot
from numpy.linalg import norm

# create a client for bedrock runtime
br_client = boto3.client(service_name="bedrock-runtime")


# define a function to get embeddings
def embedding(texts):
    response = br_client.invoke_model(
        modelId="cohere.embed-english-v3",
        contentType="application/json",
        accept="*/*",
        body=json.dumps({"texts": texts, "input_type": "search_document"}),
    )
    return json.loads(response.get("body").read())


# get embeddings for cat and dog
cat = embedding(["cat"]).get("embeddings")[0]
dog = embedding(["dog"]).get("embeddings")[0]
frog = embedding(["frog"]).get("embeddings")[0]

# print the cat embedding
print(cat, "\n")

# print the dimentions of the cat embedding
print("dimentions: ", len(cat))

# cosine similarity
cat_dog_sim = dot(cat, dog) / (norm(cat) * norm(dog))
cat_frog_sim = dot(cat, frog) / (norm(cat) * norm(frog))

# print the cosine similarity between
print("cat-dog cosine similarity", cat_dog_sim)
print("cat-frog cosine similarity", cat_frog_sim)
