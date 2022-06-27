from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .models import Result
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import DocumentClassifySerializer

from keras.models import load_model
from keras.preprocessing import image
import json 
import tensorflow as tf
import numpy as np

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

img_height, img_width = 180, 180
with open('./models/labels.json', 'r') as f:
  labelInfo = f.read()

labelInfo = json.loads(labelInfo)
# print(labelInfo)

tf.compat.v1.disable_eager_execution()
model_graph = tf.Graph()
with model_graph.as_default():
    tf_session = tf.compat.v1.Session()

    with tf_session.as_default():
        model=load_model('./models/model.h5')


# Create your views here.
def index(request):
  context={'a':1}
  return render(request, 'index.html',context)

def predictImage(request):
    
    fileObj=request.FILES['filePath']
    fs=FileSystemStorage()
    filePathName=fs.save(fileObj.name,fileObj)
    filePathName=fs.url(filePathName)
    testimage='.'+filePathName
    img = image.load_img(testimage, target_size=(img_height, img_width))
    x = image.img_to_array(img)
    x=x/255
    x=x.reshape(1,img_height, img_width,3)
    with model_graph.as_default():
        with tf_session.as_default():
            predi=model.predict(x)

    import numpy as np
    predictedLabel=labelInfo[str(np.argmax(predi[0]))]

    context={'filePathName':filePathName,'predictedLabel':predictedLabel}
    return render(request,'index.html',context) 


def viewDataBase(request):
    import os
    listOfImages=os.listdir('./media/')
    listOfImagesPath=['./media/'+i for i in listOfImages]
    context={'listOfImagesPath':listOfImagesPath}
    return render(request,'viewDB.html',context) 