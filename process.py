#!/usr/lib/env python
#-*- coding=utf-8 -*-

import numpy as np
import pickle


with open('data.pickle', 'rb') as fff:
    # Pickle the 'data' dictionary using the highest protocol available.
    all_sentence= np.array(pickle.load(fff))
    # all_extractag= np.array(pickle.load(fff))
    first_label = pickle.load(fff)
    second_label= pickle.load(fff)




from sklearn import preprocessing
label_preprocess_1  = preprocessing.LabelEncoder()
first_array         = label_preprocess_1.fit(first_label)
##################

label_preprocess_2  = preprocessing.LabelEncoder()
second_array        = label_preprocess_2.fit(second_label)

########


from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer

####
vectorizer = CountVectorizer()
all_sentence_tmp = vectorizer.fit_transform(all_sentence)
all_sentence_vec = all_sentence_tmp.toarray()


# from gensim import corpora, models
# ###TF-IDF
# dictionary = corpora.Dictionary(all_extractag,prune_at = 2000000)
# corpus = [dictionary.doc2bow(all_extractag) for all_extractag in all_extractag]
# # doc2bow(): 将collection words 转为词袋，用两元组(word_id, word_frequency)表示
#
# #  topic model, TF-IDF
# tfidf = models.TfidfModel(corpus)
# corpus_tfidf = tfidf[corpus]

#
# tf_transformer = TfidfVectorizer()
# tfidf_sentence_tmp = tf_transformer.fit_transform(all_sentence)
# tfidf_sentence_vec = tfidf_sentence_tmp.toarray()

from sklearn import cross_validation

#
#
# from sklearn.naive_bayes import MultinomialNB
# MNB_model = MultinomialNB(alpha=0.01)
# scores1 = cross_validation.cross_val_score(MNB_model, tfidf_sentence_vec, first_label, cv=5)
# scores2 = cross_validation.cross_val_score(MNB_model, tfidf_sentence_vec, second_label, cv=5)
#
# print 'score_1_first_NB=' , scores1,'score_2_second_NB=',scores2
#
#
# #######################
# from sklearn.linear_model import LogisticRegression
# LR_model = LogisticRegression()
# scores3 = cross_validation.cross_val_score(LR_model, tfidf_sentence_vec, first_label, cv=5)
# scores4 = cross_validation.cross_val_score(LR_model, tfidf_sentence_vec, second_label, cv=5)
#
# print 'score_3_first_LR=' ,scores3,  'score_4_second_LR=',scores4
#
# ########
# #KNN
# # from sklearn.neighbors import KNeighborsClassifier
# # # fit a k-nearest neighbor model to the data
# # knn_model = KNeighborsClassifier()
# # scores5 = cross_validation.cross_val_score(knn_model, tfidf_sentence_vec, first_label, cv=5)
# # scores6 = cross_validation.cross_val_score(knn_model, tfidf_sentence_vec, second_label, cv=5)
# #
# # print 'score_5_first_KNN=' , scores5, 'score_6_second_KNN=' ,scores6
#
# ###SVC
# from sklearn.svm import LinearSVC
# svc_model=LinearSVC()
# scores7 = cross_validation.cross_val_score(svc_model, tfidf_sentence_vec, first_label, cv=5)
# scores8 = cross_validation.cross_val_score(svc_model, tfidf_sentence_vec, second_label, cv=5)
#
# print 'score_7_first_svc=' , scores7, 'score_8_second_svc=' ,scores8
#
#



########################
from sklearn.naive_bayes import MultinomialNB
MNB_model = MultinomialNB(alpha=0.01)
scores1 = cross_validation.cross_val_score(MNB_model, all_sentence_vec, first_label, cv=5)
scores2 = cross_validation.cross_val_score(MNB_model, all_sentence_vec, second_label, cv=5)

print 'score_1_first_NB=' , scores1,'score_2_second_NB=',scores2


#######################
from sklearn.linear_model import LogisticRegression
LR_model = LogisticRegression()
scores3 = cross_validation.cross_val_score(LR_model, all_sentence_vec, first_label, cv=5)
scores4 = cross_validation.cross_val_score(LR_model, all_sentence_vec, second_label, cv=5)

print 'score_3_first_LR=' ,scores3,  'score_4_second_LR=',scores4

#########
##KNN
# from sklearn.neighbors import KNeighborsClassifier
# # fit a k-nearest neighbor model to the data
# knn_model = KNeighborsClassifier()
# scores5 = cross_validation.cross_val_score(knn_model, all_sentence_vec, first_label, cv=5)
# scores6 = cross_validation.cross_val_score(knn_model, all_sentence_vec, second_label, cv=5)
#
# print 'score_5_first_KNN=' , scores5, 'score_6_second_KNN=' ,scores6

###SVC
from sklearn.svm import LinearSVC
svc_model=LinearSVC()
scores7 = cross_validation.cross_val_score(svc_model, all_sentence_vec, first_label, cv=5)
scores8 = cross_validation.cross_val_score(svc_model, all_sentence_vec, second_label, cv=5)

print 'score_7_first_svc=' , scores7, 'score_8_second_svc=' ,scores8

from sklearn.tree import tree
tree_model=tree.DecisionTreeClassifier()
scores10 =  cross_validation.cross_val_score(tree_model, all_sentence_vec, first_label, cv=5)
scores11 =  cross_validation.cross_val_score(tree_model, all_sentence_vec, first_label, cv=5)

print 'score_10_first_svc=' , scores10, 'score_11_second_svc=' ,scores11


print '******'*40
