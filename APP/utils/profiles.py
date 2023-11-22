
from json import dumps, loads
from pathlib import Path


from APP.config import profiles_folder


class User:

    def __init__(self):
        self.index = 0
        self.display_name = None
        self.categories = None
        self.save_location = None
        self.max_concurrent_requests = 10
        self.db_string = None


    def build(self):
        self.display_name = input("What can we call you?: ")
        self.categories = input("What categories do you want to follow? (Separate with comma.): ").split(',')
        self.save_location = Path(input("Where do you want to save your data?: "))
        self.db_string = f"sqlite:///{self.save_location}/posts.db"
        self.save()

    def save(self):
        profile_name = f"{self.display_name}.json"
        self.save_location.mkdir(parents=True, exist_ok=True)
        self.save_location = str(self.save_location)
        with open(Path(profiles_folder) / profile_name, 'w') as f:
            f.write(dumps(self.__dict__, indent=6))

    def load(self, profile_name):
        with open(Path(profiles_folder) / profile_name, 'r') as f:
            self.__dict__ = loads(f.read())
            self.save_location = Path(self.save_location)

    def __repr__(self):
        return f"display_name={self.display_name}, categories={self.categories}, save_location={self.save_location}"

    def set_max_concurrent_requests(self):
        self.max_concurrent_requests = int(input("How many concurrent requests do you want to make? (Default is 10): "))
        self.save()


def select_profile():
    if not Path(profiles_folder).exists():
        Path(profiles_folder).mkdir(parents=True, exist_ok=True)
    profiles = [profile for profile in Path(profiles_folder).iterdir() if profile.is_file() and profile.exists()]
    if len(profiles) == 0:
        print("No profiles found. Please create one.")
        quit()
    print("Select a profile:")
    for i, profile in enumerate(profiles):
        print(f"{i+1}. {profile.stem}")
    profile_selection = int(input("Enter the number of the profile you want to use: "))
    profile = profiles[profile_selection-1]
    p = User()
    p.load(profile.name)
    return p


async def create_profile():
    p = User()
    p.build()