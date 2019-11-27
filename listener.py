import os
from github_webhook import Webhook
from flask import Flask

app = Flask(__name__)  # Standard Flask app
webhook = Webhook(app) # Defines '/postreceive' endpoint

@app.route("/")        # Standard Flask endpoint
def hello_world():
    return "Hello, World!"

@webhook.hook()        # Defines a handler for the 'push' event
def on_push(data):
    print("[-] Got push with: {0}".format(data))
    old_path = os.system("pwd")
    print(f"[-] Changing directory from {old_path}")
    os.system("cd ./code/")
    new_path = os.system("pwd")
    print(f"[-] Changed directory to {new_path}")
    os.system("git pull")
    print("[-] Performed `git pull`")
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)