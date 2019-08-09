import pandas as pd
import numpy as np
import sklearn.model_selection as ms

#######################
## Data manipulation ##
#######################

def train_val_test_split(df, test_proportion, val_proportion, seed=None):
    """
    Split a DataFrame into train, validation, and test datasets.
    df: type DataFrame, with columns=['filename', 'class'] is the dataset to train_test_split
    test_proportion: number signifying the proportion of df to put into the test set
    val_proportion: number signifying the proportion of df to put into the val set
    seed: random seed
    ---> df_train: type DataFrame, training dataset, df_val: type DataFrame, validation dataset, df_test: type DataFrame, test dataset
         in order (df_train, df_val, df_test)
    """
    filenames = df['filename'].values
    labels = df['class'].values
    filenames_train_val, filenames_test, labels_train_val, labels_test = ms.train_test_split(filenames, labels, test_size=test_proportion, stratify=labels, random_state=seed)
    filenames_train, filenames_val, labels_train, labels_val = ms.train_test_split(filenames_train_val, labels_train_val, test_size=(val_proportion/(1 - test_proportion)), stratify=labels_train_val, random_state=seed)
    df_train = pd.DataFrame({'filename': filenames_train, 'class': labels_train})
    df_val = pd.DataFrame({'filename': filenames_val, 'class': labels_val})
    df_test = pd.DataFrame({'filename': filenames_test, 'class': labels_test})
    return (df_train, df_val, df_test)



def encode(label):
    encoding = {'base_set': '1', 'not_base_set': '0'}
    return encoding[label]

def encode_dataframe(df):
    df['class'] = df['class'].map(encode)
    return df

#########################################
## Data preprocessing and augmentation ##
#########################################

def sample_dataset(dataset, samples_per_class=None, replacement=None, seed=None):
    """
    Samples a dataframe can be used to upsample or downsample the dataframe by class.
    dataset: type DataFrame, with columns=['filename', 'class'], is the dataset to sample from
    samples_per_class: type Dict, with keys equal to the number of uniqe classes in dataset['class'],
                       and values equal to the number of samples to draw from the specified class
    replacement: type Dict, with keys equal to the number of unique classes in dataset['class'],
                 and boolean values corresponding whether to sample with replacement from
                 the specified class
    seed: random seed
    ---> type DataFrame, of newly sampled dataset
    """
    df_frames = []
    classes = dataset['class'].unique()
    if samples_per_class == None:
        samples_per_class = dataset['class'].value_counts()
    if replacement == None:
        replacement = {c: False for c in classes}
    for c in classes:
        samples_per_c = dataset[dataset['class'] == c]
        sampled_df_per_c = samples_per_c.sample(n=samples_per_class[c], replace=replacement[c], random_state=seed)
        df_frames.append(sampled_df_per_c)
    return pd.concat(df_frames)
