from src.helper import load_pdf_file, text_split, download_HFE
from pinecone.grpc import PineconeGRPC as Pinecone
from pinecone import Pinecone, ServerlessSpec
from langchain_pinecone import PineconeVectorStore
from dotenv import load_dotenv
import os

load_dotenv()

PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY

extracted_data = load_pdf_file(data='Data/')
text_chunks = text_split(extracted_data)
embeddings = download_HFE()



pc = Pinecone(api_key=PINECONE_API_KEY)

index_name = "curo"

pc.create_index(
    name=index_name,
    dimension=384,
    metric = "cosine",
    spec= ServerlessSpec(
        cloud = "aws",
        region="us-east-1"
    )
)

docresearch = PineconeVectorStore.from_documents(
    documents = text_chunks,
    index_name = index_name,
    embedding=embeddings,
)