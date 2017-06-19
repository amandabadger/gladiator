def ascii_art(art_name):
    if art_name == "coliseum":
        art = """    ________                 
    |-|-|-|.\____________    
    |n|n|n|n|n|n|n|n|n|n|    
    |n|n|n|n|n|n|n|n|n|n|    
    |n|n|n|n|n|n|n|n|n|n|   o
    ~~~~~~~~~~~~~~~~~~~~~   ^
"""
    elif art_name == "sword":
        art="""         O
         |
  0{XXXX}+====================>
         |
         O
"""
    elif art_name == "axe":
        art=""" 
  {XXXXXXX====================}
                    /       \\
                   /         \\
                   \\_________/
"""
    elif art_name == "mace":
        art="""                        /\\/\\/\\
                        ||||||
  0{XXXX}+====================>
                        ||||||
                        \\/\\/\\/
"""
    elif art_name == "flail":
        art="""  {XXXXXXX===================},
                             o
                XXXX         o
               XXXXXX - o   o
                XXXX      o
"""
    elif art_name == "staff":
        art="""

  =====XXXX===========XXXX=====


"""


    print(art)
    return True
