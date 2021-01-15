@app.route("/")
def index():
    list = messages.get_list()
    return render_template("index.html", count=len(list), messages=list)
