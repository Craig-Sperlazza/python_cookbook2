# project-5d
# Author: Craig Sperlazza
# Date: 1/29/2020
# Description: The program creates a class named NeighborhoodPets that has
#           methods for adding a pet, deleting a pet, searching for the owner
#           of a pet, saving data to a JSON file, loading data from a JSON file,
#           and getting a list of all pet species. The pets will be stored in a
#           dictionary with a key (pets name) and a value which is a list of
#           (pets name, species, owners name)

import json

class NeighborhoodPets:
    """
    __init__: Creates a NeighborhoodPets class that contains an init method that
    initializes an empty dictionary.

    Methods: This class has methods for adding a pet, deleting a pet,
    searching for the owner of a pet, saving data to a JSON file,
    loading data from a JSON file, and getting a list of all pet species.
    """

    def __init__(self) -> None:
        """init method that initializes a dictionary (empty) to handle the input
        of pet information. The pet_dictionary will have one key value pair,
        which is added via the add_pet method below. The key:value pair is:
        key is the name of the pet, while the value is a list containing
        name of the pet, the species of the pet, and the name of the pet's owner
        """
        self.pet_dictionary = {}


    def __str__(self) -> str:
        return ''.join([
            'PetDictionary(',
            f'pet_dictionary={self.pet_dictionary}, ',
            ')'
        ])


    def add_pet(self, pet_name: str, pet_species: str, owner_name: str) -> None:
        """
        :param pet_name: Enter a pet name
        :param pet_species: Enter the species of the pet
        :param owner_name: Enter the owner of the pets name

        :return: If the pet name is unique, it will add the pet to the
        pet dictionary created above. The pet will be added as a key:value pair
        with the key(name of the pet): value [is a list containing
        name of the pet, the species of the pet, and the name of the pet's owner]

        If the pet name is the same name as a pet that has already been added,
        the function will return without adding the new pet.

        """
        if pet_name not in self.pet_dictionary.keys():
            self.pet_dictionary[pet_name] = [pet_name, pet_species, owner_name]

        #####TEST PRINT TO ADD ITEMS
        #for k, v in self.pet_dictionary.items():
            #print(k, ':', v)


    def delete_pet(self, pet_name: str) -> None:
        """
        :param pet_name: Enter a pet name

        :return: If the pet name is found, it will be deleted from the
        pet dictionary created above.
        """
        if pet_name in self.pet_dictionary.keys():
            del self.pet_dictionary[pet_name]

        #####TEST PRINT TO ADD ITEMS
        #for k, v in self.pet_dictionary.items():
            #print(k, ':', v)


    def get_owner(self, pet_name: str) -> str:
        """
        :param pet_name: Enter a pet name

        :return: If the pet name is found, it will return the owner names,
        which is held in index 2 of the list.
        """
        if pet_name in self.pet_dictionary.keys():
            #print(self.pet_dictionary[pet_name][2])
            return self.pet_dictionary[pet_name][2]


    def save_as_json(self, file_name) -> None:
        """Parameter: save_as_json method takes as a parameter the name of the
        file and saves it in json format with that name. This method assumes
        that the extension (if any) will be part of the provided name."""
        with open(file_name, 'w') as outfile:
            json.dump(self.pet_dictionary, outfile)


    def read_json(self, file_name):
        """Parameter: the name of the file to read and loads that file.
        This method will replace the pets currently in memory in the
        self.pet_dictionary"""
        with open(file_name, 'r') as infile:
            self.pet_dictionary = json.load(infile)


    def get_all_species(self) -> set:
        """
        The method get_all_species takes no parameters
        :return: it will return a SET of all species
        """
        empty_lst = []

        #Two for loops are needed to iterate through all dictionary values and
        #then within each value (since the value is itself a list)
        for pet_list in self.pet_dictionary.values():
            for value_in_list in range(0, len(pet_list)):
                if value_in_list == 1: #species is at the 1 index
                    #print(pet_list[value_in_list])
                    empty_lst.append(pet_list[value_in_list])
        #print(empty_lst)
        species_set = set(empty_lst)
        #print(species_set)
        return species_set


"""
#########TESTING##########################################################
np = NeighborhoodPets()
np.add_pet("Fluffy", "gila monster", "Oksana")
np.add_pet("Tiny", "stegasaurus", "Rachel")
np.add_pet("Spot", "zebra", "Farrokh")
np.add_pet("Spat", "zebra", "Barrokh")

np.save_as_json("pets.json")
np.delete_pet("Tiny")
spot_owner = np.get_owner("Spot")
np.read_json("pets.json")
species_set = np.get_all_species()
#The file must be named: NeighborhoodPets.py
"""