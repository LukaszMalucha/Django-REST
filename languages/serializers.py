from rest_framework import serializers
from .models import Language


class LanguageSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="languages:language-detail")
    class Meta:
        model = Language
        fields = ('id', 'name', 'paradigm', 'url')
