class App():
    def __init__(self, name, size, ram_usage, description, version):
        self.name = name
        self.size = size
        self.ram_usage = ram_usage
        self.opened = False
        self.description = description
        self.version = version


    def open(self):
        self.opened = True
        return [self.name, self.description, self.version]

    def close(self):
        self.opened = False
        return f"{self.name} is closed."

class Phone():
    def __init__(self, brand, model, memory, ram):
        self.brand = brand
        self.model = model
        self.memory = memory
        self.ram = ram
        self.free_ram = ram
        self.free_memory = memory
        self.installed_apps = []

    def install_app(self, app=object):
        if self.free_memory >= app.size:
            self.installed_apps.append(app)
            self.free_memory = self.free_memory - app.size
            print(f"{app.name} is successfully installed")
        else:
            print(f"{app.name} is not installed due to insufficient memory")
        
    def open_app(self, name=""):
        app = next((app for app in self.installed_apps if app.name == name), 0)
        if not app == 0:
            ram = self.free_ram - app.ram_usage
            if not ram < 0:
                print(*[app.open()])
                self.free_ram = self.free_ram - app.ram_usage
            else:
                print("Not enough RAM.")
        else:
            print("App not found.")

    def close_app(self, name = ""):
        app = next((app for app in self.installed_apps if app.opened == True), 0)
        if not app == 0:
           print(app.close)
           self.free_ram = self.free_ram + app.ram_usage
        else:
            print()