from flask import Flask, render_template
app=Flask(__name__)

@app.route("/")
def home():
    return render_template("checkerboard_practice.html")

@app.route("/<int:num>")
def checkerboard_rows(num):
    return render_template("checkerboard_practice.html", num=num)

@app.route("/<int:row>/<int:col>")
def checkerboard_row_col(row,col):
    return render_template("checkerboard_row_col.html", row=row, col=col)

@app.route("/<int:row>/<int:col>/<string:color1>/<string:color2>")
def checkerboard_row_col_colors(row,col,color1,color2):
    return render_template("checkerboard_row_col.html", row=row, col=col, color1=color1, color2=color2)

if __name__ == "__main__":
    app.run(debug=True, port=5001)