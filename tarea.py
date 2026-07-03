from pathlib import Path
import pprint

# =====================================================================
# 2. Archivos de laberinto (Generación limpia y automática)
# =====================================================================

# Creamos los archivos de texto físicos con los mapas corregidos
Path("maze1.txt").write_text(
"#####B#\n"
"##    #\n"
"#     #\n"
"# ### #\n"
"#A#####", 
encoding="utf-8"
)

Path("maze2.txt").write_text(
"#######\n"
"#     B\n"
"# #####\n"
"#     #\n"
"A #####\n"
"#######", 
encoding="utf-8"
)

Path("maze3.txt").write_text(
"###         #########\n"
"### #################\n"
"### ######### # #####\n"
"# #         # #     #\n"
"# ####### # # ##### #\n"
"#A        #   #     B\n"
"########### #########", 
encoding="utf-8"
)

Path("maze4.txt").write_text(
"A #############################################\n"
"# #         # ##### # ##### ##################\n"
"# # ####### # #   # #     # #                #\n"
"# # #       # #   # ##### # # ############## #\n"
"# # # ####### #   #       # # #            # #\n"
"#   #         #########   #   ############ B\n"
"##############################################", 
encoding="utf-8"
)

print("--- Archivos de laberinto generados correctamente ---")


# =====================================================================
# 4. Estructuras de datos: Node, Stack y Queue
