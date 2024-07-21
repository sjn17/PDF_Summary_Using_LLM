# Import necessary libraries
!pip install boto3 langchain pypdf unstructured[pdf]
from langchain_community.document_loaders import UnstructuredPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import json
import boto3

# AWS Bedrock client setup
boto3_bedrock = boto3.client('bedrock-runtime',
                             region_name='us-east-1',
                             aws_access_key_id='',
                             aws_secret_access_key='')

# Function to summarize text using AWS Bedrock model
def summarizer(prompt_data):
    body_part = json.dumps({
        'inputText': prompt_data,
        'textGenerationConfig': {
            'maxTokenCount': 4000,
            'stopSequences': [],
            'temperature': 0,
            'topP': 1
        }
    })
    response = boto3_bedrock.invoke_model(
        body=body_part,
        contentType="application/json",
        accept="application/json",
        modelId='amazon.titan-text-express-v1'
    )
    output_text = json.loads(response['body'].read())['results'][0]['outputText']
    return output_text

# Function to read PDF and split into chunks
def read_pdf_and_split(filename):
    loader = UnstructuredPDFLoader(filename)
    data = loader.load()
    print(data)  # Debugging: printing loaded data
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=400,
        chunk_overlap=50,
        length_function=len,
        add_start_index=True
    )
    splitted_text = splitter.split_documents(data)
    return splitted_text

# Example usage: read PDF and split into chunks
pdf_document = read_pdf_and_split('/content/YOGI-2-0_211022.pdf')

# Generate summaries for each chunk
summary = ""
for i in pdf_document:
    chunk_content = i.page_content  # Extract text content of chunk
    prompt = f"""Human: Provide a detailed summary for the chunk of text provided to you:\nText: {chunk_content}"""
    summary += summarizer(prompt)  # Generate summary for chunk and append to summary string

# Generate final cohesive summary from all individual summaries
final_summary_prompt = f"""Human: You will be given a set of summaries from a document. Create a cohesive
summary from the provided individual summaries. The summary should be very detailed.\nSummaries: {summary}"""
final_summary = summarizer(final_summary_prompt)
print(final_summary)  # Print the final cohesive summary
