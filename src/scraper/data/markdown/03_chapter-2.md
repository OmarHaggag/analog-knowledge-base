



This version (06 Jun 2017 14:45) was *approved* by [Doug Mercer](https://ez.analog.com/members/dmercer).The [Previously approved version](/university/courses/electronics/text/chapter-2?rev=1407324239) (06 Aug 2014 11:23) is available.[![Diff](/lib/images/diff.png)](https://wiki.analog.com/university/courses/electronics/text/chapter-2?do=diff&rev2[0]=1407324239&rev2[1]=1496760292&difftype=sidebyside)

### Table of Contents



* [Chapter 2: Introduction and Chapter Objectives](#chapter_2introduction_and_chapter_objectives)
	+ [2.1 The Ideal Voltage Feedback Op Amp](#the_ideal_voltage_feedback_op_amp)
	+ [2.2 Ideal Voltage Feedback (VFB) Model](#ideal_voltage_feedback_vfb_model)
	+ [2.3 Basic Operation](#basic_operation)
	+ [2.4 Inverting and Non-inverting Configurations](#inverting_and_non-inverting_configurations)
	+ [2.5 Inverting Op Amp Gain Derivation](#inverting_op_amp_gain_derivation)
	+ [2.6 Non-inverting Op Amp Gain Derivation](#non-inverting_op_amp_gain_derivation)
	+ [2.7 Inverting Summing Op Amp Stage](#inverting_summing_op_amp_stage)
	+ [2.8 The Differential Op Amp Stage](#the_differential_op_amp_stage)
	+ [2.9 The Instrumentation Amplifier](#the_instrumentation_amplifier)
		- [Section Summary](#section_summary)
	+ [2.10 Integration and differentiation](#integration_and_differentiation)
		- [2.10.1 The Ideal Inverting Integrator](#the_ideal_inverting_integrator)
		- [2.10.2 The Ideal Differentiator](#the_ideal_differentiator)





# Chapter 2: Introduction and Chapter Objectives




## 2.1 The Ideal Voltage Feedback Op Amp




The operational amplifier (op amp) is one of the basic building blocks of linear design. In its basic form it consists of two input terminals, one of which inverts the phase of the signal, the other preserves the phase, and an output terminal. The standard symbol for the op amp is shown in figure 2.1. This ignores the two power supply terminals, which are obviously required for operation. Op amps are often divided into two types, those that use both a positive and negative power supply and those that use only a single, usually positive power supply. Since all op amps have only two supply pins this distinction is often unnecessary.




[![](/_media/university/courses/electronics/text/chptr2-f1.png?w=400&tok=c622ea)](/_detail/university/courses/electronics/text/chptr2-f1.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-2 "university:courses:electronics:text:chptr2-f1.png")





 Figure 2.1: Standard Op Amp Symbol 





The name “op amp” is the standard abbreviation for operational amplifier. This name comes from the early days of amplifier design, when the op amp was used in analog computers. (Yes, the first computers were analog in nature, rather than digital). When the basic amplifier was used with a few added external components, various mathematical “operations” could be performed, such as addition, subtraction, integration, etc. One of the primary uses of analog computers was during World War II, when they were used for plotting ballistic trajectories.




**After completing this chapter you should be able to:**



* List the properties of the ideal voltage feedback op amp
* Draw the Inverting and Non-Inverting configurations
* Derive the gain equations for the Inverting and Non-Inverting configurations
* Draw the inverting summing amplifier configuration
* Draw the op amp differential gain configuration
* Derive the gain equations for the Instrumentation Amplifier configuration



## 2.2 Ideal Voltage Feedback (VFB) Model




The most basic model of the ideal voltage feedback op amp has the following characteristics:



1. Infinite input impedance
2. Infinite bandwidth
3. Infinite voltage gain
4. Zero output impedance
5. Zero power consumption



None of these can be actually realized, of course. How close a real implementation comes to these ideals determines the quality of the op amp. Since not all of these ideal characteristics can be maximized at the same time many real op amp designs trade one or more characteristics for the others. 
This is referred to as the voltage feedback model. This type of op amp comprises nearly all op amps below 10 MHz bandwidth and on the order of 90% of those with higher bandwidths. Another type of op amp architecture is Current Feedback and is discussed in a separate chapter. 




The attributes of an ideal VFB op amp are summarized in figure 2.2. 




[![](/_media/university/courses/electronics/text/chptr2-f2.png?w=550&tok=596650)](/_detail/university/courses/electronics/text/chptr2-f2.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-2 "university:courses:electronics:text:chptr2-f2.png")





 Figure 2.2: The Attributes of an Ideal Voltage Feedback Op Amp 





## 2.3 Basic Operation




The basic operation of the ideal op amp can be easily summarized. First, we assume that there is a portion of the output that is fed back to the inverting terminal to establish the fixed gain for the amplifier. This is negative feedback. Any differential voltage across the input terminals of the op amp is multiplied by the amplifier's open loop gain which is infinite for the ideal op amp. If the magnitude of this differential voltage is more positive on the inverting (-) terminal than on the non-inverting (+) terminal, the output will swing toward the negative supply. If the magnitude of the differential voltage is more positive on the non-inverting (+) terminal than on the inverting (-) terminal, the output voltage will swing toward the positive supply. The infinite open loop gain of the amplifier along with the external negative feedback will attempt to force the differential input voltage to zero. As long as the inputs and output stays in the operational range of the amplifier, typically bounded by the positive and negative power supply voltages, it will keep the differential input voltage at zero, and the output will be the input voltage multiplied by the gain determined by the feedback network. Note that the output responds to differential-mode voltage and not the common-mode input voltage. 




## 2.4 Inverting and Non-inverting Configurations




There are two basic ways to configure the ideal voltage feedback op amp as an amplifier. These are shown in figure 2.3 and figure 2.4. 




Figure 2.3 shows what is known as the inverting configuration. With this circuit, the output is 180º out of phase with the input. The signal gain of this circuit is determined by the ratio of the resistors used and is given by:




[![](/_media/university/courses/electronics/text/chptr2-e1.png?w=120&tok=cfb4c8)](/_detail/university/courses/electronics/text/chptr2-e1.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-2 "university:courses:electronics:text:chptr2-e1.png")




[![](/_media/university/courses/electronics/text/chptr2-f3.png?w=500&tok=61ef15)](/_detail/university/courses/electronics/text/chptr2-f3.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-2 "university:courses:electronics:text:chptr2-f3.png")





 Figure 2.3: Inverting Mode Op Amp Stage 





In the figure the inverting (-) input terminal is referred to as the Summing Junction. Since the inputs to the op amp have infinite impedance and thus no current will flow in them, the sum of the current from the input in RG and the current from the output in RF must be zero. If we suppose that a second resistor (RG2) were to be connected from a second input voltage (VIN2) to the summing junction, then the current in RF would be equal to the sum of the two input currents in RGand this new RG2.




The input impedance, as always, is the impedance to ground for an input signal. The *-* input is at the same voltage as the + input which is ground. We can thus consider the - input to be at what is referred to as virtual ground. The input impedance for the overall amplifier will be simply RG:




![Zin = R_G](/lib/plugins/mathpublish/img.php?img=d55cf239661e98ce1d6f735933053d75 "Zin = R_G")




Figure 2.4 shows what is known as the non-inverting configuration. With this circuit the output is in phase with the input. The signal gain of the circuit is also determined by the ratio of the resistors used and is given by: 




[![](/_media/university/courses/electronics/text/chptr2-e2.png?w=120&tok=828278)](/_detail/university/courses/electronics/text/chptr2-e2.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-2 "university:courses:electronics:text:chptr2-e2.png")




[![](/_media/university/courses/electronics/text/chptr2-f4.png?w=500&tok=8e1883)](/_detail/university/courses/electronics/text/chptr2-f4.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-2 "university:courses:electronics:text:chptr2-f4.png")





 Figure 2.4: Non-Inverting Mode Op Amp Stage 





Note that since the output drives a voltage divider (the gain-setting network) the maximum voltage available at the inverting terminal is the full output voltage, when the circuit is configured for a minimum gain of 1 (RG = ∞).




The input impedance, as always, is the impedance to ground for an input signal. Since no current can flow into or out of the *+* input, the input impedance is infinite:




![Zin = infty](/lib/plugins/mathpublish/img.php?img=e4c67edbe6f6243998b6fc7be17add8a "Zin = infty")




Also note that in both inverting and non-inverting configurations the feedback is from the output to the inverting terminal. This is negative feedback and has many advantages for the designer. These will be discussed more in detail. 




It should also be noted that the gain is based on the ratio of the resistors, not their actual values. This means that the designer can choose from a wide range of values, within certain practical limits. 




However, if the values of the resistors are too low, a great deal of current is required from the op amp output for proper operation. This causes excessive power dissipation in the op amp itself, which has many disadvantages. The increased dissipation leads to self-heating of the integrated circuit, which can cause a change in the dc characteristics of the op amp itself. Also, the heat generated can eventually cause the junction temperature to rise above 150º C, the commonly accepted maximum limit for most semiconductors. The junction temperature is the temperature at the silicon chip itself. On the other end of the spectrum, if the resistor values are too high, there is an increase in noise and the susceptibility to parasitic capacitances, which can limit bandwidth and possibly cause instability and oscillation. 




From a practical sense, resistors below 10 Ω and above 1 MegΩ are more difficult to produce, especially if precision resistors are required. 




## 2.5 Inverting Op Amp Gain Derivation




Let us look at the case of an inverting amp in a little more detail. Referring to figure 2.5, the non-inverting terminal is connected to ground. We are assuming a bipolar (both positive and negative) power supply. Since the op amp will force the differential voltage across the inputs to zero, the inverting input will also appear to be at ground. In fact, this node is often referred to as a virtual ground.




[![](/_media/university/courses/electronics/text/chptr2-f5.png?w=500&tok=0ba94e)](/_detail/university/courses/electronics/text/chptr2-f5.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-2 "university:courses:electronics:text:chptr2-f5.png")





 Figure 2.5: Inverting Amplifier Gain 





If there is a voltage VIN applied to the input resistor, It will set up a current I1 through the resistor RG so that:




[![](/_media/university/courses/electronics/text/chptr2-e3.png?w=120&tok=8cd768)](/_detail/university/courses/electronics/text/chptr2-e3.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-2 "university:courses:electronics:text:chptr2-e3.png")




Since the input impedance of the ideal op amp is infinite, no current will flow into the inverting input. Therefore, this same current I1 must flow through the feedback resistor RF (I2 = I1). Since infinite open loop gain of the amplifier will force the difference between the inverting terminal and the non-inverting terminal to zero, the output will assume a voltage VOUT such that: 




[![](/_media/university/courses/electronics/text/chptr2-e4.png?w=120&tok=a41808)](/_detail/university/courses/electronics/text/chptr2-e4.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-2 "university:courses:electronics:text:chptr2-e4.png")




Doing some simple arithmetic we then can come to the conclusion that: 




[![](/_media/university/courses/electronics/text/chptr2-e5.png?w=140&tok=dda4d4)](/_detail/university/courses/electronics/text/chptr2-e5.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-2 "university:courses:electronics:text:chptr2-e5.png")




## 2.6 Non-inverting Op Amp Gain Derivation




[![](/_media/university/courses/electronics/text/chptr2-f6.png?w=500&tok=1aa128)](/_detail/university/courses/electronics/text/chptr2-f6.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-2 "university:courses:electronics:text:chptr2-f6.png")





 Figure 2.6: Non-Inverting Amplifier gain 





Now we examine the non-inverting case in more detail. Referring to figure 2.6, the input voltage is applied to the non-inverting terminal. The output voltage drives a voltage divider consisting of RF and RG. The voltage at the inverting terminal VA, which is at the junction of the two resistors, is equal to: 




[![](/_media/university/courses/electronics/text/chptr2-e6.png?w=140&tok=e038f0)](/_detail/university/courses/electronics/text/chptr2-e6.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-2 "university:courses:electronics:text:chptr2-e6.png")




The negative feedback action of the op amp will force the differential voltage to 0, so:




[![](/_media/university/courses/electronics/text/chptr2-e7.png?w=100&tok=11c11b)](/_detail/university/courses/electronics/text/chptr2-e7.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-2 "university:courses:electronics:text:chptr2-e7.png")




Applying a little simple arithmetic we obtain: 




[![](/_media/university/courses/electronics/text/chptr2-e8.png?w=200&tok=d08487)](/_detail/university/courses/electronics/text/chptr2-e8.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-2 "university:courses:electronics:text:chptr2-e8.png")




which is what we specified in figure 2.3




In all of the discussions above, we referred to the gain setting components as resistors. In fact, they are impedances, not just resistances. This allows us to build frequency dependent amplifiers and will be covered in more detail in later chapters. 




## 2.7 Inverting Summing Op Amp Stage




Multiple input voltages can be summed by the addition of multiple input resistors to the simple inverting op amp configuration as shown in figure 2.7.




[![](/_media/university/courses/electronics/text/chptr2-f7.png?w=500&tok=df201d)](/_detail/university/courses/electronics/text/chptr2-f7.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-2 "university:courses:electronics:text:chptr2-f7.png")





 Figure 2.7: Summing Amplifier 





[![](/_media/university/courses/electronics/text/chptr2-e9.png?w=220&tok=1f51fc)](/_detail/university/courses/electronics/text/chptr2-e9.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-2 "university:courses:electronics:text:chptr2-e9.png")




If all the input resistors R1, R2, … Rn are equal but not equal to Rf then from the equation we can see that it can be simplified such that the output will be equal to the algebraic sum of the inputs times a common gain factor of -Rf/R1. If all the resistors are made equal including Rf then the output will be simply the negative sum of the inputs.




**ADALM1000 Lab Activity 1. [Simple Op Amps](/university/courses/alm1k/alm-lab-1 "university:courses:alm1k:alm-lab-1")**  

**ADALM2000 Lab Activity 1. [Simple Op Amps](/university/courses/electronics/electronics-lab-1 "university:courses:electronics:electronics-lab-1")**  

**ADALM1000 Lab Activity [Summing Amplifier](/university/courses/alm1k/alm-lab-vectrosumamp "university:courses:alm1k:alm-lab-vectrosumamp")**




## 2.8 The Differential Op Amp Stage




The op amp differential gain stage (also known as a differential amplifier, or subtractor) is shown in figure 2.7.




[![](/_media/university/courses/electronics/text/chptr2-f8.png?w=500&tok=55f688)](/_detail/university/courses/electronics/text/chptr2-f8.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-2 "university:courses:electronics:text:chptr2-f8.png")





 Figure 2.8: The differential amplifier stage (subtractor) 





Paired input and feedback network resistances set the gain of this stage. These resistors, RF-RG and RF'-RG', must be matched as noted, for proper operation. Calculation of individual gains for inputs V1 and V2 and their linear combination derives the stage gain.




Note that the stage is intended to amplify the difference of voltages V1and V2, so the net input is VIN = V1 - V2 . The general gain expression is then:




[![](/_media/university/courses/electronics/text/chptr2-e10.png?w=150&tok=ab83f6)](/_detail/university/courses/electronics/text/chptr2-e10.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-2 "university:courses:electronics:text:chptr2-e10.png")




For an ideal op amp and the resistor ratios matched as noted, the gain of this differential stage from VIN to VOUT is:




[![](/_media/university/courses/electronics/text/chptr2-e11.png?w=100&tok=f551d4)](/_detail/university/courses/electronics/text/chptr2-e11.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-2 "university:courses:electronics:text:chptr2-e11.png")




The great fundamental utility that an op amp stage such as this allows is the property of rejecting voltages common to V1 -V2, i.e., common-mode (CM) voltages. For example, if noise voltages appear between grounds G1 and G2, the noise will be suppressed by the common-mode rejection (CMR) of the differential amp. The CMR is however only as good as the matching of the resistor ratios allows, so in practical terms it implies precisely trimmed resistor ratios are necessary.




A disadvantage of this stage is that the resistor networks load the V1-V2 sources, potentially leading to additional errors if the driving impedance is not low compared to RG. A solution to this problem is to insert unity gain (non-inverting) follower stages before the input resistors as shown in figure 2.8.1




[![](/_media/university/courses/electronics/text/chptr2-f9.png?w=550&tok=2eb266)](/_detail/university/courses/electronics/text/chptr2-f9.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-2 "university:courses:electronics:text:chptr2-f9.png")





 Figure 2.8.1: Buffered differential amplifier stage 





**ADALM1000 Lab Activity [Difference Amplifier](/university/courses/alm1k/alm-lab-diffamp "university:courses:alm1k:alm-lab-diffamp")**  

**ADALM1000 Lab Activity [Current Sensing Difference Amplifier](/university/courses/alm1k/alm-lab-current-sense "university:courses:alm1k:alm-lab-current-sense")**




## 2.9 The Instrumentation Amplifier




Instrumentation Amplifiers are high gain differential amplifiers with high input impedance and a single ended output. They are mainly used to amplify very small differential signals from certain kinds of transducers or sensors such as strain gauges, thermocouples or current sensing resistors in motor control systems. They also have very good common mode rejection (zero output when V1 = V2) in excess of 100dB at DC. A typical example of an instrumentation amplifier with a high input impedance (Zin) is shown in figure 2.9. As you can see it is very similar to the configuration of figure 2.8.1 but with the two input buffers now serving as non-inverting gain stages.




[![](/_media/university/courses/electronics/text/chptr2-f10.png?w=550&tok=5bd5d2)](/_detail/university/courses/electronics/text/chptr2-f10.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-2 "university:courses:electronics:text:chptr2-f10.png")





 Figure 2.9 High Input impedance Instrumentation Amplifier 





The negative feedback of the top op amp causes the voltage at the negative input of amplifier A1 to be equal to the input voltage V1. Likewise, the voltage at the negative input of A2 is equal to the value of V2. This produces a voltage drop across R1 which is equal to the voltage difference between V1 and V2. This voltage drop causes a current to flow through R1, and as the two inputs of the buffer op-amps draw no current, the same amount of current flowing through R1 must also be flowing through the two resistors R2. This then produces a voltage drop between points Va and Vbequal to:




[![](/_media/university/courses/electronics/text/chptr2-e12.png?w=200&tok=0e6cce)](/_detail/university/courses/electronics/text/chptr2-e12.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-2 "university:courses:electronics:text:chptr2-e12.png")




This voltage drop between points Va and Vb is connected to the inputs of the differential amplifier which amplifies it by a gain of 1 (assuming that all the “R” resistors are of equal value). Then we have a general expression for overall voltage gain of the instrumentation amplifier circuit as:




[![](/_media/university/courses/electronics/text/chptr2-e13.png?w=280&tok=e127c1)](/_detail/university/courses/electronics/text/chptr2-e13.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-2 "university:courses:electronics:text:chptr2-e13.png")




To change the differential gain of the circuit we simply change the value of R1.
An instrumentation amplifier can also be made from two op amps; this is shown in figure 2.10.




**<fs large>R1 = R4 (matched)  


R2 = R3 (matched)  


Gain = 1 + R1/R2</fs>**




This assumes Vin- and Vin+ are referenced to Vcc/2 in the case of single supply op amps.




[![](/_media/university/courses/electronics/text/chptr2-f11.png?w=550&tok=2d8ed4)](/_detail/university/courses/electronics/text/chptr2-f11.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-2 "university:courses:electronics:text:chptr2-f11.png")





 Figure 2.10: Instrumentation amplifier using two Op Amps 





However, this topology is not as desirable because the first op amp is operated at less than unity gain, so it may be unstable. In addition, the signal path from Vin- to the output has a longer propagation delay than the signal path from Vin+ to the output. This can lead to less than the exact difference for the highest output frequencies at the bandwidth limits of the amplifiers.




### Section Summary




The basic model of the ideal voltage feedback op amp has the following characteristics:



1. Infinite input impedance
2. Infinite bandwidth
3. Infinite voltage gain
4. Zero output impedance
5. Zero power consumption



The gain equation for the inverting configuration is given by:




[![](/_media/university/courses/electronics/text/chptr2-e5.png?w=150&tok=3d4258)](/_detail/university/courses/electronics/text/chptr2-e5.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-2 "university:courses:electronics:text:chptr2-e5.png")




The gain equation for the non-inverting configuration is given by:




[![](/_media/university/courses/electronics/text/chptr2-e8.png?w=250&tok=832682)](/_detail/university/courses/electronics/text/chptr2-e8.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-2 "university:courses:electronics:text:chptr2-e8.png")




The gain equation for the three op amp instrumentation amplifier configuration is given by:




[![](/_media/university/courses/electronics/text/chptr2-e13.png?w=250&tok=3ae7b5)](/_detail/university/courses/electronics/text/chptr2-e13.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-2 "university:courses:electronics:text:chptr2-e13.png")




## 2.10 Integration and differentiation




By introducing a reactance into the feedback loop of an op-amp amplifier circuit rather than a pure resistance, we can make an output that responds to changes in the input voltage over time. The two circuits we will be exploring derive their names from their respective calculus functions, the integrator produces a voltage output proportional to the product (multiplication) of the input voltage and time; and the differentiator (not to be confused with the differential amplifier we just covered) produces a voltage output proportional to the input voltage's rate of change.




### 2.10.1 The Ideal Inverting Integrator




An integrator is a circuit which has an output voltage that is proportional to the time integral of its input voltage. Figure 2.11 shows the configuration of an ideal op amp integrator. The circuit is similar to the inverting amplifier in figure 2.3 with the exception that resistor RF is replaced by a capacitor. The voltage gain transfer function is obtained from the equation we derived in section 2.5 by replacing RF with the complex impedance of the capacitor C to obtain:




[![](/_media/university/courses/electronics/text/chptr2-e17.png?w=300&tok=43ae57)](/_detail/university/courses/electronics/text/chptr2-e17.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-2 "university:courses:electronics:text:chptr2-e17.png")




Remembering that division by s in the complex frequency domain is equivalent to an integration in the time domain, it follows from this equation that the time domain output voltage is given by:




[![](/_media/university/courses/electronics/text/chptr2-e18.png?w=300&tok=1e3fd5)](/_detail/university/courses/electronics/text/chptr2-e18.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-2 "university:courses:electronics:text:chptr2-e18.png")




[![](/_media/university/courses/electronics/text/chptr2-f12.png?w=500&tok=f5d028)](/_detail/university/courses/electronics/text/chptr2-f12.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-2 "university:courses:electronics:text:chptr2-f12.png")





 Figure 2.11 Inverting integrator 





Thus the circuit has the transfer function of an inverting integrator with the gain constant 1/RC. Because RC has the units of seconds, it is called the integrator time constant. The input resistance to the circuit is R. The output resistance is zero.




Note that this configuration can also be viewed as a low-pass filter. It is a filter with a single pole at DC (i.e., where angular frequency ? = 0 radians).




There are several potential problems with this circuit. It is usually assumed that the input Vin has zero DC component (i.e., has a zero average value). Otherwise, unless the capacitor is periodically discharged, the output will drift outside of the operational amplifier's operating range. Even when Vin has no offset, the leakage or bias currents into the operational amplifier inputs can add an unexpected offset voltage to Vin that causes the output to drift off in one or the other direction toward a supply rail. Balancing input currents and replacing the non-inverting (+) short-circuit to ground with a resistor with resistance R can reduce the severity of this problem.




Because this circuit provides no DC feedback (i.e., the capacitor appears like an open circuit to signals with ? = 0), the offset of the output may not agree with expectations (i.e., Vinitial may be out of the designer's control with the present circuit).




Many of these problems can be made less severe by adding a large resistor RF ( greater than 1 megaohm for example) in parallel with the feedback capacitor. At significantly high frequencies, this resistor will have negligible effect. However, at low frequencies where there are drift and offset problems, the resistor provides the necessary DC feedback to hold the output steady at the correct value. In effect, this resistor reduces the DC gain of the “integrator”, it goes from infinite to some finite value RF/R.




To illustrate the operation of this integrator circuit we simulated the circuit with the input resistor R = 2.5 KΩ and the feedback capacitor C = 0.1µF. The input voltage Vin, shown in green in figure 2.12 is a -1 volt to +1 volt square wave with a 1mSec period ( high for 500 µSec and low for 500 µSec). The integrator output voltage Vout is shown in blue in figure 2.12. The simulation starts when the output voltage is zero and thus the voltage across the capacitor, C is also zero (Vinitial = 0). As we can see the output waveform is a triangle wave with a slope determined by the integrator time constant RC and Vin. The RC time constant (250 mSec) was chosen such that given the -1 to +1 volt input Vin the output will ramp up and down 2 volts in each of the 500 mSec half cycles of the input square wave.




[![](/_media/university/courses/electronics/text/chptr2-f13.png?w=500&tok=14e814)](/_detail/university/courses/electronics/text/chptr2-f13.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-2 "university:courses:electronics:text:chptr2-f13.png")





 Figure 2.12 Ideal integrator simulation 





The negative input terminal of the op amp is also plotted (Vsumjnc red waveform) in figure 2.12. It is at 0 volts as it should be. The “constant” +/- 1 volt Vin appears across the input resistor making a “constant” current flow in the feedback capacitor. We get a linearly changing voltage across the capacitor because we know that the time rate of change of the voltage on a capacitor is linearly proportional to the current.




### 2.10.2 The Ideal Differentiator




A differentiator is a circuit which has an output voltage that is proportional to the time derivative of its input voltage. Figure 2.13 shows the configuration of an op amp differentiator. The circuit is similar to the inverting amplifier in figure 2.3 with the exception that resistor RG is replaced by a capacitor. It follows that the gain equation we derived in section 2.5 can be used to solve for the voltage gain transfer function of the differentiator by replacing RG with the complex impedance of the capacitor. The voltage gain transfer function is given by:




[![](/_media/university/courses/electronics/text/chptr2-e14.png?w=300&tok=c83ceb)](/_detail/university/courses/electronics/text/chptr2-e14.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-2 "university:courses:electronics:text:chptr2-e14.png")




Again remembering that multiplication by s in the complex frequency domain is equivalent to a differentiation in the time domain, it follows from the above equation that the time domain output voltage is given by:




[![](/_media/university/courses/electronics/text/chptr2-e15.png?w=230&tok=7ea732)](/_detail/university/courses/electronics/text/chptr2-e15.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-2 "university:courses:electronics:text:chptr2-e15.png")




[![](/_media/university/courses/electronics/text/chptr2-f14.png?w=500&tok=0b9168)](/_detail/university/courses/electronics/text/chptr2-f14.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-2 "university:courses:electronics:text:chptr2-f14.png")





 Figure 2.13 Inverting differentiator 





Thus the circuit has the transfer function of an inverting differentiator with the gain constant RC. Because the gain constant has the units of seconds, it is called the differentiator time constant. The output resistance of the circuit is zero. The input impedance transfer function is that of the capacitor C to virtual ground given by:




[![](/_media/university/courses/electronics/text/chptr2-e16.png?w=150&tok=39b7ff)](/_detail/university/courses/electronics/text/chptr2-e16.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-2 "university:courses:electronics:text:chptr2-e16.png")




With s = jω, it follows that |Zin| --> 0 as ω becomes large. This is a disadvantage because a low input impedance can cause large currents to flow in the input circuit. Often this differentiator is modified by inserting some relatively small resistance in series with the input capacitor.




Note that this configuration can also be viewed as a high-pass filter. It is a filter with a single zero at DC (i.e., where angular frequency ω = 0 radians). The high-pass characteristics of a differentiating amplifier (i.e., the low-frequency zero) can lead to stability challenges when the circuit is used in an analog servo loop (e.g., in a PID controller with a significant derivative gain). In particular, as a root locus analysis would show, increasing feedback gain will drive a closed-loop pole toward marginal stability at the DC zero introduced by the differentiator.




To illustrate the operation of this differentiator circuit we simulated the circuit with the feedback resistor R = 2.5 KΩ and the input capacitor C = 0.1µF. The input voltage Vin, shown in green in figure 2.14 is a -1 volt to +1 volt triangle wave with a 1mSec period ( ramp up for 500 µSec and ramp down for 500 µSec). The differentiator output voltage Vout is shown in blue in figure 2.14. The simulation starts when the input voltage is zero and thus the voltage across the capacitor, C is also zero (Vinitial = 0). As we can see the output waveform is a square wave with an amplitude determined by the differentiator time constant RC and the slope (volts/sec) of Vin. The RC time constant (250 mSec) was chosen such that given the -1 to +1 volt ramp of input Vin the output will be + and - 1volt for each of the 500 mSec half cycles of the input square wave.




[![](/_media/university/courses/electronics/text/chptr2-f15.png?w=500&tok=2ce33c)](/_detail/university/courses/electronics/text/chptr2-f15.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-2 "university:courses:electronics:text:chptr2-f15.png")





 Figure 2.14 Ideal differentiator simulation 





The negative input terminal of the op amp is also plotted (Vsumjnc red waveform) in figure 2.14. It is at 0 volts as it should be. The linear +/- 1 volt ramp from Vin appears across the input capacitor. We know that the time rate of change of the voltage on a capacitor is linearly proportional to the current thus making a “constant” current flow in the feedback resistor and we get a constant voltage on the output.




**Return to [Previous Chapter](/university/courses/electronics/text/chapter-1 "university:courses:electronics:text:chapter-1")**




**Go to [Next Chapter](/university/courses/electronics/text/chapter-3 "university:courses:electronics:text:chapter-3")**




**Return to [Table of Contents](/university/courses/electronics/text/electronics-toc "university:courses:electronics:text:electronics-toc")**






university/courses/electronics/text/chapter-2.txt · Last modified: 06 Jun 2017 14:44 by [Doug Mercer](https://ez.analog.com/members/dmercer)

