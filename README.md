# Chatbot Project in Graph Structure

Bu çalışmada Google AI tarafından geliştirilen yapay zekâ Gemini API'ı kullanılarak RAG ile bir chatbot projesi geliştirilmiştir. 

Projede __.env__ dosyasında içeriğinde şu veriler bulunmaktadır.

• GEMINI_API_KEY=

• LANGCHAIN_API_KEY=

• LANGCHAIN_TRACING_V2=true

• LANGCHAIN_PROJECT=PROJECT_NAME

• TAVILY_API_KEY=

Projede, Gemini AI ile birlikte Langchain ve Langgraph framework'ü kullanılmıştır. Langchain, büyük dil modelleri ile uygulama geliştirilmesinde kullanılmaktadır. Zincir yapısında LLM'lerin birbirleri ile ve insanlar ile konuşmasını sağlamaktadır. Doküman okuma-yükleme, chat geçmişi tutma, embedding işlemleri ve vektör database işlemleri için langchain framework'ünden faydalanılmıştır. LangChain, LLM'ler ile entegrasyon sağlayarak özelleştirilmiş sorgu yönetimi sunmaktadır. Langgraph ise agent oluşturma, chat hafızasını bellekte / veri tabanında tutma gibi hizmetler sunmaktadır.

<h3> TAVILY </h3>

<br>
Bu çalışmada, Tavily kullanılarak LLM modelinin web sayfası araştırmaları ile entegre bir şekilde bir agent yapısında çalışması sağlanmıştır.


<br>

Langgraph kullanılarak chat hafızası bir veri tabanı dosyasına kayıt edilmiştir. Bu sayede eski chat konuşmaları kaybolmamıştır ve geliştirilen model daha tutarlı sonuçlar / cevaplar üretmiştir.

<br>

Proje bir graph yapısında geliştirilmiştir. Bu graph yapısında öncelikle belirlediğimiz url adreslerinden çekilen veriler lokalde oluşturulan bir db'de vectorstore olarak tutulmaktaadır. Oluşturulan sistem öncelikle sorulan soruya ait uygun cevabı vectorstore içerisinde aramaktadır. Vectorstore'da bulunamayan cevaplar Tavily aracılığı ile websearch ile aranmaktadır. 

Çalışmada oluşturulan graph yapısı Şekil 1'de görülmektedir.
<br>
<br>
<div align="center">
<img src="https://github.com/user-attachments/assets/5e4d5042-a92c-446c-935c-0bfaf49a6568" alt="image">
</div>
Şekil 1. Graph yapısı
<br>
<br>

Vectorstore veya websearch'ten elde edilen cevaplar grader fonksiyonlarına gönderilmektedir. Retrieval grader ile dokumandandaki bilgiler ve alınan cevap tutarlı mı kontrol edilmektedir. Kontrol sonucunda string olarak "yes" ve "no" cevapları dönmektedir. Halüsinasyon grader ile ise llm'in halüsinasyon görüp görmediği kontrol edilmektedir. Kontrol sonucunda binary "0" ve "1" olarak bir cevap dönmektedir. Halüsinasyon görülmüyorsa cevabın sorulan soru ile tutarlı olup olmadığı kontrolü yapılarak kullanıcıya bir sonuç dönülmektedir.

Bu aşamalar sonucunda kod Şekil 1'de graph yapısındaki gibi bir yol izlemektedir. Graph yapısındaki düz çizgiler koşulsuz edge, kesikli çizgiler ise koşula bağlı edge olarak tanımlanmaktadır. Burada tanımlanan koşullar grader ve router fonksiyonlarıdır.
<br>

Çalışmada vectorstore içerisindeki veri kullandığında izlenilen yol Şekil 2'de görülmektedir.
<br>
<br>
<div align="center">
<img src="https://github.com/user-attachments/assets/55994703-b33f-44f2-b2e8-83de7720bba2" alt="image">
</div>
Şekil 2. Vectorstore üzerinden ilerlenilen senaryo

<br>

<br>
Vectorstore üzerinden elde edilen örnek çıktı Şekil 3'te görülmektedir.
<div align="center">
<img src="https://github.com/user-attachments/assets/b564fc1d-da38-4159-ac91-cf8fe9f8fd6b" alt="image">
</div>
Şekil 3. Vectorstore örnek çıktı

<br>
<br>

Çalışmada websearch ile elde edilen veri kullandığında izlenilen yol Şekil 4'te görülmektedir.
<div align="center">
<img src="https://github.com/user-attachments/assets/c3538054-db35-4106-b749-78a092d78731" alt="image">
</div>
Şekil 4. Websearch üzerinden ilerlenilen senaryo
<br>
<br>

Websearch üzerinden elde edilen örnek çıktı Şekil 5'te görülmektedir.
<div align="center">
<img src="https://github.com/user-attachments/assets/be93b9ff-e180-4cd1-a68b-df5f9da265b3" alt="image">
</div>
Şekil 5. Websearch örnek çıktı

<h3> KAYNAKLAR </h3>

Udemy - Yapay Zekâ Uygulamaları: Langchain, RAG, LLM Orkestrasyonu - Atıl Samancıoğlu
