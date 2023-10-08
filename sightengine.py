import requests
import json

from pathlib import Path

def evaluate(filename):
        
	params = {
		'models': 'nudity-2.0',
		'api_user': '1745038482',
		'api_secret': 'pE5BrJDfSmma27kWYsFK'
	}
	files = {'media': open(filename, 'rb')}
	r = requests.post('https://api.sightengine.com/1.0/check.json', files=files, data=params)
	output = json.loads(r.text)

	result = dict()
	print(r)
	for attribute,value in output["nudity"].items():
		if attribute=="suggestive_classes":
			for a,v in value.items():               
				result[a] = v
		else:
			result[attribute] = value

	return result


def evaluate_directory(dir):
    pathlist = Path(dir).glob('*.jpg')
    
    all_results = dict()
    for path in pathlist:
        all_results[path] = evaluate(path)
        
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
