
errors = {
    "InternalServerError": {
        "message": "Something went wrong",
        "status": 500
    },
     "SchemaValidationError": {
         "message": "Request is missing required fields",
         "status": 400
     },

     "UpdatingMovieError": {
         "message": "Update is not possible, record not found",
         "status": 404
     },
     "DeletingMovieError": {
         "message": "Deletion ",
         "status": 403
     },
     "MovieNotExistsError": {
         "message": "Record with given id doesn't exists",
         "status": 404
     },

     "UnauthorizedError": {
         "message": "Invalid username or password",
         "status": 401
     }
}