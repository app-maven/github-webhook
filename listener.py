import os
import logging
import glob
import json
from github_webhook import Webhook
from flask import Flask


app = Flask(__name__)  # Standard Flask app
# Defines '/postreceive' endpoint
webhook = Webhook(app)


@webhook.hook("push")        # Defines a handler for the 'push' event
def on_push(data):
    logger = logging.getLogger("webhook")
    logger.info("[-] Received PUSH event")
    for filepath in glob.iglob('./scripts/*.py'):
        output = os.system(f"python {filepath} {data}").read()
        logger.info("[-] Output: %s" % (output))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
