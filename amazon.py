import boto3

from pathlib import Path

def detect_labels_local_file(photo):
    client=boto3.client('rekognition')
   
    with open(photo, 'rb') as image:
        response = client.detect_moderation_labels(Image={'Bytes': image.read()},MinConfidence=0)
        
    result = dict()
    for label in response['ModerationLabels']:
        result[label['Name']] = str(label['Confidence'])

    return result

	
def evaluate_directory(dir):
    pathlist = Path(dir).glob('*.jpg')
    
    all_results = dict()
    for path in pathlist:
        all_results[path] = detect_labels_local_file(path)
        
    return all_results


def main():
	result = evaluate_directory("...")
	labels = set()
	for path in result.keys():
		for label in result[path].keys():
			labels.add(label)
	
	labels = sorted(list(labels))
	print("File",end='')
	for label in labels:
		print(f",{label}",end='')

	print("")
	for path in result.keys():
		print(f"{path}",end='')
		for label in labels:
			print(f",{result[path][label]}",end='')
		print("")
	
	
if __name__ == "__main__":
    main()

