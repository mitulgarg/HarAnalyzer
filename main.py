from fastapi import FastAPI, HTTPException
from pydantic import BaseModel



app = FastAPI()

# In-memory database (for demonstration purposes)
items = []

# Pydantic model for item data
class Item(BaseModel):
    name: str


# Create an item
@app.post("/items/", response_model=Item)
async def create_item(item: Item):
    item.name=item.name[::-1]
    items.append(item)
    return item

# class Har(BaseModel):
#     har: str


# @app.post("/haranalyzer", response_model=Har)
# async def har_file_analyzer(har: Har):
#     try:
#         # Load HAR content as JSON
#         har_json = json.loads(har.har)
#         har_parser = HarParser(har_json)

#         extracted_data = []

#         for page in har_parser.pages:
#             for entry in page.entries:
#                 mime_type = entry['response']['content'].get('mimeType', '')
#                 raw_response = entry['response']['content'].get('text', '')

#                 # Print ECID header if response is not 2xx
#                 if entry['response']['status'] >= 300 or entry['response']['status'] < 200:
#                     for key in entry['response']['headers']:
#                         if "ECID" in key['name']:
#                             print("ECID:", key["value"])

#                 # Append parsed JSON response
#                 if raw_response:
#                     try:
#                         extracted_data.append(json.loads(raw_response))
#                     except json.JSONDecodeError:
#                         pass  # Skip non-JSON responses

#         return {"parsed": extracted_data}

#     except Exception as e:
#         raise HTTPException(status_code=400, detail=f"Error processing HAR file: {str(e)}")



