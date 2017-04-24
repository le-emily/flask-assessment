from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from jinja2 import StrictUndefined

app = Flask(__name__)
app.jinja_env.undefined = StrictUndefined
app.jinja_env.auto_reload = True

# Required to use Flask sessions and the debug toolbar
app.secret_key = "helloThisIsASecret"


@app.route("/")
def show_homepage():
    """Show the homepage."""

    return render_template("index.html")


@app.route("/application-form")
def application_form():
    """Show application form."""

    positions = ["Software Engineer", "QA Engineer", "Product Manager"]

    return render_template("application-form.html", positions=positions)


@app.route("/application-success", methods=["POST"])
def process_application():
    """Process application and return response sentence."""

    first_name = request.form.get("first")
    last_name = request.form.get("last")
    salary = request.form.get("salary_required")
    position = request.form.get("position")

    salary = "${amount:,.2f}".format(amount=float(salary))

    return render_template("application-response.html", first_name=first_name,
                           last_name=last_name, salary=salary, position=position)


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")

