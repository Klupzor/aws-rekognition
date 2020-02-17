import boto3
from config import *


def add_faces_to_collection(photo, collection_id):

    client = boto3.client('rekognition',
                          aws_access_key_id=access_key_id,
                          aws_secret_access_key=secret_access_key,
                          region_name=region)

    with open(photo, 'rb') as sourceImage:
        sourceBytes = sourceImage.read()

    response = client.index_faces(CollectionId=collection_id,
                                  Image={'Bytes': sourceBytes},
                                  ExternalImageId="hola.jpg",
                                  MaxFaces=1,
                                  QualityFilter="AUTO",
                                  DetectionAttributes=['ALL'])

    print('Results for ' + photo)
    print('Faces indexed:')
    for faceRecord in response['FaceRecords']:
        print('  Face ID: ' + faceRecord['Face']['FaceId'])
        print('  Location: {}'.format(faceRecord['Face']['BoundingBox']))

    print('Faces not indexed:')
    for unindexedFace in response['UnindexedFaces']:
        print(' Location: {}'.format(
            unindexedFace['FaceDetail']['BoundingBox']))
        print(' Reasons:')
        for reason in unindexedFace['Reasons']:
            print('   ' + reason)
    return len(response['FaceRecords'])


def main():
    collection_id = 'demo-collection'
    photo = addPhoto

    indexed_faces_count = add_faces_to_collection(photo, collection_id)
    print("Faces indexed count: " + str(indexed_faces_count))


if __name__ == "__main__":
    main()
