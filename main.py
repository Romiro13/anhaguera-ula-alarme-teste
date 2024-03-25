from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange

app = Flask(__name__)
app.config["SECRET_KEY"] = "ULA demo"


class AlarmeForm(FlaskForm):
    portaA = IntegerField(
        "Porta A:",
        validators=[DataRequired(), NumberRange(min=0, max=1, message="Invalid input")],
        default=0,
    )
    portaB = IntegerField(
        "Porta B:",
        validators=[DataRequired(), NumberRange(min=0, max=1, message="Invalid input")],
        default=0,
    )
    alarme = IntegerField(
        "Alarme:",
        validators=[DataRequired(), NumberRange(min=0, max=1, message="Invalid input")],
        default=0,
    )

    submit = SubmitField("Teste")


@app.route("/", methods=["GET", "POST"])
def index():
    portaA: bool = False
    portaB: bool = False
    alarme: bool = False
    result: bool = False
    form = AlarmeForm()

    # if form.validate_on_submit():
    portaA = bool(form.portaA.data)
    portaB = bool(form.portaB.data)
    alarme = bool(form.alarme.data)

    result = (portaA or portaB) and alarme

    print(form.portaA.data, form.portaB.data, form.alarme.data)
    print(portaA, portaB, alarme, result)

    return render_template(
        "index.html",
        portaA=portaA,
        portaB=portaB,
        alarme=alarme,
        result=result,
        form=form,
    )


@app.errorhandler(404)
def page_not_found(e):
    return render_template("error_handler.html", code=404)


@app.errorhandler(500)
def page_not_found(e):
    return render_template("error_handler.html", code=500)


if __name__ == "__main__":
    app.run(debug=True)
