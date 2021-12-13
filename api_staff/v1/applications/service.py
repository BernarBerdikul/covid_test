from covidtest.core.models import TestApplication
from covidtest.utils.exceptions import NotFoundException


def get_application_or_404(pk: int):
    application = (
        TestApplication.objects.filter(pk=pk).select_related("schedule").first()
    )
    if not application:
        raise NotFoundException(detail={"notGiven": "Нет такого объекта"})
    return application
