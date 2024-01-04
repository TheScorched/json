import json

# Your string data
log_data = '''<insert your string here>'''

# Split the log_data into lines
log_lines = log_data.strip().split('\n')

# Initialize an empty list to store the JSON objects
log_list = []

# Iterate through each line and extract the key-value pairs
for line in log_lines:
    log_entry = {}
    key_value_pairs = line.strip().split(' ')
    for pair in key_value_pairs:
        key, value = pair.split(':')
        log_entry[key.strip()] = value.strip()
    log_list.append(log_entry)

# Convert the list of dictionaries to JSON format
log_json = json.dumps(log_list, indent=2)

# Print the JSON
print(log_json)
