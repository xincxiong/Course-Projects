import numpy as np
import time


def vectorize(sentence, corpus):
	# TODO: YOUR ANSWER HERE!
	return sentence, corpus


def compare_distances(input_sen_vec, corpus_vecs, corpus):
	# TODO: YOUR ANSWER HERE!
	return most_similar_sentence


def find_similar_sentence(input_sentence, corpus_file):
	start_time = time.time()
	with open(corpus_file) as f:
		corpus = f.readlines()
	corpus = [x.strip() for x in corpus]
	input_sen_vec, corpus_vecs = vectorize(input_sentence, corpus)
	most_similar_sentence = compare_distances(input_sen_vec, corpus_vecs, corpus)
	print 'Took ', time.time() - start_time, 'seconds!'
	return most_similar_sentence


most_sim_sentence = find_similar_sentence('I am large. I contain multitudes', 'LEAVES OF GRASS')
print 'most_sim_sentence: ', most_sim_sentence

