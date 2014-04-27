# -*- coding: utf-8 -*-


def get_language(request, default='en'):
    language = default
    if "unep-language" in request.cookies:
        language = request.cookies['unep-language']
    if language not in ['en', 'fr', 'es']:
        language = default
    return language


def get_translated(context, request, field_name, fallback=False,
                   language='en'):
    language = get_language(request, language)
    field = getattr(context, language + '_' + field_name)
    if fallback and not field:
        field = get_field(context, field_name, '')
    if field:
        if hasattr(field, 'output'):
            return field.output
        return field


def get_fieldname(context, field_name):
    if hasattr(context, 'en_' + field_name) and\
            getattr(context, 'en_' + field_name):
        return 'en_' + field_name
    elif hasattr(context, 'es_' + field_name) and\
            getattr(context, 'es_' + field_name):
        return 'es_' + field_name
    elif hasattr(context, 'fr_' + field_name) and\
            getattr(context, 'fr_' + field_name):
        return 'fr_' + field_name


def get_field(context, field_name, default):
    field_name = get_fieldname(context, field_name)
    if field_name:
        return getattr(context, field_name)
    return default
