class Sheep:
    def __str__(self):
        return "Sheep"

class Wolf:
    def __str__(self):
        return "Wolf"

class Cabbage:
    def __str__(self):
        return "Cabbage"

class Farmer:
    def __init__(self, passenger):
        self.passenger = passenger

    def __str__(self):
        return f"Farmer and {self.passenger}"

class Boat:
    def __init__(self):
        self.objects = []

    def __str__(self):
      return f"\nStates: {', '.join(map(str, self.objects))}" if self.objects else "The Boat is empty."


    def inBoat(self, passenger):
        self.objects.append(passenger)
        return f"\n>> The {passenger} is now in the boat."

    def crossRiver(self):
        steps = [
            "\n>> The Farmer, Sheep, Wolf, and Cabbage are in the left side of the river.",
            self.inBoat(Farmer(Sheep())),
            "\n>> The Farmer takes the Sheep across the river.",
            self.inBoat(Farmer(None)),
            "\n>> The Farmer goes back to the Wolf and the Cabbage.",
            self.inBoat(Farmer(Wolf())),
            "\n>> The Farmer takes the Wolf across the river along with the Sheep.",
            "\n>> The Farmer takes the Sheep with him and went back to the left side.",
            self.inBoat(Farmer(Sheep())),
            "\n>> The Farmer takes the Cabbage across the river with the Wolf leaving the Sheep behind.",
            self.inBoat(Farmer(Cabbage())),
            "\n>> The Farmer comes back for the sheep.",
            self.inBoat(Farmer(None)),
            "\n>> The Farmer crosses the river for the last time with the Sheep.",
            self.inBoat(Farmer(Sheep())),
            "\n>> The Farmer, Sheep, Wolf, and Cabbage crossed the river safely."
        ]

        return "\n".join(steps)
