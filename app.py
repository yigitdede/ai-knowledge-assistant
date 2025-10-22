import os, sys
os.chdir('/content/ai-knowledge-assistant')
sys.path.append('/content/ai-knowledge-assistant')

from src import data_loader, model, train

# 1. Veriyi yükle
data = data_loader.load_data("data/raw")

# 2. Modeli oluştur ve eğit
rag_model = model.MyModel()
train.train(rag_model, data)

# 3. Kullanıcı sorgusu
query = "Yapay zeka nedir?"
results = rag_model.retrieve(query)

print(f"🔎 Sorgu: {query}")
print("💡 En yakın bilgi:", results[0])

