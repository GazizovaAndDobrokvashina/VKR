from TextParser import TextParser
from Actors import Actors
import sqlite3


ourText = "One day, while preparing for classes, the main character had to descend into a dungeon with artifacts to do a little practical work. Walking through the ancient corridors, looking at unusual pedestals, the hero completely forgets about his poor tail. And on one of the turns Azazel feels how his tail touches something, and then he hears a loud clank behind his back. He no longer needs to turn around to understand that he broke something. All the same, looking back, the little fox sees what he expected: a pile of fragments of a certain artifact."

result = TextParser(ourText)

# conn = sqlite3.connect('example.db')
# actors = Actors(conn)
# conn.commit()
# actors.add_actor('mc', 'mc, Azazell') - уже записано в таблицу
# conn.commit()
# print(actors.get_actors())
#
# conn.close()


