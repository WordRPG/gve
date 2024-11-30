###########################
# GENSIM VECTORS EXPORTER #
###########################
import sys 
import dill 
from gensim import downloader as api 
import os
import array 

# --- extract arguments --- #
MODEL_NAME = sys.argv[1]

print("Gensim Vectors Exporter")
print("-----------------------------------------------")

print("Using model [" + MODEL_NAME + "]")
model = api.load(MODEL_NAME) 

print("Extracting vocabulary.")
vocabulary = list(model.key_to_index.keys())
n = len(vocabulary)
print("--- Detected " + str(n) + " words.")

print("Creating model folder.")
MODEL_PATH = "./data/" + MODEL_NAME + "/"
os.makedirs(MODEL_PATH, exist_ok=True)

print("Saving vocabulary file.")
open(MODEL_PATH + "/vocabulary.txt", "w").write("\n".join(vocabulary)) 

print("Extracting vectors.")
VECTORS_FILEPATH = MODEL_PATH + "/vectors.bin"
open(VECTORS_FILEPATH, "wb").close()
vectors_file = open(VECTORS_FILEPATH, "ab")

i = 0 
for word in vocabulary: 
    print("--- Extracting vocabulary " + str(i + 1) + " of " + str(n))
    vector = model[word]
    items_b = array.array("f", vector).tobytes()
    vectors_file.write(items_b) 
    i += 1