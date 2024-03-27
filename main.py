from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import IntegerField, SelectField, SubmitField
from wtforms.validators import DataRequired, NumberRange

app = Flask(__name__)
app.config["SECRET_KEY"] = "ULA demo"


class AlarmeForm(FlaskForm):
    portaA = IntegerField(
        "A:",
        validators=[DataRequired(), NumberRange(min=0, max=1, message="Invalid input")],
        default=0,
    )
    portaB = IntegerField(
        "B:",
        validators=[DataRequired(), NumberRange(min=0, max=1, message="Invalid input")],
        default=0,
    )
    alarme = IntegerField(
        "Alarme:",
        validators=[DataRequired(), NumberRange(min=0, max=1, message="Invalid input")],
        default=0,
    )

    logicA = SelectField(
        "Porta lógica: ",
        choices=["", "OR", "AND", "NAND", "NOT", "NOR"],
        validate_choice=DataRequired(),
    )

    logicB = SelectField(
        "Porta lógica Alarme: ",
        choices=["", "OR", "AND", "NAND", "NOT", "NOR"],
        validate_choice=DataRequired(),
    )

    submit = SubmitField("Teste")


@app.route("/", methods=["GET", "POST"])
def index():
    portaA: bool = False
    portaB: bool = False
    alarme: bool = False
    result: bool = False
    logicA: str = None
    form = AlarmeForm()

    # if form.validate_on_submit():
    portaA = bool(form.portaA.data)
    portaB = bool(form.portaB.data)
    alarme = bool(form.alarme.data)
    logicA = form.logicA.data
    logicB = form.logicB.data

    print(logicA, logicB)

    if logicA == "OR":
        result = portaA or portaB
    elif logicB == "AND":
        result = portaA and portaB

    print(result)

    if logicB == "AND":
        result = result and alarme
    else:
        result = False

    print(result)

    print(
        form.portaA.data,
        form.logicA.data,
        form.portaB.data,
        form.logicB.data,
        form.alarme.data,
    )

    return render_template(
        "index.html",
        portaA=portaA,
        portaB=portaB,
        alarme=alarme,
        logicA=logicA,
        logicB=logicB,
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
