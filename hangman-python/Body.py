# Hangman Anatomy = 8 Stages

def Hangman(Attempt):
    Body = [   
                # First Stage: Platform
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   =
                """,
                 # Second Stage: Head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   =
                """,
                # Third Stage: Body
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      
                   |     
                   =
                """, 
                # Fourth Stage: Right Arm
                """
                   --------
                   |      |
                   |      O
                   |     \|
                   |      
                   |     
                   =
                """, 
                # Fifth Stage: Left Arm
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      
                   |     
                   =
                """, 
                # Sixth Stage: Torso
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     
                   =
                """, 
                # Seventh Stage: Right Leg
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     /
                   =
                """, 
                # Eighth Stage: Left Leg
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / \\
                   =
                """
    ]
    Body.reverse()
    return Body[Attempt]
