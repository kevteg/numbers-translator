from rest_framework.views import APIView
from rest_framework.response import Response
from apps.translator.serializers.number_serializer import NumberSerializer
from apps.translator.utils.translate import number_to_english
from rest_framework.exceptions import ValidationError
from rest_framework import status


class NumberToEnglish(APIView):
    """
    View to "translate" a number to plain english.
    """

    @staticmethod
    def __process_number(data):
        """Validates the number field is present in the data and
        return a Response object with the number in text
        """
        response = {"status": "ok", "error_description": "", "num_in_english": None}
        serializer = NumberSerializer(data=data)
        status_code = status.HTTP_200_OK

        try:
            if serializer.is_valid(raise_exception=True):
                number = serializer.data["number"]
                num_in_english = number_to_english(number)
                response["num_in_english"] = num_in_english
        except ValidationError as err:
            response["status"] = "error"
            response["error_description"] = str(err)
            status_code = status.HTTP_400_BAD_REQUEST
        except Exception as err:
            response["status"] = "error"
            response["error_description"] = str(err)
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR

        return Response(response, status=status_code)

    def get(self, request):
        """Verify the number field is present in the data and
        return a Response object with the number in text
        """
        data = request.query_params
        return self.__process_number(data)

    def post(self, request):
        """Verify the number field is present in the data and
        return a Response object with the number in text
        """
        data = request.data
        return self.__process_number(data)
