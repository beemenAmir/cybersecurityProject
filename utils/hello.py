import pandas as pd

def read_and_print_data(pickle_file_path):
    try:
        data = pd.read_pickle(pickle_file_path)
        print("Data from pickle file:")
        print(data)
    except FileNotFoundError:
        print(f"Error: File not found at path {pickle_file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Replace '/path/to/your/data.pkl' with the actual path to your pickle file
pickle_file_path = '//home/beemen/project/dbn-based-nids/data/processed/test/test_labels.pkl'

read_and_print_data(pickle_file_path)
