# -*- coding: utf-8 -*-


def get_translated(context, request, field_name, fallback=False,
                   default_lang='en'):
    if "unep-language" in request.cookies:
        field = getattr(
            context, request.cookies['unep-language'] + '_' + field_name)
    else:
        field = getattr(context, default_lang + '_' + field)
    if fallback and not field:
        field = get_field(context, field_name, '')
    if field:
        if hasattr(field, 'output'):
            return field.output
        return field


def get_field(context, field, default):
    if hasattr(context, 'en_' + field) and getattr(context, 'en_' + field):
        return getattr(context, 'en_' + field)
    elif hasattr(context, 'es_' + field) and getattr(context, 'es_' + field):
        return getattr(context, 'es_' + field)
    elif hasattr(context, 'fr_' + field) and getattr(context, 'fr_' + field):
        return getattr(context, 'fr_' + field)
    else:
        return default
