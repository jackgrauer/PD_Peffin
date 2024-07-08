######################################################################################## Step 1: Imports

from scrapegraphai.graphs import SmartScraperGraph
import json

######################################################################################## Step 2: Set Key

OPENAI_API_KEY = ""

graph_config = {
    "llm": {
        "api_key": OPENAI_API_KEY,
        "model": "gpt-4o",
    },
}

smart_scraper_graph = SmartScraperGraph(
    prompt="List one article and description from this page.",
    # also accepts a string with the already downloaded HTML code
    source="https://www.cnn.com/election/2024",
    config=graph_config
)

result = smart_scraper_graph.run()

######################################################################################## Step 3: Print results

output = json.dumps(result, indent=2)

line_list = output.split("\n")  # Sort of line replacing "\n" with a new line

for line in line_list:
    print(line)
