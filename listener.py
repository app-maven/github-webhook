import os
import logging
from github_webhook import Webhook
from flask import Flask


app = Flask(__name__)  # Standard Flask app
# Defines '/postreceive' endpoint
webhook = Webhook(app)


@app.route("/")        # Standard Flask endpoint
def hello_world():
    return "-"


@webhook.hook("push")        # Defines a handler for the 'push' event
def on_push(data):
    logger = logging.getLogger("webhook")
    logger.info("[-] Got push with: %s" % (data))
    old_path = os.popen('pwd').read()
    logger.info("[-] Changing directory from: %s" % (old_path))
    os.chdir('/code')
    new_path = os.popen('pwd').read()
    logger.info("[-] Changed directory to: %s" % (new_path))
    git_pulled = os.popen("git pull").read()
    logger.info("[-] Performed `git pull`: %s" % (git_pulled))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
