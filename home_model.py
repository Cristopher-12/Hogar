import requests

# This function will pass your text to the machine learning model
# and return the top result with the highest confidence
def classify(text):
    key = "dd1fb1a0-a18b-11eb-9d21-0188bc1272ec3c0a7a03-be22-45fe-8d89-65d66b2fc6ae"
    url = "https://machinelearningforkids.co.uk/api/scratch/"+ key + "/classify"

    response = requests.get(url, params={ "data" : text })

    if response.ok:
        responseData = response.json()
        topMatch = responseData[0]
        return topMatch
    else:
        response.raise_for_status()


# CHANGE THIS to something you want your machine learning model to classify
for i in range(4):
    texto = input("Coloca aqui tu palabra")
    demo = classify(texto)

    label = demo["class_name"]
    confidence = demo["confidence"]


# CHANGE THIS to do something different with the result
print ("result: '%s' with %d%% confidence" % (label, confidence))