import os
import re

from llama_index import GPTSimpleVectorIndex, SimpleDirectoryReader


os.environ['OPENAI_API_KEY'] = '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'


def index(sub_library="Ray RLlib"):
    sub_library_name_simplified = re.sub(r"( )+", lambda x: "_", sub_library).lower()
    text_data_directory = f"./data/text/{sub_library_name_simplified}/"

    documents = SimpleDirectoryReader(text_data_directory).load_data()
    index = GPTSimpleVectorIndex.from_documents(documents)

    test_question = "How can I train a PPO agent to play pong?"
    test_response = index.query(test_question)
    print(f"Reponse to test question {test_question}: {test_response}")

    index.save_to_disk(f"./data/indexes/{sub_library_name_simplified}.json")

    return index
