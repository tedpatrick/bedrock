# bedrock

## Setup Environment

```bash
$ conda env create
$ conda activate bedrock
```

## AWS Credentials

```bash
export AWS_ACCESS_KEY_ID=AKIIIIIIIIIIIIIIIII
export AWS_ACCOUNT_ID=08675309
export AWS_REGION=us-west-2
export AWS_SECRET_ACCESS_KEY=SECRET_KEY
```

## AWS Bedrock Models to Enable (Note: Model access is region specific. We use us-west-2)

Claude 3 Haiku
https://us-west-2.console.aws.amazon.com/bedrock/home?region=us-west-2#/providers?model=anthropic.claude-3-haiku-20240307-v1:0

Cohere Embed English V3
https://us-west-2.console.aws.amazon.com/bedrock/home?region=us-west-2#/providers?model=cohere.embed-english-v3

How to enable models
https://us-west-2.console.aws.amazon.com/bedrock/home?region=us-west-2#/modelaccess

## Run 0_embedding.py

```bash
$ python 0_embedding.py
```

## Run 1_llm.py

```bash
$ python 1_llm.py
```
