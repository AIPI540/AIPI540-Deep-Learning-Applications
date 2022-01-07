![](https://storage.googleapis.com/aipi_datasets/Duke-AIPI-Logo.png)

# Natural language processing
This directory contains notebooks which introduce several of the foundational approaches and architectures used to solve problems in natural language processing.  This content accompanies the Natural Language Processing module of the course.

The directory contains the following demo notebooks (which should be reviewed in the order listed):  
- **classification**  
    - **text_classification_tfidf**  
        - classification of text documents using classical bag-of-words and TF-IDF approaches
    - **text_classification_pytorch**  
        - classification of text documents using learned word embeddings
    - **text_classification_doc2vec**  
        - classification of text documents using Doc2vec: pre-trained word embeddings plus a learned document-level embedding
    - **text_classification_sent_transformer**  
        - classification of text documents using pre-trained Sentence Transformer model to create document-level embeddings for short documents


- **summarization**  
    - **extractive_summarization**  
        - introduces the use a graph based approach to representing text and PageRank to extract the main points for summarization
    - **generative_summarization**  
        - abstractive summarization of text documents using a pre-trained transformer model to generate summary text


- **topic_modeling**  
    - **topic_modeling_lda_nmf**  
        - introduces the use of classical approaches to extracting latent topics within sets of text documents (LDA and NMF), where the list of topics included is not previously known
    - **topic_modeling_transformer**  
        - demonstrates the use of a pre-trained transformer model to identify the most relevant topics for each document in a set, where the list of topics included in the set is not previously known
    - **topic_modeling_defined_topics**  
        - demonstrates the use of a pre-trained transformer model to identify the most relevant topics for each document in a set, where the list of topics included in the set IS known



    









