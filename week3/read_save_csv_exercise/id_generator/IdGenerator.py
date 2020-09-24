import random
from week3.read_save_csv_exercise.utils.GeneratorLogger import GeneratorLogs

# Create Logger Instance
generator_id_logger = GeneratorLogs()


class IdGenerator:

    stored_keys = {}

    def __init__(self):
        self.stored_keys = set([])

    def create_id(self):
        generator_id_logger.info_calls(" Times Generator was Called ")
        while True:
            id_option = self.id_generator()
            if id_option not in self.stored_keys:
                self.stored_keys.add(id_option)
                return id_option
                break
            else:
                generator_id_logger.info_ids(" Times ID was repeated")

    def retrieve_ids(self):
        return self.stored_keys

    def id_generator(self):
        token =  "".join(str([str(random.randint(1,10)) for x in range(0,6)]))\
            .replace("[","").replace("\'","").replace("]","").replace(",","").replace(" ","")
        if len(token) == 6 : return token + "1"
        else: return token


    def id_ordered_generator(self, list_length ):
        for i in range(1,list_length+1):
            yield self.create_id()