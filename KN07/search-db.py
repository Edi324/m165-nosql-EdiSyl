import chromadb

client = chromadb.PersistentClient(path="./chroma_data")
collection = client.get_collection(name="support_tickets")

suchanfrage = "Mein Monitor zeigt kein Bild an."
print(f"Suche nach: '{suchanfrage}'...")

# RICHTIG: semantische Suche über Vektor-Ähnlichkeit
resultate = collection.query(
    query_texts=[suchanfrage],
    n_results=2
)
print("Gefundene Tickets:", resultate["documents"])