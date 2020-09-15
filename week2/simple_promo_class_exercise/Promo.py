from datetime import datetime


class Promo:
    def __init__(self, name, expire_date=None, day=None, month=None, year=None):
        self.name = name
        self.expire_date = expire_date
        self.day = day
        self.month = month
        self.year = year
        self.has_expired(expire_date=expire_date, day=day, month=month, year=year)

    def has_expired(self, expire_date=None, day=None, month=None, year=None):
        #  Functions for determining if the product has expired. Returns True/False boolean
        #  Arguments can be on the following form:
        #  - A datetime object, has_expired(expire_date = datetime object)
        #  - Inserting day, month, year values. Day is not necessary. i.e has_expired(month=month, year=year)
        temporal_expire_date = self.convert_to_datetime(expire_date=expire_date, day=day, month=month, year=year)
        self.now = datetime.now()
        self.remaining_days = (temporal_expire_date - self.now).days
        if self.remaining_days > 0:
            self.expired = False
        else:
            self.expired = True
        return self.expired

    def convert_to_datetime(self, expire_date=None, day=None, month=None, year=None):
        # Function for creating datetime object from :
        # - inserting values as convert_to_datetime(day = day, month = month, year = year)
        #                       convert_datetime(month = month, year = year)
        # - inserting a datetime object as convert_to_datetime(expirate_date = datetime)
        # Returns a datetime object

        if self.year is not None and self.month is not None:
            if self.day is None:
                self.expire_date = datetime.strptime("{}-{}".format(year, month), "%Y-%m")
                return self.expire_date
            else:
                self.expire_date = datetime.strptime("{}-{}-{}".format(year, month, day), "%Y-%m-%d")
                return self.expire_date
        elif self.expire_date is not None:
            return expire_date
        else:
            return self.expire_date

    def __str__(self):
        if self.expired:
            return "{} has expired the past {} Don't eat it ".format(self.name, self.expire_date.strftime("%Y-%m"))
        else:
            return "{} expires on {} Still {} days left ".format(self.name, self.expire_date.strftime("%Y-%m"),
                                                                 self.remaining_days)

    def get_name(self):
        return self.name

    def get_expiration_date(self):
        return self.expire_date


meat = Promo("Meat", datetime(year=2019, day=14, month=2))


def instantiate_promo():
    return meat.has_expired()


def instantiate_promo_name():
    return meat.get_name()


def instantiate_promo_expiration_date():
    return meat.get_expiration_date()
