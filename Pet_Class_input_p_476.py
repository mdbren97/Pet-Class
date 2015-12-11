import Pet_Class_create_p_476

def main():
    name = input("What do you want to name your pet?")
    an_type = input("What type of animal is your pet?")
    age = input("How old is your pet?")

    pet = Pet_Class_create_p_476.Pets(name,an_type,age)

    print("Your pet's name is", pet.get_name())
    print("Your pet is a", pet.get_animal_type())
    print("Your pet is", pet.get_age(), "years old.")




main()