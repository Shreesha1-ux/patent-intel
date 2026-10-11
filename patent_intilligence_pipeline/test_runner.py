# test_runner.py
from utils.api_client import fetch_patent_data

# Let's send our messenger to find patents about "flying car"
print("Sending messenger to the patent library...")
results = fetch_patent_data("flying car")

# Print what it brought back!
print("Look what came back:")
print(results)