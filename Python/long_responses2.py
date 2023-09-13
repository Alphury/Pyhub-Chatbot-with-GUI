import random
#long response SAMAH will give for eating
R_EATING = "I don't like eating anything because I'm a bot obviously!"
#long response SAMAH will give for as an advice 
R_ADVICE = "If I were you, I would go to the internet and type exactly what you wrote there!"
R_FAV = "My favourite song is an underated one dil dooba!"

def unknown():
    response = ["Could you please re-phrase that? ",
                "...",
                "Sounds about right.",
                "What does that mean?"][
        random.randrange(4)]
    return response