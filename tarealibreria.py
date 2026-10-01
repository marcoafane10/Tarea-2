from flask import Flask, jsonify, request

app = Flask(__name__)

# Version vigente publicada (valor de prueba).
# La ficha no fija un numero: confirmar con el Socio Formador.
VERSION_VIGENTE = 3

# Perfiles definidos en la ficha: solo lectura, y lectura + edicion
ROL_LECTURA = "lectura"
ROL_EDICION = "edicion"


@app.route("/instruccion/<titulo>/<int:versionDocumento>")
def evaluarInstruccion(titulo, versionDocumento):
    # El rol llega por query string: ?rol=lectura  o  ?rol=edicion
    rolUsuario = request.args.get("rol", ROL_LECTURA)

    if versionDocumento < 1 or versionDocumento > VERSION_VIGENTE:
        # La version no existe en el historial de versiones
        estado = "version invalida"
    elif versionDocumento < VERSION_VIGENTE:
        # Version anterior: queda en el historial, no se edita
        estado = "version obsoleta"
    elif rolUsuario == ROL_LECTURA:
        estado = "vigente, solo lectura"
    elif rolUsuario == ROL_EDICION:
        estado = "vigente, edicion habilitada"
    else:
        # Caso por defecto: rol que la ficha no define
        estado = "rol no reconocido"

    return jsonify({
        "instruccion": titulo,
        "version": versionDocumento,
        "rol": rolUsuario,
        "estado": estado,
    })


if __name__ == "__main__":
    app.run(debug=True)
