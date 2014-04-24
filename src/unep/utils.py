# -*- coding: utf-8 -*-


def get_field(context, field, default):
    if hasattr(context, 'en_' + field) and getattr(context, 'en_' + field):
        return getattr(context, 'en_' + field)
    elif hasattr(context, 'es_' + field) and getattr(context, 'es_' + field):
        return getattr(context, 'es_' + field)
    elif hasattr(context, 'fr_' + field) and getattr(context, 'fr_' + field):
        return getattr(context, 'fr_' + field)
    else:
        return default
