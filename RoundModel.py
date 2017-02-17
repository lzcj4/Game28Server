import datetime


class RoundModel:
    def __init__(self, r_id, r_date, r_value):
        self.id = r_id
        self.date = datetime.datetime.strptime(r_date, "%Y-%m-%d %H:%M")
        try:
            self.value = int(r_value)
        except:
            self.value = 0
