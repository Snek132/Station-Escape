import random
import time
import sys
















# Game state
inventory = []
game_state = {
  "oxygen_level": 100,
  "ethics_score": 0,
  "location": "damaged_room",
  "endings": {
      "good": "You successfully escaped the station. You were lucky to survive, but you'll never forget the friends you lost.",
      "heroic": "You sacrificed yourself to save the others. Your bravery will be remembered, so you smile as the world fades around you, knowing you did the right thing.",
      "cowardly": "You escaped, but at the cost of your fellow crew members' lives.",
      "failure": "You made a valiant effort, but it wasn't enough. This station will be your grave.",
      "short": "You didn't even try. You just gave up. You're a coward."
  }
}
















def print_slow(text):
  #Print text slowly for dramatic effect
  for char in text:
      sys.stdout.write(char)
      sys.stdout.flush()
      time.sleep(0.02)
  print()
















def end_game(ending_type):
   # Handle game ending
   print_slow("\n" + game_state["endings"][ending_type])
   print_slow("Your ethics score: " + str(game_state["ethics_score"]))
  
   choice = input("\n1. Play again\n2. Quit\nChoice (1/2): ")
   if choice == "1":
       print_slow(random.choice(["Here we go again...","Another try can't hurt...","What do you gain from this...","Sure, waste your time...","Really?...","Good luck...","Why are you still here?..."]))
       # Reset inventory
       inventory = []
       start_game()
   else:
       print_slow("Quitter >:(")
       sys.exit()








def examine_room():
  #Pathway A: Examine the Room
  print_slow("\nYou carefully examine the damaged room...")
  print_slow("You find data logs mentioning a crew member who needs help.")
  print_slow("\nYou also find two items: an oxygen mask and a wrench.")
  print_slow("You can only carry one.")
   choice = input("\n1. Take oxygen mask\n2. Take wrench\nChoice (1/2): ")
  if choice == "1":
      inventory.append("oxygen_mask")
      print_slow("You picked up the oxygen mask.")
  elif choice == "2":
      inventory.append("wrench")
      print_slow("You picked up the wrench.")
  elif choice == "stop":
       end_game("short")
  else:
       print_slow("Invalid choice. Try again.")
       examine_room()
















  print_slow("\nDo you help the crew member or prioritize escape?")
  choice = input("\n1. Help crew member\n2. Prioritize escape\nChoice (1/2): ")
  while True:
   if choice == "1":
       follow_crew_member()
   elif choice == "2":
       clear_debris()
   elif choice == "stop":
       end_game("short")
   else:
       print_slow("Invalid choice. Try again.")






def clear_debris():
  #Pathway B: Clear the Debris
  print_slow("\nYou enter a vent system...")
  if "wrench" in inventory:
      print_slow("Using the wrench, you clear the debris and find a maintenance hatch.")
      print_slow("Inside, you discover a laser cutter.")
      choice = input("\n1. Switch wrench for laser cutter\n2. Keep wrench\nChoice (1/2): ")
      if choice == "1":
          inventory.remove("wrench")
          inventory.append("laser_cutter")
      elif choice == "2":
             print_slow("You keep the wrench.")
      elif choice == "stop":
           end_game("short")
      else:
           print_slow("Invalid choice. Try again.")
           clear_debris()


      while True:
       print_slow("\nWhich path do you take?")
       choice = input("\n1. Return to the communication terminal\n2. Explore further through sealed sections\nChoice (1/2): ")
       if choice == "1":
           repair_terminal()
       elif choice == "2":
           explore_further()
       elif choice == "stop":
           end_game("short")
       else:
           print_slow("Invalid choice. Try again.")
  else:
      print_slow("Without tools, you're trapped. The vent floor caves in...")
      end_game("failure")
















def explore_further():
  #Handle exploration path to escape pods
  print_slow("\nYou encounter a sealed bulkhead blocking your path...")
  if "laser_cutter" in inventory:
      print_slow("Using the laser cutter, you carefully cut through the wall.")
      print_slow("Beyond, you find the escape pod bay!")
      navigate_escape_pods()
  else:
      print_slow("The wall is too thick to breach without proper tools.")
      print_slow("You have to turn back...")
      repair_terminal()
















