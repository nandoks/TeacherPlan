from datetime import date


def is_start_before_end(start, end, error_list):
    print(start)
    print(end)
    print(start >= end)
    if start >= end:
        error_list['start'] = 'Start time must be before end time'


def is_date_after_today(form_date, error_list):
    if form_date <= date.today():
        error_list['date'] = 'Lesson date invalid, cannot be before or equals today'
