from rest_framework import serializers
import re


class PersonSerializer(serializers.Serializer):
    person_number = serializers.CharField(max_length=50)
    password = serializers.CharField(max_length=128)

    def validate_password(self, value):
        errors = []
        print("i am running")
        if len(value) < 6:
            errors.append(serializers.ValidationError("حداقل 6 کاراکتر باشد").detail)
        if not re.search('[a-z]', value):
            errors.append(serializers.ValidationError("یک حرف کوچک انگلیسی داشته باشد").detail)
        if not re.search('[0-9]', value):
            errors.append(serializers.ValidationError("باید حداقل شامل یک عدد باشد").detail)
        if re.search('[آ-ی]', value):
            errors.append(serializers.ValidationError("نباید شامل حروف فارسی باشد").detail)
        if re.search('[۰-۹]', value):
            errors.append(serializers.ValidationError("نباید شامل اعداد فارسی باشد").detail)
        if errors:
            raise serializers.ValidationError(errors)
        return value
    
    def update(self, instance, validated_data):
        instance.person_number = validated_data.get('person_number', instance.person_number)
        instance.password = validated_data.get('password', instance.password)
        instance.save()
        return instance