import os
import tabula
import pandas as pd
from scrapegraphai.graphs import PDFScraperGraph
from scrapegraphai.utils import convert_to_csv, convert_to_json, prettify_exec_info

# Set your OpenAI API key
OPENAI_API_KEY = ''

# Define the file path for the PDF file
file_path = "/Users/jack/Desktop/p21.pdf"

# Extract tables from the second page of the PDF using tabula
tables = tabula.read_pdf(file_path, pages=2, multiple_tables=True)

# Check the number of tables extracted
print(f"Total tables extracted from page 2: {len(tables)}")

# If tables are found, process the first table as an example
if tables:
    first_table = tables[0]

    # Display the raw extracted table
    print("Raw Extracted Table:")
    print(first_table)

    # Clean up the table by removing rows with all NaN values
    first_table.dropna(how='all', inplace=True)

    # Save the cleaned table to a CSV file
    cleaned_csv_path = "cleaned_table_page2.csv"
    first_table.to_csv(cleaned_csv_path, index=False)

    # Read the cleaned CSV file as text to pass to ScrapeGraph AI
    with open(cleaned_csv_path, 'r', encoding="utf-8") as file:
        csv_text = file.read()

    # Define the configuration for the graph
    graph_config = {
        "llm": {
            "api_key": OPENAI_API_KEY,
            "model": "gpt-4o",
        },
        "verbose": False,
    }

    # Define the prompt
    prompt = "Extract the relevant financial data from this table."

    # Create the PDFScraperGraph instance (using the cleaned CSV text)
    pdf_scraper_graph = PDFScraperGraph(
        prompt=prompt,
        source=csv_text,  # Pass the CSV text
        config=graph_config
    )

    # Run the PDF scraper graph
    result = pdf_scraper_graph.run()
    print("Generated Answer:")
    print(result)

    # Get graph execution info
    graph_exec_info = pdf_scraper_graph.get_execution_info()
    print(prettify_exec_info(graph_exec_info))

    # Save the result to JSON and CSV files
    convert_to_csv(result, "result_from_table")
    convert_to_json(result, "result_from_table")

else:
    print("No tables found on page 2.")

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
