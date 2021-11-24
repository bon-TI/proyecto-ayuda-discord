from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    data={
        'titulo':'Ayuda Escolar de Discord'
    }
    return render_template('index.html',data=data)

@app.route('/descargas')
def descargas():
    data= {
        'titulo':'Ayuda Escolar de Discord | Descargas'
    }
    return render_template('download-page.html', data=data)

@app.route('/contacto')
def contacto():
    data= {
        'titulo':'Ayuda Escolar de Discord | Contacto'
    }
    return render_template('contact-page.html', data=data)

@app.route('/docs')
def docs():
    data= {
        'titulo':'Ayuda Escolar de Discord | Docs'
    }
    return render_template('docs-page.html', data=data)

if __name__=='__main__':
    app.run(debug=True, port=5000)


# Activar el entorno virtual
# .\env\Scripts\activate 