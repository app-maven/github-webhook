import os
from github_webhook import Webhook
from flask import Flask

app = Flask(__name__)  # Standard Flask app
# Defines '/postreceive' endpoint
webhook = Webhook(app, secret="AWeU4q9FpR03")


@app.route("/")        # Standard Flask endpoint
def hello_world():
    return "-"


@webhook.hook("push")        # Defines a handler for the 'push' event
def on_push(data):
    print("[-] Got push with: {0}".format(data))
    old_path = os.popen('pwd').read()
    print(f"[-] Changing directory from: {old_path}")
    os.chdir('/code')
    new_path = os.popen('pwd').read()
    print(f"[-] Changed directory to: {new_path}")
    git_pulled = os.popen("git pull").read()
    print(f"[-] Performed `git pull`: {git_pulled}")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
