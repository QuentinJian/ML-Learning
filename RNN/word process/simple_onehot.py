import numpy as np

samples = ['The cat sat on the mat', 'The quick brown fox jump over the lazy dog.']

token_index = {}

for sample in samples:
    for word in sample.split():
        if word not in token_index:
            token_index[word] = len(token_index) + 1

print(token_index)
max_length = 10
results = np.zeros(shape=(len(samples), max_length, max(token_index.values()) + 1))
print(results.shape)

for i, sample in enumerate(samples):
    for j, word in list(enumerate(sample.split()))[:max_length]:
        index = token_index.get(word)
        results[i, j, index] = 1

print(results)