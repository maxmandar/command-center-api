import requests

def validate_token(token):
    print("validating token..")
    try:
        response = requests.get(
            "http://localhost:8444/api/authorizations/user-authorization/",
            headers={"Authorization": f"Bearer {token}"}
        )
        
        print("response:",response)

        if response.status_code == 200:
            return response.json(), True
        return None, False
    except Exception as e:
        print(f"Error validating token: {e}")
        return None, False
    

def check_user_role(user_authorizations, role):
    print("checking user role..")
    print("user_authorizations:",user_authorizations)
    try:
        # Loop through all authorizations for the user
        for authorization in user_authorizations:
            group_name = authorization.get("group_name", "")
            user_role = authorization.get("role", {}).get("name", "")
            if group_name == "COMMAND_CENTER_OPERATOR" and user_role == role:
                print("user has operator role")
                return True
        return False
    except Exception as e:
        print(f"Error checking user role: {e}")
        return False