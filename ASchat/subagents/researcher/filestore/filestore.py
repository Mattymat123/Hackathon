from google import genai
from google.genai import types
import time

client = genai.Client()

# Create the File Search store with an optional display name
file_search_store = client.file_search_stores.create(config={'display_name': 'ASchat Store'})

# Upload and import a file into the File Search store, supply a file name which will be visible in citations
operation = client.file_search_stores.upload_to_file_search_store(
  file='example.pdf',
  file_search_store_name=file_search_store.name,
  config={
      'display_name' : 'Call of Cthulhu',
  }
)

# Wait until import is complete
while not operation.done:
    time.sleep(5)
    operation = client.operations.get(operation)

# Ask a question about the file
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="""Can you tell me about Robert Graves""",
    config=types.GenerateContentConfig(
        tools=[
            file_search=(
                  file_search_store_names=[file_search_store.name]
            )
        ]
    )
)