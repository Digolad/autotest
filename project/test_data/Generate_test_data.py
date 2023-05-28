from faker import Faker
fake = Faker()


class GenerationTestData:

    @staticmethod
    def generation() -> dict:
        email = fake.email()
        email = email.split('@')
        input_your_email = email[0]
        domain = email[1].split('.')[0]

        passwd = 'Sн1' + input_your_email
        if len(passwd) < 10:
            x = 10 - len(passwd)
            while len(passwd) < 10:
                passwd = passwd + str(x)
                x += 1

        return {
            "email": input_your_email,
            "domain": domain,
            "password": passwd
        }
