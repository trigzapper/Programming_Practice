# My First RAG Pipeline

This notebook is my first working sample Retrieval-Augmented Generation (RAG) pipeline. It retrieves relevant pieces of a source document and gives them to a language model as context for answering a question. I also enabled LangSmith tracing and confirmed that the run appears there.

## What I built

The notebook now uses a Formula 1 article as its source material. I first tested it with Formula 1's [beginner's guide](https://www.formula1.com/en/latest/article/drivers-teams-cars-circuits-and-more-everything-you-need-to-know-about.7iQfL3Rivf1comzdqV5jwc/), then successfully ran the pipeline with a different F1 URL whose content discussed Max Verstappen and the São Paulo Grand Prix:

1. **Load** — `WebBaseLoader` fetches the page and extracts its text without a site-specific CSS filter. The HTML classes on one website may not exist on another.
2. **Split** — `RecursiveCharacterTextSplitter` turns the loaded document into chunks of 1,000 characters with 200 characters of overlap. Overlap helps preserve context across chunk boundaries.
3. **Embed and index** — Ollama's `nomic-embed-text` model creates local vector embeddings, which are stored in Chroma.
4. **Retrieve** — the retriever finds chunks relevant to a question.
5. **Generate** — a local `qwen3.5:9b` chat model receives the question and retrieved context. A local `ChatPromptTemplate` instructs it to answer concisely and say when the context does not contain the answer.
6. **Parse** — `StrOutputParser` returns the model response as a string.
7. **Trace** — LangSmith tracing is enabled for the project `rag-qwen-local`, and I can inspect the run there.

The notebook's example question asks what achievements of Max Verstappen are mentioned in the retrieved context and asks for a little more detail. With the different F1 source, the successful run returned a context-based answer rather than a blank result.

## What I learned

- RAG is a pipeline: loading documents, chunking, embedding, indexing, retrieval, and generation each have a separate role.
- The model does not need to memorize the source article. The retriever supplies relevant text at question time.
- Chat models and embedding models serve different purposes. Qwen generates answers; `nomic-embed-text` represents text as vectors for similarity search.
- Chroma provides a vector store and retriever interface for finding relevant chunks.
- A LangChain runnable chain can connect retrieval, prompt formatting, the model, and output parsing.
- LangSmith tracing can be used alongside local model inference. The model and embedding calls run locally, while tracing data is sent to LangSmith.
- A prompt can be written locally with `ChatPromptTemplate`; pulling one from LangSmith Hub is not necessary for this example.
- A web loader that works for one site may not work for another if its HTML selectors are hard-coded to the first site's CSS classes.
- The source URL determines what the retriever can answer. A broad F1 guide and a specific race report provide different evidence, so choose a source that matches the question.
- Questions that explicitly ask for details in the context help keep answers grounded. The model can summarize retrieved evidence, but its response should still be checked against the source.

## Challenges I worked through

### Missing `bs4`

The notebook initially failed with `ModuleNotFoundError: No module named 'bs4'`. The import is supplied by the `beautifulsoup4` package, so the package name to install is not `bs4`.

### LangChain import changes

The original `langchain.text_splitter` import was unavailable in the installed LangChain version. The splitter is now imported from `langchain_text_splitters`:

```python
from langchain_text_splitters import RecursiveCharacterTextSplitter
```

Likewise, `hub` was not exported from `langchain`; the older compatible import path was `langchain_classic`. For this pipeline, I switched to a local prompt template instead, so pulling a Hub prompt is optional.

### OpenAI API credits

Creating embeddings with `OpenAIEmbeddings()` returned an API `429` because the account had no credits remaining. I changed the pipeline to use local Ollama models instead:

- Chat: `qwen3.5:9b`
- Embeddings: `nomic-embed-text`

This avoids OpenAI API charges. The embedding model is separate from the chat model and must also be available locally (`ollama pull nomic-embed-text` if it is not installed yet).

### Public Hub prompt safety guard

`hub.pull("rlm/rag-prompt")` raised a `ValueError` because the installed LangChain version protects against deserializing public prompt manifests by default. A standalone assignment such as `dangerously_pull_public_prompt = True` does not pass an option to `hub.pull`. The alternative used in the notebook is a locally defined `ChatPromptTemplate`, which avoids that Hub request and its deserialization risk.

### Website-specific page parsing

The original loader used a `SoupStrainer` for the blog-specific classes `post-content`, `post-title`, and `post-header`. When I switched the source to Formula 1, those classes did not match the page, so the loader returned an empty document. Also, the Formula 1 URL was still commented out while the original blog URL remained active. I fixed this by making the Formula 1 URL active and removing the fixed CSS filter. The notebook now checks for empty extracted text and reports the number of characters loaded.

The loader was verified to extract 18,313 characters from the Formula 1 page in the current environment. Some sites may still require JavaScript or block automated requests, in which case `WebBaseLoader` alone may not be sufficient.

### Successful run with a different Formula 1 URL

After changing the source to a different F1 page, the RAG chain produced a non-empty, more detailed response to the Verstappen question. The response said that the context described him as a four-time champion and reported a second-place finish at the 2026 São Paulo Grand Prix after starting 21st, an eighth consecutive podium, and praise from his team principal. This confirmed that the same loading, chunking, vector indexing, retrieval, and generation pipeline can be reused with a new URL. The answer is a model-generated summary, so I should verify such claims against the retrieved chunks and the linked source.

During troubleshooting, Qwen sometimes answered only “I don't know” even when a retrieved chunk contained relevant information. A more specific question and a prompt asking for a concise answer based on context helped. If I want a brief explanation, I can ask for the supporting facts or evidence from the context; I should not rely on the model to reveal private internal reasoning.

### Seeing traces in LangSmith

Tracing must be enabled in the notebook kernel before invoking the chain. The notebook sets `LANGSMITH_TRACING`, asks for a LangSmith API key, and sets the project name to `rag-qwen-local`. After invoking `rag_chain`, I confirmed that its tracing is visible in LangSmith.

## Running the notebook

1. Select the project's `.venv` kernel in VS Code.
2. Ensure Ollama is running and the models are available:

   ```powershell
   ollama list
   ollama pull nomic-embed-text
   ```

   The Qwen model used by the notebook is `qwen3.5:9b`.
3. Run the setup and LangSmith configuration cells. Enter the LangSmith API key when prompted; an OpenAI API key is not needed.
4. Run the notebook cells in order to load, split, and index the document, then build and invoke the RAG chain.

## Next steps

- Try other questions and inspect which document chunks the retriever selected.
- Experiment with chunk size, overlap, and the number of retrieved chunks.
- Compare answers with and without retrieved context.
- Review inputs, retrieved context, outputs, and child runs in the LangSmith project.
