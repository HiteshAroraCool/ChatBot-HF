import _pickle

with open("data.pkl", "rb") as f:
    loaded_data = _pickle.load(f)

# Check if 'label' is a dictionary and contains the key 'Home page'
if isinstance(loaded_data, dict) and 'Home page' in loaded_data.get('label', ''):
    features_data = loaded_data
    context = features_data.get('context', None)
    label = features_data.get('label', None)
    links_list = features_data.get('links', [])

    # Use 'context' and 'label' as needed
    if context is not None and label is not None:
        print("Label:", label)
        print("Context:", context)
        print("Links:", links_list)
    else:
        print("Invalid or missing data in 'Home page' label.")
else:
    print("Invalid data structure in the pickled file.")
