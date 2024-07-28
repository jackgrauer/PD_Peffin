import os
import json
from dotenv import load_dotenv
from scrapegraphai.graphs import PDFScraperGraph

load_dotenv()

# Set your OpenAI API key
OPENAI_API_KEY = ''

# Define the configuration for the graph
graph_config = {
    "llm": {
        "api_key": OPENAI_API_KEY,
        "model": "gpt-4o",
    },
    "verbose": True,
}

# Define the file path for the PDF file
source = "/Users/jack/Desktop/2023.pdf"

# Define the prompt to specify the page range
prompt = """"

Did the organization receive more than $25,000 in noncash contributions?

"""
# Create the PDFScraperGraph instance
pdf_scraper_graph = PDFScraperGraph(
    prompt=prompt,
    source=source,
    config=graph_config,
    
)

# Run the PDF scraper graph
result = pdf_scraper_graph.run()

# Print the extracted result
print(json.dumps(result, indent=4))
