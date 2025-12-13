'''coderadi &bull; Handles all socket routes in the Project.'''

# ? IMPORTING LIBRARIES
from plugins import *
from plugins.models import *

# & HANDLE VALIDATION ROUTE
@socket.on('handle-validation')
def validate_handle(handle: str):
    # CHECK FOR LENGTH
    if (len(handle) <= 3):
        socket.emit('handle-validation', {
            'status': 403,
            'message': 'handles should be at least 4 characters long.'
        })

    # CHECK FOR STRUCTURE
    elif (" " in handle) or (handle.startswith(" ")) or (handle.endswith(" ")):
        socket.emit('handle-validation', {
            'status': 403,
            'message': 'handles can\'t contain whitespaces.'
        })

    # CHECK FOR AVAILABILITY
    elif (User.query.filter_by(username=handle).first()):
        socket.emit('handle-validation', {
            'status': 404,
            'message': 'handle isn\'t available.'
        })

    else:
        socket.emit('handle-validation', {
            'status': 200,
            'message': 'handle is available.'
        })