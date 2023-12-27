class CantGetCoordinates(Exception):
    """Program can't request GPS coordinates"""
    pass

class ApiServiceError(Exception):
    """Error with api service"""
    pass
