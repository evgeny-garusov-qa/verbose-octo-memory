import faker
import os

def write_some_log():
    fp = 'logs.log'
    if os.path.exists(fp):
        os.remove(fp)
    with open(fp, 'a') as file:
        file.write(faker.Faker().sentence())
