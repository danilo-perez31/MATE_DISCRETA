from flask import Flask, render_template, request

app = Flask(__name__)

PERMISOS = {
    'Gerente': {'Leer', 'crear', 'editar', 'eliminar'},
    'Encargado': {'Leer', 'crear', 'editar'},
    'Empleado': {'Leer'},
       
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

  
  permisos_del_Puesto = PERMISOS.get(Puesto, set())

  
  tiene_permiso = accion in permisos_del_Puesto

 
  if tiene_permiso and activo:
    return render_template('pagina.html')
  else:
    
    return f"<h3>Permiso no autorizado</h3><p>El Puesto {Puesto} no tiene autorización para la acción de '{accion}'.</p><br><a href='/'>← Volver</a>"


if __name__ == '__main__':
  app.run(debug=True)