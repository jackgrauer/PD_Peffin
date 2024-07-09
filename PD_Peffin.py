import os
from scrapegraphai.graphs import XMLScraperGraph
from scrapegraphai.utils import convert_to_csv, convert_to_json, prettify_exec_info

# Set your OpenAI API key
OPENAI_API_KEY = ""

# Define the file path for the XML file
file_path = "/Users/jack/Desktop/UArts/2016-06-CENSUS-0000026108.xml"

# Read the XML file
with open(file_path, 'r', encoding="utf-8") as file:
    text = file.read()

# Define the configuration for the graph
graph_config = {
    "llm": {
        "api_key": OPENAI_API_KEY,
        "model": "gpt-4o",
    },
    "verbose": False,
}

# Define the prompt
prompt = "what were UARts accounts payable and accrued expenses in 2015?"

# Create the XMLScraperGraph instance
xml_scraper_graph = XMLScraperGraph(
    prompt=prompt,
    source=text,  # Pass the content of the file, not the file object
    config=graph_config
)

# Run the XML scraper graph
result = xml_scraper_graph.run()
print("Generated Answer:")
print(result)

# Get graph execution info
graph_exec_info = xml_scraper_graph.get_execution_info()
print(prettify_exec_info(graph_exec_info))

# Save the result to JSON and CSV files
convert_to_csv(result, "result")
convert_to_json(result, "result")

# ASCII Puffin and quote
print("\nPuff up your life!")
print('''
                      .-"-.
                     / ^ ^ \\
                     \\_ v _/
                     //   \\\\
                    ((     ))
              =======""===""=======
                       |||
                       '|'
''')
