from flask import request
from werkzeug.datastructures import FileStorage

from flask_restx import Resource, fields, Namespace
from models.content import ContentModel
from utilities.responses import http_response
from utilities.storage import upload
from utilities.validate import allowed_file
from config import VIDEO_CONTENT_BUCKET


api = Namespace('Content', description='upload & transencoding video endpoints')

parser = api.parser()
parser.add_argument('file', type=FileStorage, location='files')


# Getting the list of all videos and adding new video
'''
 @route    POST api/content
 @desc     Add video content from transencoding
 @access   Public
'''


@api.route('/api/content/file-upload')
class Content(Resource):

    @api.expect(parser)
    @api.doc(responses={201: 'Content Inserted'})
    def post(self):
        file = request.files['file']
        if file.filename == "":
            return http_response(422, {"status": "please use valid mp4 file"})

        if file and allowed_file(file.filename):
            upload(request.files['file'])
            content = {}
            content['content'] = file.filename
            content['bucket'] = VIDEO_CONTENT_BUCKET
            content['status'] = 'PENDING'
            ContentModel().insert(content)
        else:
            return http_response(422, {"status": "please use valid mp4 file"})
            
        return http_response(201, {"status": "video content record added"})


