from abc import ABC, abstractmethod

class Section(ABC):
    @abstractmethod
    def describe(self):
        pass

class PersonalSection(Section):
    def describe(self):
        print("Personal Section")

class AlbumSection(Section):
    def describe(self):
        print("Album Section")

class PatentSection(Section):
    def describe(self):
        print("Patent Section")

class PublicationSection(Section):
    def describe(self):
        print("Publication Section")

class Profile(ABC):
    def __init__(self):
        self.sections = []
        self.createProfile()

    @abstractmethod
    def createProfile(self):
        pass

    def getSections(self):
        return self.sections

    def addSections(self, section):
        self.sections.append(section)

class LinkedIn(Profile):
    def createProfile(self):
        self.addSections(PersonalSection())
        self.addSections(PatentSection())
        self.addSections(PublicationSection())

class Facebook(Profile):
    def createProfile(self):
        self.addSections(PersonalSection())
        self.addSections(AlbumSection())

def main():
    profile_classes = {
        "linkedin": LinkedIn,
        "facebook": Facebook
    }

    profile_type = input("Profil apa yang ingin anda buat? [Linkedin atau Facebook]: ").strip().lower()
    
    if profile_type in profile_classes:
        profile = profile_classes[profile_type]()
        print(f"Profil {type(profile).__name__} sedang dibuat..")
        print("Profil mempunyai Section:")
        for section in profile.getSections():
            section.describe()
    else:
        print("Tipe profil tidak dikenali.")

if __name__ == "__main__":
    main()