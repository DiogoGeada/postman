import os
import azure.functions as func
import datetime
import json
import logging

app = func.FunctionApp()

@app.route(route="ingredients/{id?}", auth_level=func.AuthLevel.ANONYMOUS, methods=["get"])
def GetIngredients(req: func.HttpRequest) -> func.HttpResponse:
    file = open("./ingredients.json")
    data = json.loads(file.read())
    resp_body = data

    id = req.route_params.get("id")
    if id != None:
        if id.isnumeric() == False:
            return func.HttpResponse(
                f"The provided id '{id}', is not an integer.",
                status_code=400,
                mimetype="application/json"
            )
        id = int(id)
        resp_body = {}
        for ingredient in data:
            logging.info(f"{ingredient['id']} == {id} ({ingredient['id'] == id})")
            if ingredient["id"] == id:
                resp_body = ingredient
 
    if resp_body == {}:
        return func.HttpResponse(
            "Ingredient not found",
            status_code=404,
            mimetype="application/json"
        )
    return func.HttpResponse(
        json.dumps(resp_body),
        status_code=200,
        mimetype="application/json"
    )

@app.route(route="potions/{id?}", auth_level=func.AuthLevel.ANONYMOUS, methods=["get"])
def GetPotions(req: func.HttpRequest) -> func.HttpResponse:
    
    potion_file = open("./potions.json")
    potions = json.loads(potion_file.read())

    resp_body = potions

    id = req.route_params.get("id")
    if id != None:
        if id.isnumeric() == False:
            return func.HttpResponse(
                f"The provided id '{id}', is not an integer.",
                status_code=400,
                mimetype="application/json"
            )
        id = int(id)
        resp_body = {}
        for potion in potions:
            if potion["id"] == id:
                resp_body = potion
 
    if resp_body == {}:
        return func.HttpResponse(
            "Potion not found",
            status_code=404,
            mimetype="application/json"
        )

    return func.HttpResponse(
        json.dumps(resp_body),
        status_code=200,
        mimetype="application/json"
    )

    
    file = open("./potions.json")
    data = json.loads(file.read())
    ingredients = req.get_json()

    id = req.route_params.get("id")
    if id != None:
        if id.isnumeric() == False:
            return func.HttpResponse(
                f"The provided id '{id}', is not an integer.",
                status_code=400,
                mimetype="application/json"
            )
        id = int(id)
        resp_body = {}
        for potion in data:
            if potion["id"] == id:
                resp_body = potion
 
    if resp_body == {}:
        return func.HttpResponse(
            "Potion not found",
            status_code=404,
            mimetype="application/json"
        )
    return func.HttpResponse(
        json.dumps(resp_body),
        status_code=200,
        mimetype="application/json"
    )