import sys
import pandas as pd
import matplotlib.pyplot as plt

events = open("biosnoop_dump",'r').readlines()
diskEvents = []
for event in events:
  if sys.argv[1] in event:
    diskEvents.append(event)
diskEvents = [event.split() for event in diskEvents]
jbdEvents = []
currJDB = 0
currFixed = 0
fixedEvents = []
for event in diskEvents:
  if 'jbd' in event[1]:
    currJDB += int(event[6])
    jbdEvents.append([float(event[0]), currJDB])
  else:
    currFixed += int(event[6])
    print(event)
    fixedEvents.append([float(event[0]), currFixed])

jbd = pd.DataFrame(jbdEvents, columns=['ts','bytes'])
fixed = pd.DataFrame(fixedEvents, columns=['ts','bytes'])

fig, ax = plt.subplots()

ax.plot(jbd['ts'],jbd['bytes'], label = 'Journal')
ax.plot(fixed['ts'],fixed['bytes'], label = 'fixed postion')
ax.grid(True)
ax.legend()
plt.show()
