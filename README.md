# GVE
**Gensim Vectors Exporter** 
Exports the word vectors found in default gensim models to files that can be loaded
and used in other programming languages.

# Usage 
1. Download repository.
2. Run `bash prepare.sh`
3. Configure settings in `settings.py`
4. Run `bash export.sh`

# Files
The `word2vec-google-news-300`, `fasttext-wiki-news-subwords-300` and all `glove-wiki-gigaword-X` models from
50 to 300 are stored at `mega.nz`.

**Dataset Link (Mega.NZ)** 
https://mega.nz/folder/o6cH3ZTa#mMFtVjs7K5ooEhBeUehbhQ

# How to use files? 
1. Model files are stored in a folder which consists of only two files.
2. Vocabulary words are stored separated by newlines in `vocabulary.txt`
3. Vector files are stored in `vectors.bin` as a flat sequence of bytes (float32 - 4 byte)
   numbers.
    - It is up to you how to parse the `.bin` file in the programming language of your choice.
    - To parse the `.bin` file, collecting the sequence of numbers into fixed size 
      vectors, e.g. a 2D array with each item having a length of say 50 
      (for 50 dimensional vectors). 
    - **Tip:** For large files, you may want to use streaming mode to reduce memory 
     consumption.
       
