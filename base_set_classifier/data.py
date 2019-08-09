import pandas as pd
import numpy as np
import sklearn.model_selection as ms

def train_val_test_split(df, test_proportion, val_proportion, random_seed):
    filenames = df['filename'].values
    labels = df['class'].values
    filenames_train_val, filenames_test, labels_train_val, labels_test = ms.train_test_split(filenames, labels, test_size=test_proportion, stratify=labels, random_state=random_seed)
    filenames_train, filenames_val, labels_train, labels_val = ms.train_test_split(filenames_train_val, labels_train_val, test_size=(val_proportion/(1 - test_proportion)), stratify=labels_train_val, random_state=random_seed)
    return None


def encode(label):
    encoding = {'base_set': '1', 'not_base_set': '0'}
    return encoding[label]

def encode_dataframe(df):
    df['class'] = df['class'].map(encode)
    return df
