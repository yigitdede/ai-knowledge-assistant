🤖 AI Knowledge Assistant
## Projenin Amacı

Bu proje, kullanıcının doğal dilde sorduğu sorulara veri tabanındaki metinlerden yanıt veren bir RAG (Retrieval-Augmented Generation) tabanlı AI asistanıdır. Amacımız, AI bilgisiyle desteklenmiş bir chatbot oluşturmak ve gerçek dünya bilgilerini hızlıca erişilebilir hale getirmektir.

## Veri Seti Hakkında

Veri seti data/raw klasöründe yer alan kısa metin paragraflarından oluşmaktadır.

Bu paragraflar, yapay zeka, makine öğrenmesi ve derin öğrenme gibi konuları kapsayan örnek belgeler içerir.

Veri seti tamamen hazır veri seti olarak kullanılmıştır, dolayısıyla toplama süreci manuel olarak yapılmamıştır.

Her belge .txt formatında saklanır ve model tarafından embedding işlemi için kullanılır.

## Kullanım

Modeli ve veriyi Google Colab üzerinde çalıştırabilirsiniz.

Arayüz için Hugging Face Space üzerinden canlı demo sağlanmaktadır.

Colab ve Hugging Face Space birbirinden bağımsızdır, arayüz için Hugging Face Space linkine yönlendirme yapılır.

## Kullanılan Yöntemler

Veri Yükleme: src/data_loader.py ile raw verilerin yüklenmesi.

Model: src/model.py içinde basit bir RAG modeli ve embedding mekanizması (sentence-transformers) kullanılmıştır.

Eğitim: src/train.py ile verilerden embedding’ler çıkarılır ve FAISS tabanlı vektör veritabanı oluşturulur.

Sorgu İşleme: Kullanıcının sorusu embed edilir, en yakın metin FAISS ile bulunur ve sonuç kullanıcıya gösterilir.

Web Arayüzü: streamlit ile basit bir arayüz geliştirilmiştir.

## Çözüm Mimarisi

Proje, RAG (Retrieval-Augmented Generation) mimarisi kullanır.

Veri yükleme: src/data_loader.py ile raw veriler alınır.

Model: src/model.py içinde embedding + retrieval mekanizması (sentence-transformers + FAISS).

Eğitim: src/train.py ile verilerden vektörler çıkarılır ve FAISS vektör tabanı oluşturulur.

Web arayüzü: Colabte başlanan proje hugging face streamlit üzerinden arayüze sunulur.


## Elde Edilen Sonuçlar

Model, kısa sorulara veri seti içerisinden doğru ve anlamlı yanıtlar verebilmektedir.

Örnek çıktı:

Soru: "Yapay zeka nedir?"

Cevap: "Yapay zeka, bilgisayar sistemlerinin insan zekasına benzer şekilde öğrenme, akıl yürütme ve problem çözme yetenekleri kazanmasını amaçlayan bir bilim dalıdır."

Soru: "Makine öğrenmesi ne işe yarar?"

Cevap: "Derin öğrenme, çok katmanlı yapay sinir ağlarını kullanarak karmaşık verilerden anlamlı özellikler çıkaran bir makine öğrenmesi alt dalıdır."

## Web Arayüzü & Kullanım Kılavuzu

Arayüz Streamlit ile geliştirilmiştir.

Kullanıcı sorusunu yazıp "Yanıtla" butonuna bastığında model en yakın metni veri setinden bularak yanıt verir.

Örnek kullanım:

Soru kutusuna "Yapay zeka nedir?" yazılır.

Model cevabı gösterir: "Yapay zeka, bilgisayar sistemlerinin insan zekasına benzer şekilde öğrenme…"

🌐 [Canlı Hugging Face Space Linki](https://huggingface.co/spaces/yigitdede/ai-knowledge-assistant)

  [Kod yazıldığı Google Colab Linki] (https://colab.research.google.com/drive/1Ah6PVVuJ3AYT75RpiP-S7lNGtzyFa9A8?usp=sharing)

## Gereksinimler

Python 3.9+

Streamlit

pandas

altair

sentence-transformers

faiss-cpu
### Proje Mimarisi
```/ai-knowledge-assistant
│
├─ streamlit_app.py      # Ana dosya, HF Space main file olarak gösterilecek
├─ requirements.txt
├─ data/
│   └─ raw/
│       ├─ 1.txt
│       ├─ 2.txt
│       └─ ... (toplam 7-8 txt)
├─ src/
│   ├─ __init__.py
│   ├─ data_loader.py
│   ├─ model.py
│   └─ train.py
└─ README.md
```





## Çalıştırma Kılavuzu

### 

# 1.Repo klonlama
`git clone https://github.com/<your-username>/ai-knowledge-assistant.git
cd ai-knowledge-assistant`

# 2.Python sanal ortamı oluşturun ve aktif edin

`python -m venv venv`
`source venv/bin/activate`

`venv\Scripts\activate`

# 3. Gereken paketleri yükleyin

`pip install -r requirements.txt`

# 4. Streamlit uygulamasını başlatın

`streamlit run src/streamlit_app.py`

