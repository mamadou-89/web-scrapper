from flask import Flask,request, render_template
import requests
from bs4 import BeautifulSoup
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def hello_world():
    result=None
    if request.method == "POST":
        url = request.form.get("url")
        if url:
            try:
                response = requests.get(url)
                soup = BeautifulSoup(response.content, 'html.parser')
                result = soup.prettify()
            except Exception as e:
                result = f"Error fetching the URL: {e}"
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True, host="localhost")