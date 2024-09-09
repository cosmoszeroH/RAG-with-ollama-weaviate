import weaviate


client = weaviate.connect_to_local()
client.collections.delete_all()

# Create collection
collection = client.collections.create_from_dict(
    {
    "class": "Question",
    "description": "A question",
    "vectorizer": "text2vec-ollama",
    "moduleConfig": {
      "text2vec-ollama": {
        "apiEndpoint": "http://ollama:11434",
        "model": "nomic-embed-text"
      },
      "generative-ollama": {
        "apiEndpoint": "http://ollama:11434",
        "model": "phi"
      }
    }
}
)

# Insert object
collection = client.collections.get("Question")
collection.data.insert({
    'category': 'SCIENCE',
    'question': 'This organ removes excess glucose from the blood & stores it as glycogen',
    'answer': 'Liver'
})
collection.data.insert({
    'category': 'ANIMALS',
    'question': 'The gavial looks very much like a crocodile except for this bodily feature',
    'answer': 'the nose or snout'
})
collection.data.insert({
    'category': 'SCIENCE',
    'question': 'In 1953 Watson & Crick built a model of the molecular structure of this, the gene-carrying substance',
    'answer': 'DNA'
})

# Query near text
collection = client.collections.get("Question")
result = collection.query.near_text(['biology'], 
    return_properties= ['question', 'answer', 'category'],
    limit= 2
  )

for o in result.objects:
    print(o.properties)


client.close()
