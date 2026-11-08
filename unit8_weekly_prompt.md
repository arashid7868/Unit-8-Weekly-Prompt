# Unit 8: Weekly Prompt — Question 2

Question 2: Create different histogram charts for rolling two six-sided die, or two eight-sided die. Use the example from the textbook resources, “dice_visual.py.” Discuss the     differences and similarities of the distribution of the results. In general, how does this correlate with the distribution of two n-sided die. Search for relevant discussions on the internet.

## Answer

To examine the distribution of rolling two dice, I used a Python simulation to generate 100,000 rolls for two six-sided dice and two eight-sided dice. The two dice were rolled, and the total of the two dice is shown in histograms. The random module in Python can be used to generate random integers for a given range of values, and the hist() function in Matplotlib groups numerical observations into bins and plots the number of observations in each bin (Matplotlib Development Team, n.d.; Python Software Foundation, n.d.).

Both simulations show a similar overall pattern: The frequency distribution is somewhat symmetrical, with the major frequencies occurring in the vicinity of the middle possible sum. Two dice add to a total that can be anywhere from 2 up to 12, with 7 being the most favorable total. 6 combinations make sums equal to 7; 1 for the sum of 2 and 1 for the sum of 12. If the two dice are 8-sided, the sum can be 2, 3, 4, ..., 16, with 9 being the most likely sum due to the fact that there are 8 ways this sum can be achieved. It is this reason that the histograms are rising towards the middle and falling towards the extremes. Middle sums of two dice have more possible combinations than extreme sums, as the number of combinations for all sums is calculated using the theoretical probability distribution for two dice (Diez et al., 2022).

The distinction is that there are a multitude of possibilities and a range of outcomes. Two dice with six faces and two dice with eight faces have 11 and 15 different possible sums, respectively. This results in a broader distribution with an overall triangular shape of the eight-sided dice. For two fair (n)-sided dice, if the dice are numbered from 1 to (n), the sum of the dice can be any value between 2 and (2n), with the most likely sum being (n+1). The number of combinations rises toward the middle and falls symmetrically from the middle back to the minimum. Overall, this simulation illustrates that the frequency of randomly repeated experiments can be an approximation to a theoretical probability distribution and that histograms are useful in making patterns easier to interpret in numerically based data.

## References

Diez, D. M., Barr, C. D., & Çetinkaya-Rundel, M. (2022). 2.1: Defining probability. OpenIntro Statistics. Statistics LibreTexts. https://stats.libretexts.org/Bookshelves/Introductory_Statistics/OpenIntro_Statistics_(Diez_et_al)./02%3A_Probability/2.01%3A_Defining_Probability

Matplotlib Development Team. (n.d.). matplotlib.pyplot.hist. Matplotlib documentation. https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html

Python Software Foundation. (n.d.). random — Generate pseudo-random numbers. Python documentation. https://docs.python.org/3/library/random.html
