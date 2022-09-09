from rest_framework import generics
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer

from .models import Data
from .serializers import DataSerializer

class TemplateHTMLRendererImplementation(TemplateHTMLRenderer):
    """Workaround class for issue: https://github.com/encode/django-rest-framework/issues/5236"""

    def get_template_context(self, data, renderer_context):
        response = renderer_context['response']
        if response.exception:
            data['status_code'] = response.status_code
        return {'data': data}

class DataList(generics.ListAPIView):
    queryset = Data.objects.all()
    serializer_class = DataSerializer
    renderer_classes = [TemplateHTMLRendererImplementation, JSONRenderer]
    template_name = 'custom_renderer/data_list.html'

