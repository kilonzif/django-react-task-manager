# import serializers from the REST framework
from rest_framework import serializers

# import the taski data model
from .models import Taski

# create a serializer class
class TaskiSerializer(serializers.ModelSerializer):

	# create a meta class
	class Meta:
		model = Taski
		fields = ('id', 'title','description','completed')