def repair_terminal():
  #Pathway C: Repair the Communication Terminal
  if "wrench" in inventory:
      print_slow("\nYou use the wrench to repair the terminal.")
      print_slow("Do you want to send a distress signal or preserve life support?")
      choice = input("\n1. Send distress signal\n2. Preserve life support\nChoice (1/2): ")
      if choice == "1":
          if random.random() < 0.25:
              print_slow("The distress signal was received.\nHelp soon arrives, and you are able to return to the Earth.")
              end_game("good")
          else:
              print_slow("You were too far away from any rescue ships, or maybe they just didn't care.")
              end_game("failure")
      elif choice == "2":
          investigate_core()
      elif choice == "stop":
           end_game("short")
      else:
           print_slow("Invalid choice. Try again.")
           repair_terminal()


  else:
      print_slow("Without the necessary tools, you can't repair the terminal. The AI core detects unwanted interference and locks down the room. You have no food, no water, and no way out.")
      end_game("failure")
















def follow_crew_member():
  #Pathway A2: Follow Crew Member's Advice
  print_slow("\nThe dying crew member shares information about the escape pods...")
  if "oxygen_mask" in inventory:
      print_slow("To get there, you'll need to navigate through some low-oxygen areas.")
      navigate_escape_pods()
  else:
      print_slow("The path to the escape pods goes through a low-oxygen area. You suffocate before you can reach them.")
      end_game("failure")
















def navigate_escape_pods():
  #Handle escape pod sequence
  print_slow("\nYou reach the escape pod bay, but there's only one left. You can hear the others making their way here, but it only has enough rations for 1 person's trip back to Earth...")
  choice = input("\n1. Take pod for yourself\n2. Leave it for others\nChoice (1/2): ")
  if choice == "1":
      game_state["ethics_score"] -= 1
      print_slow("You take the escape pod for yourself, leaving the others behind with no way out.")
      end_game("cowardly")
  elif choice == "2":
      game_state["ethics_score"] += 2
      print_slow("You leave the escape pod for the others, knowing that you've lived a rich life already.")
      end_game("heroic")
  elif choice == "stop":
       end_game("short")
  else:
       print_slow("Invalid choice. Try again.")
       navigate_escape_pods()














def investigate_core():
  #Handle station core sequence
  print_slow("\nYou discover that the station's AI core is malfunctioning, causing the station to slowly self-destruct. You can try to save everyone, but it's risky.")
  choice = input("\n1. Shut down AI\n2. Use AI to escape\nChoice (1/2): ")
  if choice == "1":
      game_state["ethics_score"] += 2
      print_slow("You shut down the AI, stopping the station's destruction, but you're trapped inside the main computer.")
      end_game("heroic")
  elif choice == "2":
      game_state["ethics_score"] -= 1
      print_slow("You use the AI's resources to escape, but the toll on the station's hardware is too much for it to bear. As you leave, you see the station burst into flames.")
      end_game("cowardly")
  elif choice == "stop":
      end_game("short")
  else:
       print_slow("Invalid choice. Try again.")
       investigate_core()
















def start_game():
  #Initialize and start the game
  print_slow("\nStation Escape: A short choice-based story by Sanchit Dhingra and Vedant Dhingra")
  print_slow("You can end the game at any time by typing 'stop'.")
  print_slow("\nYou wake up in a damaged room. Alarms are blaring...")
  print_slow("A distorted voice crackles over the comm system...")
















  while True:
      choice = input("\n1. Examine the room\n2. Check communication terminal\nChoice (1/2): ")
      if choice == "1":
          examine_room()
          break
      elif choice == "2":
          repair_terminal()
          break
      elif choice == "stop":
          end_game("short")
          break
      else:
          print_slow("Invalid choice. Try again.")
















if __name__ == "__main__":
  start_game()
