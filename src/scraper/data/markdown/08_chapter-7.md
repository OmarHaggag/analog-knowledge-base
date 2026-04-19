



This version (18 Mar 2018 16:52) was *approved* by [Doug Mercer](https://ez.analog.com/members/dmercer).The [Previously approved version](/university/courses/electronics/text/chapter-7?rev=1496761559) (06 Jun 2017 15:05) is available.[![Diff](/lib/images/diff.png)](https://wiki.analog.com/university/courses/electronics/text/chapter-7?do=diff&rev2[0]=1496761559&rev2[1]=1521391923&difftype=sidebyside)

### Table of Contents



* [Chapter 7: Diode application topics](#chapter_7diode_application_topics)
	+ [7.1 Half-wave rectifier with filter capacitor or peak detector](#half-wave_rectifier_with_filter_capacitor_or_peak_detector)
	+ [7.2 Absolute value circuits](#absolute_value_circuits)
		- [7.2.1 Precision half wave rectifier](#precision_half_wave_rectifier)
		- [An Application Example: Measuring the peak value of an AC Voltage](#an_application_examplemeasuring_the_peak_value_of_an_ac_voltage)
		- [7.2.2 Precision full wave rectifier](#precision_full_wave_rectifier)
	+ [7.3 Envelope Detector](#envelope_detector)
	+ [7.4 Diode Clamp](#diode_clamp)
		- [Op-amp clamp circuit](#op-amp_clamp_circuit)
	+ [7.5 Diode Clippers / Limiters](#diode_clipperslimiters)
	+ [7.6 Voltage controlled variable attenuator](#voltage_controlled_variable_attenuator)
	+ [7.7 Logarithmic output amplifiers](#logarithmic_output_amplifiers)
	+ [7.8 Exponential (antilog) output amplifiers](#exponential_antilog_output_amplifiers)





# Chapter 7: Diode application topics




In this chapter we will investigate a variety of circuits that make use of certain characteristics of the PN junction diode. In chapter 6 we discussed the use of the diode as a means to convert AC power into DC power. There are other cases where a time varying signal might need to be converted into a DC signal. In these situations it is often desirable to effectively cancel or correct for the forward voltage drop of the diode to accurately measure the required value of the signal.




Another property of the diode is that the small signal conductance (or resistance) of the diode is a function of the DC current flowing through the diode (the operating point). This characteristic can be used to make a voltage (actually current) dependent attenuator. Also as we discovered in chapter 5 the diode voltage, in the forward conduction region, is exponentially related to the current through the diode. This property can be used to make non-linear amplifier circuits which have either logarithmic or anti-logarithmic (exponential) input to output relationships. 




## 7.1 Half-wave rectifier with filter capacitor or peak detector




The simplest form of a peak detector circuit is the series connection of a diode and a capacitor which outputs a DC voltage across the capacitor equal to the peak value of the input AC signal (minus the forward bias voltage drop of the diode). A switch of some sort in parallel with the capacitor is generally needed to periodically reset the output voltage such as when a new peak detection is desired.




[![](/_media/university/courses/electronics/text/chptr7-f1.png?w=600&tok=d97e78)](/_detail/university/courses/electronics/text/chptr7-f1.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-7 "university:courses:electronics:text:chptr7-f1.png")





 Figure 7.1.1 Simple peak detector 





With the diode facing as shown in figure 7.1.1 the circuit detects the positive peaks. If the direction of the diode were reversed then the circuit will detect the negative peaks of the input. The output of the simple peak detector is not actually the true peak value of the input due to the inherent built-in voltage drop of the diode. By including an op-amp as in figure 7.1.2 the error due to the diode drop is greatly reduced by the forward gain of the op-amp.




[![](/_media/university/courses/electronics/text/chptr7-f2.png?w=600&tok=143d83)](/_detail/university/courses/electronics/text/chptr7-f2.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-7 "university:courses:electronics:text:chptr7-f2.png")





 Figure 7.1.2 Precession half-wave rectifier or peak detector 





There is, however, a fundamental problem with this simple circuit in that when the input signal is less (more negative) than the voltage being held on the capacitor, the diode will be reverse biased and the output of the op amp will be “disconnected” from the inverting input terminal. The amplifier will in this case have no negative feedback and the op amp output will saturate at the negative supply rail. When the input voltage again becomes more positive than the voltage held on the capacitor and the output moves out of saturation the response time of the amplifier will be affected. The circuit may not respond properly to fast, short duration positive peaks in the input signal. We will investigate a better form of the half wave rectifier in the next section.




## 7.2 Absolute value circuits




In this section we investigate absolute value circuits. Rectifiers, or 'absolute-value' circuits are often used as detectors to convert the amplitudes of AC signals to DC values to be more easily measured. For this type of circuit, the AC signal is first high-pass filtered to remove any DC term and then rectified and perhaps low pass filtered. As we discovered in Chapter 6, the simple rectifier circuits constructed with diodes does not respond well to signals with a magnitude less than a diode-drop (0.6V for silicon diodes). This limits their use in designs where small amplitudes need to be measured. For designs in which a high degree of precision is needed, op-amps can be used in conjunction with diodes to build precision rectifiers or absolute value circuits.




### 7.2.1 Precision half wave rectifier




The inverting op-amp circuit can be converted into an “ideal” (linear precision) half-wave rectifier by adding two diodes as shown in figure 7.2.1. For the negative half of the input swing, diode D1 is reverse biased and diode D2 is forward biased and the circuit operates as a conventional inverter with a gain of -1, assuming that R1=R2. For the positive half of the input swing, diode D1 is forward biased, closing the feedback around the amplifier. Diode D2 is reverse biased disconnecting the output from the amplifier. The output will be at the virtual ground potential (- input terminal) through resistor R2.




[![](/_media/university/courses/electronics/text/chptr7-f3.png?w=600&tok=ecb170)](/_detail/university/courses/electronics/text/chptr7-f3.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-7 "university:courses:electronics:text:chptr7-f3.png")





 Figure 7.2.1 Precision half-wave rectifier circuit. 





The peak of the rectified output, as seen in figure 7.2.2, is now equal to the peak value of the input. There is also a sharp transition as the input crosses zero. The reader should investigate the waveforms at different points in the circuit, such as the op amp output, to explain why this circuit works better than the simple diode half wave rectifier.




[![](/_media/university/courses/electronics/text/chptr7-f4.png?w=600&tok=22599c)](/_detail/university/courses/electronics/text/chptr7-f4.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-7 "university:courses:electronics:text:chptr7-f4.png")





 Figure 7.2.2 Precision half-wave rectifier simulation. 





### An Application Example: Measuring the peak value of an AC Voltage




We only have access to a DC voltmeter and need to design a circuit that can measure the peak voltage of an AC signal. We can use the precision half wave rectifier to provide just the negative half of the input signal and then low pass filter the rectified output as shown in figure 7.2.3. What is the DC output voltage of the following circuit if R1 = 3.24 kΩ, R2 = 10.2 kΩ, R3= 20 kΩ and R4 = 20 kΩ Assume Vp = 1 V.




[![](/_media/university/courses/electronics/text/chptr7-f5.png?w=600&tok=fecb4c)](/_detail/university/courses/electronics/text/chptr7-f5.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-7 "university:courses:electronics:text:chptr7-f5.png")





 Figure 7.2.3 





For a sine wave input with peak value VP the output of the half wave rectifier is a half sine wave with a peak value of VP(R2/R1). The half sine wave has a DC component given by:




[![](/_media/university/courses/electronics/text/chptr7-e1.png?w=500&tok=87e269)](/_detail/university/courses/electronics/text/chptr7-e1.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-7 "university:courses:electronics:text:chptr7-e1.png")




The first order low pass filter will remove the AC content and pass the DC component with a gain equal to R4/R3. The final DC output will be:




[![](/_media/university/courses/electronics/text/chptr7-e2.png?w=250&tok=4a7952)](/_detail/university/courses/electronics/text/chptr7-e2.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-7 "university:courses:electronics:text:chptr7-e2.png")




### 7.2.2 Precision full wave rectifier




The circuit shown figure 7.2.4 isan absolute value circuit, often called a precision full-wave rectifier. It should operate like a full wave rectifier circuit constructed with ideal diodes (the voltage across the diode, in forward conduction, equals 0 volts). The actual diodes used in the circuit will have a forward voltage of around 0.6 V. In order for both halves of the input waveform to have the same gain from the input to the output resistor R2 = R3 and R4 = R5.




[![](/_media/university/courses/electronics/text/chptr7-f6.png?w=600&tok=df475a)](/_detail/university/courses/electronics/text/chptr7-f6.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-7 "university:courses:electronics:text:chptr7-f6.png")





 Figure 7.2.4 Absolute value circuit. 





If the value of R1 is made lower than R2 and R3, the circuit has gain. If the value of R1 is higher than R2 and R3, the circuit can accept higher input voltages because it acts as an attenuator. For example, if R1 is 1kΩ with R2 and R3 equal to 10kΩ, the circuit has a gain of 10, and if R1 is 100kΩ, the gain is 0.1 (an attenuation of 10). All other normal opamp restrictions apply like other inverting op amp stages, so if a high gain is used the frequency response will be affected.




The input impedance of the circuit is equal to the value of R1, and is constant as long as the first op amp is operating within its limits, that is it's inverting input is at a virtual ground. One interesting feature of using the inverting topology is that it allows the circuit to function as a summation circuit for multiple inputs. R1 can be replicated to provide a second input, or it could be extended with a third resistor etc.




The peak of the rectified output, as seen in figure 7.2.5, is again equal to the peak value of the input. There is the sharp transition as the input crosses zero. The reader should investigate the waveforms at different points in the circuit, such as the op amp output and across the diodes, to explain why this circuit works better than the diode full wave or bridge rectifier.




[![](/_media/university/courses/electronics/text/chptr7-f7.png?w=600&tok=e949ee)](/_detail/university/courses/electronics/text/chptr7-f7.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-7 "university:courses:electronics:text:chptr7-f7.png")





 Figure 7.2.5 Full-wave rectifier simulation. 





**ADALM1000 Lab Activity,  [Precision Rectifiers, Absolute value circuits](/university/courses/alm1k/circuits1/alm-cir-precision-rectifier "university:courses:alm1k:circuits1:alm-cir-precision-rectifier")**




## 7.3 Envelope Detector




An envelope detector is a circuit that takes a high-frequency amplitude modulated input and produces an output which is the “envelope” of the AM signal. The capacitor in the circuit stores up charge on the rising edge, and releases it slowly through the resistor when the signal falls. The diode in series rectifies the incoming signal, allowing current flow only when the positive input terminal is at a higher potential than the negative input terminal.




Most practical envelope detectors use either half-wave or full-wave rectification of the signal to convert the AM input into a pulsed DC signal where the peaks of the DC pulses represent the modulating signal. Low pass filtering is then used to smooth the final result, leaving the low frequency modulating signal component. This filtering is rarely perfect and some “ripple” is likely to remain on the envelope detector output, particularly for low frequency inputs such as notes from a bass guitar. More filtering gives a smoother result, but decreases the high frequency response to the original modulating signal. Real world designs must be optimized for the given application.




[![](/_media/university/courses/electronics/text/chptr7-f8.png?w=600&tok=feacf3)](/_detail/university/courses/electronics/text/chptr7-f8.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-7 "university:courses:electronics:text:chptr7-f8.png")





 Figure 7.3.1 Envelope detector 





[![](/_media/university/courses/electronics/text/chptr7-f9.png?w=600&tok=50a7a6)](/_detail/university/courses/electronics/text/chptr7-f9.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-7 "university:courses:electronics:text:chptr7-f9.png")





 Figure 7.3.2 Envelope detector input and output waveforms 





The simple diode envelope detector has several drawbacks:




1) The input to the detector must be band-pass filtered around the desired carrier signal, or else the detector will simultaneously demodulate several signals. The filtering can be done with a tunable filter or, more practically, a superheterodyne receiver  


2) It is more susceptible to noise than a product detector  


3) If the signal is overmodulated, distortion will occur




Most of these drawbacks are relatively minor and are usually acceptable tradeoffs for the simplicity and low cost of using an envelope detector.




**ADALM1000 Lab Activity, [AM Modulation and the Envelope Detector](/university/courses/alm1k/circuits1/alm-cir-envelope-detector "university:courses:alm1k:circuits1:alm-cir-envelope-detector")**  

**ADALM2000 Lab Activity, [Envelope Detector](/university/courses/electronics/electronics-lab-envelope-detector "university:courses:electronics:electronics-lab-envelope-detector")**




## 7.4 Diode Clamp




When a signal drives an open-ended AC coupling capacitor the average voltage level on the output terminal of the capacitor is determined by some initial charge on that terminal of the capacitor and therefore will be unpredictable. It is then necessary to provide a DC path from the output terminal of the capacitor to ground or some other reference voltage via a large resistor. This DC path drains any excess charge and results in an average or DC output voltage of zero. This is useful if we want to force the average value of the AC signal to be referenced to a known value, however, what if we want to force the positive or negative peak of the AC signal to the know value? The so called clamp circuit can be used to “clamp” the peak value to a known reference level.




A clamp is an electronic circuit that prevents a signal from going above or below a certain defined DC value or clamping level. The clamp does not alter the peak-to-peak magnitude of the signal, it shifts it up or down by a fixed value. A diode clamp (a simple, common type) relies on the property of a diode to conduct in only one direction, along with resistors and capacitors to maintain the altered dc level at the clamp output.




The clamp circuit will fix either the upper or lower peak of a signal waveform to a fixed DC voltage level. This circuit is also sometimes referred to as a DC voltage restorer for obvious reasons. When unbiased, clamp circuit will fix the output voltage lower limit (or upper limit, in the case of negative clampers) to 0 Volts. By including a fixed bias voltage in series with the diode the circuit will clamp the peak of a waveform to a specific DC level.




[![](/_media/university/courses/electronics/text/chptr7-f10.png?w=600&tok=b77006)](/_detail/university/courses/electronics/text/chptr7-f10.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-7 "university:courses:electronics:text:chptr7-f10.png")





 Figure 7.4.1 DC Clamp Input and Output Waveforms 





The schematic of a diode clamp as shown in figure 7.4.2 reveals that it is a relatively simple device. The two components creating the clamping effect are a capacitor, followed by a diode in parallel with the output. The clamp circuit relies on a change in the capacitor's time constant; this is the result of the diode changing current path, either conducting or non-conducting, with the changing input voltage. The value of C1 and the magnitude of any external load R are chosen so that Τ = RC is large enough to ensure that the voltage across the capacitor does not discharge significantly during the diode's non-conducting interval. During the first negative phase of the AC input voltage, the capacitor in the positive clamper charges rapidly. As VIN becomes positive, the capacitor serves as a voltage doubler; since it has stored the equivalent of the peak value of VIN during the negative cycle, it provides nearly that voltage during the positive cycle; this essentially doubles the voltage seen at the output VOUT. As VIN becomes negative, the capacitor acts as a battery of the same voltage of VIN. The input voltage and the capacitor counteract each other, resulting in a net voltage of zero as seen at the output VOUT.




[![](/_media/university/courses/electronics/text/chptr7-f11.png?w=600&tok=2f2d6f)](/_detail/university/courses/electronics/text/chptr7-f11.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-7 "university:courses:electronics:text:chptr7-f11.png")





 Figure 7.4.2 Diode DC restoring circuit 





A simple method of establishing a DC reference for the output voltage is by using a diode clamp as shown in figure 7.4.2. By conducting whenever the voltage at the output terminal of the capacitor goes negative, this circuit builds up an average charge on the terminal that is sufficient to prevent the output from ever going more negative than the forward voltage of the diode. Positive charge on this terminal is effectively trapped.




### Op-amp clamp circuit




The schematic in figure 7.4.3 includes an op-amp clamp circuit with a non-zero reference clamping voltage. The very large op amp open loop gain provides the advantage that the clamping level is at very nearly the reference voltage. There is no need to take into account the forward volt drop of the diode (which is necessary in the previous simple circuits as this adds to the reference voltage). The effect of the diode volt drop on the circuit output will be reduced by the open loop gain of the amplifier, resulting in an insignificant error.




[![](/_media/university/courses/electronics/text/chptr7-f12.png?w=600&tok=f98fd9)](/_detail/university/courses/electronics/text/chptr7-f12.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-7 "university:courses:electronics:text:chptr7-f12.png")





 Figure 7.4.3 Precision op-amp clamp circuit 





## 7.5 Diode Clippers / Limiters




A diode clipping circuit can be used to limit the voltage swing of a signal. The input vs. output transfer function of an ideal clipping circuit is shown in figure 7.5.1. VOUT is equal to VIN as long as VIN is less than VL+ and greater than VL-. When VIN is outside these limiting voltages VOUT is clipped or limited to VL+ or VL-.




[![](/_media/university/courses/electronics/text/chptr7-f13.png?w=600&tok=fff33d)](/_detail/university/courses/electronics/text/chptr7-f13.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-7 "university:courses:electronics:text:chptr7-f13.png")





 Figure 7.5.1 Voltage clipping characteristic 





[![](/_media/university/courses/electronics/text/chptr7-f14.png?w=600&tok=0d7724)](/_detail/university/courses/electronics/text/chptr7-f14.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-7 "university:courses:electronics:text:chptr7-f14.png")





 Figure 7.5.2 Clipper waveforms 





Figure 7.5.3 shows a diode circuit that clips both the positive and negative voltage swings to references voltages. The basic components required for a clipping circuit are, an ideal diode and a resistor. To fix the clipping level to the desired level other than ground, a dc source must also be included in series with the diode as shown in the figure. When the diode is forward biased, it acts as a closed switch shorting VOUT to VL+ or VL-, and when the diode is reverse biased, it acts as an open switch. Different levels of clipping can be obtained by varying the voltage of the DC source and also interchanging the positions of the diode and resistor.




Depending on the features of the diode, the positive or negative region of the input signal is “clipped” off and accordingly the diode clippers may be positive or negative clippers.




[![](/_media/university/courses/electronics/text/chptr7-f15.png?w=600&tok=81b898)](/_detail/university/courses/electronics/text/chptr7-f15.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-7 "university:courses:electronics:text:chptr7-f15.png")





 Figure 7.5.3 Parallel or shunt clipper circuit 





There are two general forms of clippers: series and parallel (or shunt). The shunt clipper has the diode in a branch parallel to the load while the series configuration, figure 7.5.4, is defined as one where the diode is in series with the load.




[![](/_media/university/courses/electronics/text/chptr7-f16.png?w=600&tok=0b0442)](/_detail/university/courses/electronics/text/chptr7-f16.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-7 "university:courses:electronics:text:chptr7-f16.png")





 Figure 7.5.4 Series clipper circuit 





**Drawbacks of Shunt and Series Diode Clippers**
In shunt clippers, when the diode is in the non-conducting state, transfer of input signal should take place to output without any attenuation or loss. But in the case of high frequency, RF, input signals, the diode capacitance affects the circuit operation adversely and the signal gets attenuated (that is, it passes through diode capacitance to ground).




In series clippers, when the diode is in non-conducting state, there will be no transmission of input signal to output. But in case of high frequency RF signals leakage occurs through the diode capacitance which is undesirable. This is the drawback of using diode as a series element in such clippers.




## 7.6 Voltage controlled variable attenuator




Electronically controllable variable RF attenuators are common in the design of RF signal chains. For example, it is often desirable to be able to control the amplitude of a radio frequency signal using a control voltage. These variable RF attenuators can even be used in programmable RF attenuators. Here the controlling voltage is generated by a digital to analog converter which is programed from a micro-controller or digital signal processor (DSP).




By changing the bias current through a PN diode, it's possible to change the RF resistance. At high frequencies, the diode appears as a resistor whose resistance is an inverse function of its forward current. In addition a diode can be used in some variable attenuator designs as amplitude modulators or output leveling (automatic gain control) circuits. An example attenuator circuit configuration is shown in figure 7.6.1.




[![](/_media/university/courses/electronics/text/chptr7-f17.png?w=650&tok=dcfe99)](/_detail/university/courses/electronics/text/chptr7-f17.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-7 "university:courses:electronics:text:chptr7-f17.png")





 Figure 7.6.1 Voltage controlled variable attenuator 





The purpose of C1 (and C2) is to block DC current from the input and output circuits so the operating point of the diode is not affected. The purpose of inductor L1 is to block the AC signal from flowing in R2. The attenuator uses the fact that that “small signal” resistance of the diode rD is a function the DC current flowing in the diode ID. See Equations below:




[![](/_media/university/courses/electronics/text/chptr7-e3.png?w=300&tok=fefdaf)](/_detail/university/courses/electronics/text/chptr7-e3.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-7 "university:courses:electronics:text:chptr7-e3.png")




Where:  


n is the diode area (size) scale factor  

VT is the Thermal Voltage  


ID is the diode current  

k is Boltzmann's constant  


q is the electron charge  


T is the absolute temperature




In the circuit a voltage divider is set up between R1 and the resistance of D1. The current in D1is varied by changing the current in R2. When the current in D1 is small rDis large and the fraction of the input signal seen at the output is large. As the current in D1 increases, its resistance decreases and the fraction of the input seen at the output decreases.




## 7.7 Logarithmic output amplifiers




[![](/_media/university/courses/electronics/text/chptr7-f18.png?w=500&tok=8e5ab1)](/_detail/university/courses/electronics/text/chptr7-f18.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-7 "university:courses:electronics:text:chptr7-f18.png")





 Figure 7.7.1 Logarithmic amplifier 





The relationship between the input voltage Vin and the output voltage Vout is given by:




[![](/_media/university/courses/electronics/text/chptr7-e5.png?w=300&tok=8391fc)](/_detail/university/courses/electronics/text/chptr7-e5.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-7 "university:courses:electronics:text:chptr7-e5.png")




where IS is the saturation current and VT is the thermal voltage.




If the operational amplifier is considered ideal, the negative pin is at a virtual ground, so the current flowing into the resistor from the input (and thus through the diode to the output, since no current flows into the op-amp inputs) is:




[![](/_media/university/courses/electronics/text/chptr7-e6.png?w=250&tok=c034b5)](/_detail/university/courses/electronics/text/chptr7-e6.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-7 "university:courses:electronics:text:chptr7-e6.png")




where ID is the current through the diode. 




As we know from chapter 5, the relationship between the current and the voltage for a diode is:




[![](/_media/university/courses/electronics/text/chptr7-e7.png?w=300&tok=4aa592)](/_detail/university/courses/electronics/text/chptr7-e7.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-7 "university:courses:electronics:text:chptr7-e7.png")




This equation, when the voltage VD is greater than zero, can be approximated by:




[![](/_media/university/courses/electronics/text/chptr7-e8.png?w=300&tok=66d967)](/_detail/university/courses/electronics/text/chptr7-e8.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-7 "university:courses:electronics:text:chptr7-e8.png")




Putting these two formulae together and considering that the output voltage is the negative of the voltage across the diode (Vout = -VD), the logarithmic relationship of the output to the input is true.




Note that this implementation does not consider the temperature drift of the diode voltage due to the thermal voltage VT and other non-ideal effects.




To illustrate the input voltage to output voltage characteristics of the diode log amplifier the circuit of figure 7.7.1 was simulated with R set to 1 kΩ and a 1N4148 diode. The results are plotted in figure 7.7.2. The bottom green curve is a linear sweep of VIN from 0 to 5V. With a 1 kΩ resistor the current through the diode is thus swept from 0 to 5 mA. The top blue curve shows the characteristic logarithmic shape we are expecting.




[![](/_media/university/courses/electronics/text/chptr7-f19.png?w=600&tok=c2a854)](/_detail/university/courses/electronics/text/chptr7-f19.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-7 "university:courses:electronics:text:chptr7-f19.png")





 Figure 7.7.2 Log Amp simulation 





## 7.8 Exponential (antilog) output amplifiers




[![](/_media/university/courses/electronics/text/chptr7-f20.png?w=500&tok=ef17af)](/_detail/university/courses/electronics/text/chptr7-f20.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-7 "university:courses:electronics:text:chptr7-f20.png")





 Figure 7.8.1 Anti-Logarithmic amplifier 





The relationship between the input voltage Vin and the output voltage Voutis given by:




[![](/_media/university/courses/electronics/text/chptr7-e9.png?w=300&tok=eeee82)](/_detail/university/courses/electronics/text/chptr7-e9.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-7 "university:courses:electronics:text:chptr7-e9.png")




where IS is the saturation current and VT is the thermal voltage.




If we again consider the operational amplifier as ideal, then the negative pin is at a virtual ground, so the current through the diode is given by:




[![](/_media/university/courses/electronics/text/chptr7-e10.png?w=300&tok=a8618d)](/_detail/university/courses/electronics/text/chptr7-e10.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-7 "university:courses:electronics:text:chptr7-e10.png")




when the diode voltage VD is greater than zero, it can be approximated by:




[![](/_media/university/courses/electronics/text/chptr7-e11.png?w=300&tok=4af515)](/_detail/university/courses/electronics/text/chptr7-e11.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-7 "university:courses:electronics:text:chptr7-e11.png")




The output voltage is given by:




[![](/_media/university/courses/electronics/text/chptr7-e12.png?w=400&tok=bd2716)](/_detail/university/courses/electronics/text/chptr7-e12.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-7 "university:courses:electronics:text:chptr7-e12.png")




To illustrate the input voltage to output voltage characteristics of the diode anti-logarithmic amplifier the circuit of figure 7.8.1 was simulated with R set to 1 kΩ and a 1N4148 diode. The results are plotted in figure 7.8.2. The bottom green curve is a linear sweep of VIN from 0 to 660 mV. By using the same diode as we did in section 7.7 on log amps we know that 660 mV will result in a 1 mA current through the diode and with the same 1 kΩ resistor output voltage will be 5V. The top blue curve shows the characteristic exponential shape we are expecting.




[![](/_media/university/courses/electronics/text/chptr7-f21.png?w=600&tok=f4f514)](/_detail/university/courses/electronics/text/chptr7-f21.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-7 "university:courses:electronics:text:chptr7-f21.png")





 Figure 7.8.2 Anti-Logarithmic amp simulation 





**Return to [Previous Chapter](/university/courses/electronics/text/chapter-6 "university:courses:electronics:text:chapter-6")**




**Go to [Next Chapter](/university/courses/electronics/text/chapter-8 "university:courses:electronics:text:chapter-8")**




**Return to [Table of Contents](/university/courses/electronics/text/electronics-toc "university:courses:electronics:text:electronics-toc")**






university/courses/electronics/text/chapter-7.txt · Last modified: 18 Mar 2018 16:52 by [Doug Mercer](https://ez.analog.com/members/dmercer)

