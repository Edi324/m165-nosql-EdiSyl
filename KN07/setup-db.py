import chromadb

# Speichert die DB lokal im Ordner "chroma_data"
client = chromadb.PersistentClient(path="./chroma_data")
collection = client.get_or_create_collection(name="support_tickets")

documents = [
    "Der Bildschirm meines Laptops bleibt komplett schwarz.",
    "Ich kann mich nicht mehr ins Firmen-VPN einloggen.",
    "Der Drucker im 2. Stock zieht das Papier schief ein.",
    "Mein Passwort für das E-Mail-Postfach ist abgelaufen."
]
ids = ["ticket_1", "ticket_2", "ticket_3", "ticket_4"]

# ChromaDB wandelt die Texte hier automatisch in Vektoren (Embeddings) um!
collection.add(documents=documents, ids=ids)
print("Support-Tickets wurden erfolgreich vektorisiert und gespeichert!")