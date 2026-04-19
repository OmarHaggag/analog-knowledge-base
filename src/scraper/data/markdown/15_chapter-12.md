



This version (06 Jun 2017 15:50) was *approved* by [Doug Mercer](https://ez.analog.com/members/dmercer).The [Previously approved version](/university/courses/electronics/text/chapter-12?rev=1429047093) (14 Apr 2015 21:31) is available.[![Diff](/lib/images/diff.png)](https://wiki.analog.com/university/courses/electronics/text/chapter-12?do=diff&rev2[0]=1429047093&rev2[1]=1496764199&difftype=sidebyside)

### Table of Contents



* [Chapter 12: Differential amplifiers](#chapter_12differential_amplifiers)
	+ [12.1 Starting with the basics](#starting_with_the_basics)
	+ [12.2 Long-tailed pair](#long-tailed_pair)
	+ [12.3 Differential Gain](#differential_gain)
		- [The current mirror as a load](#the_current_mirror_as_a_load)
	+ [Summary](#summary)





# Chapter 12: Differential amplifiers




The differential amplifier is probably the most widely used circuit building block in analog integrated circuits, principally op amps. We had a brief glimpse at one back in Chapter 3 section 3.4.3 when we were discussing input bias current. The differential amplifier can be implemented with BJTs or MOSFETs. A differential amplifier multiplies the voltage difference between two inputs (Vin+ - Vin-) by some constant factor Ad, the differential gain. It may have either one output or a pair of outputs where the signal of interest is the voltage difference between the two outputs. A differential amplifier also tends to reject the part of the input signals that are common to both inputs (Vin+ + Vin-)/2 . This is referred to as the common mode signal.




## 12.1 Starting with the basics




It is often easiest to start again with the very basic single transistor and build a workable differential amplifier as a logical progression from there. Consider the single transistor amplifier stage, figure 12.1.1, which is similar to what we explored in the section on the degenerated common emitter back in Chapter 9. This amplifier can actually be viewed as either an inverting common emitter amplifier when driven from Vneg and with Vpos considered an AC ground. Or as a non-inverting common base amplifier when driven from Vpos and with Vneg considered an AC ground.




[![](/_media/university/courses/electronics/text/chptr12_f1.png?w=650&tok=59bf2a)](/_detail/university/courses/electronics/text/chptr12_f1.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-12 "university:courses:electronics:text:chptr12_f1.png")





 Figure 12.1.1 AC coupled difference amplifier 





Let's assume that we make the coupling capacitors, C1 and C2, sufficiently large so that we can view them as AC shorts for the signal frequencies of interest. The small signal voltage gain from Vneg to Vout is:




![A_vn = -g_m R_L](/lib/plugins/mathpublish/img.php?img=53f88b0d4bc6c1276f5210caf3f0246d "A_vn = -g_m R_L")




Likewise, the small signal voltage gain from Vpos to Vout is:




![A_vp = g_m R_L](/lib/plugins/mathpublish/img.php?img=762ffcb0bce5631cc0e025a07c081c8d "A_vp = g_m R_L")




The transistor amplifies the small signal voltage across its Vbe which in this case is Vpos-Vneg. If we apply equal amplitude, in phase signals to Vpos and Vneg, such that Vpos-Vneg = 0 then there will be no varying signal across Vbe and the output signal at Vout will be zero. On the other hand, if we apply equal amplitude signals that are 180º out of phase with each other, then Vpos-Vneg = twice the amplitude of the inputs. This difference voltage will appear across Vbe and be amplified by gm\*RL at Vout.




The inverting or negative input terminal of our simple difference amplifier has the relatively high input impedance of the common emitter stage while the non-inverting or positive input terminal of the amplifier has the relatively low input impedance of the common base stage. The importance of this observation and how it can be put to good use will become apparent in the next chapter (13) on transimpedance amplifiers.




It would be advantageous if our differential amplifier had more symmetric inputs where the input impedance for both the positive and negative inputs was as high as possible, ideally infinite. An additional step to get us in that direction is shown in figure 12.1.2. If we now include an emitter follower stage, Q2, to buffer the relatively low impedance of the common base amplifier path of the positive input we get a more symmetrical pair of inputs.




[![](/_media/university/courses/electronics/text/chptr12_f2.png?w=650&tok=0ad181)](/_detail/university/courses/electronics/text/chptr12_f2.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-12 "university:courses:electronics:text:chptr12_f2.png")





 Figure 12.1.2 difference amplifier with emitter follower added. 





Because we are still AC coupling our input signals a second set of biasing resistors, RB3 and RB4 are necessary to provide DC bias for the new emitter follower. If we instead DC couple the now symmetric inputs the biasing resistors become unnecessary and our difference amplifier now takes on the look of the classic differential pair we will discuss in the next section.




## 12.2 Long-tailed pair




[![](/_media/university/courses/electronics/text/chptr12_f3.png?w=650&tok=caca7a)](/_detail/university/courses/electronics/text/chptr12_f3.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-12 "university:courses:electronics:text:chptr12_f3.png")





 Figure 12.2.1: A long-tailed pair with resistor loads 





The classic differential pair amplifier is formed from at least two identical transistors, configured with the emitters for BJT transistors or the sources for FETs connected together. A long-tailed pair (LTP), or emitter coupled (source coupled) pair, is a pair of transistors where the shared emitter or source node is supplied from a more or less constant current source/sink, which could be as simple as a relatively large value resistor connected to the negative supply, such as Rtail in figure 12.2.1, (or the positive supply for p-type devices) that develops a large voltage drop relative to the amplitude of the input signal thus the “long tail”. Given the more or less constant current supplied to the emitters or sources the summation of the two collector or drain currents is also more or less constant with signal.




The two inputs at the bases or gates can be fed with a differential or balanced input signal and the two outputs from the collectors or drains remain balanced, or one input could be grounded to convert a single ended input signal to a differential output.




The higher the resistance of the current source Rtail, the lower the common mode gain or Ac is, and the better the common mode rejection ratio (CMRR). In more sophisticated designs, an active constant current source may be substituted for the high resistance Rtail.
With two inputs and two outputs, this forms a differential amplifier stage. The two bases or gates are inputs which are differentially amplified by the pair.




Even though this circuit is designed to have two inputs and two outputs, it is not necessary to use both inputs and both outputs. (Remember, a differential amplifier was defined as having two possible inputs and two possible outputs.) A differential amplifier can be connected as a single-input, single-output device; a single-input, differential-output device; or a differential-input, differential-output device. The output may be single-ended (taken from just one of the collectors or drains, or differential depending on the needs of the subsequent circuitry.




In a long-tailed pair built using BJTs, the emitters are connected together, and then through the current source to ground or to a negative supply (for an LTP using NPN transistors). In this form, one of the transistors can be thought of as an amplifier operating in common emitter configuration, and the other as an emitter follower, feeding the other input signal into the emitter of the first stage as we discussed in the previous section. Since a transistor will amplify the current flowing between base and emitter, it follows that the current flowing in the collector circuit of the first transistor is proportional to the difference between the two inputs. However since the circuit is totally symmetrical, either element can be viewed as an amplifier or as a follower, understanding how the circuit functions does not depend on which role you assign to which device.




The bias condition assumes equal voltages at Vpos and Vneg, forcing the bias current Itail (set by Rtail) to split equally between the transistors resulting in IC1 = IC2. With RC1 = RC2, equal voltages develop at Vout+ and Vout-.




Using MOSFETs, we can construct an source-coupled differential pair, which is a counterpart of the emitter-coupled differential pair using BJTs. The main advantage of using MOSFETs for a differential pair compared to BJTs is the nearly infinite input impedance, while the disadvantage is generally lower differential gain.




Assuming the two MOSFETs are the same. The analysis of the source-coupled differential pair proceeds in the same way as the emitter-coupled differential pair for both common-mode signal and differential input signal. The transfer characteristics for drain current Id1 and Id2 are shown in the figure.




## 12.3 Differential Gain




We can calculate the differential voltage gain as follows. Consider Q1 and Q2 as current sources controlled by their base voltages. RC1 and RC2 then convert the currents back into voltages. First, the small signal collector current




![i_C = g_m v_BE](/lib/plugins/mathpublish/img.php?img=2bd618af52ca21146f83db991d3846ee "i_C = g_m v_BE")




Where the transconductance gm (Amps/Volts) is set by the DC collector current 




![g_m = I_c / V_T = I_c / 25 mV](/lib/plugins/mathpublish/img.php?img=9598698f69a85261833e9d1dd15bc2e3 "g_m = I_c / V_T = I_c / 25 mV") at room temperature. 




Then, RC converts Ic back to a voltage.




![v_C = R_C * g_m v_BE](/lib/plugins/mathpublish/img.php?img=0968027a7a5f121a937b2f2c7ba4dc9d "v_C = R_C * g_m v_BE")




Bringing the input Vdiff = Vpos - Vneginto the picture, notice it divides equally across the two base-emitter junctions, but with opposite polarities. Putting it all together you get a single-ended output at each collector




![v_C1 = R_C1 * g_m * (+V_diff / 2)](/lib/plugins/mathpublish/img.php?img=b30afc6a9d85c1d0ebda07a3601b6006 "v_C1 = R_C1 * g_m * (+V_diff / 2)")




![v_C2 = R_C2 * g_m * (-V_diff / 2)](/lib/plugins/mathpublish/img.php?img=29eb4b75d53499f6adaa92ca9aea0158 "v_C2 = R_C2 * g_m * (-V_diff / 2)")




Subtracting the two outputs gets you a differential output of




![v_C1 - v_C2 = R_C * g_m * V_diff](/lib/plugins/mathpublish/img.php?img=742369d0f0cbe4ef5f5aff3c626c53c6 "v_C1 - v_C2 = R_C * g_m * V_diff")




An example to set the bias: Rtail sets the bias at Ie = (-0.6V - VDD) / Rtail = (-0.6 V - (-15 V)) / 7.2 kΩ = 2 mA which divides equally between Q1 and Q2 giving




![I_c1 = I_c2 approx I_e / 2 approx 1mA](/lib/plugins/mathpublish/img.php?img=7aac36c25991e72dba2ed62fa807151a "I_c1 = I_c2 approx I_e / 2 approx 1mA")




Finally, we easily calculate gm = 1 mA / 25 mV = 0.04 A/V. The single-ended gain becomes:




![v_C1 / V_diff = R_C1 * g_m * 1/2 = 1 k * 0.04 * 1/2 = 20 V/V](/lib/plugins/mathpublish/img.php?img=058b69bae1372ad4295616c38561c02e "v_C1 / V_diff = R_C1 * g_m * 1/2 = 1 k * 0.04 * 1/2 = 20 V/V")




[![](/_media/university/courses/electronics/text/chptr12_f4.png?w=650&tok=e2114f)](/_detail/university/courses/electronics/text/chptr12_f4.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-12 "university:courses:electronics:text:chptr12_f4.png")




The output from a differential amplifier is itself often differential. If this is not desired, then only one output can be used, disregarding the other output. Or to avoid sacrificing gain, a differential to single-ended stage can be used following the differential stage. This is often implemented with an active current mirror load instead of the collector/drain resistors.




Long-tailed pairs are frequently used in circuits that implement linear amplifiers with feedback, as in operational amplifiers, and in other circuits that require a differential amplifier.




When used as a switch, the “left” base or gate is used as signal input and the “right” base or gate is grounded; output is taken from the right collector or drain. When the input is zero or negative, the output is close to zero; when the input is positive, the output is most-positive, dynamic operation being the same as the amplifier use described above.




Bias stability and independence from variations in device parameters can be improved by negative feedback introduced via emitter or source degeneration resistors.




The differential pair with a small differential input signal vi




[![](/_media/university/courses/electronics/text/chptr12_e1.png?w=150&tok=efbea5)](/_detail/university/courses/electronics/text/chptr12_e1.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-12 "university:courses:electronics:text:chptr12_e1.png")
[![](/_media/university/courses/electronics/text/chptr12_e2.png?w=150&tok=550d21)](/_detail/university/courses/electronics/text/chptr12_e2.png?id=university%3Acourses%3Aelectronics%3Atext%3Achapter-12 "university:courses:electronics:text:chptr12_e2.png")




Small-Signal Operation




![v_d << V_T](/lib/plugins/mathpublish/img.php?img=d19f0fbc4c50eeeccdaee21a12c9a92b "v_d << V_T")




**Some Formulas**




1. Differential Input Resistance




![R_id = 2 ( ß+1 ) ( r_e + R_Tail )](/lib/plugins/mathpublish/img.php?img=e30ea969a6af3f5efa8eea21c611ebd3 "R_id = 2 ( ß+1 ) ( r_e + R_Tail )")




2. Differential Voltage gain




![A_d = -(2 alpha R_c)/(2(r_e+R_E)) approx -R_C/(r_e+R_E)](/lib/plugins/mathpublish/img.php?img=56dcbcc4c4248ee92c46cc121a6a6926 "A_d = -(2 alpha R_c)/(2(r_e+R_E)) approx -R_C/(r_e+R_E)")




3. Common mode gain:




![v_C1 = v_C2 = -v_CM (alpha R_C )/(2R+r_e) approx - v_CM (alpha R_c)/(2R)](/lib/plugins/mathpublish/img.php?img=75ecae2b5b07d89ad81264e5ac1cc82e "v_C1 = v_C2 = -v_CM (alpha R_C )/(2R+r_e) approx - v_CM (alpha R_c)/(2R)")




![A_CM = - (alpha R_c)/(2R)](/lib/plugins/mathpublish/img.php?img=07a1119292a9dbf3b712226f7804e1a5 "A_CM = - (alpha R_c)/(2R)")




**Increasing the linear differential input range of the diff pair**




Sometimes it is advantageous to add emitter degeneration resistor REF to the circuit, as shown in the figure 12.3.1. The resistors have the disadvantage of reducing the differential voltage gain of the circuit. However, two reasons for this is to increase input impedance and to reduce distortion due to the nonlinearity of the BJTs. The right figure shows the transfer characteristic of the differential amplifier (REF=40VT/IEE).




To improve linearity, we introduce emitter-degeneration resistors, which increase the linear range from a few VT to about ITailR.




**ADALM1000 Lab Activity 12, [BJT Differential Amplifier](/university/courses/alm1k/alm-lab-12 "university:courses:alm1k:alm-lab-12")**  

**ADALM1000 Lab Activity 12m, [MOS Differential Amplifier](/university/courses/alm1k/alm-lab-12m "university:courses:alm1k:alm-lab-12m")**




**ADALM2000 Lab Activity 12, [BJT Differential Amplifier](/university/courses/electronics/electronics-lab-12 "university:courses:electronics:electronics-lab-12")**  

**ADALM2000 Lab Activity 12m, [MOS Differential Amplifier](/university/courses/electronics/electronics-lab-12m "university:courses:electronics:electronics-lab-12m")**




### The current mirror as a load




The following figure shows a variation of the emitter-coupled pair in which the collector resistors are replaced by a current mirror. This circuit is particularly favored in integrated circuits, because matched transistors are much easier to construct than precession matched high value resistors. A simple analysis by assuming large ß so that base currents of Q3 and Q4 are neglected, results in the equation as follows:




![i_o = partial I_EE tanh(v_id/(2V_T))](/lib/plugins/mathpublish/img.php?img=4b7aeacb5cbb2ed573982e7eae091a5c "i_o = partial I_EE tanh(v_id/(2V_T))")




For 




![|i_o| < V_T, i_o](/lib/plugins/mathpublish/img.php?img=706a4edb3648738d8ae9e73fee1ec1c7 "|i_o| < V_T, i_o")




is approximately proportional to vid. Notice furthermore that the common-mode input component does not affect the output current.




## Summary




This chapter has presented information on differential amplifiers. The information that follows summarizes the important points of this chapter. 




A difference amplifier is any amplifier with an output signal dependent upon the difference between the input signals. A two-input, single-output difference amplifier can be made by combining the common-emitter and common-base configurations in a single transistor.




A difference amplifier can have input signals that are in phase with each other, 180º out of phase with each other, or out of phase by something other than 180º with each other.




**Return to [Previous Chapter](/university/courses/electronics/text/chapter-11 "university:courses:electronics:text:chapter-11")**




**Go to [Next Chapter](/university/courses/electronics/text/chapter-13 "university:courses:electronics:text:chapter-13")**




**Return to [Table of Contents](/university/courses/electronics/text/electronics-toc "university:courses:electronics:text:electronics-toc")**






university/courses/electronics/text/chapter-12.txt · Last modified: 06 Jun 2017 15:49 by [Doug Mercer](https://ez.analog.com/members/dmercer)

