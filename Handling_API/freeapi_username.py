import requests

def fectch_random_user():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    data_obj = response.json()
    
    if data_obj["success"] and "data" in data_obj:
        user_data = data_obj["data"]
        username = user_data["login"]["username"]
        country = user_data["location"]["country"]
        return username,country
    
    else:
        raise Exception("Failed to fatch user data")
    
    
def main():
    try:
        username,country = fectch_random_user()
        print(f"username: {username} \ncountry: {country}")
    except Exception as e:
        print(str(e))
        
        
if __name__ == "__main__":
    main()
    
    