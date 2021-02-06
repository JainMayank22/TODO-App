
from sys import argv

ifGiven = False
obs = []
happ_event = []
B_prob = 0.001
E_prob = 0.002

class BNet(object):

	def event_info(self,happ_event):
		E_ = []
		if "Bf" in happ_event:
			E_.append(False)
		elif "Bt" in happ_event:
			E_.append(True)
		else:
			E_.append(None)

		if "Ef" in happ_event:
			E_.append(False)
		elif "Et"	in happ_event:
			E_.append(True)
		else:
			E_.append(None)

		if "Af" in happ_event:
			E_.append(False)
		elif "At" in happ_event:
			E_.append(True)
		else:
			E_.append(None)

		if "Jf" in happ_event:
			E_.append(False)
		elif "Jt" in happ_event:
			E_.append(True)
		else:
			E_.append(None)

		if "Mf" in happ_event:
		   E_.append(False)
		elif "Mt" in happ_event:
			E_.append(True)
		else:
			E_.append(None)

		return E_

	def _res_(self, event, condition1, condition2, condition3):
		if event == "E":
			if condition1:
				return E_prob
			else:
				return 1 - E_prob
		if event == "B":
			if condition1:
				return B_prob
			else:
				return 1- B_prob

		if event == "A|B,E":
			if not condition2 and not condition3:
				Prob_C_ = 0.001
			if not condition2 and condition3:
				Prob_C_ = 0.29
			if condition2 and not condition3:
				Prob_C_ = 0.94
			if condition2 and condition3:
				Prob_C_ = 0.95
			if condition1:
				return Prob_C_
			else:
				return (1-Prob_C_)

		if event == "M|A":
			if condition2:
				Prob_C_ = 0.7
			else:
				Prob_C_ = 0.01

			if condition1:
				return Prob_C_
			else:
				return (1-Prob_C_)


		if event == "J|A":
			if condition2:
				Prob_C_ = 0.9
			else:
				Prob_C_ = 0.05

			if condition1:
				return Prob_C_
			else:
				return (1-Prob_C_)



	def EQ_(self,values):
		if not None in values:
			return self.CProb(values)
		else:
			temp = values.index(None)
			latestList = list(values)
			latestList[temp] = True
			itr1 = self.EQ_(latestList)
			latestList[temp] = False
			itr2 = self.EQ_(latestList)
			return itr1 + itr2



	def CProb(self, condition):
		part1 = self._res_("B",condition[0],None,None) * self._res_("E",condition[1],None,None)
		part2 = self._res_("A|B,E",condition[2],condition[0],condition[1])
		part3 = self._res_("J|A",condition[3],condition[2],None) * self._res_("M|A",condition[4],condition[2],None)
		prob_joint = part1 * part2 * part3
		return  prob_joint



if __name__ == '__main__':
    for x in argv:
        if x == "given":
                ifGiven = True
        happ_event.append(x)
        if ifGiven:
                obs.append(x)
    bnet = BNet()
    numer = bnet.EQ_(bnet.event_info(happ_event))
    if obs:
    	deno = bnet.EQ_(bnet.event_info(obs))
    else:
    	deno = 1
    print("The probability of given combination of events is: %.9f" % (numer/deno))
