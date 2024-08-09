gadgets = [("Explosive Batarangs", 3, True), ("Batarangs", 5, True), ("Smoke Pellets", 0, False),
           ("Tear Gas Grenades", 2, True),("Night Vision Goggles", 1, True),("Batclaw", 0, False),
           ("Grapple Gun", 3, True), ("Batsignal", 0, False), ("Utility Belt", 1, True),
           ("Batmobile Tires", 4, True)]

gadgets.sort(key=lambda a: (-a[2],-a[1],a[0]))
print('The gadgets list in sorted order is:')
print(gadgets)