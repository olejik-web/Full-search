def need_function(json_response):
    json_envelope = \
        json_response['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['boundedBy']['Envelope']
    object_x1, object_y1 = [float(elem) for elem in json_envelope['lowerCorner'].split()]
    object_x2, object_y2 = [float(elem) for elem in json_envelope['upperCorner'].split()]
    object_width = object_x2 - object_x1
    object_height = object_y2 - object_y1
    return (object_width, object_height)