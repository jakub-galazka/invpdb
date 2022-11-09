import string
import random
import pandas as pd
from typing import List
import datetime
from const import CSV_PATH, SEP

class Software:

    def __init__(self, quantity=1):
            self.softwares = {
            "Microsoft": ["Internet Explorer", "Microsoft Outlook", "Microsoft Office 365", "Visual Studio Code", "Notepad++", "Microsoft Edge", "OneDrive", "Microsoft To Do", "Microsoft Azur"],
            "Mozilla": ["Mozilla Firefox", "Mozilla Thunderbird", "Mozilla Reality"],
            "Yahoo": ["Yahoo Email", "Yahoo Massanger", "Yahoo Music Jukebox"],
            "Adobe": ["Acrobat Reader","Photoshop", "Illustrator", "Premiere Pro", "Lightroom", "Scan", "Experience Cloud"],
            "Kakao": ["PotPlayer"],
            "Foxit": ["Foxit PDF Reader"],
            "PandoraTV": ["KMPlayer"],
            "Google": ["Google Drive", "Google Maps", "Google Analytics", "Google Earth", "Google Cloud Platform", "Google Finance", "Google Chrome", "AdSense", "Google Web Designer", "Android Studio", "Google Workspace"],
            "IBM": ["WebSphere", "IBM Db2", "IBM pureQuery", "IBM DisplayWrite", "IBM OfficeVision", "IBM Planning Analytics", "IBM Cognos Analytics"], 
            "JetBrains": ["Intellij IDEA", "PyCharm", "WebStorm", "PhpStorm", "ReSharper", "Rider", "CLion", "Datalore", "DataSpell", "DataGrip", "RubyMine", "AppCode", "GoLand", "dotPeek", "dotTrace", "TeamCity", "Hub", "Kotlin", "MPS", "PyCharm Edu", "Edu Tools", "Code With Me", "Gateway", "Qodana"]
            }
            self._prepare_csv(quantity)
        
    def create_publisher_name(self, quantity=1) ->List[str]:
        return [random.choice(list(self.softwares.keys())) for _ in range(quantity)]
        
    def create_software_name(self, publishers, quantity) ->List[str]:
        softwares = []
        for p in publishers:
            sw_len = len(self.softwares[p])
            index = random.randint(0, sw_len - 1)
            softwares.append(self.softwares[p][index])
        return softwares

    def create_license_key(self, quantity=1) -> List[str]:
            return[
                "".join(self._random_key(16)) for _ in range(quantity)
            ]
                        
    def _random_key(self, length):
            letters = string.ascii_lowercase + string.digits
            return  ''.join(random.choice(letters) for i in range(length))
               
    def create_expire_date(self, quantity=1) -> List[str]:
            date1 = datetime.date(2015, 1, 1)
            date2 = datetime.date(2025, 1, 1)
            
            return [
                "".join(self._random_date(date1, date2)) for _ in range(quantity)
            ]

    def _random_date(self, start, end):
            delta = end - start
            random_day = delta.days
            random_number_of_days = random.randrange(random_day)
            return str(start + datetime.timedelta(days=random_number_of_days))

    def _prepare_csv(self, quantity):
            publishers = self.create_publisher_name(quantity)
            df = pd.DataFrame(
                {
                    "software_name": self.create_software_name(publishers, quantity),
                    "publisher_name": publishers,
                    "license_key": self.create_license_key(quantity),
                    "expire_date": self.create_expire_date(quantity),
                }
            )
            df.index.name = "id"
            df.to_csv(CSV_PATH % "software", index=True, sep=SEP)