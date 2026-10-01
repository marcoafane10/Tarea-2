from app import app

CASOS = [
    ("/instruccion/Empaque/2?rol=edicion", "version obsoleta"),
    ("/instruccion/Empaque/3?rol=lectura", "vigente, solo lectura"),
    ("/instruccion/Empaque/3?rol=edicion", "vigente, edicion habilitada"),
    ("/instruccion/Empaque/3?rol=visitante", "rol no reconocido"),
    ("/instruccion/Empaque/9?rol=edicion", "version invalida"),
]

cliente = app.test_client()
for url, esperado in CASOS:
    datos = cliente.get(url).get_json()
    resultado = "OK  " if datos["estado"] == esperado else "FAIL"
    print(resultado, url, "->", datos["estado"])
