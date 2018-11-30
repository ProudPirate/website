#Service layer for routines
from routine.choices import day_choices
from routine.models import Routine, Period


def get_section_routine(sec_id):
    """
    :param sec_id: section id for which routine is required
    :return: list containing routine
    """

    routine_array = []

    days_list = [{'day':x[0],'name':x[1]} for x in day_choices]
    periods = Period.objects.all().order_by('start_time')
    routine = Routine.objects.filter(section_id=sec_id)

    for each in days_list:
        temp_dict = {}
        temp_dict['day_info'] = each
        temp_dict['period_info'] = [{'period': x} for x in periods]

        for period_dict in temp_dict['period_info']:
            period_dict['routine_details'] = [x.details.all() for x in routine if x.period == period_dict['period']
                                              and x.day == each['day']]


        routine_array.append(temp_dict)


    return routine_array




