



This version (07 Oct 2020 14:38) was *approved* by [Doug Mercer](https://ez.analog.com/members/dmercer).The [Previously approved version](/university/courses/electronics/text/chapter-9?rev=1602081449) (07 Oct 2020 14:37) is available.[![Diff](/lib/images/diff.png)](https://wiki.analog.com/university/courses/electronics/text/chapter-9?do=diff&rev2[0]=1602081449&rev2[1]=1602081472&difftype=sidebyside)

### Table of Contents



* [Chapter 9: Single Transistor Amplifier Stages:](#chapter_9single_transistor_amplifier_stages)
	+ [9.1 Basic Amplifiers](#basic_amplifiers)
	+ [9.2 The inverting voltage amplifier or Common emitter/source](#the_inverting_voltage_amplifier_or_common_emittersource)
		- [9.2.1 DC Bias techniques, common emitter/source](#dc_bias_techniques_common_emittersource)
		- [9.2.2 Small signal voltage gain, common emitter or source](#small_signal_voltage_gain_common_emitter_or_source)
		- [9.2.3 Small signal input impedance, common emitter or source](#small_signal_input_impedance_common_emitter_or_source)
		- [9.2.4 Small signal output impedance, common emitter or source](#small_signal_output_impedance_common_emitter_or_source)
		- [9.2.5 common emitter and source Lab Activities](#common_emitter_and_source_lab_activities)
	+ [9.3 The Current Follower also known as Common base or gate amplifier](#the_current_follower_also_known_as_common_base_or_gate_amplifier)
		- [9.3.1 DC Biasing techniques, current follower or common base/gate amplifier](#dc_biasing_techniques_current_follower_or_common_basegate_amplifier)
		- [9.3.2 Small signal voltage gain, current follower or common base/gate amplifier](#small_signal_voltage_gain_current_follower_or_common_basegate_amplifier)
		- [9.3.3 Input impedance, current follower or common base/gate amplifier](#input_impedance_current_follower_or_common_basegate_amplifier)
		- [9.3.4 Output impedance, current follower or common base/gate amplifier](#output_impedance_current_follower_or_common_basegate_amplifier)
		- [9.4 Voltage followers (also called Emitter or Source follower or Common collector or drain amplifiers)](#voltage_followers_also_called_emitter_or_source_follower_or_common_collector_or_drain_amplifiers)
		- [9.4.1 DC Biasing techniques, Voltage Follower or common collector/drain amplifier](#dc_biasing_techniques_voltage_follower_or_common_collectordrain_amplifier)
		- [9.4.2 Voltage gain, common collector or drain amplifier](#voltage_gain_common_collector_or_drain_amplifier)
		- [Example 9.4.2 Calculating the Voltage Gain](#example_942_calculating_the_voltage_gain)
		- [9.4.3 Input impedance, Voltage Follower (common collector or drain)](#input_impedance_voltage_follower_common_collector_or_drain)
		- [9.4.4 Output impedance, Voltage Follower (common collector or drain)](#output_impedance_voltage_follower_common_collector_or_drain)
		- [9.4.5 Voltage Follower (common collector or drain) Lab Activities](#voltage_follower_common_collector_or_drain_lab_activities)
	+ [9.5 Series Feedback: emitter/source degeneration](#series_feedbackemittersource_degeneration)
		- [9.5.1 Small signal voltage gain with emitter/source degeneration](#small_signal_voltage_gain_with_emittersource_degeneration)
		- [9.5.2 Small signal input impedance with emitter/source degeneration](#small_signal_input_impedance_with_emittersource_degeneration)
		- [9.5.3 Small signal output impedance with emitter/source degeneration](#small_signal_output_impedance_with_emittersource_degeneration)
		- [9.5.4 DC Biasing techniques with emitter/source degeneration](#dc_biasing_techniques_with_emittersource_degeneration)
		- [9.5.5 Summary - performing small-signal analyses:](#summary_-_performing_small-signal_analyses)
	+ [9.6 Miller’s Theorem](#miller_s_theorem)
	+ [9.7 Shunt feedback:](#shunt_feedback)
		- [9.7.1 MOS version](#mos_version)
		- [9.7.2 BJT Version DC Biasing techniques](#bjt_version_dc_biasing_techniques)
		- [Example 9.7.2 Using Miller’s Theorem](#example_972_using_miller_s_theorem)
		- [Exercise 9.7](#exercise_97)
		- [9.7.5 The Miller Effect](#the_miller_effect)
		- [Example 9.7.3 Miller Capacitance Example](#example_973_miller_capacitance_example)
	+ [Chapter Summary:](#chapter_summary)
		- [Appendix: Source absorption theorem](#appendixsource_absorption_theorem)
		- [Example A1: Finding the Emitter Resistance using Source absorption theorem](#example_a1finding_the_emitter_resistance_using_source_absorption_theorem)
	+ [Advanced Topics:](#advanced_topics)
		- [AT1 Diode bias generation](#at1_diode_bias_generation)





# Chapter 9: Single Transistor Amplifier Stages:




## 9.1 Basic Amplifiers




The term amplifier as used in this chapter means a circuit (or stage) using a single active device rather than a complete system such as an integrated circuit operational amplifier. An amplifier is a device for increasing the power of a signal. This is accomplished by taking energy from a power supply and controlling the output to duplicate the shape of the input signal but with a larger (voltage or current) amplitude. In this sense, an amplifier may be thought of as modulating the voltage or current of the power supply to produce its output.




The basic amplifier, figure 9.1, has two ports and is characterized by its gain, input impedance and output impedance. An ideal amplifier has infinite input impedance (Rin = ∞), zero output impedance (Rout = 0) and infinite gain (Avo = ∞) and infinite bandwidth if desired.




[![](/_media/university/courses/electronics/text/chptr9-f1.png?w=500&tok=49b00f)](/_detail/university/courses/electronics/text/chptr9-f1.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-9 "university:courses:electronics:text:chptr9-f1.png")





 Figure 9.1 Basic Amplifier Model 





The transistor, as we have seen in the previous chapter, is a three-terminal device. Representing the basic amplifier as a two port network as in figure 9.1, there would need to be two input and two output terminals for a total of four. This means one of the transistor terminals must be common to both the input and output circuits. This leads to the names common emitter, etc. for the three basic types of amplifiers. The easiest way to determine if a device is connected as common emitter/source, common collector/drain, or common base/gate is to examine where the input signal enters and the output signal leaves. The remaining terminal is what is thus common to both input and output. In this chapter we will primarily be using n-type transistors (NPN, NMOS) in the example circuits. The same basic amplifier stages can just as easily be implemented using p-type transistors (PNP, PMOS). When larger multi-stage amplifiers are assembled, both types of transistors are often interspersed with each other. 




Building-block amplifier stages:



1. Inverting voltage amplifier (also called Common emitter or Common source amplifier)
2. Current Follower (also called Common base or Common gate or cascode)
3. Voltage Follower (also called Common collector or Common drain amplifier)
4. Series feedback (more commonly: emitter/source degeneration)
5. Shunt feedback



## 9.2 The inverting voltage amplifier or Common emitter/source




The common emitter/source amplifier is one of three basic single-stage amplifier topologies. The BJT and MOS versions function as an inverting voltage amplifier and are shown in figure 9.2. The base or gate terminal of the transistor serves as the input, the collector or drain is the output, and the emitter or source is common to both input and output (it may be tied to the ground reference or the power supply rail), which gives rise to its common name. 




[![](/_media/university/courses/electronics/text/chptr9-f2.png?w=500&tok=bab15c)](/_detail/university/courses/electronics/text/chptr9-f2.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-9 "university:courses:electronics:text:chptr9-f2.png")





 Figure 9.2: Basic n-type inverting voltage amplifier circuit (neglecting biasing details) 





The common emitter or source amplifier may be viewed as a transconductance amplifier (i.e. voltage in, current out) or as a voltage amplifier (voltage in, voltage out). As a transconductance amplifier, the small signal input voltage, vbe for a BJT or vgs for a FET, times the device transconductance gm, modulates the amount of current flowing through the transistor, ic or id. By passing this varying current through the output load resistance, RL it will be converted back into a voltage Vout. However, the transistor’s small signal output resistance, ro, is not typically high enough for a reasonable transconductance amplifier (ideally infinite). Nor is the output load, RL, low enough for a decent voltage amplifier (ideally zero). Another major drawback is the amplifier’s limited high-frequency response due in part to the built in collector base or drain gate capacitance inherent to the transistor. More on how this capacitance effects the frequency response in a later section of this chapter. Therefore, in practice the output often is routed through either a voltage follower (common collector or drain stage), or a current follower (common base or gate stage), to obtain more favorable output and frequency characteristics. This latter combination is called a cascode amplifier as we will see later in the chapter on multi-stage amplifiers. 




In comparison to the BJT common emitter amplifier, the FET common source amplifier has higher input impedance. The generally lower gmof the FET vs. the BJT at equal current levels leads to lower voltage gain for the MOS version. 




### 9.2.1 DC Bias techniques, common emitter/source




In order for the common emitter or source amplifier to provide the largest output voltage swing, the voltage at the Base or Gate terminal of the transistor is offset in such a way that the transistor is nominally operating halfway between its cut-off and saturation points. Note the NMOS (a) and NPN (b) characteristic curves in figure 9.2.1. This allows the amplifier stage to more accurately reproduce the positive and negative halves of the input signal superimposed upon the DC Bias voltage. Without this offsetting Bias Voltage only the positive half of the input waveform would be amplified. 




[![](/_media/university/courses/electronics/text/chptr9-f3.png?w=500&tok=dfce17)](/_detail/university/courses/electronics/text/chptr9-f3.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-9 "university:courses:electronics:text:chptr9-f3.png")





(a) NMOS





[![](/_media/university/courses/electronics/text/chptr9-f4.png?w=500&tok=662cbe)](/_detail/university/courses/electronics/text/chptr9-f4.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-9 "university:courses:electronics:text:chptr9-f4.png")





(b) NPN





 Figure 9.2.1 (a) ID vs. VDScurves and (b) IC vs. VCE curves





The red line superimposed on the two sets of curves represents the DC load line of a 400 ohm RL. To maximize the output swing it is desirable to set the operating point of the transistor, with a zero input signal, at a drain or collector voltage of one half the supply voltage, which would be 4 volts in this case. Finding the corresponding drain or collector current along the load line gives us the target current level. This is around 10mA for RL equal to 400 ohms. The next step is to determine the corresponding VGS or IB for a 10mA ID or IC. In the NMOS example each curve represents a different VGS from 0.9 volts to 1.5 volts in 0.1 volt steps. The NMOS device used in this example has a transconductance of about 40mA/V. The ID equal to 10mA point on the load line falls between the 1.4V and 1.3V curves or a VGS of 1.32V. In the NPN example each curve represents a different IB from 10uA to 100uA in 10uA steps. The 50uA curve happens to cross the load line at IC =10mA. The β of the transistor must therefore be about 200. The task now is to somehow provide this DC offset or bias at the Gate or Base of the transistor.




The first bias technique we will explore is called voltage divider bias and is shown in figure 9.2.2. If we choose the correct resistor values for R1 and R2 that will result in a collector or drain current such that one half of the supply voltage, V+ appears across RL we should have our desired value of VGS or VBE (IB) for biasing with no signal input. For the MOS case we know that no current flows into the gate so the simple voltage divider ratio can be used to pick R1 and R2. If V+ = 8V and we want VGS to equal 1.32 V then:




[![](/_media/university/courses/electronics/text/chptr9-e1.png?w=180&tok=cc3cb0)](/_detail/university/courses/electronics/text/chptr9-e1.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-9 "university:courses:electronics:text:chptr9-e1.png")




The actual values of R1 and R2 are not so important just their ratio. However, the divider ratio we choose will be correct for only one set of conditions of power supply voltage, transistor threshold voltage and transconductance, and temperature. Actual designs often use more involved bias schemes.




[![](/_media/university/courses/electronics/text/chptr9-f5.png?w=500&tok=da28a1)](/_detail/university/courses/electronics/text/chptr9-f5.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-9 "university:courses:electronics:text:chptr9-f5.png")





Figure 9.2.2 Voltage divider bias





For the NPN case the calculation is somewhat more involved. We know we want IB to be equal to 50uA. The current that flows in R1 is the sum of the current in R2 and IB which puts an upper bound on R1 when R2 is infinite and no current flows in R2. If we assume a nominal VBE of 0.65 volts then R1 must be no larger than 7.35V/50uA or 147KΩ. The purpose of the voltage divider is to attenuate the variations in V+ and thus make the DC operating point of the transistor less sensitive to V+. To that end we need to make the current in R2 many times larger than IB. If we, for example, choose to make IR2 9 times IB then the current in R1 will be 10\*IB or 500uA. R1 will be 1/10 what we just calculated as the upper bound or 14.7KΩ. R2 will be VBE divided by 450uA or 1.444KΩ which is a divider ratio of 0.8921. If we had simply used 8V-VBE/8V as the ratio (assume VBE = 0.65V) the divider ratio would have been 0.8125. Taking IB into account shifted the required ratio. These values would need to be adjusted slightly if the actual VBE was not the 0.65 volts (or β was not 200) we used in this calculation. This points out a major limitation of this bias scheme as we pointed out in the MOS example above. That is the sensitivity to device specific characteristics like VBE and β as well as supply voltage and temperature.




A consequence of including this bias scheme is a lowering of the input impedance. The input now includes the parallel combination of R1 and R2 across the input. For the MOS case this now sets the input resistance. For the BJT case we now have R1||R2||rπ as the effective input resistance.




There is another minor inconvenient problem with this bias scheme when it is connected to a prior stage in the signal path. This bias configuration places the AC input signal source directly in parallel with R2 of the voltage divider. This may not be acceptable, as the input source may tend to add or subtract from the DC voltage dropped across R2. 




One way to make this scheme work, although it may not be obvious why it will work, is to place a coupling capacitor between the input voltage source and the voltage divider as in figure 9.2.3 below. 




[![](/_media/university/courses/electronics/text/chptr9-f6.png?w=500&tok=9d1969)](/_detail/university/courses/electronics/text/chptr9-f6.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-9 "university:courses:electronics:text:chptr9-f6.png")





 Figure 9.2.3 Coupling capacitor CC prevents voltage divider bias current from flowing into the input signal source. 





The capacitor forms a high-pass filter between the input source and the DC voltage divider, passing almost the entire AC portion of the input signal on to the transistor while blocking all the DC bias voltage from being shorted through the input signal source. This makes much more sense if you understand the superposition theorem and how it works. According to superposition, any linear, bilateral circuit can be analyzed in a piecemeal fashion by only considering one power source at a time, then algebraically adding the effects of all power sources to find the final result. If we were to separate the capacitor and the R1/R2voltage divider circuit from the rest of the amplifier, it might be easier to understand how this superposition of AC and DC would work. 




With only the AC signal source in effect, and a capacitor with an arbitrarily low impedance at the input signal frequency, almost all the AC voltage appears across R2. 




### 9.2.2 Small signal voltage gain, common emitter or source




To calculate the small signal voltage gain of the common emitter or source amplifier we need to insert a small signal model of the transistor into the circuit. The small signal models of the BJT and MOS FET are actually very similar so the gain calculation for either version is much the same. The small signal hybrid-π models for the BJT and MOS amplifiers are shown in figure 9.2.4.




[![](/_media/university/courses/electronics/text/chptr9-f7.png?w=500&tok=c9f310)](/_detail/university/courses/electronics/text/chptr9-f7.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-9 "university:courses:electronics:text:chptr9-f7.png")





Figure 9.2.4 Common emitter or source small signal models.





The following are some of the key model equations we will need to calculate the amplifier stage voltage gain. These equations are used for the other amplifier configurations that we will discuss in following sections as well.




(BJT)[![](/_media/university/courses/electronics/text/chptr9-e2.png?w=100&tok=9dc191)](/_detail/university/courses/electronics/text/chptr9-e2.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-9 "university:courses:electronics:text:chptr9-e2.png")
(MOS)[![](/_media/university/courses/electronics/text/chptr9-e3.png?w=100&tok=b1c2b3)](/_detail/university/courses/electronics/text/chptr9-e3.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-9 "university:courses:electronics:text:chptr9-e3.png")




[![](/_media/university/courses/electronics/text/chptr9-e4.png?w=100&tok=997a04)](/_detail/university/courses/electronics/text/chptr9-e4.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-9 "university:courses:electronics:text:chptr9-e4.png")
[![](/_media/university/courses/electronics/text/chptr9-e5.png?w=150&tok=ae9be4)](/_detail/university/courses/electronics/text/chptr9-e5.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-9 "university:courses:electronics:text:chptr9-e5.png")




The small signal voltage gain Av is the ratio of the input voltage to the output voltage:




[![](/_media/university/courses/electronics/text/chptr9-e6.png?w=100&tok=582ee5)](/_detail/university/courses/electronics/text/chptr9-e6.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-9 "university:courses:electronics:text:chptr9-e6.png")




The input voltage Vin (vbe for the BJT and vgs for the MOS) times the transconductance gm is equal to the small signal output current, io in the collector or drain. Vout will be simply this current times the load resistance RL,neglecting the small signal output resistance ro for the moment. Notice the minus sign because of the direction of the current io.




[![](/_media/university/courses/electronics/text/chptr9-e7.png?w=250&tok=b5e4d6)](/_detail/university/courses/electronics/text/chptr9-e7.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-9 "university:courses:electronics:text:chptr9-e7.png")




Rearranging for the gain we get:




[![](/_media/university/courses/electronics/text/chptr9-e8.png?w=200&tok=84d281)](/_detail/university/courses/electronics/text/chptr9-e8.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-9 "university:courses:electronics:text:chptr9-e8.png")




Substituting the BJT and MOS gm equations we get:




(BJT)[![](/_media/university/courses/electronics/text/chptr9-e9.png?w=200&tok=67a170)](/_detail/university/courses/electronics/text/chptr9-e9.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-9 "university:courses:electronics:text:chptr9-e9.png")
(MOS)[![](/_media/university/courses/electronics/text/chptr9-e10.png?w=200&tok=0ac65f)](/_detail/university/courses/electronics/text/chptr9-e10.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-9 "university:courses:electronics:text:chptr9-e10.png")




Comparing these two gain equations we see that they both depend on the DC collector or drain currents. The BJT gain is inversely proportional to VT (the Thermal Voltage) which is approximately 26mV at room temperature. The Thermal Voltage, VT increases with increasing temperature so from the equation we see that the gain will actually decrease with increasing temperature. The MOS gain is inversely proportional to the over drive voltage, Vov (VGS – Vth) which is often much larger than VT at similar drain currents leading to the lower gain for the MOS stage vs. the BJT stage for approximately equal bias currents. 




If RL is relatively large when compared to the small signal output resistance then the gain will be reduced because the actual output load is the parallel combination of RL and ro. In fact ro puts an upper bound on the possible gain that can be achieved with a single transistor amplifier stage.




### 9.2.3 Small signal input impedance, common emitter or source




Again looking at the small signal models in figure 9.2.4 we see that for the BJT case the input Vin will see rπ as a load. For the MOS case Vin will see basically an open circuit (for low frequencies anyway). This will of course be the case absent any Gate or Base bias circuitry.




### 9.2.4 Small signal output impedance, common emitter or source




Again looking at the small signal models in figure 9.2.4 we see that for both the BJT case and the MOS case the output impedance is the parallel combination of RL and ro. For most practical applications we can ignore ro because it is very often much larger than RL. Below are the BJT and MOS ro equations.




(BJT)[![](/_media/university/courses/electronics/text/chptr9-e11.png?w=200&tok=f9207e)](/_detail/university/courses/electronics/text/chptr9-e11.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-9 "university:courses:electronics:text:chptr9-e11.png")
(MOS)[![](/_media/university/courses/electronics/text/chptr9-e12.png?w=200&tok=de7665)](/_detail/university/courses/electronics/text/chptr9-e12.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-9 "university:courses:electronics:text:chptr9-e12.png")




### 9.2.5 common emitter and source Lab Activities




**ADALM1000 Lab Activity 5, [Common emitter amplifier](/university/courses/alm1k/alm-lab-5 "university:courses:alm1k:alm-lab-5")**  

**ADALM1000 Lab Activity 5M, [Common source amplifier](/university/courses/alm1k/alm-lab-5m "university:courses:alm1k:alm-lab-5m")**




**ADALM2000 Lab Activity 5, [Common emitter amplifier](/university/courses/electronics/electronics-lab-5 "university:courses:electronics:electronics-lab-5")**  

**ADALM2000 Lab Activity 5M, [Common source amplifier](/university/courses/electronics/electronics-lab-5m "university:courses:electronics:electronics-lab-5m")**  

**ADALM2000 Lab Activity 5FR, [Amplifier Frequency Response](/university/courses/electronics/electronics-lab-5fr "university:courses:electronics:electronics-lab-5fr")**




## 9.3 The Current Follower also known as Common base or gate amplifier




The Current Follower or Common base/gate amplifier has a high voltage gain, relatively low input impedance and high output impedance compared to the voltage follower or common collector/drain amplifier. The BJT and MOS versions are shown in figure 9.3




[![](/_media/university/courses/electronics/text/chptr9-f8.png?w=500&tok=651eea)](/_detail/university/courses/electronics/text/chptr9-f8.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-9 "university:courses:electronics:text:chptr9-f8.png")





 Figure 9.3: Basic n-type current follower or common base/gate circuit (neglecting biasing details) 





### 9.3.1 DC Biasing techniques, current follower or common base/gate amplifier




In applications where only a positive power supply voltage is provided some means of providing the necessary DC voltage level for the common gate or base terminal is required. This might be as simple as a voltage divider between ground and the supply. In applications where both positive and negative supply voltages are available, ground is a convenient node to use for the common gate or base terminal.




The common gate or base stage is most often used in combination with the common emitter or source amplifier in what is known as the cascode configuration. The cascode will be covered in the next chapter on multi stage amplifiers in greater detail.




### 9.3.2 Small signal voltage gain, current follower or common base/gate amplifier




To calculate the small signal voltage gain of the common base or gate amplifier we insert the small signal model of the transistor into the circuit. The small signal models for the BJT and MOS amplifiers are shown in figure 9.3.1.




[![](/_media/university/courses/electronics/text/chptr9-f9.png?w=500&tok=aacbd1)](/_detail/university/courses/electronics/text/chptr9-f9.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-9 "university:courses:electronics:text:chptr9-f9.png")





 Figure 9.3.1 Current follower or Common base/gate small signal models. 





Much like in the common emitter/source amplifier stage the small signal input voltage, Vin (vbe for the BJT and vgs for the MOS) times the transconductance gm is equal to the small signal output current, io in the collector or drain. Vout will be simply this current times the load resistance RL,neglecting the small signal output resistance ro for the moment.




It is perhaps more useful to consider the current gain of the current follower stage rather than its voltage gain. In the case of the MOS version we know that IS = IDbecause IG= 0. Thus the MOS stage current gain is exactly 1. In the case of the BJT version we know that the ratio of IC to IEis equal to α and thus will be slightly less than 1.




### 9.3.3 Input impedance, current follower or common base/gate amplifier




Again looking at the small signal models in figure 9.3.1 we see that for the BJT case the input Vin will see rπin parallel with the series combination of gm and RL as a load. For the MOS case Vin will see basically just the series combination of gm and RL. The equation below (from the BJT small signal T model) relates gm and the resistance seen at the emitter rE. We can also use this relationship to give us the resistance seen at the source rS.




[![](/_media/university/courses/electronics/text/chptr9-e13.png?w=200&tok=8942a4)](/_detail/university/courses/electronics/text/chptr9-e13.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-9 "university:courses:electronics:text:chptr9-e13.png")
(also rS for MOS)




It is also important to note here that 100% (neglecting IB in the BJT case) of the current from the input source flows through the transistor and becomes the output current. Thus the name current follower.




### 9.3.4 Output impedance, current follower or common base/gate amplifier




Again looking at the small signal models in figure 9.3.1 we see that for both the BJT case and the MOS case the output impedance is the parallel combination of RL and ro. We can generally assume this is true if we consider that Vin is driven from a low impedance (nearly ideal) voltage source. If this is not the case then the finite output impedance must be added in series with ro. If the input of the current follower is driven by the relatively high output impedance of a transconductance amplifier such as the common emitter or source amplifier from earlier then the output impedance for the combined amplifier can be very high. For most practical applications we can ignore ro because it is very often much larger than RL. 




**ADALM1000 Lab Activity, [BJT Common Base Amplifier](/university/courses/alm1k/alm-lab-cb "university:courses:alm1k:alm-lab-cb")**  

**ADALM1000 Lab Activity, [BJT Common Gate Amplifier](/university/courses/alm1k/alm-lab-cg "university:courses:alm1k:alm-lab-cg")**  

**ADALM1000 Lab Activity, [Folded Cascode Amplifier](/university/courses/alm1k/alm-lab-fca "university:courses:alm1k:alm-lab-fca")**




### 9.4 Voltage followers (also called Emitter or Source follower or Common collector or drain amplifiers)




The Emitter or Source follower is often called a common Collector or Drain amplifier because the collector or drain is common to both the input and the output. This amplifier configuration, figure 9.4, has its output taken from the emitter/source resistor and is useful as an impedance matching device since its input impedance is much higher than its output impedance. The voltage follower is also termed a “buffer” for this reason.




[![](/_media/university/courses/electronics/text/chptr9-f10.png?w=500&tok=5aaffb)](/_detail/university/courses/electronics/text/chptr9-f10.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-9 "university:courses:electronics:text:chptr9-f10.png")





 Figure 9.4:Basic n-type Voltage follower or common collector/drain circuit (neglecting biasing details) 





The gain of the voltage follower is always less than one since rEand RLor rS and RL form a voltage divider. The input to output offset is set by the VBE drop of about 0.65 volts below the base for the BJT and VGS below the gate for the MOS. This configuration’s function is not voltage gain but current or power gain and impedance matching. The input impedance is much higher than its output impedance so that a signal source does not have to supply as much power to the input. This can be seen from the fact that the base current is on the order of 100 times (β) less than the emitter current. The low output impedance of the emitter follower matches a low impedance load and buffers the signal source from that low impedance.




### 9.4.1 DC Biasing techniques, Voltage Follower or common collector/drain amplifier




The collector/source current is basically determined by the emitter/source resistor so the main design variables in this case is simply RL and the power supply voltage.




### 9.4.2 Voltage gain, common collector or drain amplifier




To calculate the small signal voltage gain of the voltage follower configuration we insert the small signal model of the transistor into the circuit. The small signal models for the BJT and MOS amplifiers are shown in figure 9.4.1.




[![](/_media/university/courses/electronics/text/chptr9-f11.png?w=500&tok=7aeb34)](/_detail/university/courses/electronics/text/chptr9-f11.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-9 "university:courses:electronics:text:chptr9-f11.png")





Figure 9.4.1 Voltage Follower small signal models.





[![](/_media/university/courses/electronics/text/chptr9-e14.png?w=300&tok=8ed919)](/_detail/university/courses/electronics/text/chptr9-e14.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-9 "university:courses:electronics:text:chptr9-e14.png")




### Example 9.4.2 Calculating the Voltage Gain




For the circuit in figure 9.4.2 calculate the voltage gain AV = Vout/Vin.




[![](/_media/university/courses/electronics/text/chptr9-f12.png?w=500&tok=7ece9b)](/_detail/university/courses/electronics/text/chptr9-f12.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-9 "university:courses:electronics:text:chptr9-f12.png")





Figure 9.4.2 BJT Voltage gain example





To use the voltage gain formula we just obtained using the small signal models we need to first calculate rE. From section 9.3.3 we are given the equation for rE:




[![](/_media/university/courses/electronics/text/chptr9-e13.png?w=150&tok=90f134)](/_detail/university/courses/electronics/text/chptr9-e13.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-9 "university:courses:electronics:text:chptr9-e13.png")




To use this formula we need to know IE. We know that the voltage across RL is Vout. We also know that Vout = Vin - VBE. If we use an estimate of VBE to be 0.6 volts, we get Vout = 5.6 - 0.6 or 5 volts. If RL is 1KΩ then IE is 5mA. Using a room temperature value for VT = 25mV, we get rE is equal to 5Ω. Substituting these values into our gain equation we get:




[![](/_media/university/courses/electronics/text/chptr9-e15.png?w=400&tok=3cf27d)](/_detail/university/courses/electronics/text/chptr9-e15.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-9 "university:courses:electronics:text:chptr9-e15.png")




### 9.4.3 Input impedance, Voltage Follower (common collector or drain)




(BJT)[![](/_media/university/courses/electronics/text/chptr9-e16.png?w=400&tok=2416e1)](/_detail/university/courses/electronics/text/chptr9-e16.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-9 "university:courses:electronics:text:chptr9-e16.png")




### 9.4.4 Output impedance, Voltage Follower (common collector or drain)




The output impedance is simple the parallel combination of the Emitter (Source) resistor RL and the small signal emitter (source) resistance of the transistor rE. Again from section 9.3.3, the equation for rE is as follows:




[![](/_media/university/courses/electronics/text/chptr9-e13.png?w=150&tok=90f134)](/_detail/university/courses/electronics/text/chptr9-e13.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-9 "university:courses:electronics:text:chptr9-e13.png")




Similarly, the small signal source resistance, rS, for a MOS FET is 1/gm.




Referring back to our gain example in figure 9.4.2, we can also calculate the output resistance, which will be the parallel combination of the 1KΩ RL and the 3Ω rE or 2.99Ω.




### 9.4.5 Voltage Follower (common collector or drain) Lab Activities




**ADALM1000 Lab Activity 11, [BJT Emitter follower](/university/courses/alm1k/alm-lab-11 "university:courses:alm1k:alm-lab-11")**  

**ADALM1000 Lab Activity 11M, [MOS Source follower](/university/courses/alm1k/alm-lab-11m "university:courses:alm1k:alm-lab-11m")**




**ADALM2000 Lab Activity 11, [BJT Emitter follower](/university/courses/electronics/electronics-lab-11 "university:courses:electronics:electronics-lab-11")**  

**ADALM2000 Lab Activity 11m, [MOS Source follower](/university/courses/electronics/electronics-lab-11m "university:courses:electronics:electronics-lab-11m")**




## 9.5 Series Feedback: emitter/source degeneration




Common emitter/source amplifiers give the amplifier an inverted output and can have a very high gain and can vary widely from one transistor to the next. The gain is a strong function of both temperature and bias current, and so the actual gain is somewhat unpredictable. Stability is another problem associated with such high gain circuits due to any unintentional positive feedback that may be present. Other problems associated with the circuit are the low input dynamic range imposed by the small-signal limit; there is high distortion if this limit is exceeded and the transistor ceases to behave like its small-signal model. When negative feedback is introduced, many of these problems are reduced, resulting in improved performance. There are several ways to introduce feedback in this simple amplifier stage, the easiest and most reliable of which is accomplished by introducing a small value resistor in the emitter circuit (RE). This is also referred to as series feedback. The amount of feedback is dependent on the relative signal level dropped across this resistor. The signal seen across RE is out of phase with the signal seen at Vout and thus subtracts from Vout reducing its amplitude. When the emitter resistor value approaches that of the collector load resistor (RL), the gain will approach unity (Av ~ 1).




[![](/_media/university/courses/electronics/text/chptr9-f16.png?w=500&tok=cdf284)](/_detail/university/courses/electronics/text/chptr9-f16.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-9 "university:courses:electronics:text:chptr9-f16.png")





 Figure 9.5: Adding an emitter/source resistor decreases gain. However, with increased linearity and stability 





It is much less common to include a degeneration resistor in MOS designs. This is because, in microelectronic integrated circuits, the gain (gm) of the device can be adjusted by changing the W/L ratio. This degree of design freedom is not generally available in Bipolar (BJT) processes.




**DC Biasing example with emitter degeneration**




There are some BJT biasing rules of thumb:




1. Set IE not IB or VBE : less dependence on β and temperature (VT)  


2. Allow 1/3VCC across RC, VCE and RB2  


3. Save power by allowing only 10% of IE in RB




We are given the following for circuit in figure 9.5.1, VCC = 20V ; IE = 2mA ; β = 100. From our rules of thumb we set VB = 1/3\*VCC = 6.7 V. 




[![](/_media/university/courses/electronics/text/chptr9-f17.png?w=500&tok=cd9a04)](/_detail/university/courses/electronics/text/chptr9-f17.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-9 "university:courses:electronics:text:chptr9-f17.png")





Figure 9.5.1 DC Biasing example





VB = (RB2/(RB1+RB2))\*VCC ⇒ 6.7V = (RB2/(RB1+RB2))\*20 (1)




VCC /(RB1 + RB2 ) = 0.1\*IE ⇒ 20/(RB1 + RB2) = 200 μA (2)




Solving equations (1) and (2) we get:




RB1=2RB2 then from (2)




3RB2 = 20/200 μA = 100kΩ




So, RB2 = 33kΩ and RB1 = 66kΩ




Now we have VE = VB – VBE = 6.7 – 0.7 = 6 V and IE is 2 mA: RE = VE/IE = 6/2mA = 3kΩ.




IC = (β/(β+1))\*IE = (100/101)\*2mA = 1.98 mA and IB = IC/β = 1.98mA/100 = 19.8μA.




From our rules of thumb we know that VC = 2/3\*20V = 13.3 V




So to find RL we have: RL = (VCC – VC)/IC = (20 – 13.3)/1.98mA = 3.4kΩ




### 9.5.1 Small signal voltage gain with emitter/source degeneration




To calculate the small signal voltage gain of the common emitter/source amplifier with the addition of emitter/source degeneration we again insert the small signal model of the transistor into the circuit. The small signal models for the BJT and MOS amplifiers are shown in figure 9.5.1.




[![](/_media/university/courses/electronics/text/chptr9-f18.png?w=500&tok=914136)](/_detail/university/courses/electronics/text/chptr9-f18.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-9 "university:courses:electronics:text:chptr9-f18.png")





Figure 9.5.1 Common emitter/source with degeneration





The impedance RE reduces the overall transconductance gm of the circuit by a factor of gmRE + 1, which makes the voltage gain:




[![](/_media/university/courses/electronics/text/chptr9-e17.png?w=290&tok=15a544)](/_detail/university/courses/electronics/text/chptr9-e17.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-9 "university:courses:electronics:text:chptr9-e17.png")
(when gmRE » 1)




So the voltage gain depends almost exclusively on the ratio of the resistors RL / RE rather than the transistor’s intrinsic and unpredictable characteristics. The distortion and stability characteristics of the circuit are thus improved at the expense of a reduction in gain.




Going back to our earlier biasing example, figure 9.5.1, values for IC = 2mA, RL = 3.4KΩ and RE = 3KΩ to calculate the small signal gain we first find gm = IC/VT = 2mA/25mV = 0.08. Using our formula for AV:




[![](/_media/university/courses/electronics/text/chptr9-e18.png?w=300&tok=c49cc2)](/_detail/university/courses/electronics/text/chptr9-e18.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-9 "university:courses:electronics:text:chptr9-e18.png")




### 9.5.2 Small signal input impedance with emitter/source degeneration




Again looking at the small signal models in figure 9.4.1 we see that for the BJT case the input Vin see rin series with degeneration resistor RE as a load. For the MOS case Vin see basically an open circuit.




[![](/_media/university/courses/electronics/text/chptr9-e19.png?w=200&tok=6e0111)](/_detail/university/courses/electronics/text/chptr9-e19.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-9 "university:courses:electronics:text:chptr9-e19.png")




### 9.5.3 Small signal output impedance with emitter/source degeneration




Again looking at the small signal models in figure 9.5.1 we see that for both the BJT case and the MOS case, much like in the earlier common emitter/source stage, the output impedance is the parallel combination of RL and ro but now degeneration resistor RE is in series with ro. For most practical applications we can ignore ro because it is very often much larger than RL.




### 9.5.4 DC Biasing techniques with emitter/source degeneration




Basically the same techniques used in the simple common emitter/source amplifier stage, which were discussed in section 9.2.1, can be used when the emitter degeneration resistor is added. The added voltage across the RE (RE\*IE) must be added to the bias level. This added voltage drop actually make the operating point (IC) much less sensitive to the bias level.




The small signal voltage gain of the common emitter amplifier with the emitter resistance is approximately RL / RE. For cases when a gain larger than 5-10 is needed, RE may be become so small that the necessary good biasing condition, VE = RE\*IE > 10\* VT cannot be achieved. A way to restore the small signal voltage gain while maintaining the desired DC operating bias is to use a by-pass capacitor as is figure 9.5.4. The small AC signal sees an emitter resistance of just RE1 while for DC bias the emitter resistance is the series combination of RE = RE1+RE2. Calculations for the common emitter amplifier with emitter degeneration can be applied here by replacing RE with RE1 when deriving the amplifier gain, and input and output impedances, because a sufficiently large bypass capacitor in effects shorts RE2and is effectively removed from the circuit for sufficiently high frequency inputs.




[![](/_media/university/courses/electronics/text/chptr9-f19.png?w=500&tok=2161de)](/_detail/university/courses/electronics/text/chptr9-f19.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-9 "university:courses:electronics:text:chptr9-f19.png")





Figure 9.5.4 addition of emitter by-pass capacitor





Using our earlier biasing exercise in figure 9.5.1 as an example but splitting the 3KΩ RE into two resistors as in figure 9.5.4 with RE1= 1KΩ and RE2 = 2KΩ with C1 = 1uF we can recalculate the small signal gain for high frequencies, where C1 effectively shorts out RE2, to be:




[![](/_media/university/courses/electronics/text/chptr9-e20.png?w=300&tok=264567)](/_detail/university/courses/electronics/text/chptr9-e20.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-9 "university:courses:electronics:text:chptr9-e20.png")




The addition of by-pass capacitor C1, however, modifies the low frequency response of the circuit. We know from our two gain calculations that the DC gain of the circuit is -1.13 and the gain increases to -3.36 for high frequencies. We can therefore assume that the frequency response consists of a relatively low frequency zero followed by a somewhat higher frequency pole. The formulas for the zero and pole are as follows:




![F_Z = 1/(2 pi R_E2 C_1)](/lib/plugins/mathpublish/img.php?img=68a096493440e06dc8d8be3bf916b2c8 "F_Z = 1/(2 pi R_E2 C_1)")




![F_P = 1/(2R prime _E C_1)](/lib/plugins/mathpublish/img.php?img=2edd9a0b8f913a85a4e792614dc2ac42 "F_P = 1/(2R prime _E C_1)")




where R’E= RE2 || (RE1 + re)




For our example problem with RE1 = 1K , RE2 = 2K and C1 = 1uF we get the frequency for the zero equal to 80 Hz and the frequency for the pole equal to 237 Hz. The simulated frequency response from 1 Hz to 100 KHz for the example circuit is shown in figure 9.5.5.




[![](/_media/university/courses/electronics/text/chptr9-f20.png?w=500&tok=fb32fb)](/_detail/university/courses/electronics/text/chptr9-f20.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-9 "university:courses:electronics:text:chptr9-f20.png")





 Figure 9.5.5 simulated frequency response





### 9.5.5 Summary - performing small-signal analyses:




1. Find DC operating point.  


2. Calculate small-signal parameters: gm, r, re etc.  


3. Replace DC voltage sources with AC grounds and DC current sources with open circuits.  


4. Replace transistor with small-signal model (hybrid-π model or T model)  





## 9.6 Miller’s Theorem




At this point we are going to take a diversion to discuss Miller’s Theorem. While the methods we have been using up to this point are completely general, there are certain configurations that lend themselves to be analyzed more simply by Miller’s Theorem. Miller’s theorem states that in a linear circuit, if there is a branch where an impedance Z, connects two nodes with node voltages V1and V2, this branch can be replaced by two other branches connecting the corresponding nodes to ground by impedances respectively Z / (1-K) and KZ / (K-1), where the gain from node 1 to node 2 is K = V2 / V1.




[![](/_media/university/courses/electronics/text/chptr9-f21.png?w=350&tok=14c019)](/_detail/university/courses/electronics/text/chptr9-f21.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-9 "university:courses:electronics:text:chptr9-f21.png")
[![](/_media/university/courses/electronics/text/chptr9-f22.png?w=350&tok=b97a15)](/_detail/university/courses/electronics/text/chptr9-f22.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-9 "university:courses:electronics:text:chptr9-f22.png")





 Figure 9.6.1 Miller’s Theorem 





At this point we will go through the steps that show how the Miller impedances are arrived at. We can use the equivalent two-port network technique to replace the two-port represented in figure 9.6.1(a) to its equivalent in figure 9.6.2. 




[![](/_media/university/courses/electronics/text/chptr9-f23.png?w=350&tok=6f72d1)](/_detail/university/courses/electronics/text/chptr9-f23.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-9 "university:courses:electronics:text:chptr9-f23.png")





 Figure 9.6.2 





Replacing the voltage sources in figure 9.6.2 with their Norton equivalent current sources we get figure 9.6.3.




[![](/_media/university/courses/electronics/text/chptr9-f24.png?w=500&tok=8a260b)](/_detail/university/courses/electronics/text/chptr9-f24.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-9 "university:courses:electronics:text:chptr9-f24.png")





 Figure 9.6.3 





Using the source absorption theorem (see the Appendix at the end of this chapter), we get figure 9.6.4.




[![](/_media/university/courses/electronics/text/chptr9-f25.png?w=500&tok=028300)](/_detail/university/courses/electronics/text/chptr9-f25.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-9 "university:courses:electronics:text:chptr9-f25.png")





 Figure 9.6.4 





Which gives us figure 9.6.5 (which is figure 9.6.1(b) ) when we parallel combine the two impedances.




[![](/_media/university/courses/electronics/text/chptr9-f26.png?w=500&tok=554319)](/_detail/university/courses/electronics/text/chptr9-f26.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-9 "university:courses:electronics:text:chptr9-f26.png")





 Figure 9.6.5 





## 9.7 Shunt feedback:




Another biasing technique for the common emitter or source amplifier, called shunt feedback, is accomplished by the introduction of some fraction of the collector or drain signal back to the input at the base or gate. This is done via the biasing resistor (RF), as shown in figure 9.7.1. Resistor RF connects between two nodes that have gain, AV (K), between them and thus the application of Miller’s theorem is the best way analyze the small signal characteristics of this circuit.




[![](/_media/university/courses/electronics/text/chptr9-f27.png?w=500&tok=67e179)](/_detail/university/courses/electronics/text/chptr9-f27.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-9 "university:courses:electronics:text:chptr9-f27.png")





 Figure 9.7.1 Drain-to-Gate (a) and Collector-to-Base (b) shunt feedback 





### 9.7.1 MOS version




Figure 9.7.1(a) shows a common source NMOS amplifier using drain feedback biasing. This type of biasing is often used with enhancement mode MOSFETS and can be useful when operating with a low voltage power supply (V+). If Vin is AC coupled, the voltage on the gate is equal to the voltage on the drain (VGS = VDS) since no gate current flows through RF. If Vin is DC coupled then a voltage divider is formed by RF and RS and VGS will be less than VDS. It is useful to note that the transistor is always in saturation when VGS = VDS. If the drain current increases for some reason, such as a change in V+, the gate voltage drops. The decreased gate voltage in turn causes the drain current to decreases which causes the gate voltage to increase. The negative feedback loop reaches an equilibrium that is the bias point for the circuit.




Some data sheets for enhancement MOSFETS give a value for ID(on), where VGS = VDS lf ID(on) is known, the circuit component can be easily calculated as shown in Example 9.3. The input impedance of a circuit using drain feedback biasing is equal to the value of RF divided by the voltage gain plus one.




### 9.7.2 BJT Version DC Biasing techniques




This configuration employs negative feedback to stabilize the operating point. In this form of biasing, the base feedback resistor RF is connected to the collector instead of connecting it to the DC source V+. So any large increase in the collector current will induce a voltage drop across the RL resistor that will in turn reduce the transistor’s base current.




If we assume that the input source Vin is AC coupled and no DC bias current flows in RS, from Kirchhoff’s voltage law, the voltage VRFacross the base resistor RF is:




![V_RF = V_+ - (I_c + I_b )R_L - V_BE](/lib/plugins/mathpublish/img.php?img=11f0543d828b8bcc851a89d9d32b6742 "V_RF = V_+ - (I_c + I_b )R_L - V_BE")




By the Ebers–Moll model, Ic = βIb, and so:




![V_RF = V_+ - (βI_b + I_b )R_L - V_BE = V_+ - I_b (β + 1 )R_L - V_BE](/lib/plugins/mathpublish/img.php?img=e27012ebe36c97c0ad6579314208c6ce "V_RF = V_+ - (βI_b + I_b )R_L - V_BE = V_+ - I_b (β + 1 )R_L - V_BE")




From Ohm’s law, the base current Ib=VRF/RF, and so:




![I_b R_F = V_+ - I_b (β + 1 )R_L - V_BE](/lib/plugins/mathpublish/img.php?img=7b854ddf5ccd00785efb6286b9807278 "I_b R_F = V_+ - I_b (β + 1 )R_L - V_BE")




Hence, the base current Ib is:




![I_b = (V_+ - V_BE ) / (R_F + (β + 1 )R_L )](/lib/plugins/mathpublish/img.php?img=5a4eb6723860abdae054788fb28a5814 "I_b = (V_+ - V_BE ) / (R_F + (β + 1 )R_L )")




If VBE is held constant and temperature increases, then the collector current Ic increases. However, a larger Ic causes the voltage drop across resistor RL to increase, which in turn reduces the voltage VRF across the base resistor RF. A lower base-resistor voltage drop reduces the base current Ib, which results in less collector current Ic. Because an increase in collector current with temperature is opposed, the operating point is kept more stable.




**Pros:**



1. Circuit stabilizes the operating point against variations in temperature and β (ie. Transistor process variations)



**Cons:**



1. In this circuit, to keep Ic independent of β, the following condition must be met:



![I_c = βI_b = (βV_+ - βB_BE ) / (R_F +(β+1)R_L) approx (V_+ - V_BE)/R_L](/lib/plugins/mathpublish/img.php?img=05cfc9e66957266cc032bf84d400c20d "I_c = βI_b = (βV_+ - βB_BE ) / (R_F +(β+1)R_L) approx (V_+ - V_BE)/R_L")




which is the case when:




![βR_L >> R_F](/lib/plugins/mathpublish/img.php?img=a973ca52b323331c2c1f0b9ea7822824 "βR_L >> R_F")



1. As β is fixed (and generally not known precisely) for a given transistor, this relation can be satisfied either by keeping RL fairly large or making RF very low.
2. If RL is large, a high V+ is necessary, which increases cost as well as precautions necessary while handling.
3. If RF is low, the reverse bias of the collector–base region is small, which limits the range of collector voltage swing that leaves the transistor in active mode.
4. The resistor RF causes an AC feedback, reducing the voltage gain of the amplifier. This undesirable effect is a trade-off for greater quiescent operating point stability.



**Usage:** The feedback also decreases the input impedance of the amplifier as seen from the base, which can be advantageous. Due to the gain reduction from feedback, this biasing form is used only when the trade-off for stability is warranted.




### Example 9.7.2 Using Miller’s Theorem




For the amplifier shown in figure 9.7.2(a) with a DC coupled input source Vin calculate the input and output resistance and voltage gain AV. We first need to start with some preliminary DC analysis to determine the operating point of Q1. For this we set Vin to zero volts, i.e. short it out. If we assume a VBE of 0.65 volts we will have 65 uA flowing in the 10K resistor RS. Given that V+ is 10V, we would like Vout to be 5 volts. The current in RL is equal to 500uA and will split between the collector of Q1 and the feedback resistor RF. The voltage across the 62.7KΩ feedback resistor is 5-0.65 or 4.35 volts. The current in RF splits between the current in RS and IB. The base current IB is equal to 4.35/62.7KΩ – 65uA or 4.3 uA. We should get a collector current of 500uA - 69.3uA or 430.3uA with a β of about 100. 




If we use Miller’s theorem to replace the feedback resistor RF with its two equivalent impedances we get figure 9.7.2(b). Assuming that the voltage gain from base to collector AV is significantly greater than 1 we can make the simplification that AV/(AV-1) is close to 1. The effective load resistance, RLeq we will use to calculate the gain will be 10KΩ||62.7KΩ or 8.62KΩ. Now we can use the same common emitter or source small signal gain equations we used in section 9.2.2. The 430uA collector currents gives us a gm of 430uA/25mV or 0.0172. We know that AV = -gmRLeq or AV = -0.0172\*8.62K = -148 which is » 1. The input resistance seen at the base of Q1 will be the rπof Q1, which is equal to β/gm or 100/0.0172 = 5.814KΩ, in parallel with the Miller resistance 62.7KΩ/149 = 421Ω thus the effective input resistance, Rbase will be about 392.5Ω.




[![](/_media/university/courses/electronics/text/chptr9-f28.png?w=500&tok=aea9fa)](/_detail/university/courses/electronics/text/chptr9-f28.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-9 "university:courses:electronics:text:chptr9-f28.png")





 Figure 9.7.2 Example using Miller’s theorem 





The input source resistance RS and the equivalent resistance at the base, Rbase form a voltage divider. To calculate the overall voltage gain from voltage source Vin to Vout we multiply this divider ratio times the base to collector gain, AV we just calculated.




![R_base / (R_S + R_base ) A_V = (392.5/10392.5) * 148 = 5.6](/lib/plugins/mathpublish/img.php?img=913f03af508f45dda89d5fcdfb9e6835 "R_base / (R_S + R_base ) A_V = (392.5/10392.5) * 148 = 5.6")




From our investigation of the inverting op amp configuration in Chapter 3 we learned that for amplifiers with less than infinite gain the actual gain will be less than the ideal gain equation, Gain = -RF/RS predicts. If our single transistor amplifier had infinite gain the gain from Vin to Vout would be 62.7KΩ/10KΩ or 6.27. In Chapter 3 we got an estimation of the percentage error, ε, due to finite gain AV (remember β in this equation is the feedback factor not the current gain of the transistor):




![epsilon(%) approx 100/(A_V beta ) = 100/(148*6.2) = 10.7%](/lib/plugins/mathpublish/img.php?img=e6fb2bac4fbafecfa5acab77ddaf96de "epsilon(%) approx 100/(A_V beta ) = 100/(148*6.2) = 10.7%")




The actual gain of 5.6 is about 10% smaller than the ideal gain of 6.27.




### Exercise 9.7




Part 1 DC operating point:




For the circuit in figure 9.7.3 calculate the required RF to bias the DC operating point such that Vout is equal to ½ the supply voltage or +5V when Vin = 0. Assume VBE = 0.65V and β = 200.




[![](/_media/university/courses/electronics/text/chptr9-f29.png?w=350&tok=682efd)](/_detail/university/courses/electronics/text/chptr9-f29.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-9 "university:courses:electronics:text:chptr9-f29.png")





 Figure 9.7.3 





Part 2 Small signal gain and impedance:




Given the value for RF calculated in part 1 calculate the voltage gain AV, the input resistance Rbase and the output resistance Rout. Also calculate the overall voltage gain Vout/Vin and explain why this is different than the ideal value of –RF/RS.




### 9.7.5 The Miller Effect




The Miller effect is key to predicting the frequency response of an inverting amplifier stage where capacitive feedback is included. Typically there’s a low-pass pole in the voltage gain stage created by RS of the signal source and a feedback capacitor CC. But, the low pass cutoff is not simply determined by RS and CC. The Miller effect creates an effective capacitance at the base/gate of the transistor that appears as CC scaled by the amplifier’s voltage gain.




[![](/_media/university/courses/electronics/text/chptr9-f30.png?w=500&tok=9ff7f4)](/_detail/university/courses/electronics/text/chptr9-f30.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-9 "university:courses:electronics:text:chptr9-f30.png")





 Figure 9.7.3 Miller feedback capacitor 





The Miller effect is especially useful when you’re trying to produce a low-pass filter on an IC op amp with a relatively low frequency cut-off. The difficulty is that large capacitors are difficult to make because they take up so much space on the IC. The solution is to make a small capacitor and then scale up its behavior using the Miller effect.




Equivalent Circuit




Here’s a simplified version of the circuit above.




[![](/_media/university/courses/electronics/text/chptr9-f31.png?w=500&tok=7f9d7c)](/_detail/university/courses/electronics/text/chptr9-f31.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-9 "university:courses:electronics:text:chptr9-f31.png")





 Figure 9.7.4 Miller feedback equivalent circuit 





Miller said that you can approximate the input capacitance by replacing CC with a different capacitance CM across the RIN. How much bigger is CM? CC is multiplied by the voltage gain (AV = gmRL) of the amplifier. Miller’s theorem also states there will be a capacitor C’C across RL that is equal to CC times (AV+1)/AV which for large values of AV we assume to be 1. 




![C_M = C_C · (1+A_V) , C’_C ~ C_C](/lib/plugins/mathpublish/img.php?img=efb06946182dcd43bc1a178cf8f8398b "C_M = C_C · (1+A_V) , C’_C ~ C_C")




How does this work? Well, we know that forcing a voltage across a capacitor causes a current to flow. How much current depends on the capacitance: I = CC · ΔV/Δt. However, in this circuit, the voltage gain at RL causes a much larger ΔV across CC - causing an even larger current to flow through CC. Therefore, it looks like a much larger capacitance from the point of view of VIN.




### Example 9.7.3 Miller Capacitance Example




In this example we will use the circuit shown in figure 9.7.5 to illustrate the Miller multiplication of the feedback capacitor CC. Bias resistors R1 and RS are chosen to set the DC operating point such that Vout is at a DC value of approximately V+/2 or 5V. With the given RL of 10KΩ the low frequency small signal voltage gain AV is approximately 80. 




We can now calculate the -3 dB frequency and unity gain (0dB) frequency for a feedback capacitor, CC, of 0.001 uF. The frequency where the gain from Vin to Vout falls by -3 dB from its DC values is approximately equal to:




The unity gain frequency is approximately equal to :




[![](/_media/university/courses/electronics/text/chptr9-f32.png?w=500&tok=3b2852)](/_detail/university/courses/electronics/text/chptr9-f32.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-9 "university:courses:electronics:text:chptr9-f32.png")





 Figure 9.7.5 Miller Capacitance Example 





The circuit in figure 9.7.5 was simulated and the AC frequency response from 1 Hz to 1 MHz is plotted in figure 9.7.6. The gain from Vin to Vout in dB is 20Log(AV) or about 38 dB. The -3 dB frequency in this case would be where the gain curve crosses 35 dB (~263 Hz) and the unit gain frequency would be where the gain curve crosses the 0 dB line (~21.7 KHz ). The simulation results are in reasonably close agreement with our approximate hand calculations. For our hand calculations we assumed that R1 was sufficiently larger than RS so it could be ignored and likewise the rπ of Q1 was large enough to not materially affect RS.




[![](/_media/university/courses/electronics/text/chptr9-f33.png?w=500&tok=eeb0c7)](/_detail/university/courses/electronics/text/chptr9-f33.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-9 "university:courses:electronics:text:chptr9-f33.png")





 Figure 9.7.6 Frequency sweep simulation 





## Chapter Summary:



* The Common Emitter stage has high gain but low input and high output impedance.
* RE emitter degeneration improves input impedance and provides negative feedback to stabilize DC operating point but with some loss in gain.
* The Common Base stage has low input, high output impedance but is good at high frequencies. Good current buffer sometimes called the current follower.
* The Common Collector or Emitter follower can be biased with large input impedance, low output impedance but has approximately unity gain. Good voltage buffer.



### Appendix: Source absorption theorem




The source absorption theorem has two dual forms: the voltage source absorption and the current source absorption theorems.




The voltage source absorption theorem states that if, in one branch of the circuit with current I, there is a voltage source controlled by I, the source can be replaced by a simple impedance with value equal to the source controlling factor.




[![](/_media/university/courses/electronics/text/chptr9-f34.png?w=500&tok=6667b8)](/_detail/university/courses/electronics/text/chptr9-f34.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-9 "university:courses:electronics:text:chptr9-f34.png")





 Figure 9A.1 





The proof is trivial. An impedance Z where a current I flows has the same voltage drop the I controlled source generates at its terminals.




The current source absorption theorem states that if, in one branch of the circuit there is a current source controlled by a voltage V, the source can be replaced by a simple admittance with value equal to the source controlling factor.




[![](/_media/university/courses/electronics/text/chptr9-f35.png?w=500&tok=276111)](/_detail/university/courses/electronics/text/chptr9-f35.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-9 "university:courses:electronics:text:chptr9-f35.png")





 Figure 9A.2 





The proof is again trivial. An admittance Y submitted to a voltage V imposes the same current that the source Y V provides.




### Example A1: Finding the Emitter Resistance using Source absorption theorem




Figure A9.3 shows the small signal equivalent circuit model of a transistor. Find the resistance Rin looking into the emitter (with base and collector at small signal AC grounds).




[![](/_media/university/courses/electronics/text/chptr9-f36.png?w=500&tok=aee7cd)](/_detail/university/courses/electronics/text/chptr9-f36.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-9 "university:courses:electronics:text:chptr9-f36.png")





 Figure 9A.3 





Using what we just learned about the source absorption theorem for current sources we know we can replace the controlled source with a resistance equal to 1/gmits transconductance.




## Advanced Topics:




### AT1 Diode bias generation




[![](/_media/university/courses/electronics/text/chptr9-f37.png?w=500&tok=578414)](/_detail/university/courses/electronics/text/chptr9-f37.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-9 "university:courses:electronics:text:chptr9-f37.png")





 Figure AT1.1 Inserting a Diode connected device in the bias divider 





[![](/_media/university/courses/electronics/text/chptr9-f38.png?w=500&tok=a2332d)](/_detail/university/courses/electronics/text/chptr9-f38.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-9 "university:courses:electronics:text:chptr9-f38.png")





 Figure AT1.2 Inserting R2increases the input resistance 





**Return to [Previous Chapter](/university/courses/electronics/text/chapter-8 "university:courses:electronics:text:chapter-8")**




**Go to [Next Chapter](/university/courses/electronics/text/chapter-10 "university:courses:electronics:text:chapter-10")**




**Return to [Table of Contents](/university/courses/electronics/text/electronics-toc "university:courses:electronics:text:electronics-toc")**






university/courses/electronics/text/chapter-9.txt · Last modified: 07 Oct 2020 14:37 by [Doug Mercer](https://ez.analog.com/members/dmercer)

