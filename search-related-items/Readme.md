## Prerequisites

- Node package manager (npm).

> 📘 Note
> 
> You can download npm [here](https://nodejs.org/en/download).

## Nomad SDK NPM

To learn how to download and setup the nomad sdk npm, go to [Nomad SDK NPM](https://github.com/Nomad-Media/nomad-sdk/tree/main/nomad-sdk-npm).

## Setup

To run the Node application, follow these steps:
```
npm install
npm start
```

Then open a webpage and go to localhost:4200.

## Nomad SDK Files

In the nomad-sdk/js directory there are two versions of the Nomad SDK. There is the sdk.min.js file which is a minified version of the sdk, and the sdk-debug.js file which is a concatenated version of the sdk. The sdk-debug file will show you all the parameter documentation and readable code.

## Search

The `relatedItems` list in the search output is a flat list of related records. This is populated when children searchResultFields values are specified in the searchResultFields searching attribute. Note that all records in this list are flattened, regardless of the hierarchy structure specified and records are not duplicated more than once.

Here is an example where the content definition is `Hero`

```python
nomad_sdk = Nomad_SDK(config)

search_results = nomad_sdk.search(None, None, None, 
        [  
            {
                "fieldName": "contentDefinitionId",  
                "operator": "Equals",  
                "values": "eb710e28-7c44-492e-91f9-8acd0cd9331c"  
            },  
            {  
                "fieldName": "languageId",  
                "operator": "Equals",  
                "values": "c66131cd-27fc-4f83-9b89-b57575ac0ed8"  
            }  
        ], None, 
        [  
            {  
                "name": "contentDefinitionId"  
            },  
            {  
                "name": "contentDefinitionTitle"  
            },  
            {  
                "name": "plot"  
            },  
            {  
                "name": "releaseDate"  
            },  
            {  
                "name": "genre"  
            },  
            {  
                "name": "image",  
                "SearchResultFields": [  
                    {  
                        "name": "fullUrl"  
                    }  
                ]  
            },  
      	    {  
                "name": "movieFile",  
                "SearchResultFields": [  
                    {  
                        "name": "fullUrl"  
                    }  
                ]  
            }  
        ])

# Loop through items and display each title
print("items:")
for item in search_results['items']:
    print(item['id'] + " - " + item['title'])

# Loop through related items and display each title
print("related items:")
for item in search_results['relatedItems']:
    print(item['id'] + " - " + item['title'] + " - " + item['identifiers'].get('tipperId', 'None'))
```

## Sample Result
```
2025-12-12 14:05:10,484 - Start search
2025-12-12 14:05:10,731 - Search complete
items:
08266775-42b0-42f4-a0b1-203b2d9a8b46 - 1488 Test
328658c6-f2d3-4147-bea9-e5015c375b62 - Date Test New
df959df8-1059-4301-965a-6793a95eb70d - Godzilla vs. Kong (2021)
c8e8d88d-dfa2-4241-be0e-c85c9dcdd9bf - Harry Potter and the Order of the Phoenix
88237f71-c811-4b46-a098-23604fe10980 - New
62763dd0-c813-46d2-a6b7-2eb0db70eaeb - New 1
c510154c-a7ba-4e03-8f47-b8fe95b5781b - New 2
40a30a8b-7cc1-4423-bdb8-323bd3deb589 - New Movie Date
076d8330-edb5-42ae-abfb-058fc23d250a - Spider-Man 3
9c7629fb-9acd-4d31-8dba-1b90ad10da0c - Wonder Woman 1984
related items:
7dc4e78f-5583-4fc0-a6a8-5a7abb7564a5 - The-Office.jpeg - None
df62ca06-8576-42bf-861d-89ada516fa06 - Tom_And_Jerry_-_Baby_Butch_Part_1-590053.mp4 - None
```


> 📘 Note
> 
> For more information about the API call used go to [Search](https://developer.nomad-cms.com/docs/search-api)