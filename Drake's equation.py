# Drake's equation
# N = R∗ * fp * ne * fl * fi * fc * L
# R∗ = the average rate of star formation in our Galaxy.
# fp = the fraction of those stars that have planets.
# ne = the average number of planets that can potentially support life per star that has planets.
# fl = the fraction of planets that could support life that actually develop life at some point.
# fi = the fraction of planets with life that go on to develop intelligent life (civilizations).
# fc = the fraction of civilizations that develop a technology that releases detectable signs of their existence into space.
# L = the length of time for which such civilizations release detectable signals into space.

# R = the rate of star formation in our Galaxy
# 1.5-3.0 is the stars per year
# the average between 1.5 and 3 is 2.25, so that is what I selected as R
R = 2.25

# fp = The fraction of Stars that have planets
# Since all stars have platets the value is 1
fp = 1

# ne is the number of planets that could potentially support life
# ne has ben estimated to have a value between 3-5, so I put 4
ne = 4

# fl = the fraction of planets that could support life that actually develop life at some point.
fl = 1

# fi = the fraction of planets with life that go on to develop intelligent life (civilizations)
# 0.0002 is the number proposed by Pascal Lee of the SETI institute
fi = 0.0002

# fc = the fraction of civilizations that develop a technology that releases detectable signs of their existence into space
fc = 1

# L = the length of time for which such civilizations release detectable signals into space
# This is difficult to determine, 100-0 seems like a reasonable lifespan of a society
L = 1000

N = R * fp * ne * fl * fi * fc * L
print(f"An estimation of Technologically advanced civilazations in our galaxy: {N}")
