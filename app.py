from flask import Flask, render_template, request, redirect, url_for
from database import init_db, add_visit, get_visit_count, add_message, get_messages

app = Flask(__name__)

# Initialize the database
init_db()

@app.route("/")
def index():
    # Record a visit
    add_visit()
    return render_template("landing.html")

@app.route("/guestbook")
def guestbook():
    # Retrieve current statistics and guestbook messages
    visit_count = get_visit_count()
    messages = get_messages()
    
    return render_template(
        "index.html",
        visit_count=visit_count,
        messages=messages,
        messages_count=len(messages)
    )

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form.get("name", "").strip()
    message = request.form.get("message", "").strip()
    
    if name and message:
        add_message(name, message)
        
    return redirect(url_for("guestbook"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
