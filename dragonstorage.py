def dragon_features(selectedDragon):
  dragons = {
    "mudwing": {
      "speciality": "fire-proof scales, big in size",
      "powers": "breathes fire, strong claws",
      "weaknesses": "venom and isolation"
    },
    "skywing": {
      "speciality":
      "fastest flyer than any other dragon in dragonia, due to it's wide wings",
      "powers": "capable of breathing fire",
      "weaknesses": "tiny spaces"
    },
    "seawing": {
      "speciality": "have gills, exceptional night vision, and powerful tails",
      "powers": "exceptional night vision",
      "weaknesses": "lack of water"
    },
    "sandwing": {
      "speciality": "have scales that radiate warmth",
      "powers": "venomous barb, like a scorpion",
      "weaknesses": "taking venom from Rainwings"
    },
    "nightwing": {
      "speciality": "can see the future",
      "powers": "venom, can see the future, mind reads",
      "weaknesses": "'classified'"
    },
    "icewing": {
      "speciality": "",
      "powers": "",
      "weaknesses": ""
    },
    "rainwing": {
      "speciality": "",
      "powers": "",
      "weaknesses": ""
    }
  }

  selectedDragon = selectedDragon.lower()
  dragon = dragons[selectedDragon] if selectedDragon in dragons.keys(
  ) else None

  if not dragon:
    print(f"hmm? I don't think '{selectedDragon}' is a valid input.")
    print(
      "Please retry by restarting the project and entering the correct input.")
  else:
    print(f"You selected the '{selectedDragon}' Egg!")
    print()
    print(
      f"To hatch your '{selectedDragon}', You will be asked a question. If you type in the word hatch, then the egg will hatch. If you type collect, it will stay in your collection and you will have nothing to do with it."
    )
    print()
    collectorhatch = input("Which option? > ")
    if collectorhatch.lower() == "collect":
      print(
        "Your egg is now in your collection. You can only fight Dragons and build shelter and weapons for survival. Good Luck"
      )
    if collectorhatch.lower() == "hatch":
      print()
      print(
        f"You hatched your '{selectedDragon}' Egg! It's speciality is {dragon['speciality']}. It's powers are {dragon['powers']}. It's weaknesses are {dragon['weaknesses']}."
      )
      
