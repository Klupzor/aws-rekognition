import boto3
from config import *

if __name__ == "__main__":

    collectionId = 'demo-collection'
    # photo = './images/faces.png'
    photo = comparePhoto
    threshold = 70
    maxFaces = 2

    client = boto3.client('rekognition',
                          aws_access_key_id=access_key_id,
                          aws_secret_access_key=secret_access_key,
                          region_name=region)
    with open(photo, 'rb') as sourceImage:
        sourceBytes = sourceImage.read()

    response = client.search_faces_by_image(CollectionId=collectionId,
                                            Image={'Bytes': sourceBytes},
                                            FaceMatchThreshold=threshold,
                                            MaxFaces=maxFaces)
    
    print("response: ")
    print(response)

    faceMatches = response['FaceMatches']
    print('Matching faces')
    for match in faceMatches:
        print('FaceId:' + match['Face']['FaceId'])
        print('Similarity: ' + "{:.2f}".format(match['Similarity']) + "%")
        print
