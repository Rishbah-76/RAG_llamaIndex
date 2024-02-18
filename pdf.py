import os
from llama_index.core import StorageContext, VectorStoreIndex, load_index_from_storage
from llama_index.core.readers import SimpleDirectoryReader


def get_index(data,index_name):
    index=None
    if not os.path.exists(index_name):
        print("Building Index: ",index_name)
        index=VectorStoreIndex.from_(data,show_progress=True)
        index.storage_context.persist(persist_dir=index_name)
        
    else:
        index = load_index_from_storage(
            StorageContext.from_defaults(persist_dir=index_name)
        )

    return index 

pdf_path=os.path.join("data", "India.pdf")
India_pdf= SimpleDirectoryReader().load_data(file=pdf_path)
India_index = get_index(India_pdf, "India")
India_engine = India_index.as_query_engine()