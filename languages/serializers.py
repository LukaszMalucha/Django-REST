from rest_framework import serializers
from .models import Language, Paradigm, Programmer


class ParadigmSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="languages:paradigm-detail")

    class Meta:
        model = Paradigm
        fields = ('id', 'name', 'url')


class LanguageSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="languages:language-detail")

    class Meta:
        model = Language
        fields = ('id', 'name', 'paradigm', 'url')


class ProgrammerSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="languages:programmer-detail")

    class Meta:
        model = Programmer
        fields = ('id', 'url', 'name', 'languages')
