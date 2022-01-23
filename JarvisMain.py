import requests
from jproperties import Properties

configs = Properties()
with open('config.properties', 'rb') as read_prop:
    configs.load(read_prop)
    
prop_view = configs.items()

for item in prop_view:
    print(item)

print("API Endpoint:",configs.get("API_ENDPOINT").data)

userName = configs.get("USERNAME").data

API_ENDPOINT = "https://pixe.la/v1"
userEndPoint = "/users"
updateEndPoint = "/graphs"
userPayLoad= {"token":"thisissecretcodeForA","username":"abhijeetpnwr1sdasdasd","agreeTermsOfService":"yes","notMinor":"yes","thanksCode":"ThisIsThanksCode"}
graphDefinitionData = {"id":"abhijeet1","name":"codegraph","unit":"TimeSpent","type":"int","color":"shibafu"}

tokenHeader = {'X-USER-TOKEN': "thisissecretcodeForA"}

print(userPayLoad)

def createUser():
    print("I should create a new user in pixela")
    # sending post request and saving response as response object
    responseText = requests.post(url = API_ENDPOINT+userEndPoint, json = userPayLoad)
    # extracting response text 
    returnedResult = responseText.text
    if(returnedResult.__contains__("already exist")):
        print("User already exists in Pixela.")
        return
    print("The pastebin URL is:%s"%returnedResult)

def graphAppDefinition():
    print("I should define basic graph definition")     
    responseText = requests.post(url = API_ENDPOINT+userEndPoint+"/"+userName+updateEndPoint ,headers=tokenHeader, json = graphDefinitionData)
    returnedResult = responseText.text
    print("Result is:%s"%returnedResult)

def postToTheGraph(date,quantity):
    userPayLoad = {"date":date,"quantity":quantity}
    responseText = requests.post(url=API_ENDPOINT+userEndPoint+"/"+userName+"/graphs/"+"abhijeet1",headers=tokenHeader,json=userPayLoad)
    returnedResult = responseText.text
    print("Result is:%s"%returnedResult)

#lets create user for tracking habits
#createUser()

#Graph terms
#graphAppDefinition()

postToTheGraph("20220123","5")
