class Owner:
    def __init__(self, name):
        self.name = name
    
    def pets(self):
        # Return a list of pets owned by this owner
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("The pet must be an instance of the Pet class.")
        pet.owner = self

    def get_sorted_pets(self):
        # Return a sorted list of pets by their names
        return sorted(self.pets(), key=lambda pet: pet.name)


class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []  # Class variable to store all instances of Pet

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet type. Allowed types are: {', '.join(Pet.PET_TYPES)}")
        
        if owner is not None and not isinstance(owner, Owner):
            raise Exception("Owner must be an instance of the Owner class.")
        
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)  # Add this instance to the class variable `all`

# Example usage
try:
    owner1 = Owner("Alice")
    pet1 = Pet("Fido", "dog", owner1)
    pet2 = Pet("Whiskers", "cat", owner1)
    owner1.add_pet(Pet("Rex", "dog"))  # This will add a pet without an owner

    print("Owner's pets:", [pet.name for pet in owner1.pets()])
    print("Sorted pets by name:", [pet.name for pet in owner1.get_sorted_pets()])

except Exception as e:
    print("Error:", e)

