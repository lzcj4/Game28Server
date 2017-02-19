import datetime


class RoundModel:
    def __init__(self, r_id, r_date, r_value, r_jing=0, r_shou=0):
        self.id = r_id
        self.date = datetime.datetime.strptime(r_date, "%Y-%m-%d %H:%M")
        try:
            self.value = int(r_value)
        except:
            self.value = 0
        self.jing = r_jing
        self.shou = r_shou
