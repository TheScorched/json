import csv

def process_data(data):
    with open('threatfox_data.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        
        # Write header
        headers = ['ID', 'IOC', 'Threat Type', 'Malware', 'Confidence Level', 'First Seen', 'Last Seen', 'Reference', 'Reporter', 'Tags']
        writer.writerow(headers)

        # Iterate over each entry in the data
        for entry in data['data']:
            # Extract relevant information
            tags = entry.get('tags', [])
            if not isinstance(tags, list):
                tags = [tags]  # Convert to list if not already a list
                tags = [str(tag) for tag in tags if tag is not None]

            row = [
                entry.get('id', ''),
                entry.get('ioc', ''),
                entry.get('threat_type', ''),
                entry.get('malware_printable', ''),
                entry.get('confidence_level', ''),
                entry.get('first_seen', ''),
                entry.get('last_seen', ''),
                entry.get('reference', ''),
                entry.get('reporter', ''),
                ', '.join(tags)  # Join tags with comma
            ]

            # Write the row to the CSV file
            writer.writerow(row)

    print("Data exported to threatfox_data.csv")
