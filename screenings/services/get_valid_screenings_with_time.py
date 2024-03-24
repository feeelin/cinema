from dataclasses import dataclass
from screenings.models import Screening
from django.utils import timezone


@dataclass
class ScreeningsWithTime:
    screenings: list[Screening]
    screenings_time: list[str]


def get_valid_screenings_with_time() -> ScreeningsWithTime:
    screenings = Screening.objects.order_by('time').filter(time__gt=timezone.now())

    screenings_time = list(
        set(
            map(lambda x: x[0].date(), screenings.values_list('time'))
        )
    )[::-1]

    return ScreeningsWithTime(screenings=screenings, screenings_time=screenings_time)
