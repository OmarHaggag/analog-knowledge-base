



This version (08 Dec 2025 14:53) was *approved* by [Mark Thoren](https://ez.analog.com/members/MarkThoren).

### Table of Contents



* [Chapter 15. MOSFET Applications:](#chapter_15_mosfet_applications)
	+ [15.1 MOSFET as an analog switch](#mosfet_as_an_analog_switch)
		- [15.1.1 Single-type MOSFET switch](#single-type_mosfet_switch)
		- [15.1.2 Complementary (CMOS) type MOSFET switch, Transmission gate](#complementary_cmos_type_mosfet_switch_transmission_gate)
	+ [15.2 Chopper Stabilized (Auto-Zero) Precision Op Amps](#chopper_stabilized_auto-zero_precision_op_amps)
		- [15.2.1 Basic Chopper Amplifier](#basic_chopper_amplifier)
		- [15.2.2 Auto-Zero Chopper Stabilized OP AMP](#auto-zero_chopper_stabilized_op_amp)
		- [15.2.3 Noise Considerations for Chopper Stabilized OP AMPS](#noise_considerations_for_chopper_stabilized_op_amps)
	+ [15.3 Switched Capacitor Circuits](#switched_capacitor_circuits)
		- [15.3.1 The switched capacitor resistor:](#the_switched_capacitor_resistor)
		- [15.3.2 Example Switched Capacitor Low Pass Filter](#example_switched_capacitor_low_pass_filter)
		- [15.3.3 Switched capacitor differencing circuit](#switched_capacitor_differencing_circuit)





# Chapter 15. MOSFET Applications:




In this chapter we will be exploring certain applications for MSOFET devices other than as linear amplifier stages.




## 15.1 MOSFET as an analog switch




Enhancement mode MOSFET based analog switches use the transistor channel as a low resistance to pass analog signals when on, and as a high impedance when off. Signals can flow in either direction across a MOSFET switch. In this application the drain and source of a MOSFET exchange places depending on the voltages of each electrode compared to that of the gate and the direction of current flow. For a simple MOSFET without an integrated diode from source to drain (or the back gate or body terminal tied to the source), the source is the more negative side for an NMOS or the more positive side for a PMOS. All of these switches are limited as to what signals they can pass when on or block when off by their gate-source, gate-drain and source-drain voltages, and source-to-drain currents; exceeding these voltage or current limits will potentially damage the switch.




### 15.1.1 Single-type MOSFET switch




This analog switch uses a four-terminal simple, generally enhancement mode, MOSFET of either P or N type. In the case of an N-type switch, the body or back gate terminal is connected to the most negative supply (usually GND in single power supply systems) and the gate is used as the switch control. Whenever the gate voltage exceeds the source voltage by at least a threshold voltage, the MOSFET conducts. The higher the gate voltage with respect to the source, the lower the resistance of the switch will be. An NMOS switch passes all voltages less than (Vgate-Vtn). When the switch is conducting, it typically operates in the linear (or triode) region of operation, since the source and drain voltages will typically be nearly equal.




[![](/_media/university/courses/electronics/text/chptr15_f1.png?w=500&tok=6461c4)](/_detail/university/courses/electronics/text/chptr15_f1.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-15 "university:courses:electronics:text:chptr15_f1.png")





 Figure 15.1.1 MOSFET cross sections 





In the case of a PMOS, the body or back gate is connected to the most positive voltage, and the gate is brought to a lower potential to turn the switch on. The PMOS switch passes all voltages higher than (Vgate+|Vtp|). Threshold voltage (Vtp) is typically negative in the case of PMOS.




[![](/_media/university/courses/electronics/text/chptr15_f2.png?w=600&tok=24ba25)](/_detail/university/courses/electronics/text/chptr15_f2.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-15 "university:courses:electronics:text:chptr15_f2.png")





 Figure 15.1.2 MOS Ids vs Vds curves 





A PMOS switch will have about three times the resistance of an NMOS device of equal dimensions because electrons have about three times the mobility of holes in silicon.




[![](/_media/university/courses/electronics/text/chptr15_f3.png?w=500&tok=ee0206)](/_detail/university/courses/electronics/text/chptr15_f3.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-15 "university:courses:electronics:text:chptr15_f3.png")





 Figure 15.1.4 NMOS and PMOS turn on characteristics 





### 15.1.2 Complementary (CMOS) type MOSFET switch, Transmission gate




This “complementary” or CMOS type of switch uses one PMOS and one NMOS FET to counteract the turn on limitations of the single-type switch. The FETs have their drains and sources connected in parallel, the body of the PMOS is connected to the high potential (VDD) and the body of the NMOS is connected to the low potential (GND). To turn the switch on the gate of the PMOS is driven to the low potential and the gate of the NMOS is driven to the high potential. For voltages between (VDD-Vtn) and (GND+Vtp) both FETs conduct the signal, for voltages less than (GND+Vtp) the NMOS conducts alone and for voltages greater than (VDD-Vtn) the PMOS conducts alone.




[![](/_media/university/courses/electronics/text/chptr15_f4.png?w=500&tok=2018a7)](/_detail/university/courses/electronics/text/chptr15_f4.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-15 "university:courses:electronics:text:chptr15_f4.png")





 Figure 15.1.5 Switch resistance vs applied voltage. NMOS, PMOS, CMOS 





The only limits for this switch are the gate-source, gate-drain and source-drain voltage limits for both FETs. Also, the PMOS is typically three times the width of the NMOS so the switch on resistance will be balanced across the signal voltage.




Tri-state circuitry used in digital logic or data buses sometimes incorporates a CMOS MOSFET switch on its output to provide for a low ohmic, full range output when on and a high ohmic, mid-level signal when off.




**ADALM1000 Lab Activity 18, [CMOS Analog Switches](/university/courses/alm1k/alm-lab-18 "university:courses:alm1k:alm-lab-18")**




**ADALM2000 Lab Activity 18, [CMOS Analog Switches](/university/courses/electronics/electronics-lab-18 "university:courses:electronics:electronics-lab-18")**




## 15.2 Chopper Stabilized (Auto-Zero) Precision Op Amps




For the lowest offset and drift performance, chopper-stabilized ( or auto-zero ) amplifiers may be the best solution. The best bipolar amplifiers offer offset voltages of 25 µV and 0.1 µV/ºC drift. Offset voltages less than 5 µV with practically no measurable offset drift are obtainable by using chopper stabilization techniques, albeit with some penalties.




### 15.2.1 Basic Chopper Amplifier




A basic chopper amplifier circuit is shown in figure 15.2.1 below. This is a common example where the CMOS analog switch we just discussed in section 15.1 can be put to good use. When the switches are in the “Z” (auto-zero) position, capacitors C2 and C3 are charged to the amplifier input and output offset voltage, respectively. When the switches are in the “S” (sample) position, VIN is connected to VOUT through the path comprised of R1, R2, C2, the amplifier, C3, and R3. The frequency used to chop is usually between a few hundred Hz and several kHz, and it should be noted that because this is a sampling system, the input frequency must be much less than one-half the chopping frequency in order to prevent errors due to aliasing. The R1-C1 combination serves as an antialiasing filter. It is also assumed that after a steady state condition is reached, there is only a minimal amount of charge transferred during the switching cycles. The output “hold” capacitor, C4, and the load, RL, must be chosen such that there is minimal VOUT droop during the auto-zero cycle.




[![](/_media/university/courses/electronics/text/chptr15_f5.png?w=500&tok=f406fb)](/_detail/university/courses/electronics/text/chptr15_f5.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-15 "university:courses:electronics:text:chptr15_f5.png")





 Figure 15.2.1: Classic Chopper Amplifier 





**ADALM2000 Lab Activity [CMOS Amplifier](/university/courses/electronics/electronics-lab-20 "university:courses:electronics:electronics-lab-20")**




### 15.2.2 Auto-Zero Chopper Stabilized OP AMP




The basic chopper amplifier of figure 15.2.1 can pass only frequencies lower than one half the chopping frequency because of the input filtering required to prevent aliasing. In contrast to this, the chopper-stabilized architecture shown in figure 15.2.2 is most often used in chopper op amp implementations.




[![](/_media/university/courses/electronics/text/chptr15_f6.png?w=500&tok=d137b4)](/_detail/university/courses/electronics/text/chptr15_f6.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-15 "university:courses:electronics:text:chptr15_f6.png")





 Figure 15.2.2: Auto-Zero (Chopper-Stabilized) Op Amp 





In this circuit, A1 is the main amplifier, and A2 is the nulling amplifier. Both amplifiers are considered identical and both have an additional Null input terminal. In the sample mode (switches in “S” position), the nulling amplifier, A2, monitors the input offset voltage of A1 and drives its output to zero by applying a suitable correcting voltage at A1's Null pin. Note, however, that A2 also has an input offset voltage, so it must correct its own error before attempting to null A1's offset. This is achieved in the auto-zero mode (switches in “Z” position) by momentarily disconnecting A2 from A1, shorting its inputs together, and coupling its output to its own Null pin. During the auto-zero mode, the correction voltage for A1 is momentarily held by C1. Similarly, C2 holds the correction voltage for A2 during the sample mode. In integrated IC chopper-stabilized op amps, both amplifiers and the storage capacitors C1 and C2 are on a single chip.




Note in this architecture that the input signal is always connected to the output, through A1. The bandwidth of A1 thus determines the overall signal bandwidth, and the input signal is not limited to less than one-half the chopping frequency as in the case of the traditional chopper amplifier architecture. However, the switching action does produce small transients at the chopping frequency, that can mix with the input signal frequency and produce intermodulation distortion.




### 15.2.3 Noise Considerations for Chopper Stabilized OP AMPS




It is interesting to consider the effects of a chopper amplifier on low frequency 1/f noise. If the chopping frequency is considerably higher than the 1/f corner frequency of the input noise, the chopper-stabilized amplifier continuously nulls out the 1/f noise on a sample-by-sample basis. Theoretically, a chopper op amp therefore has no 1/f noise. However, the chopping action produces wideband switching noise which is generally much worse than that of a precision bipolar op amp and would need to be filtered out.




In order to take advantage of the chopper op amp's lack of 1/f noise, much filtering is required, otherwise the total noise of a chopper will always be worse than a good bipolar op amp. Chopper stabilized amplifiers should therefore be used because of their low offset voltage and offset temperature drift, not necessarily because of their lack of 1/f noise.




## 15.3 Switched Capacitor Circuits




A switched capacitor is an electronic circuit element used in discrete time signal processing systems. It works by transferring charge into and out of a capacitor when switches are opened and closed. This is another example where the CMOS analog switch discussed in section 15.1 is used almost exclusively. 
Usually, non-overlapping signals are used to control the switches, often termed Break before Make switching, so that all switches are open for a very short time during the switching transitions. Discrete time filters implemented with these elements are termed 'switched-capacitor filters'. Unlike continuous time analog filters, which must be constructed with resistors, capacitors and sometimes inductors whose values are accurately known, switched capacitor filters depend only on the ratios between capacitances and the switching frequency. This makes them much more suitable for use within integrated circuits, where the accurately specified absolute value of components such as resistors and capacitors are not economical to construct.




### 15.3.1 The switched capacitor resistor:




The most basic switched capacitor circuit as illustrated in figure 15.3.1, is the switched capacitor resistor. It consists of one capacitor C1 and two switches S1 and S2 which connect the capacitor alternately to the input, VIN and the output, VOUT. 




[![](/_media/university/courses/electronics/text/chptr15_f7.png?w=500&tok=d0e3c9)](/_detail/university/courses/electronics/text/chptr15_f7.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-15 "university:courses:electronics:text:chptr15_f7.png")





 Figure 15.3.1, Basic Switched Capacitor Resistor 





Each switching cycle transfers a charge ?q from the input to the output at the switching frequency F. Recall that the charge q on a capacitor C with a voltage V between the plates is given by:




![q = CV](/lib/plugins/mathpublish/img.php?img=98751ca0989aa03817e233a6a0f94ec6 "q = CV")




Where V is the voltage across the capacitor. Therefore, when S1 is closed while S2 is open, the charge transferred from the input source to C is:




![q_IN = C_1V_IN](/lib/plugins/mathpublish/img.php?img=f3315bf0664d3f652781fc1870355a95 "q_IN = C_1V_IN")




And when S2 is closed while S1 is open, the charge transferred from C1 to the output is:




![q_OUT = C_1 V_OUT](/lib/plugins/mathpublish/img.php?img=b228661ca27858753008bab1ef4a2322 "q_OUT = C_1 V_OUT")




The charge Δq transferred in each cycle is:




![Δq = q_OUT - q_IN = C_1 ( V_OUT - V_IN )](/lib/plugins/mathpublish/img.php?img=31a1c1aff20178e41801a06aec04cdd6 "Δq = q_OUT - q_IN = C_1 ( V_OUT - V_IN )")




Since a charge ?q is transferred at a rate F, the rate of transfer of charge per unit time is:




![I = ΔqF](/lib/plugins/mathpublish/img.php?img=61e8b52b337511155217fbe348bf3b3a "I = ΔqF")




Note that I is used, the symbol for electric current, for this quantity. This is to demonstrate that a continuous transfer of charge from one node to another is the same as current. Substituting for Δq in the equation above, we get:




![I = C_1 ( V_OUT - V_IN ) F](/lib/plugins/mathpublish/img.php?img=024447db89d0a71a204334225e205013 "I = C_1 ( V_OUT - V_IN ) F")




We define ΔV, the voltage across the circuit from input to output, as:




![ΔV = V_OUT - V_IN](/lib/plugins/mathpublish/img.php?img=6dfd020f5cedf13eb2d5796a9749513b "ΔV = V_OUT - V_IN")




We now have a relationship between I and V, which we can rearrange to give an equivalent resistance R:




![R = V / I = 1 / (C_1 F)](/lib/plugins/mathpublish/img.php?img=eab79a5246a8c2f8dcb926812186f191 "R = V / I = 1 / (C_1 F)")




Thus, the circuit behaves like a resistor whose value depends on C1 and F.




The Switched Capacitor resistor is often used as a replacement for simple resistors in integrated circuits because it is easier to fabricate reliably with a wide range of values. It also has the benefit that the equivalent resistor value can be adjusted by changing the switching frequency.




This same circuit can be used in discrete time systems (such as analog to digital converters) as a track and hold circuit. During the appropriate clock phase, the capacitor samples the analog voltage through switch one and in the second phase presents this held sampled value to the next part of the electronic system for further processing.




### 15.3.2 Example Switched Capacitor Low Pass Filter




Now we can examine an example circuit using the Switched Capacitor as a resistor. By adding a second capacitor C2 across the output of figure 15.3.1, we get the RC low pass circuit shown in figure 15.3.2.




[![](/_media/university/courses/electronics/text/chptr15_f8.png?w=500&tok=51f23c)](/_detail/university/courses/electronics/text/chptr15_f8.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-15 "university:courses:electronics:text:chptr15_f8.png")





 Figure 15.3.2, Switched Capacitor RC low pass filter 





From the previous section we get the equation for the equivalent resistor R:




![R_eq = 1 / (C_1 F_clock)](/lib/plugins/mathpublish/img.php?img=b3c462acf07314e7b4f3adf46e46226d "R_eq = 1 / (C_1 F_clock)")




The 3 dB frequency response of a single pole RC low pass filter is:




![F_3db = 1 / (2πR_eq C_2 )](/lib/plugins/mathpublish/img.php?img=c59f070210f519e3aac36e8cd5507392 "F_3db = 1 / (2πR_eq C_2 )")




Substituting the switched capacitor resistor Req in to the frequency response we get:




![F_3db = ( C_1 F_clock ) / ( 2πC_2 )](/lib/plugins/mathpublish/img.php?img=d078a805fd30699eb9cfcc78a3a835b2 "F_3db = ( C_1 F_clock ) / ( 2πC_2 )")




So we can see that the 3 dB frequency response is directly related to the clock frequency and the ratio of C1 to C2.




The following two graphs plot the frequency response for the basic switched capacitor low pass filter from figure 15.3.2 with the value of C1 equal to 100pF and with the value of C2 equal to 4.7nF for a C1 to C2 ratio of 1 to 47. Figure 15.3.3 plots the amplitude vs. frequency response for Fclock equal to 100 KHz, 200 KHz and 500 KHz. Figure 15.3.4 plots the phase vs. frequency for the same three clock frequencies.




[![](/_media/university/courses/electronics/text/chptr15_f9.png?w=600&tok=be8b5e)](/_detail/university/courses/electronics/text/chptr15_f9.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-15 "university:courses:electronics:text:chptr15_f9.png")





 Figure 15.3.3 Filter output amplitude vs frequency plot for three different switching frequencies 





[![](/_media/university/courses/electronics/text/chptr15_f10.png?w=600&tok=e696df)](/_detail/university/courses/electronics/text/chptr15_f10.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-15 "university:courses:electronics:text:chptr15_f10.png")





 Figure 15.3.4 Filter output phase vs frequency plot for three different switching frequencies 





Note that the amplitude curve for 200 KHz switching frequency crosses the -5 dB line at exactly twice the input frequency as the 100 KHz curve. And that the 500 KHz curve crosses at a frequency 2.5 times the frequency of the 200 KHz curve.




**ADALM2000 Lab Activity [Switched Capacitor Circuits](/university/courses/electronics/electronics-lab-19 "university:courses:electronics:electronics-lab-19")**




### 15.3.3 Switched capacitor differencing circuit




A switched capacitor differential to single ended configuration is shown in figure 15.3.5. In this circuit capacitor C1 is charged to the differential voltage applied to VIN $s$+$s$ and VIN $s$-$s$ during the first half of the clock cycle when switches S1 and S2 are closed as shown in the figure, to position 1. During the second half of the clock cycle switches S1 and S2 are moved to position 2 connecting capacitor C1 in parallel with capacitor C2. One end of C2 is connected to ground so that the voltage seen at VOUT is referenced to ground and will, in steady state, be equal to VIN $s$+$s$ - VIN $s$-$s$. The values of capacitors C1 and C2 can in general be in any ratio but often they are equal or C2 is sized to be larger than C1 depending on the nature of the load the circuit might be required to drive at VOUT.




[![](/_media/university/courses/electronics/text/chptr15_f11.png?w=500&tok=3b6289)](/_detail/university/courses/electronics/text/chptr15_f11.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-15 "university:courses:electronics:text:chptr15_f11.png")





 Figure 15.3.5 Differential input to single ended output circuit 





The capacitor used to transfer the input voltage to the output in these circuits is typically known as the “flying capacitor”.




**Other Flying-Capacitor applications:**




In addition to the differential to single ended function we saw in figure 15.3.5, flying capacitor configurations can double the input voltage, triple the voltage, halve the voltage, invert the voltage, fractionally multiply or scale voltages such as x3/2, x4/3, x2/3, etc. and generate arbitrary voltages, depending on the capacitor ratios and circuit topology. The following are additional useful variations of the flying-capacitor circuit from figure 15.3.5.




The first is a voltage inverter where the output voltage VOUT is the negative of VIN, VOUT = -VIN shown in figure 15.3.6. Very similar to the first configuration but with what was VIN $s$-$s$ now connected to ground and ground on the output side now connected to one terminal of S1 and the now inverted output voltage taken at one terminal of S2.




[![](/_media/university/courses/electronics/text/chptr15_f12.png?w=500&tok=6946e0)](/_detail/university/courses/electronics/text/chptr15_f12.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-15 "university:courses:electronics:text:chptr15_f12.png")





 Figure 15.3.6 Voltage inverter 





The flying capacitor circuit can also be configured as a precession divide by 2 voltage divider as we see in figure 15.3.7. During the first half of the clock cycle, with switches S1 and S2 in position 1, the two capacitors, C1 and C2, are placed in series across VIN. If C1 is exactly equal to C2 then they will act as a voltage divider with VOUT equal to one half VIN. This assumes that there was no preexisting charge on either capacitor. During the second half of the clock cycle when S1 and S2 are in position 2, the two capacitors are connected in parallel. This will cause the voltage across both capacitors to be equal and thus redistribute any preexisting charge difference to redistribute equally between the two capacitors. After a few clock cycles the voltage across each capacitor will be equal to each other and equal to one half of VIN.




[![](/_media/university/courses/electronics/text/chptr15_f13.png?w=500&tok=3b7d8c)](/_detail/university/courses/electronics/text/chptr15_f13.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-15 "university:courses:electronics:text:chptr15_f13.png")





 Figure 15.3.7 Divide VIN by 2 circuit 





Similarly, the circuit in figure 15.3.7 can be configured as a precession multiply by 2 voltage multiplier as we see in figure 15.3.8. In this example, capacitor C1 is charged to VIN during the first half clock cycle when switches S1 and S2 are in position 1. During the second half clock cycle when switches S1 and S2 are in position 2, the previously grounded end of C1 is now connected to VIN. The other end of C1 which was previously connected to VIN is now connected to VOUT. Now VOUT will be equal to VIN plus the VIN stored on capacitor C1 or 2xVIN. Capacitor C2 will take a few clock cycles to charge up to 2xVIN and will serve to store or hold the voltage at VOUT at 2xVIN while the switches are in position 1, sampling VIN onto C1.




[![](/_media/university/courses/electronics/text/chptr15_f14.png?w=500&tok=78ddd1)](/_detail/university/courses/electronics/text/chptr15_f14.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-15 "university:courses:electronics:text:chptr15_f14.png")





 Figure 15.3.8 voltage multiplier 





So far in this section we have been assuming that VIN is some varying arbitrary signal which presumably carries some sort of information in a system. VIN could just as easily be a DC power supply voltage which we wish to scale up or down in voltage to be used elsewhere in the system. When used for this application flying capacitor circuits are often called DC/DC converters. Because we are trying to transfer power from VIN to VOUT in this application the MOS transistors are much larger to carry higher currents with low on resistance and the capacitors have much higher values to store more charge and deliver it to the load during the half of the clock cycle when charge is not being transferred from the input supply.




The basic concept of a capacitor based DC to DC power converter is shown below in figure 15.3.9. As we said these are often referred to as “flying capacitor” or “charge-pump” DC/DC converters. The operation alternates between the two configurations shown in figure 15.3.9 which is in effect two copies of the circuit we saw in figure 15.3.8. On the left, switches S1 and S5 are closed connecting C1 between ground and VIN. On the right, switches S4 and S8 are closed connecting C2 between VIN and VOUT. For the half cycle shown capacitor C1 is charged to the voltage at VIN and VOUT is the sum of the voltage at VIN and the voltage on capacitor C2. For the second half cycle the switches are reversed. Now with S2 and S6 closed C1 is connected between VIN and VOUT. Also switches S3 and S7 will now be closed connecting C2 between ground and VIN. So now we can see that after a few cycles VOUT, the voltage across capacitor C3 will be equal to twice VIN. As you can see the capacitors “fly” back and forth between VIN and VOUT, thus the name “flying capacitor”. One can also see that what is in effect happening is the charge on capacitors C1 and C2 is alternately transferred or pumped onto capacitor C3 charging it up to two times VIN. This action gives rise to the second “charge pump” name. 




[![](/_media/university/courses/electronics/text/chptr15_f15.png?w=600&tok=e2d874)](/_detail/university/courses/electronics/text/chptr15_f15.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-15 "university:courses:electronics:text:chptr15_f15.png")





 Figure 15.3.9 Capacitor based voltage doubler with ideal switches 





We will now replace the ideal switches in the diagram with MOSFET switches. The next diagram figure 15.3.10, shows a direct substitution of NMOS ( S1,S3,S5,S7 ) and PMOS ( S2,S4,S6,S8 ) devices for the switches in the first diagram. It can be noted that switches S1 and S2 form a complementary pair and take the same form as a CMOS inverter logic gate. The other three sets of switches form similar complementary pairs.




[![](/_media/university/courses/electronics/text/chptr15_f16.png?w=600&tok=94e1aa)](/_detail/university/courses/electronics/text/chptr15_f16.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-15 "university:courses:electronics:text:chptr15_f16.png")





 Figure 15.3.10 CMOS voltage doubler 





**Return to [Previous Chapter](/university/courses/electronics/text/chapter-14 "university:courses:electronics:text:chapter-14")**




**Go to [Next Chapter](/university/courses/electronics/text/chapter-16 "university:courses:electronics:text:chapter-16")**




**Return to [Table of Contents](/university/courses/electronics/text/electronics-toc "university:courses:electronics:text:electronics-toc")**






university/courses/electronics/text/chapter-15.txt · Last modified: 06 Jun 2017 15:58 by [Doug Mercer](https://ez.analog.com/members/dmercer)

