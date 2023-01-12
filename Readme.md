<h1 align="center">Image management system</h1>

## API calls
All calls except calls to crate_user/ enpoint should be authorized using headers = {'Authorization': 'Bearer your token'}

To retrieve filtered images by field send the value of filtering 
in the payload.


### Create new User instance `crate_user/` 

Method: `GET`

```
curl -XGET
-H "Content-Type: application/json"
-H "Bearer <your_token>"
-d     "{'admin':True}"
"<hostname>/api/v1/crate_user"
```

Response:

```
{
    "Token": "179965567450641667934392721119362596563"
}
```


### Create new Image instance `images/`

Method: `POST`

```
curl -XPOST
-H "Content-Type: application/json"
-H "Bearer <your_token>"
-F     "{
         'image':image
         }"
"<hostname>/api/v1/images/"
```
Response:

```
{
    "message": "The Image instance has been created"
}
```



### Retrieve Images's instances `images/`

To retrieve filtered images by field send the value of filtering 
in the payload.

To retrieve all images do not pass any key as a payload

Method: `GET`

```
curl -XGET
-H "Content-Type: application/json"
-d {
    "name": "Alex" 
    }
"<hostname>/api/v1/images"
```

Response:

```
[
    {'id': 5,
     'image': '/media/test_2XLzhbS.jpg',
     'geolocation': None, 
     'date': None,
     'name': 'Alexander'
    }
]
```

