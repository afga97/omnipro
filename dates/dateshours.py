from datetime import datetime, timedelta, time
import json
import pytz
import holidays as pyholidays
import businesstimedelta

class DateHours:
    """
        Fechas y Horas
        Dada 2 fechas, A y B, en el formato:
        DD/MM/YYYY hh:mm:ss +xxxx
        ◦ Imprimir el número de días Lunes, Martes, Miércoles, Jueves, 
            Viernes, Sábados y Domingos que hay entre estas fechas. Asuma misma zona horaria.
        ◦ Imprimir el número de horas laborales entre ese rango de fechas (no tomar en cuenta 
            días feriados, asumir jornada de 8hr/día, Lunes-Viernes). Asuma misma zona horaria.
        ◦ Imprimir la diferencia entre las fechas (asuma misma zona horaria) en:
            ▪ Segundos
            ▪ Horas
            ▪ Días
        ◦ Realizar nuevamente el cálculo del punto anterior, utilizando fechas de diferentes zonas horarias
    """
    format_date = '%d/%m/%Y %H:%M:%S'
    date_initial = None
    date_end = None

    def __init__(self, date_initial, date_end, time_zone, time_zone2=None):
        date_initial = datetime.strptime(date_initial, self.format_date)
        date_end = datetime.strptime(date_end, self.format_date)
        if not time_zone2:
            timezone = pytz.timezone("{}".format(time_zone))
            self.date_initial = timezone.localize(date_initial)
            self.date_end = timezone.localize(date_end)
        else:
            timezone_1 = pytz.timezone("{}".format(time_zone))
            self.date_initial = timezone_1.localize(date_initial)
            time_zone_2 = pytz.timezone("{}".format(time_zone2))
            self.date_end = time_zone_2.localize(date_end)

    def number_days(self):
        """
            Imprimir el número de días Lunes, Martes, Miércoles, Jueves, 
            Viernes, Sábados y Domingos que hay entre estas fechas. Asuma misma zona horaria.
        """
        days_week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        count_days = [0, 0, 0, 0, 0, 0, 0]
        date_initial_copy = self.date_initial
        while date_initial_copy <= self.date_end:
            day_date = datetime.weekday(date_initial_copy)
            count_days[day_date] = count_days[day_date] + 1
            date_initial_copy = date_initial_copy + timedelta(days=1)
        return dict(zip(days_week, count_days))
    
    def work_hours(self):
        """
            Imprimir el número de horas laborales entre ese rango de fechas (no tomar en cuenta 
            días feriados, asumir jornada de 8hr/día, Lunes-Viernes). Asuma misma zona horaria.
        """
        co_holidays = pyholidays.CountryHoliday('CO', prov=None, state=None)
        holidays = businesstimedelta.HolidayRule(co_holidays)
        workday = businesstimedelta.WorkDayRule(
                    start_time=time(7),
                    end_time=time(15),
                    working_days=[0, 1, 2, 3, 4]
                )
        businesshrs = businesstimedelta.Rules([workday, holidays])
        result = businesshrs.difference(self.date_initial, self.date_end)
        seconds = result.timedelta.total_seconds()
        h = seconds // 3600
        return h

    def difference_dates(self):
        """
            Imprimir la diferencia entre las fechas (asuma misma zona horaria) en:
            ▪ Segundos
            ▪ Horas
            ▪ Días
        """
        difference = self.date_end - self.date_initial
        seconds = int(difference.total_seconds())
        days = seconds // 86400
        hours = (seconds - (days * 86400)) // 3600        
        seconds = (seconds - (days * 86400) - ( hours * 3600 ))
        return { 'days': days, 'hours': hours, 'seconds': seconds }        

    def output_data(self):
        try:
            days = self.number_days()
            print('Los dias que hay entre las fechas son : \n' + json.dumps(days, sort_keys=False, indent=5))
            hours = self.work_hours()
            print('Las horas laborales que hay entre las fechas son {}'.format(hours))
            data_difference = self.difference_dates()
            print('Diferencia entre las dos fechas es de:\n{} dias, {} minutos y {} segundos'.format(
                data_difference['days'], data_difference['hours'], data_difference['seconds']
            ))
        except Exception as e:
            print("Ocurrio un error {}".format(e))

    def output_dates_timezone(self):
        try:
            data_difference = self.difference_dates()
            print('Diferencia entre las dos fechas es de:\n{} dias, {} minutos y {} segundos'.format(
                data_difference['days'], data_difference['hours'], data_difference['seconds']
            ))
        except Exception as e:
            print("Ocurrio un error {}".format(e))

date_initial_1 = '01/05/2020 10:00:00'
date_end_1 = '17/05/2020 17:00:00'
time_zone = "America/Bogota"

instance_date = DateHours(date_initial_1, date_end_1, time_zone)
instance_date.output_data()

date_initial_2 = '01/05/2020 10:00:00'
date_end_2 = '17/05/2020 10:00:00'
time_zone = "America/Bogota"
time_zone2 = 'Europe/Madrid'

instance_date_2 = DateHours(date_initial_2, date_end_2, time_zone, time_zone2)
instance_date_2.output_dates_timezone()