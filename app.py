from flask import Flask, render_template, request

app = Flask(__name__)

# 1. Definimos las opciones de permisos para cada Puesto
PERMISOS = {
    'Gerente': {'Leer', 'crear', 'editar', 'eliminar'},
    'Encargado': {'Leer', 'crear', 'editar'},
    'Empleado': {'Leer'},
        # El Empleado SOLO tiene acceso a 'Leer'
}


@app.route('/')
def index():
  return render_template('index.html')


@app.route('/pagina', methods=['POST'])
def pagina():
  usuario = request.form.get('usuario')
  Puesto = request.form.get('Puesto')
  accion = request.form.get('accion')
  activo = request.form.get('activo') == 'si'

  # Obtenemos los permisos del rol seleccionado
  permisos_del_Puesto = PERMISOS.get(Puesto, set())

  # CONDICIÓN 1: Verificamos si la acción está dentro de sus permisos
  tiene_permiso = accion in permisos_del_Puesto

  # CONDICIÓN 2: Validamos con lógica proposicional (Tiene permiso AND está activo)
  if tiene_permiso and activo:
    return render_template('pagina.html')
  else:
    # Si eligió Empleado y seleccionó crear, editar o eliminar -> entra aquí
    return f"<h3>Permiso no autorizado</h3><p>El Puesto {Puesto} no tiene autorización para la acción de '{accion}'.</p><br><a href='/'>← Volver</a>"


if __name__ == '__main__':
  app.run(debug=True)