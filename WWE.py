# What Should I Do Tonight?

import random


# Our list of friends
people = ["Barrack Obama",
          "Donal Trump",
          "Hillary Clinton",
          "Chris Bryant",
          "Samuel L. Jackson",
          "Kanye West",
          "Eddie Murphy",
          "Shake Shack",
          "The Yeti",
          "Penguin"]
random_person = random.choice(people)


print("Welcome to the WWE! Chris Jericho says %s is on The List !" % (random_person)) 