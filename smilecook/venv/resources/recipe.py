from flask import request
from flask_restful import Resource
from http import HTTPStatus
from models.recipe import Recipe, recipe_list


class RecipeListResource(Resource):

    def get(self):

        data = []

        for recipe in recipe_list:
            if recipe.is_publish is True:
                data.append(recipe.data)

        return {'data': data}, HTTPStatus.OK

    def post(self):
        data = request.get_json()
        recipe = Recipe(name=data['name'],
                        description=data['description'],
                        num_of_servings=data['num_of_servings'],
                        cook_time=data['cook_time'],
                        directions=data['directions'])

        recipe_list.append(recipe)

        return recipe.data, HTTPStatus.CREATED


class RecipeResource(Resource):

    def get(self, recipe_id):
        recipe = next((recipe for recipe in recipe_list if recipe_id == recipe_id and
                       recipe.is_publish == True), None)

        if recipe is None:
            return {'message': 'recipe not found'}, HTTPStatus.NOT_FOUND

        return recipe.data, HTTPStatus.OK
