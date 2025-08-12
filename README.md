# A Python (Flask) web app with PostgreSQL ~~in Azure~~
### Workshop for the BU Data Science Association, Fall 2025
## This was adapted from BU Data Science Association's Spring 2025 Workshop, which was adapted from Pamela Fox

This is a Python web app using the Flask framework and a Postgres database  
  
- It can be used as a playground for testing SQL queries  
  
## How to Use Locally
Preferably, this is used locally (not on GitHub Codespaces)

1. Download this project from GitHub and put it on your local computer.

2. On your local IDE, get a DevContainer running. On VSCode, a pop-up should appear if you have the right extensions downloaded. If not, go to the left-hand side and click on the "Remote Explorer." icon that looks like a computer monitor, and then start the DevContainer.

3. Open the terminal and run 'python3 -m flask run' to get Flask started.

4. Go to your browser and go to 'http://localhost:5000' to see the web app running. You may get a warning because the link is not https. 

5. You should be all set! Try modifying the SQL commands under the TODOs in app.py and notice how the results change. 

If you have issues, navigate to bottom of the screen and look at your ports. You may have ports set to private that need to be public.

## If using GitHub Codespaces:

1. Open the project on Codespaces.

2. Wait for SQLTools extension to load on the left navbar of VS Code  

3. Connect to the postgres database in the SQLTools menu (the cylinder) - if this does not work by default, the connection info is in the .env file   

4. There should be a container database tab from SQLTools, you can type in a query and press `Run on Active Connection` to see the result

5. Run `python3 -m flask run` to start the flask server

6.  Go to the `ports` tab in the VS Code console, and right click on port 5000. Change `port visibility` to public

7. Open the link to port 5000 and try out the flask app

- Note that Github Copilot is automatically installed and offers terrible suggestions. Gf this is a problem you can disable it in extensions  
