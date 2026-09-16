 import faiss
import numpy as np
import pandas as pd


def load_faiss_index(index_path):
    index = faiss.read_index(
        str(index_path)
    )

    return index


def load_metadata(metadata_path):
    metadata = pd.read_csv(
        metadata_path
    )

    return metadata


def search_similar_tickets(
    query_embedding,
    index,
    metadata,
    top_k=5
):
    query_embedding = np.asarray(
        query_embedding,
        dtype="float32"
    )

    similarity_scores, indices = index.search(
        query_embedding,
        top_k
    )

    results = metadata.iloc[
        indices[0]
    ].copy()

    results.insert(
        0,
        "Rank",
        range(1, top_k + 1)
    )

    results["Similarity"] = similarity_scores[0]

    return results