class PersonaRouter():

    def __init__(self):
        self.persona = "Ares"
        self.switched = False
    
    def select(self, persona, user_input):
        inp = user_input.strip().lower()

        if user_input == "switch to hades":
            self.persona = "Hades"
            self.switched = True
            print("SWITCHED TO HADES")
        elif user_input == "switch to athena":
            self.persona = "Athena"
            self.switched = True
            print("SWITCHED TO ATHENA")
        elif user_input == "switch to ares":
            self.persona = "Ares"
            self.switched = True
            print("SWITCHED TO ARES")
        else:
            self.persona = persona
            self.switched = False
        
        return self.persona
    
    def hasSwitched(self):
        return self.switched

