# coding: utf-8
from flask import Blueprint, jsonify, make_response, request
from flask_httpauth import HTTPTokenAuth
from banco import Banco

auth = HTTPTokenAuth(scheme="Bearer")


@auth.verify_token
def verify_token(token):
    if token == "123":
        return True
    return False


bp_api = Blueprint("api", __name__, url_prefix="/jogos/api/v1/lista")
banco = Banco()

lista = []


@bp_api.route("/", methods=["GET"])
@bp_api.route("/<int:id>", methods=["GET"])
@auth.login_required
def get_games(id=None):
    lista = banco.listJogos()
    if lista != False:
        if id != None:
            lista = banco.getJogo(id)
            return jsonify({"lista": lista})
        return jsonify({"lista": lista})

    return make_response(jsonify({"Sucess": "Nenhum dado encontrado!"}), 200)


@bp_api.route("/add/", methods=["POST"])
@auth.login_required
def add_games():
    if request.json:
        banco.saveJogo(request.json[0])
    return make_response(jsonify({"Sucess": "Dados inseridos com sucesso!"}), 200)


@bp_api.route("/alter/<int:id>", methods=["PUT"])
@auth.login_required
def put_games(id=None):
    if request.json and id != None:
        banco.updateJogo(id, request.json[0])
    return make_response(jsonify({"Sucess": "Dados alterado com sucesso!"}), 200)


@bp_api.route("/del/<id>", methods=["DELETE"])
@auth.login_required
def del_games(id=None):
    if id != None:
        banco.deleteJogo(id)
    return make_response(
        jsonify({"Sucess": "O item ({}) foi excluido com sucesso!".format(id)}), 200
    )
