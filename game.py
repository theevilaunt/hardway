from sys import exit
from random import randint

class Scene(object):
  def enter(self):
    print("unimplemented. subclass and implement enter()")
    exit(1)

class Engine(object):
  """ scene map might be a save db state? """
  def __init__(self, scene_map):
    self.scene_map = scene_map

  def play(self):
    current_loc = self.scene_map.opening_scene()
    print("engine.play() starting at: '%s'" % current_loc)
    while True:
      next_loc = self.scene_map.next_scene(current_loc).enter()
      print("next_loc: '%s'" % next_loc)
      current_loc = next_loc
    # while True:
    #   print("\n------")
    #   print("play current_scene: '%s'" % current_scene)
    #   next_scene_name = self.scene_map.next_scene(current_scene)
    #   print("play: '%s'" % next_scene_name)
    #   current_scene = self.scene_map.scenes.get(next_scene_name)

class Death(Scene):
  quips = [
    "you died!",
    "bad luck!",
    "luser!",
  ]
  def enter(self):
    print(Death.quips[randint(0,len(self.quips)-1)])
    exit(1)

class CentralCorridor(Scene):
  def enter(self):
    msg = """
    gothons invaded ship & destroyed crew
    gothon blocking armory wants to shoot you
    """
    print(msg)

    action = input("shoot/dodge/joke > ")
    if action == "shoot":
      print("sorry, gothon shoots and kills you")
      return 'death'
    elif action == "dodge":
      print("sorry, your dodge failed")
      return 'death'
    elif action == "joke":
      print("joke stalls gothon and you escape to armory")
      return 'armory'
    else:
      print("does not compute")
      return 'central_corridor'

class Armory(Scene):
  def enter(self):
    print("you have 10 tries to enter correct 1 digit code")
    #code = "%d%d%d" % (randint(1,9),randint(1,9),randint(1,9))
    code = "%d" % randint(1,9)
    print("code '%s'" % code)
    guess = input("[keypad guess]: ")
    print("guess '%s'" % guess)
    guesses = 0
    while int(guess) != int(code) and guesses < 10:
      print("incorrect!")
      guesses += 1
      guess = input("[keypad guess]: ")

    if int(guess) == int(code):
      print("grab bomb and head towards the bridge")
      return 'bridge'
    else:
      print("you lose")
      return 'death'

class Bridge(Scene):
  def enter(self):
    msg = """
    on bridge with bomb
    throw/place
    """
    print(msg)
    action = input("> ")
    if action == "throw":
      print('gothons on bridge kill you')
      return 'death'
    elif action == "place":
      print("place bomb and escape to pod")
      return 'escape_pod'
    else:
      print("does not compute")
      return 'bridge'

class EscapePod(Scene):
  def enter(self):
    print("select 1 of 5 pods")
    good_pod = randint(1,5)
    guess = input("[pod#]> ")
    if int(guess) != good_pod:
      print("pod %s is the wrong one; you are dead!" % guess)
      return 'death'
    else:
      print("pod %s is the right one; you win!" % guess)
      return 'finish'

class Map(object):
  scenes = {
    'central_corridor': CentralCorridor(),
    'armory': Armory(),
    'bridge': Bridge(),
    'escape_pod': EscapePod(),
    'death': Death()
  }
  def __init__(self, start_scene):
    #self.start_screne = Scene()
    self.start_scene = start_scene
    print('Here I am in the ' + self.start_scene)

  def next_scene(self, scene_name):
    print("next_scene input: '%s'" % scene_name)
    return Map.scenes.get(scene_name)

  def opening_scene(self):
    return self.start_scene

current_loc = 'central_corridor'
my_map = Map(current_loc)
# while True:
#   next_loc = my_map.next_scene(current_loc).enter()
#   current_loc = next_loc
a_game = Engine(my_map)
a_game.play()
