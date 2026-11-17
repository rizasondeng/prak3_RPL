try:
    from controllers.buku_controller import BukuController
except ModuleNotFoundError:
    from Controllers.buku_controller import BukuController

if __name__ == "__main__":
    app = BukuController()
    app.run()
