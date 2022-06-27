#  Document Classification Application

### An application that uses a Convolutional Neural Network(CNN) to classify an image as passport or ID card

#### By **Joy Machuka**

+ [Description](#Description)
+ [How to run the code](#Setup)
+ [Live Site](#Live-Site)
+ [Technologies](#Technologies-and-Languages-Used)
+ [Authors Info](#Author)
+ [Licence](#Licence)

# Description
This is a Django application that deploys a machhine learning model and utilizes the model in prediction within the application.

## Live-Site
[View Site](https://doc-classified.herokuapp.com/)

## Setup

To get the project .......  
  
##### Fork then Clone the repository:  
 ```bash 
git clone https://github.com/MachukaJoy/document-classification.git 
```
##### Navigate into the folder
 ```bash 
cd document-classification
```
##### Create and activate virtual environment  
 ```bash 
pipenv –-three
```
##### Activate Virtual Environment
 ```bash 
pipenv shell 
```  
##### Install Dependencies  
 ```bash 
 pipenv  install -r requirements.txt 
```  
 ##### Setup Database  
  SetUp your database User,Password, Host then make migrate  
 ```bash 
python manage.py makemigrations classifierApp
 ``` 
 Now Migrate  
 ```bash 
 python manage.py migrate 
```
##### Run the application  
 ```bash 
 python manage.py runserver 
``` 
##### Testing the application  
 ```bash 
 python manage.py test classifierApp
```
Open the application on your browser `127.0.0.1:8000`.


## Known Bugs
There are not any known bugs as at now. But feel free to let us know should you find any.

## Technologies-and-Languages-Used
* Python
* Visualstudio
* Django
* postgress sql
* colab

## Support and contact details
Should you have any issues or questions, ideas or concerns feel free to reach out to me. Also feel free to make contribution to the code and can contact me at machukajoy@gmail.com
## Author

- [Joy Machuka](https://github.com/MachukaJoy)
### Licence
[MIT LICENSE](https://github.com/MachukaJoy/document-classification/blob/main/LICENSE)<br>


** <br>
Copyright (c) {2022} [Joy Machuka ](https://github.com/MachukaJoy)