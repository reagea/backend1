
from email import message
from pickle import GET
from select import select
from flask import Flask,jsonify,request
from flask_mysqldb import MySQL
from config import config

app = Flask(__name__)

conexion = MySQL(app)

@app.route('/juego', methods=['GET'])
def agregar_usuarios():
    try:
        cursor=conexion.connection.cursor()
        sql="select id, nombre, contrasena FROM usuario"
        cursor.execute(sql) 
        datos=cursor.fetchall()
        users=[]
        for fila in datos:
            usuarios={'id':fila[0], 'nombre':fila[1], 'contrasena':fila[2]}
            users.append(usuarios)
        return jsonify({'users':users, 'mensaje': "listo"})
    except Exception as ex:
        return jsonify ({'mensaje':"Error"})


@app.route('/juego/<codigo>', methods=['GET'])
def leer_usuario(codigo):
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT id, nombre, contrasena FROM usuario WHERE id = '{0}'".format(codigo)
        cursor.execute(sql)
        datos = cursor.fetchone()
        if datos != None:
            usuarios = {'id': datos[0], 'nombre': datos[1], 'contrasena': datos[2]}
            return jsonify({'usuarios': usuarios, 'mensaje': "usuario encontrado"})
        else:
            return jsonify({'mensaje': "usuario no encontrado"})
    except Exception as ex:
        return jsonify({'mensaje': "error"})

@app.route('/juego', methods=['POST'])
def registrar_usuario():
    try:
        cursor = conexion.connection.cursor()
        sql="INSERT INTO usuario(id, nombre, contrasena) VALUES ('{0}', '{1}', '{2}')".format(request.json['id'], request.json['nombre'], request.json['contrasena'])
        cursor.execute(sql)
        conexion.connection.commit()
       # print(request.json)
        return jsonify({'mensaje': "usuario registrado"})
    except Exception as ex:
        return jsonify({'mensaje': "error"})

@app.route('/juego/<codigo>', methods=['PUT'])
def modificar_usuario(codigo):
    try:
        cursor = conexion.connection.cursor()
        sql="UPDATE usuario SET nombre = '{0}', contrasena = '{1}' WHERE id = '{2}'".format(request.json['nombre'], request.json['contrasena'], codigo)
        cursor.execute(sql)
        conexion.connection.commit()
       # print(request.json)
        return jsonify({'mensaje': "usuario modificado"})
    except Exception as ex:
        return jsonify({'mensaje': "error"})

@app.route('/juego/<codigo>', methods=['DELETE'])
def eliminar_usuario(codigo):
        try:
            cursor = conexion.connection.cursor()
            sql="DELETE FROM usuario WHERE id = '{0}'".format(codigo)
            cursor.execute(sql)
            conexion.connection.commit()
       # print(request.json)
            return jsonify({'mensaje': "usuario eliminado"})
        except Exception as ex:
            return jsonify({'mensaje': "error"})

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run()