from pathlib import Path

def detect_safe_search(path):
    """Detects unsafe features in the file."""
    from google.cloud import vision

    client = vision.ImageAnnotatorClient()

    with open(path, "rb") as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.safe_search_detection(image=image)
    safe = response.safe_search_annotation

    # Names of likelihood from google.cloud.vision.enums
    likelihood_name = (
        "UNKNOWN",
        "VERY_UNLIKELY",
        "UNLIKELY",
        "POSSIBLE",
        "LIKELY",
        "VERY_LIKELY",
    )

    result = dict()
	
    result["adult"] = likelihood_name[safe.adult]
    result["medical"] = likelihood_name[safe.medical]
    result["spoof"] = likelihood_name[safe.spoof]
    result["violence"] = likelihood_name[safe.violence]
    result["racy"] = likelihood_name[safe.racy]
        
    return result

def evaluate_directory(dir):
    pathlist = Path(dir).glob('*.jpg')
    
    all_results = dict()
    for path in pathlist:
        all_results[path] = detect_safe_search(path)
        
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

