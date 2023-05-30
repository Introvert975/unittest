from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def main():
    return render_template("Discriminant.html")


@app.route('/', methods=['post', 'get'])
def form():
    try:
        if request.method == 'POST':
            a = float(request.form.get('a'))
            b = float(request.form.get('b'))
            c = float(request.form.get('c'))
            D = b*b - (4*a*c)
            strD = f"D = {b}²-4·{a}·{c}"
            x1 = (-b + D ** 0.5) / (2*a)
            x2 = (-b - D ** 0.5) / (2 * a)
            if D < 0:
                x1 = round(x1.real, 5) + round(x1.imag, 5) * 1j
                x2 = round(x2.real, 5) + round(x2.imag, 5) * 1j
                D = D ** 0.5
                D = round(D.real, 5) + round(D.imag, 5) * 1j
            else:
                x1 = round(x1, 5)
                x2 = round(x2, 5)
                D = D ** 0.5
                D = round(D, 5)
        return render_template('Discriminant.html', ansD=f"√D={D}", x1=f"x₁={x1}", x2=f"x₂={x2}",STRD=strD, b=f"-({b})±{D}", a=f"2·{a}", X="x₁₂=")
    except:
        strr = "Введите корректные значения(2, 20, 3.53,...)"
        return render_template('Discriminant.html', STR=strr)

def run():
    app.run()