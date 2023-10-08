from pathlib import Path
import time

from azure.cognitiveservices.vision.contentmoderator import ContentModeratorClient
import azure.cognitiveservices.vision.contentmoderator.models
from msrest.authentication import CognitiveServicesCredentials

def evaluate(photo):
	endpoint = "https://timomiessen.cognitiveservices.azure.com/"
	subscription_key = "f2d16aa2ba35400a9cfbaf3d6d12e9e9"

	client = ContentModeratorClient(
		endpoint=endpoint,
		credentials=CognitiveServicesCredentials(subscription_key)
	)

	evaluation = client.image_moderation.evaluate_file_input(
	  media_type="image/png",
	  cache_image=True,
	  image_stream = open(photo , 'rb')
	)
	
	ms_result = evaluation.as_dict()
	result = dict()
	result["adult"] = ms_result["adult_classification_score"]
	result["racy"] = ms_result["racy_classification_score"]
	
	return result

def evaluate_directory(dir):
    pathlist = Path(dir).glob('*.jpg')
    
    all_results = dict()
    for path in pathlist:
        all_results[path] = evaluate(path)
        time.sleep(1)
        
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
