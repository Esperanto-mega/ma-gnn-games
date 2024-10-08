import pickle
import numpy as np
from data.Dataset import DataSet

class Baseline(DataSet):
    def __init__(self, dataset):
        num_users = {
            'Instruments': 24772,
            'Games': 50546,
            'Arts': 45141
        }

        num_items = {
            'Instruments': 9922,
            'Games': 16859,
            'Arts': 20956
        }
        
        self.user_record_file = f'/datain/v-yinju/rqvae-zzx/data/MA-GNN/{dataset}/user_records.txt'
        self.num_users, self.num_items = num_users[dataset], num_items[dataset]

    def generate_dataset(self, index_shift = 1):
        user_records = pickle.load(open(self.user_record_file, 'rb'))

        user_records = self.data_index_shift(user_records, increase_by = index_shift)
        train_val_set, test_set = self.split_data_sequentially(user_records, test_radio = 0.2)
        train_set, val_set = self.split_data_sequentially(train_val_set, test_radio = 0.1)

        return train_set, val_set, train_val_set, test_set, self.num_users, self.num_items + index_shift


# Amazon review dataset
class Books(DataSet):
    def __init__(self):
        self.dir_path = './data/dataset/Amazon/Books/'
        self.user_record_file = 'Books_item_sequences.pkl'
        self.user_mapping_file = 'Books_user_mapping.pkl'
        self.item_mapping_file = 'Books_item_mapping.pkl'

        self.num_users = 52406
        self.num_items = 41264
        self.vocab_size = 0

        self.user_records = None
        self.user_mapping = None
        self.item_mapping = None

    def generate_dataset(self, index_shift=1):
        user_records = self.load_pickle(self.dir_path + self.user_record_file)
        user_mapping = self.load_pickle(self.dir_path + self.user_mapping_file)
        item_mapping = self.load_pickle(self.dir_path + self.item_mapping_file)

        assert self.num_users == len(
            user_mapping) and self.num_items == len(item_mapping)

        user_records = self.data_index_shift(
            user_records, increase_by=index_shift)

        # split dataset
        train_val_set, test_set = self.split_data_sequentially(
            user_records, test_radio=0.2)
        train_set, val_set = self.split_data_sequentially(
            train_val_set, test_radio=0.1)

        return train_set, val_set, train_val_set, test_set, self.num_users, self.num_items + index_shift


class CDs(DataSet):
    def __init__(self):
        self.dir_path = './data/dataset/Amazon/CDs/'
        self.user_record_file = 'CDs_item_sequences.pkl'
        self.user_mapping_file = 'CDs_user_mapping.pkl'
        self.item_mapping_file = 'CDs_item_mapping.pkl'

        self.num_users = 17052
        self.num_items = 35118
        self.vocab_size = 0

        self.user_records = None
        self.user_mapping = None
        self.item_mapping = None

    def generate_dataset(self, index_shift=1):
        user_records = self.load_pickle(self.dir_path + self.user_record_file)
        user_mapping = self.load_pickle(self.dir_path + self.user_mapping_file)
        item_mapping = self.load_pickle(self.dir_path + self.item_mapping_file)

        assert self.num_users == len(
            user_mapping) and self.num_items == len(item_mapping)

        user_records = self.data_index_shift(
            user_records, increase_by=index_shift)

        # split dataset
        train_val_set, test_set = self.split_data_sequentially(
            user_records, test_radio=0.2)
        train_set, val_set = self.split_data_sequentially(
            train_val_set, test_radio=0.1)

        return train_set, val_set, train_val_set, test_set, self.num_users, self.num_items + index_shift


if __name__ == '__main__':
    data_set = CDs()
    train_set, val_set, train_val_set, test_set, num_users, num_items = data_set.generate_dataset(
        index_shift=1)
    print(train_set[0])
    print(val_set[0])
    print(train_val_set[0])
    print(train_set[-1])
    print(val_set[-1])
    print(train_val_set[-1])
    print(max(len(item_sequence) for item_sequence in train_set))
    # user_ids, item_ids = [], []
    # for uid, item_seq in enumerate(train_val_set):
    #     for iid in item_seq:
    #         user_ids.append(uid)
    #         item_ids.append(iid)

    # user_ids = np.asarray(user_ids)
    # item_ids = np.asarray(item_ids)
    # print(user_ids)
    # print(item_ids)
    # data_set.save_pickle([train_val_set, test_set, num_users, num_items], 'Books_for_SASR', protocol=2)
