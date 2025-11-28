# Crowd Funding Backend

### A link to the deployed project.
[Crowd Funding Backend](https://bridget-crowdfunding-29f799e098ab.herokuapp.com)
### A screenshot of Insomnia, demonstrating a successful GET method for any endpoint.
![insomnia_get_users.png](insomnia_get_users.png)
### A screenshot of Insomnia, demonstrating a successful POST method for any endpoint.
![insomnia_register_user.png](insomnia_register_user.png)
### A screenshot of Insomnia, demonstrating a token being returned.
![insomnia_get_token.png](insomnia_get_token.png)
### Step-by-step instructions for how to register a new user and create a new fundraiser (i.e., endpoints and body data).
* Open Insomnia app
* Create a **POST** request to https://bridget-crowdfunding-29f799e098ab.herokuapp.com/users/
* Switch to the **Body** tab and add a JSON object with the new user's info, like:
    ```json
    {
      "name": "John Smith",
      "username":"johnsmith",
      "email": "john.smith@email.com",
      "password": "A02w94d@k%"
    }
    ```
* Click on the **Send** button to register a new user.
    ![insomnia_register_user.png](insomnia_register_user.png)
* Create a **POST** request to https://bridget-crowdfunding-29f799e098ab.herokuapp.com/api-token-auth/
* Switch to the **Body** tab and add a JSON object with the new user's credential, like:
    ```json
    {
      "username":"johnsmith",
      "password": "A02w94d@k%"
    }
    ```
* Click on the **Send** button to get the new user's token. Take note of the **token** returned. (In this example, the token is **89f3dfb0c4f9cf587153636c70edafea47d1e5c7**)
    ![insomnia_get_token.png](insomnia_get_token.png)
* Create a **POST** request to https://bridget-crowdfunding-29f799e098ab.herokuapp.com/fundraisers/
* Switch to the **Body** tab and add a JSON object with the new fundraiser's info, like:
    ```json
    {
	  "title": "Fundraiser One",
	  "description": "The first fundraiser.",
	  "goal": 150,
	  "image": "https://via.placeholder.com/300.jpg",
	  "is_open": true
    }
    ```
    ![insomnia_create_fundraiser_body.png](insomnia_create_fundraiser_body.png)
* Switch to the **Auth** tab and add a **Bearer Token**.
  * The token value should be the one you got from the previous step. (In this example, the token value is **89f3dfb0c4f9cf587153636c70edafea47d1e5c7**)
  * The prefix is **Token**.
    ![insomnia_create_fundraiser_auth.png](insomnia_create_fundraiser_auth.png)
* Click on the **Send** button to create a new fundraiser.
    ![insomnia_create_fundraiser_response.png](insomnia_create_fundraiser_response.png)
### Your refined API specification and Database Schema.
* API specification in Swagger format is [here](https://bridget-crowdfunding-29f799e098ab.herokuapp.com/swagger/)
* Database Schema
  * User Table
  
    ![db_scheme_customuser.png](db_scheme_customuser.png)
  
  * Fundraiser Table
  
    ![db_scheme_fundraiser.png](db_scheme_fundraiser.png)
  
  * Pledge Table
  
    ![db_scheme_pledge.png](db_scheme_pledge.png)