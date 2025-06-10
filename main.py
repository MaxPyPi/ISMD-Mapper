from Database import Geological_Place

Place = Geological_Place()

Place.ask_temp()
Place.ask_cont()
Place.sync_clock()
print(Place.check_clock())
Place.print_knowledge_check()