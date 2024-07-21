# PDF_Summary_Using_LLM

# Text Summarization with Large Language Models 📄

Text summarization is a powerful application of Large Language Models (LLMs). By using LLMs, we can summarize large documents to provide precise summaries, saving time and effort.

## Table of Contents

- [Introduction](#introduction)
- [How to Perform Text Summarization](#how-to-perform-text-summarization)
- [Implementing Text Summarization with MapReduce](#implementing-text-summarization-with-mapreduce)
- [Creating a Bedrock Client](#creating-a-bedrock-client)
- [Functions Overview](#functions-overview)
  - [summarizer](#summarizer)
  - [read_pdf_and_split](#read_pdf_and_split)
- [Example Usage](#example-usage)
- [Installation](#installation)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Introduction

Text summarization involves using LLMs to condense large documents into brief, informative summaries. This is particularly useful in fields like financial analysis, where analyzing lengthy documents can be time-consuming.

## How to Perform Text Summarization

Text summarization can be performed by using prompt engineering, which involves providing a specific prompt to an LLM and passing the text information to generate a summary.

### Prompt Engineering

The process of designing and refining input prompts to an LLM to achieve the desired output. However, LLMs have a limited context window, which can be problematic for summarizing large documents.

### MapReduce Algorithm

To address the context window issue, we use the MapReduce algorithm:
1. **Splitting**: Split the large document into smaller chunks.
2. **Mapping**: Apply text summarization to each chunk using prompt engineering.
3. **Shuffling**: Combine the summaries from each chunk.
4. **Reducing**: Apply summarization to the combined summaries to get the final output.

## Implementing Text Summarization with MapReduce

By following these steps, we can implement text summarization using the MapReduce algorithm:
1. Split the document into chunks.
2. Apply text summarization to each chunk.
3. Combine the summaries from each chunk.
4. Apply summarization to the combined summaries to get the final output.

## Creating a Bedrock Client

To connect with Bedrock from Python, create a Boto3 client using your AWS access key and secret key.

## Functions Overview

### `summarizer`

This function takes prompt data and converts it to the expected JSON format for the Titan model. It then calls the Bedrock Titan text express model using `invoke_model` from the Boto3 client.

###read_pdf_and_split
This function reads a PDF file, splits it into multiple chunks, and returns the chunks.

###Installation
To install the necessary libraries, run:
'''pip install boto3 langchain pypdf unstructured[pdf]'''

Contributing
If you'd like to contribute, please fork the repository and use a feature branch. Pull requests are warmly welcome.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Contact
For any questions or feedback, please contact shubhamjnikam@gmail.com



