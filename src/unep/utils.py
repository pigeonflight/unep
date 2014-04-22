
def get_field(self, field, default):
    if hasattr(self, 'en_' + field):
        return getattr(self, 'en_' + field)
    elif hasattr(self, 'es_' + field):
        return getattr(self, 'es_' + field)
    elif hasattr(self, 'fr_' + field):
        return getattr(self, 'fr_' + field)
    else:
        return default
