from sentence_transformers import SentenceTransformer


def load_embedding_model():
    model = SentenceTransformer(
        "all-MiniLM-L6-v2",
        device="cpu"
    )

    return model


def generate_embeddings(
    texts,
    model,
    batch_size=32
):
    embeddings = model.encode(
        texts,
        batch_size=batch_size,
        show_progress_bar=True,
        convert_to_numpy=True,
        normalize_embeddings=True
    )

    return embeddings


def generate_query_embedding(
    query,
    model
):
    embedding = model.encode(
        [query],
        convert_to_numpy=True,
        normalize_embeddings=True
    )

    return embedding