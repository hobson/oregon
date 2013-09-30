from django.core.serializers import serialize
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models.query import QuerySet
from django.template import Library
from django.utils import simplejson

register = Library()

#@register.filter(name='jsonify')
def jsonify(object):
    if isinstance(object, QuerySet):
        return serialize('json', object)
    return simplejson.dumps(object, cls=DjangoJSONEncoder)
jsonify.is_safe=True


register.filter('jsonify', jsonify)


