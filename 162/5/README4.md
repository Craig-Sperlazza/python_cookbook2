# project-5d

Write a class named NeighborhoodPets that has methods for adding a pet, deleting a pet, searching for the owner of a pet, saving data to a JSON file, loading data from a JSON file, and getting a list of all pet species.  It will only be loading JSON files that it has previously created, so the internal organization of the data is up to you. 
* The add_pet method takes as parameters the name of the pet, the species of the pet, and the name of the pet's owner.  If a pet has the same name as a pet that has already been added, then the function should just return without adding the new pet. 
* The delete_pet method takes as a parameter the name of the pet and deletes it.
* The get_owner method takes as a parameter the name of the pet and returns the name of its owner.
* The save_as_json method takes as a parameter the name of the file and saves it in json format with that name.  You can assume the extension (if any) will be part of the provided name. 
* The read_json method takes as a parameter the name of the file to read and loads that file.  This will replace the pets currently in memory.
* The get_all_species method takes no parameters and returns a **set** of the species of all pets.

For example, your class could be used like this:
```
np = NeighborhoodPets()
np.add_pet("Fluffy", "gila monster", "Oksana")
np.add_pet("Tiny", "stegasaurus", "Rachel")
np.add_pet("Spot", "zebra", "Farrokh")
np.save_as_json("pets.json")
np.delete_pet("Tiny")
spot_owner = np.get_owner("Spot")
np.read_json("other_pets.json")
species_set = np.get_all_species()
```

The file must be named: **NeighborhoodPets.py**
