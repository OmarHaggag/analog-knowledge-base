



This version (20 Jan 2021 14:51) was *approved* by [Doug Mercer](https://ez.analog.com/members/dmercer).The [Previously approved version](/university/courses/electronics/text/chapter-16?rev=1391799132) (07 Feb 2014 18:52) is available.[![Diff](/lib/images/diff.png)](https://wiki.analog.com/university/courses/electronics/text/chapter-16?do=diff&rev2[0]=1391799132&rev2[1]=1611154273&difftype=sidebyside)

### Table of Contents



* [Chapter 16: Advanced Amplifier topics:](#chapter_16advanced_amplifier_topics)
	+ [16.1 Improvements to the emitter follower](#improvements_to_the_emitter_follower)
	+ [16.2 Complementary Feedback Pair Emitter Follower](#complementary_feedback_pair_emitter_follower)
		- [16.2.1 FET Source Followers](#fet_source_followers)
		- [16.2.2 The Body effect](#the_body_effect)
	+ [16.3 Improved series voltage regulator](#improved_series_voltage_regulator)
		- [16.3.1 Transistor based Capacitance multiplier](#transistor_based_capacitance_multiplier)
		- [16.3.2 Adding an output current limit](#adding_an_output_current_limit)
	+ [16.4 Single Transistor high pass filter](#single_transistor_high_pass_filter)
	+ [16.5 Frequency Multiplication](#frequency_multiplication)





# Chapter 16: Advanced Amplifier topics:




In this chapter we will explore a few circuit techniques involving multiple transistors that are beyond the basic configurations we discussed in earlier chapters.




## 16.1 Improvements to the emitter follower




The incremental voltage gain, AV, (VOUT / VIN) of the emitter follower should ideally be 1 but will always be slightly less than 1. The gain is generally given by the following equation:




[![](/_media/university/courses/electronics/text/chptr16_e1.png?w=120&tok=434f8c)](/_detail/university/courses/electronics/text/chptr16_e1.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-16 "university:courses:electronics:text:chptr16_e1.png")




From the equation we can see that in order to obtain a gain close to one we can either increase RL or decrease re. We also know that re is a function of IE and that as IE increases re decreases. Also from the circuit, figure 16.1(a) we can see that IE is related to RL and that as RL increases IE decreases for a fixed supply voltage. These two effects work counter to each other in the simple resistively loaded emitter follower. Thus to optimize the gain of the follower we need to explore ways to either decrease re or increase RL without effecting the other.




Looking at the follower in another way, because of the inherent DC shift due to the transistor's VBE, the difference between input and output should be constant over the intended signal swing. Due to the simple resistive load RLin figure 16.1(a), the emitter current IE increases and decreases as the output swings up and down. We know that VBE is an exponential function of IE and will change approximately 18 mV (at room temperature) for a factor of 2 change in IE. Given RL = 2.2KΩ and a +/- 2V swing and an 8V total supply voltage, ( V+ = +4V and V- = -4V ), the minimum IE= 2V/2.2KΩ or 0.91 mA and the maximum IE= 6V/2.2KΩ or 2.7 mA. This results in a difference of 1.8 mA and results in a 28 mV change in VBE. This observation leads us to the first possible improvement in the emitter follower shown in figure 16.1(b).




[![](/_media/university/courses/electronics/text/chptr16_f1.png?w=600&tok=4151f5)](/_detail/university/courses/electronics/text/chptr16_f1.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-16 "university:courses:electronics:text:chptr16_f1.png")





 Figure 16.1 Emitter follower with current source load. 





The current mirror from chapter 11 can be substituted for the emitter load resistor to supply a fixed emitter current to the amplifier transistor, figure 16.1(b). A current mirror will sink a more or less constant current over a wide range of voltages. Ignoring any current in an external load on VOUT, this more or less constant current flowing in transistor Q1 will result in a more or less constant VBE. 




Viewed another way, the very high output resistance of the current source has effectively increased RL while re remains at a low value set by the current IE. We saw in Chapter section 11.5.3 on the output resistance of the current mirror that the use of emitter degeneration resistors can greatly increase rObeyond that set by the transistor's Early voltage VA.




## 16.2 Complementary Feedback Pair Emitter Follower




An alternate approach to improving the emitter follower is to reduce the effective re through negative feedback. Reducing re can be addressed by adding a second transistor to increase the negative feedback factor by increasing the open-loop-gain. The single transistor is replaced by a pair of transistors with 100% voltage feedback to the emitter of the first transistor. This is often referred to as a complementary feedback pair as shown in figure 16.2.




[![](/_media/university/courses/electronics/text/chptr16_f2.png?w=600&tok=8aa4f0)](/_detail/university/courses/electronics/text/chptr16_f2.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-16 "university:courses:electronics:text:chptr16_f2.png")





 Figure 16.2 Complementary Feedback Pair Emitter Follower 





The value of R1 is crucial to good linearity, as it sets the IC of transistor Q1. The collector current of Q1 will be approximately equal to the VBE of Q2 divided by R1. This current in Q1 will be relatively more constant than the current in RL. The majority of the variable current in RL (as VOUT changes) will flow in Q2 rather than Q1. Resistor RL can of course be additionally replaced with a constant current source as a further improvement as we just saw in section 16.1.




An important consequence of adding the complementary transistor Q2 is that it further limits the maximum positive output swing. In the simple emitter follower of figure 16.1(a) the output can swing no higher than V+ - VBEQ1. Whereas the output of the follower in figure 16.2 can swing no higher than V+ - VBEQ1 - VBEQ2 and have the collector base junctions of the transistors remain reverse biased.




### 16.2.1 FET Source Followers




It is important to note that the gain equation for FET based source followers is much the same as for BJT based followers substituting the small signal source resistance rs.




[![](/_media/university/courses/electronics/text/chptr16_e2.png?w=125&tok=5b2447)](/_detail/university/courses/electronics/text/chptr16_e2.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-16 "university:courses:electronics:text:chptr16_e2.png")




We also know that the small signal source resistance is a function of the DC drain current ID so using these same circuit techniques to keep ID more constant with changes in the load current will improve the performance of FET based followers as well.




### 16.2.2 The Body effect




All MOS transistors have a fourth terminal which must be considered when designing circuits that use these devices. An additional effect that limits the gain accuracy of a FET based source follower comes from possible changes in the voltage on this fourth terminal, often called the body or back-gate, in cases where the body or substrate is connected to the fixed negative power supply ( for NMOS devices or positive supply for PMOS devices ) rather than the source. 




The body effect refers to the change in the threshold voltage, Vth, by the change in VSB, the source to back-gate voltage. Because the voltage on the back-gate influences the threshold voltage (when it is not tied to the source), it can be thought of as a second gate. The body effect is sometimes called the “back-gate effect”.




For an enhancement mode, NMOS device the body effect upon threshold voltage is calculated by applying the Shichman-Hodges model using the following equation:




![V_TB=V_TO +\gamma (\sqrt {{V_SB + 2\phi _F}}-{\sqrt {2\phi _F}})](/lib/plugins/mathpublish/img.php?img=6b9ebdca46b431cec74c4a85a734e58d "V_TB=V_TO +\gamma (\sqrt {{V_SB + 2\phi _F}}-{\sqrt {2\phi _F}})")




Where:  

VTB is the threshold voltage when substrate bias is present,  

VSB is the source-to-body substrate bias  


2fF is the surface potential  

VTO is threshold voltage for zero substrate bias




The body effect parameter:




![\gamma = (t_ox)/(\epsilon _ox) {\sqrt {2q\epsilon _si N_A}}](/lib/plugins/mathpublish/img.php?img=6dddb0f348cad7cbf338a0a7c1a277d9 "\gamma = (t_ox)/(\epsilon _ox) {\sqrt {2q\epsilon _si N_A}}")




Where:  


tox is oxide thickness  


εox is oxide permittivity  


εsi is the permittivity of silicon  


NA is a doping concentration  


q is the charge of an electron




## 16.3 Improved series voltage regulator




Back in chapter 6 we briefly looked at the zener diode as a shunt regulator figure 16.3(a). If we incorporate an emitter follower transistor stage in place of the series resistor we can greatly improve the load regulation performance of the regulator. Adding an emitter follower stage to the simple Zener regulator as shown in figure 16.3(b) forms a simple series voltage regulator and substantially improves the regulation of the circuit. Here, the load current IRL is supplied by the transistor whose base is now connected to the Zener diode. Thus the transistor's base current (IB) is the only variable current flowing in the Zener diode and is smaller than the current through RL by the ß or current gain of the emitter follower. This regulator is classified as “series” because the regulating element, the transistor, appears in series with the load. R1 sets the Zener current (IZ) and is determined as:




![R_1=(V_S-V_Z)/(I_Z+KI_B )](/lib/plugins/mathpublish/img.php?img=105ed2029fe5164e5d5a58266de7c8a4 "R_1=(V_S-V_Z)/(I_Z+KI_B )")




where, VZ is the Zener voltage, IB is the transistor's base current and K is a scaling factor of 1.2 to 2 to ensure that R1 is low enough for the maximum IB under heavy output load currents.




![I_B=I_L/ß](/lib/plugins/mathpublish/img.php?img=27ef6b4700fe139da314736fa0b87618 "I_B=I_L/ß")




where:  


IL is the required load current, also the transistor's emitter current (assumed to be approximately equal to the collector current)  


ß(min) is the minimum acceptable DC current gain for the transistor.




[![](/_media/university/courses/electronics/text/chptr16_f3.png?w=600&tok=118514)](/_detail/university/courses/electronics/text/chptr16_f3.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-16 "university:courses:electronics:text:chptr16_f3.png")





 Figure 16.3.1 Improved zener voltage regulator 





This circuit has much better load regulation than the simple Zener shunt regulator, since the base current of the transistor forms a very light load on the Zener, thereby minimizing variation in the Zener voltage due to variation in the load. It is also useful to note here that the output voltage would now be about 0.65V less than VZ due to the transistor's VBE drop if we did not include the extra diode D1 in series with the zener. The voltage drop across D1 can be thought to be approximately the same as the VBE of Q1. A second diode connected NPN transistor similar to Q1 used in place of D1 would provide a better approximation. Although this circuit has good regulation, it is still somewhat sensitive to the load and supply variation. This can be further improved by incorporating negative feedback. This simple regulator is often used as a “pre-regulator” in more advanced linear voltage regulator circuits.




The circuit can be made adjustable by adding a variable resistor as a voltage divider across the Zener, moving the transistor base connection from the top of the Zener to the potentiometer wiper. Another way to make the output voltage adjustable in steps is by switching in Zeners with different breakdown voltages.




### 16.3.1 Transistor based Capacitance multiplier




In a related power supply circuit shown in figure 16.3.2 the effective capacitance of capacitor C1is multiplied by the transistor's current gain (β).




[![](/_media/university/courses/electronics/text/chptr16_f4.png?w=600&tok=e1b373)](/_detail/university/courses/electronics/text/chptr16_f4.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-16 "university:courses:electronics:text:chptr16_f4.png")





 Figure 16.3.2 Transistor based Capacitance multiplier 





R1 and C1 form a low-pass filter that helps smooth any ripple on VSsuch as from a full wave rectifier. R1 supplies the charging current as well as the transistor's (Q1) base current. RL is the load on the circuit. Without Q1, RL would be the load on the capacitor and C1 would have to be very large to maintain low ripple. With Q1 in place, the loading imposed upon C1 is simply the load current reduced by a factor of β. Conversely, C1 appears “multiplied” by a factor of β to the load.




Note that this circuit is not a voltage regulator, since the output voltage varies directly with the input VIN. The output voltage is less than the base voltage by VBE (about 0.65V). The Base will be less than VS (when loaded) by the base current times R1. Larger values of R1 (and C1) reduce the output ripple to almost negligible levels. On the downside this causes the output to rise slowly towards the required value (especially when the load is connected), due to the larger time constant of R1 and C1. However the circuits of figure 16.3.1 and figure 16.3.2 could be combined to provide improved filtering and voltage regulation.




### 16.3.2 Adding an output current limit




A current limiting circuit is an essential element of any power supply. There is always a risk that the load may draw too much current or the power supply rails may even get accidentally shorted. The inclusion of a current limiter circuit will prevent any further damage occurring to the external circuit as well as preventing damage to the power supply itself.




It is possible to implement a power supply current limiter with just diodes, but the one we will be looking at here uses a single transistor and a current sense resistor. This circuit forms the basis of most power supply current limiter designs used today and is commonly used to limit the current in the output stage of operational amplifiers. The limiting circuit consisting of Q2 and R2 is incorporated into the simple regulator circuit shown in figure 16.3.3.




The operation of the current limiter is very straightforward. When the power supply is supplying current below the maximum level, current flows through the sense resistor and a small potential difference develops across it. The value of the resistor is chosen so that when the maximum allowable current flows from the power supply, a voltage equal to the VBE of the current sense transistor, Q2, is developed across it. This is typically 0.6 volts, assuming that a silicon transistor is used.




As the voltage across the current sense resistor approaches 0.6 volts, the current sense transistor starts to turn on. When it does, the voltage at the base of the main power supply pass transistor is pulled down, thereby preventing any increase in the output current of the power supply. In this way it is very easy to calculate the value for the sense resistor using Ohms Law. It is simply VBE / ILmax. The current sense transistor, Q2, should have a sufficiently large current capacity to be able to take away all the current from the base of the main series pass transistor.




[![](/_media/university/courses/electronics/text/chptr16_f5.png?w=600&tok=e4ae6e)](/_detail/university/courses/electronics/text/chptr16_f5.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-16 "university:courses:electronics:text:chptr16_f5.png")





 Figure 16.3.3 Power supply regulator with feedback and transistor current limiting 





In view of the fact that the regulator sense point occurs after the current sense resistor, any voltage drop across the resistor will not affect the output voltage of the circuit as this will be compensated for by the regulator. This assumes that the input supply voltage is sufficiently large enough for the circuit to regulate correctly. In this way the current sense resistor will not cause any reduction in the voltage output from the power supply regulator circuit.




The power supply current limiter circuit is shown within the circuit of a very simple regulator. However it can be placed within most regulator circuits made from discrete components with little change. For circuits using integrated circuit regulators, they are virtually certain to contain current limiter circuitry based around this principle.




## 16.4 Single Transistor high pass filter




It is sometimes desirable to design a simple active high pass filter using a single transistor amplifier stage. The transistor filter circuit shown in figure 16.4 provides a two pole filter with unity gain. This filter is convenient to place in a larger circuit because it contains few components and does not occupy much space.




The active high pass transistor circuit is quite straightforward, using just a total of four resistors, two capacitors and a single transistor. The operating conditions for the transistor are set up in the normal way. R2 and R3 are used to set up the bias point for the base of the transistor. The resistor RL is the emitter resistor and sets the current for the transistor.




The filter components are included in negative feedback from the output of the circuit to the input. The components that form the active filter network consist of C1, C2, R1 and the combination of R2 and R3 in parallel, assuming that the input resistance to the emitter follower circuit are very high and can be ignored.




[![](/_media/university/courses/electronics/text/chptr16_f6.png?w=500&tok=e78f37)](/_detail/university/courses/electronics/text/chptr16_f6.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-16 "university:courses:electronics:text:chptr16_f6.png")





 Figure 16.4 Transistor active high pass filter circuit 





![C_1 = 2 * C_2](/lib/plugins/mathpublish/img.php?img=bbdb7370ad7c3cb3d6f4a59b7c381272 "C_1 = 2 * C_2")




![R_1 = R_2 * R_3 /(R_2 + R_3)](/lib/plugins/mathpublish/img.php?img=a6d9bf56211094604d59bd0fd98a43bd "R_1 = R_2 * R_3 /(R_2 + R_3)")




This is for values where the effect of the emitter follower transistor itself within the high pass filter circuit can be ignored, i.e.:




![R_L (β+1) >> R_2 * R_3 /(R_2 + R_3 )](/lib/plugins/mathpublish/img.php?img=1c1d9bc831cbc2c36dfc99b9dba88916 "R_L (β+1) >> R_2 * R_3 /(R_2 + R_3 )")




![f_o = 1.414 / (4 π R_1 C_2)](/lib/plugins/mathpublish/img.php?img=33f81e917d7e113ea8148c1eb2ce8a93 "f_o = 1.414 / (4 π R_1 C_2)")




Where:  


β = the forward current gain of the transistor  


fo = the cut-off frequency of the high pass filter  


π = equal to 3.14159




The equations for determining the component values provide a Butterworth response, which provides maximum flatness within the pass-band at the expense of achieving the ultimate roll off as quickly as possible. This has been chosen because this form of filter suits most applications and the mathematics works out easily.




## 16.5 Frequency Multiplication




Frequency Multipliers are a special class of amplifiers that are biased at 3 to 10 times the normal cutoff bias. They are used to generate a frequency that is a multiple (harmonic) of a lower frequency. Such circuits are called frequency multipliers or harmonic generators.




Figure 16.5.1 illustrates a frequency multiplier known as a Frequency Doubler or Second Harmonic Generator. As illustrated, the input is 10 KHz and the output is 20 KHz, or twice the input frequency. In other words, the second harmonic of 10 KHz is 20 KHz. The third harmonic (frequency tripler) would be 30 KHz, or 3 times the input signal. The fourth harmonic (quadruplet) would be 40 KHz, or 4 times the 10 KHz input signal. The fifth harmonic (frequency quintupler) is normally as high in multiplication as is practical, because at harmonics higher than the fifth, the output diminishes to a very weak signal.




[![](/_media/university/courses/electronics/text/chptr16_f7.png?w=600&tok=bd8a68)](/_detail/university/courses/electronics/text/chptr16_f7.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-16 "university:courses:electronics:text:chptr16_f7.png")





 Figure 16.5.1, Frequency multiplication using single transistor 





Frequency multipliers are operated by the pulses of collector current produced by a class C amplifier. Although the collector current flows in pulses, the alternating collector voltage is sinusoidal because of the action of the tank circuit. With the output tank circuit tuned to the required harmonic, the tank circuit acts as a filter, accepting the desired frequency and rejecting all others.




[![](/_media/university/courses/electronics/text/chptr16_e4.png?w=150&tok=04165e)](/_detail/university/courses/electronics/text/chptr16_e4.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-16 "university:courses:electronics:text:chptr16_e4.png")




The following circuit, figure 16.5.2, is a better frequency multiplier using an NPN differential amplifier with an LC resonate output load. With the component values shown in the figure, the output level is about 4V p-p at 33 KHz with a 1v p-p, 11 KHz input. Other frequencies and multiplication factors are possible by adjusting the resonate frequency of the L1,C1tank.




[![](/_media/university/courses/electronics/text/chptr16_f8.png?w=600&tok=c87cb7)](/_detail/university/courses/electronics/text/chptr16_f8.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-16 "university:courses:electronics:text:chptr16_f8.png")





 Figure 16.5.2, Improved Frequency Multiplier. 





Amplitude modulation may be applied to the output frequency by capacitor coupling the modulating (audio) signal to base of current source transistor Q3.




Figure 16.5.3 illustrates the waveforms in a typical circuit. You can see that the pulses of collector current are the same frequency as the input signal. These pulses of collector current energize the tank circuit and cause it to oscillate at twice the base signal frequency. Between the pulses of collector current, the tank circuit continues to oscillate. Therefore, the tank circuit receives a current pulse for every other cycle of its output




Figure 16.5.3




**Return to [Previous Chapter](/university/courses/electronics/text/chapter-15 "university:courses:electronics:text:chapter-15")**




**Go to [Next Chapter](https://www.analog.com//media/en/training-seminars/design-handbooks/Basic-Linear-Design/Chapter9.pdf "https://www.analog.com//media/en/training-seminars/design-handbooks/Basic-Linear-Design/Chapter9.pdf")**




**Return to [Table of Contents](/university/courses/electronics/text/electronics-toc "university:courses:electronics:text:electronics-toc")**






university/courses/electronics/text/chapter-16.txt · Last modified: 20 Jan 2021 14:51 by [Doug Mercer](https://ez.analog.com/members/dmercer)

