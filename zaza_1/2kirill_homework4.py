
class TimeDAsk:
    def __init__(self, seconds):
            self.seconds = seconds

    def make_readable(self):

        minutes = self.seconds // 60
        second = self.seconds % 60

        hours = minutes // 60
        minutes = minutes % 60

        days = hours // 24
        hours = hours % 24

        if len(str(hours)) < 2:
            hours = '0' + str(hours)

        if len(str(second)) < 2:
            second = '0' + str(second)

        if len(str(minutes)) < 2:
            minutes = '0' + str(minutes)

        print(f"{days} days, {hours}:{minutes}:{second}")

p1 = TimeDAsk(20220202)
p1.make_readable()
