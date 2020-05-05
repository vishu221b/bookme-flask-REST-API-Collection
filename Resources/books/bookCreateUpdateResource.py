from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, get_jwt_identity
from Constants import REQUEST_FIELDS_FOR_CREATE_UPDATE, MANDATORY_FIELDS_FOR_CREATION
from service.bookCreateUpdateService import BookCreateUpdateService
from Utils.BookUtils import validate_incoming_request_dto


class BookCreateUpdateResource(Resource):
    creation_parser = reqparse.RequestParser()
    for field in REQUEST_FIELDS_FOR_CREATE_UPDATE:
        creation_parser.add_argument(field)

    @jwt_required
    def post(self):
        request = BookCreateUpdateResource.creation_parser.parse_args()
        validate = validate_incoming_request_dto(request)
        if not validate:
            user = get_jwt_identity()
            response = BookCreateUpdateService.create_new_book(request, user['email'])
            return response
        return validate

    @jwt_required
    def get(self):
        response = BookCreateUpdateService.get_books_for_user(get_jwt_identity())
        return response

    @jwt_required
    def put(self, book_id):
        request = reqparse.RequestParser().parse_args()
        # Update book through service
        return

    @jwt_required
    def delete(self, book_id):
        user = get_jwt_identity()
        response = BookCreateUpdateService.delete_book(book_id, user['email'])
        return response