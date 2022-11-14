import random
import string
import pandas as pd
from faker import Faker
from .generator import Generator

class SoftwareGenerator(Generator):

    SOFTWARES = {
        "Microsoft": ["Internet Explorer", "Microsoft Outlook", "Microsoft Office 365", "Visual Studio Code", "Notepad++", "Microsoft Edge", "OneDrive", "Microsoft To Do", "Microsoft Azure"],
        "Mozilla": ["Mozilla Firefox", "Mozilla Thunderbird", "Mozilla Reality"],
        "Yahoo": ["Yahoo Email", "Yahoo Messenger", "Yahoo Music Jukebox"],
        "Adobe": ["Acrobat Reader","Photoshop", "Illustrator", "Premiere Pro", "Lightroom", "Scan", "Experience Cloud"],
        "Kakao": ["PotPlayer"],
        "Foxit": ["Foxit PDF Reader"],
        "PandoraTV": ["KMPlayer"],
        "Google": ["Google Drive", "Google Maps", "Google Analytics", "Google Earth", "Google Cloud Platform", "Google Finance", "Google Chrome", "AdSense", "Google Web Designer", "Android Studio", "Google Workspace"],
        "IBM": ["WebSphere", "IBM Db2", "IBM pureQuery", "IBM DisplayWrite", "IBM OfficeVision", "IBM Planning Analytics", "IBM Cognos Analytics"], 
        "JetBrains": ["Intellij IDEA", "PyCharm", "WebStorm", "PhpStorm", "ReSharper", "Rider", "CLion", "Datalore", "DataSpell", "DataGrip", "RubyMine", "AppCode", "GoLand", "dotPeek", "dotTrace", "TeamCity", "Hub", "Kotlin", "MPS", "PyCharm Edu", "Edu Tools", "Code With Me", "Gateway", "Qodana"]
    }

    def __init__(self, seed: int = None) -> None:
          super().__init__(seed)
          self.faker = Faker()
          if not seed == None:
            self.faker.seed_instance(seed)

    def generate(self, quantity: int = 1) -> None:
        publishers = random.choices(list(SoftwareGenerator.SOFTWARES.keys()), k=quantity)
        software = pd.DataFrame({
            "software_name": self._generate_software_names(publishers),
            "publisher_name": publishers,
            "license_key": random.choices(string.ascii_letters + string.digits, k=quantity),
            "expire_date": super().generate_list(quantity, lambda: self.faker.date_between("-5y", "+5y")),
        })
        self.csvw.write(software, "software")
        
    def _generate_software_names(self, publishers: list[str]) -> list[str]:
        softwares = []
        for p in publishers:
            sw_len = len(SoftwareGenerator.SOFTWARES[p])
            i = random.randint(0, sw_len - 1)
            softwares.append(SoftwareGenerator.SOFTWARES[p][i])
        return softwares
