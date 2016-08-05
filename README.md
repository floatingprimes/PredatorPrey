# PredatorPrey

For the scenario, our Predator Prey Model is a little more complicated. We will assume that there has been a wide-scale zombie apocalypse in the world. The parties involved will be zombies and humans.


Primary Goal: Design a Dynamic Predator-Prey model utilizing differential equations to animate the overarching relationship.

- There will be user-determined rates which will underscore the outcome of the simulation.
      - To include:
        - Zombification Rate: Rate in which humans turn into zombies (for any given interaction)
        - Zombie Kill Rate: Rate in which humans kill zombies (for any given interaction)
        - Human Birth Rate: Human birth rate per human per month in the world.
        - Human Death Rate: Natural human death rate (non-Zombie related).
        - Zombie Death Rate: Natural zombie death rate (non-Human related).
        - Human Population: Initial human population before interactions occur.
        - Zombie Population: Initial zombie population before interactions occur.

- Note that continuous time is partitioned into discrete monthly units for our simulation

- User also determines the overall scope of the simulation by setting number of months to whatever is desirable

- The equations underscoring the dynamic are taken from the classic Predator-Prey model (proposed by Alfred Lotka, 1910)

- Utilize the scipy library's integration functionality in determining outcome

- Display results in a clear, comprehensive manner for analysis
