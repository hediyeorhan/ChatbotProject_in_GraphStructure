from dotenv import load_dotenv

load_dotenv()

from graph.graph import app

if __name__ == "__main__":
    print("Hello Advanced RAG")
    print(app.invoke(input={"question": "Necmettin Erbakan Üniversitesi?"}))
    #print(app.invoke(input={"question": "Şu an Ankara hava durumu?"}))
    #print(app.invoke(input={"question": "How can i make hamburgers?"}))