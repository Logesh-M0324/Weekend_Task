import numpy as np


def retrieve_documents(
    query,
    embedding_model,
    index,
    metadata,
    top_k=5
):
    
    query_embedding = embedding_model.encode(
        [query],
        convert_to_numpy=True,
        normalize_embeddings=True
    ).astype("float32")

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


def build_context(results):

    context_parts = []

    for _, row in results.iterrows():

        context_parts.append(
            f"Document: {row['title']}\n"
            f"Category: {row['category']}\n"
            f"Content: {row['content']}"
        )

    return "\n\n".join(context_parts)


def create_rag_prompt(
    question,
    context
):

    prompt = f"""
You are a customer support assistant.

Answer the user's question using ONLY the information
provided in the context below.

If the context does not contain enough information to answer
the question, clearly say that the available knowledge base
does not contain enough information.

Do not invent policies, procedures, prices, dates, or other
facts that are not present in the context.

Context:
{context}

User Question:
{question}

Answer:
"""

    return prompt


def generate_rag_answer(
    question,
    embedding_model,
    index,
    metadata,
    llm,
    top_k=5,
    max_tokens=200
):

    results = retrieve_documents(
        question,
        embedding_model,
        index,
        metadata,
        top_k
    )

    context = build_context(
        results
    )

    prompt = create_rag_prompt(
        question,
        context
    )

    response = llm(
        prompt,
        max_tokens=max_tokens,
        temperature=0.2,
        stop=["User Question:"]
    )

    answer = response[
        "choices"
    ][0]["text"].strip()

    return answer, results