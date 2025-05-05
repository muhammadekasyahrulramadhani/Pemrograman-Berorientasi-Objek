class Model(object):
    services = {
        'email': {'number': 1000, 'price': 2,},
        'sms': {'number': 1000, 'price': 10,},
        'voice': {'number': 1000, 'price': 15,},
    }

class View(object):
    def list_services(self, services):
        for svc in services:
            print(svc)

    def list_pricing(self, services):
        for svc in services:
            print("For", Model.services[svc]['number'],
                  svc, "messages you pay $",
                  Model.services[svc]['price'])

class View2(object):
    def list_services(self, services):
        for svc in services:
            print(svc)

    def list_pricing(self, services):
        for svc in services:
            print("Untuk setiap", Model.services[svc]['number'],
                  svc, " Anda membayar $",
                  Model.services[svc]['price'])

class Controller(object):
    def __init__(self, language = 1):
        self.model = Model()
        if language == 2:
            self.view = View2()
        else:
            self.view = View()

    def get_services(self):
        services = self.model.services.keys()
        self.view.list_services(services)

    def get_pricing(self):
        services = self.model.services.keys()
        self.view.list_pricing(services)

# Instansiasi objek
language = int(input("What language do you choose? [1] English [2] Indonesia: "))
if language not in [1 , 2]:
   print("choose the language number!")
else:
    controller = Controller(language)
    if language == 2:
        print("Layanan yang Disediakan:")
    else:
        print("Services Provided:")

    controller.get_services()

    if language == 2:
        print("Tarif tiap layanan:")
    else:
        print("Pricing for Services:")

    controller.get_pricing()