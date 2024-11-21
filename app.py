from flask import Flask, render_template
from scraper import scrape_headlines

app = Flask(__name__)

@app.route("/")
def home():
    headlines = scrape_headlines()
    print("Headlines Passed to Template:", headlines)  # Debugging: Check the data sent to the template
    return render_template("index.html", headlines=headlines)

if __name__ == "__main__":
    app.run(debug=True)
