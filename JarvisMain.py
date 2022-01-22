import requests

userPayLoad= {"token":"thisissecretcodeForA","username":"abhijeetpnwr","agreeTermsOfService":"yes","notMinor":"yes","thanksCode":"ThisIsThanksCode"}

API_ENDPOINT = "https://pixe.la/v1"
userEndPoint = "/users"

print(userPayLoad)

def createUser(): 
    print("I should create a new user in pixela")
    # sending post request and saving response as response object
    responseText = requests.post(url = API_ENDPOINT+userEndPoint, json = userPayLoad)
    # extracting response text 
    pastebin_url = responseText.text
    print("The pastebin URL is:%s"%pastebin_url)

#lets create user for tracking habits
createUser()