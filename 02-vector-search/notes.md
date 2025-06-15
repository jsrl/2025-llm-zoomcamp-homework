Which Fields Could Be Used for Semantic Search
Here we can observe semantic similarity in practice: some of the questions and answers don’t share many overlapping words,
yet they clearly address the same topic. One asks about a topic, the other provides an answer.

For example:

Question:

“I have registered for the Data Engineering Bootcamp. When can I expect to receive the confirmation email?”
Answer:

“You don't need it. You're accepted. You can also just start learning and submitting homework without registering. It is not checked against any registered list. Registration is just to gauge interest before the start date.”
These two could be matched via the keyword registered,
but a sentence like “Not registered participants are not getting certification” would also match that keyword, while having a different semantic meaning.

So, if we’re building a Q&A retrieval-augmented generation (RAG) system,
it makes sense to store the text field (answers) as embeddings, and use vector search to find the most relevant answer to a given question query.