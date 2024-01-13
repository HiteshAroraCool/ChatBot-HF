# Chatbot with Web Scraping and Hugging Face API
Relinns Tech Assessment 

### Overview

This project involves creating a chatbot that interacts with a given website URL using the deepset/roberta-base-squad2 API. The chatbot is designed to be demonstrable via the console.

### Project Structure

- **`web_scrape.py`**: Contains functions for web scraping, extracting website content, and storing it in a pickled file (`data.pkl`). It utilizes the BeautifulSoup library for parsing HTML.

- **`model.py`**: Implements the chatbot functionality using the Hugging Face API. It loads context and label from `data.pkl` and utilizes the question-answering pipeline from the transformers library.

- **`api.py`**: Demonstrates interaction with the Hugging Face API by sending a predefined question and context.

- **`check_data.py`**: Checks and prints information from `data.pkl`, ensuring that the loaded data structure is as expected.

### Setup

1. Install required packages listed in `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

2. Configure environment variables:

- Create a `.env` file with your Hugging Face API key:

     ```
     API_KEY=your_api_key_here
     ```

### Usage

1. Run `web_scrape.py` to scrape the content of a specified website (e.g., https://botpenguin.com/) and store it in `data.pkl`. Optionally, Use `check_data.py` to verify the content and structure of the stored data in `data.pkl`.

2. Run `api.py` to interact directly with the Hugging Face API, providing a custom question and context.

3. Run `model.py` to interact with the Hugging Face API using the extracted data. The chatbot answers predefined questions about the website.


### Notes

- The project utilizes the deepset/roberta-base-squad2 API from Hugging Face and includes web scraping using BeautifulSoup for data extraction.

- The chatbot interacts with the Hugging Face question-answering pipeline, and the scraped data is stored in a pickled file for reuse.

# Objective: 
* Create a chatbot using the ChatGPT API that interacts with a given website URL. Although no front end is required, the chatbot must be demonstrable via console.*

In this project, the engineer will be responsible for:

1. Setting up the environment: Acquire necessary API keys for ChatGPT and install required libraries/packages for Python or Node.js. Configure the development environment to make API calls efficiently.

2. Extracting data: Create a script to fetch the website's content via the provided URL. Extract relevant information from the website by using web scraping techniques, such as Beautiful Soup for Python or Cheerio for Node.js.

3. Processing data: Identify and structure key information from the scraped content, which can be used as input to the ChatGPT API to generate meaningful responses.

4. Implementing the chatbot: Utilize the ChatGPT API to build the chatbot. Design the chatbot to take user inputs, process them, and generate suitable responses using the information obtained from the website.

5. Console demonstration: Prepare the chatbot to function seamlessly via the console, enabling users to interact with it, provide inputs, and receive relevant responses.
