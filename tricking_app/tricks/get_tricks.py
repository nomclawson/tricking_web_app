import requests


    

def parse_data():
    """
    data : [statusCode, flash, 
            {data : [classes, origins, tricks]}
                    {tricks: }
    """

    response = requests.get('http://club540.com/api/tricks')
    data = response.json()
    data = data["data"]["tricks"]
    
 


    for trick in data:
        name = trick["name"]
        description = trick["description"]
        print(description)
        canPerform = False
    
        # trick = Trick(name=name,description=description,canPerform=canPerform,trickClass=trickClass)
        # trick.save()




parse_data()