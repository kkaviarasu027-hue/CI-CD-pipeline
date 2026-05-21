from flask import Flask, request
from plyer import notification

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def github_webhook():
    data = request.json

    print("GitHub Event Received:", data)

    # Extract useful info
    repo = data.get("repository", {}).get("name", "Unknown repo")
    pusher = data.get("pusher", {}).get("name", "Unknown user")
    ref = data.get("ref", "")

    message = f"{pusher} pushed changes to {repo}\nBranch: {ref}"

    notification.notify(
        title="GitHub Webhook Alert 🚀",
        message=message,
        timeout=5
    )

    return {"status": "ok"}

@app.route("/", methods=["GET"])
def home():
    return "Webhook server running"

if __name__ == "__main__":
    app.run(port=5000)